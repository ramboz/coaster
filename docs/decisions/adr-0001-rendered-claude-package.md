---
status: Accepted
dependencies: []
last_verified: 2026-11-09
frame_review: true
---

# ADR-0001: Render a self-contained Claude package from neutral source

## Status

Accepted (2026-11-09)

## Context

coaster's Claude Code package has to give each skill its templates and shared rules without relying on a runtime read of the plugin's own files.

Probes on 2026-11-09 (spec 001) showed why. In a headless run with no read grant, `capture` was refused the packaged template, carried on, and wrote 9 of the template's 22 headings without reporting a problem. An interactive session would probably ask for permission instead, which has not been run. A scoped frontmatter grant let the reads through in the turn that invoked the skill, and how long it lasts is unsettled.

Three facts shape the options:

- Seven of the eight packaged files have one consumer. Only the evidence rules are shared, by `capture`, `scout` and `challenge`.
- The pack is Claude-first, with chat and Codex planned, so source carries no host-only paths today.
- jig, servo and shaper's Claude builds copy files unchanged. Text rewriting appears only in jig's Codex and Copilot builds and servo's Codex build.

The release plan rules out a "bespoke plugin framework or build system", so any script needs an explicit exception.

## Decision Options Considered

### Option A: A generated, committed `hosts/claude`, rendered from neutral source
- **Pros:** One place to edit, so the shared evidence rules cannot drift. Source stays free of host-only paths for later chat and Codex builds. Reading packaged text needs no runtime read and no permission grant.
- **Cons:** Goes beyond the family's copy-only Claude builds and relaxes the release plan's no-go. Adds a script, an explicit skill-to-files map, a drift guard, and a second tree in every diff.

### Option B: A hand-kept plugin folder with the text built in
- **Pros:** No script or drift guard, and it honours the no-go as written. It would duplicate only the 75-line evidence rules and hand-edit two helper paths.
- **Cons:** The evidence rules are kept by hand in three skills. Host-only helper paths sit in the source. Chat or Codex would later need a build or more copies.

### Option C: A family-style copy build with a scoped read grant
- **Pros:** Closest to the sibling packs, and templates stay separate files.
- **Cons:** The grant has only been seen working in the invoking turn. A public plugin would ask for read access. Source references would still have to change to reach the packaged files.

### Option D: A plain copy with no grant
- **Pros:** The simplest build, matching shaper's ungranted packaged reads.
- **Cons:** An interactive user would probably see a permission prompt. Where no one can answer it, the run can write a partial dossier silently.

### Option E: The repository root as the plugin
- **Pros:** No `hosts/` tree at all.
- **Cons:** Puts the dossiers and dogfood logs in the plugin cache. The bare template paths would still not resolve from a user's repository.

### Option F: Option A, with each `challenge` hat rendered as a plugin agent
- **Pros:** Each hat gets its rules in its own prompt, with no retyping by the parent. The family already ships plugin agents.
- **Cons:** Widens the package and the script for a skill scope 1 does not run. It has not been tried, and chat ignores plugin agents.

## Recommended Decision

Option A, chosen by Julien on 2026-11-09 with the alternatives in front of him.

`scripts/build_host_packages.py` renders `hosts/claude/` from `skills/` and `templates/`. It is standard-library only, Claude-only and under 200 lines. Its only changes to skill text are an explicit skill-to-files map, which appends each skill's packaged files under `## Packaged:` headings, and the two helper paths. `--check` fails when the committed package is stale. The rendered `challenge` tells the parent to paste the packaged sections into each hat's prompt, because a subagent cannot see its parent's skill.

Whether the parent passes that text intact is unproven. Scope 2 checks it before the `v0.1.0` tag, by comparing each hat's prompt in a `challenge` run's log with the packaged sections. Intact means each prompt holds the rules every hat follows, its own hat section, the evidence rules and the round shape. If the text is condensed, the hats move to Option F, which may raise the script's size bound. The check can follow publication because a failure leaks nothing and ships as a pre-release bump.

The release plan's no-go now names this one script as its exception. The gain over a plain copy is no prompts and reliable headless runs. It is not a fix for a dossier that an interactive user would otherwise have seen broken. Option B has the same runtime gain, so what Option A buys over it is single-sourced evidence rules and a start on later hosts.

## Consequences

**Becomes easier:**
- Changing a template or the evidence rules, which happens in one place.
- Trusting the installed package, which reads none of its own text at runtime and asks for no read permission.
- Starting a chat or Codex build from source that names no host-only paths.

**Becomes harder:**
- Every skill edit needs a rebuild, and shows twice in the diff.
- A skill that gains a dependency also needs an entry in the map.
- Each rendered skill carries its own copy of the text it needs, so the largest is about 325 lines. That text costs context only when the skill is invoked, and `challenge` re-emits it once per hat.

## Assumptions

- An interactive session behaves like the headless runs: `capture` reads no packaged file, so no permission prompt appears for one. 001-01's AC 12 tests this.
- The rendering works for the skills other than `capture`, including the parent passing packaged text to `challenge`'s hats. Only `capture` has been run in this form, and scope 2 runs the rest.

## Kill criteria

- 001-01's AC 12, or scope 2, shows that a rendered skill still prompts for, or fails on, packaged text.
- A `challenge` run's log shows a hat prompt that omits or condenses the packaged rules. Option F then replaces the paste.
- A rendered skill outgrows what survives compaction. A static read of Claude Code 2.1.300 shows an invoked skill re-attached at its first 5,000 tokens, and the packaged sections come last.
- The script outgrows its bound, or the map changes so often that keeping it costs more than Option B's hand-kept copies.

## Open questions

Whether self-contained skills also suit claude.ai. R-02's chat-path run will show that.
