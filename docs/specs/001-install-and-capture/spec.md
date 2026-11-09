---
status: IN_PROGRESS
skill:
use_cases: [UC-5]
---

<!-- jig self-defining vocabulary (soft, forward-only): expand each acronym on first use and link the term to docs/memory/glossary.md (or jig's lexicon). See docs/workflow.md "Self-defining vocabulary". -->

# Spec 001: Install and capture

> Reserved on 2026-11-09 as a local provisional number, because the repository
> has no remote yet. Serves scope 1 of the
> [Claude Code first release](../../releases/claude-code-first-release.md).

## Overview

coaster exists only as a local draft, so nobody can install it. This spec makes
the thinnest path real: add coaster's marketplace from GitHub in Claude Code,
install it, run `capture` in an empty repository, and get a correct dossier.

Scope 1 is also the first time the repository goes public. The release plan
puts the review of `docs/prospects/` first for that reason, so the review
happens here, before anything is pushed.

### Current state (verified 2026-11-09)

**Packaging**

- The repository has no `.claude-plugin/`, `hosts/`, `LICENSE` or git remote.
  `gh repo view ramboz/coaster` finds no such repository.
- shaper's `scripts/build_host_packages.py` is 262 lines, standard library
  only, builds Claude and Codex packages, and has a `--check` drift guard.
  shaper's marketplace entry is a `git-subdir` source pointing at
  `hosts/claude`, and jig's ADR-0036 records an isolated install of that shape.
- jig, servo and shaper's Claude builds copy files unchanged. Text rewriting
  appears only in jig's Codex and Copilot builds and servo's Codex build.
- A local-directory marketplace installed into a disposable `CLAUDE_CONFIG_DIR`
  with no sign-in, and the installed `SKILL.md` was byte-identical to the built
  one.
- `claude plugin validate --strict` accepts the version `0.1.0-pre.1`.

**How `capture` reads its files**

- A plain plugin copy passed strict validation, and `capture` wrote a correct
  dossier from it in 3 of 3 Sonnet runs. Those runs were granted `Read` with
  `--allowedTools`, so they did not show what a session without that grant gets.
- Without the grant the read is refused. Under `--permission-mode acceptEdits`,
  `capture` was denied the packaged template, carried on, wrote a dossier with
  9 of the template's 22 headings, and reported no problem. Moving the template
  into the skill's own folder gave the same result. Those were headless runs,
  where nobody can answer a prompt. An interactive session would probably ask
  instead, which has not been run.
- A frontmatter grant, `allowed-tools: Read(/${CLAUDE_PLUGIN_ROOT}/**)`, let the
  reads through when they happened in the turn that invoked the skill. Whether
  it lasts into a later turn is not settled. A static read of Claude Code
  2.1.300 suggests it is reset on the next prompt, and the one two-turn run did
  its reads in the first turn.
- Building the text into the skill removes the question. With the template and
  evidence rules appended to a rendered `capture` `SKILL.md` and no grant, a
  two-turn run read no packaged file, had no denials, wrote all 22 headings and
  recorded the second turn's answers. That package passes strict validation.
  Rendered this way, the largest of the six skills, `challenge`, would be about
  325 lines.
- Source names packaged files in three path forms: `templates/<file>`
  (5 references), `../_shared/<file>` (5) and `scripts/<file>` (2). The earlier
  runs had to search for them. Two more dependencies carry no path:
  `skills/_shared/hats.md` names a bare `evidence.md`, and `challenge` tells its
  hats to use "the evidence rules".
- Seven of the eight packaged files have one consumer. Only `evidence.md` is
  shared, by `capture`, `scout` and `challenge`.
- `skills/_shared/evidence.md` and `templates/dossier.md` name repository paths
  that do not exist for an installed user.
- `${CLAUDE_PLUGIN_ROOT}` resolves in a skill body under `--plugin-dir`, and
  jig's skills use it.

**Publication**

- Eleven lines in five tracked files hold a path under the home directory, nine
  of them absolute. All five commits contain at least one of them, including
  the first.
- The sensitive material is in the prose as well.
  `docs/prospects/field-research/scout/own-record.md` says to keep the detail of
  its `local` entries out of anything shared. In coaster's research, `ENB-04` in
  `scout/enablers.md`, seven lines in the `research_notes` copy of `enablers.md`
  and line 74 of the landscape report paraphrase a skill with no public source
  (`S-04`).
  `field-research/dossier.md` quotes Julien's turns from a session transcript
  that is kept local.
- coaster's evidence depends on field-research. All seven `OWN` entries are
  `grounded` and cite only field-research IDs, and the first dogfood note links
  to it for five steps. Outside `own-record.md`, airlock appears on 9 lines in
  that folder.
- `claude plugin marketplace add` clones the whole repository to the installer's
  disk, as jig's marketplace folder on this machine shows. Only the plugin cache
  is limited to `hosts/claude`.
- A disposable `CLAUDE_CONFIG_DIR` does not carry the sign-in over. A model run
  there stops with "Not logged in".
- Every commit carries `ramboz@adobe.com`, which is already public in the jig,
  servo and shaper histories, so it needs no action here.

## Decisions

- **What goes public (Julien, 2026-11-09).** `docs/prospects/coaster/`,
  `docs/prospects/field-research/` and `docs/dogfood/` go public after a content
  review, except `docs/prospects/field-research/scout/own-record.md`, which holds
  the private airlock record and is held back. Julien first chose to hold back
  the whole folder, and changed that once the review showed coaster's evidence
  cites it. Holding back all of the research was also set aside, because the
  README, vision and release plan cite it.
- **How the history goes public (Julien, 2026-11-09).** The reviewed tree is
  published as one new first commit. The five existing commits, the held-back
  file and `publication-review.md` stay on a local `pre-publication` branch that
  is never pushed.
- **How the package is produced (Julien, 2026-11-09).** A standard-library script
  renders neutral source into a generated, committed `hosts/claude`. This goes
  beyond the family's copy-only Claude builds and relaxes the release plan's
  build-system no-go, which now records the exception. A hand-kept plugin folder
  and a copy build with a read grant were weighed and set aside. Over a plain
  copy, the gain is no prompts and reliable headless runs: an interactive user
  of a plain copy would probably get a prompt rather than a broken dossier.
- **Packaged text is built into each skill.** The script appends each skill's
  templates and shared files to its rendered `SKILL.md`. Reading packaged text
  then needs no runtime read and no permission grant, so it does not depend on
  how long a grant lasts. Helpers still run through Bash, and scope 2 settles
  their permission. A hat subagent cannot see its parent's skill, so the rendered
  `challenge` tells the parent to paste the packaged sections into each hat's
  prompt.
- **Versions before the tag (from the frame review).** The package starts at
  `0.1.0-pre.1`, and every change to its bytes before the `v0.1.0` tag bumps the
  pre-release number. An installed plugin updates only when its version changes
  (jig ADR-0036), so early installers would otherwise be stuck on these bytes.
- **After publication (from the frame review).** The finding definition in
  001-02's AC 1 applies to anything added later to `docs/dogfood/`,
  `docs/prospects/` or spec evidence. Dossiers for other ideas, including scope
  2's real idea, stay out of this repository.

## Non-goals

- The rest of the loop from the installed plugin, including the two helpers
  (scope 2).
- Deferral to richer skills (scope 3).
- The `v0.1.0` tag, the ai-pegboard listing, `CHANGELOG`, CI and release
  automation (scope 4).
- R-04's activation test, which lands before the tag.
- The claude.ai chat path, Codex and Copilot.
- A test harness for the Markdown skills, which the release plan rules out.
  These slices are verified by plugin validation and recorded runs.

## Assumptions

- **A1.** An interactive session behaves like the headless runs: `capture` reads
  no packaged file, so the user sees no permission prompt for one. Every run so
  far was headless. In 001-01's AC 12 Julien runs it by hand, before anything is
  public, and if it fails the rendering is reopened.
- **A2.** The rendering works for the skills other than `capture`, including the
  parent passing packaged text to `challenge`'s hats. Only `capture` has been
  run in this form. Scope 2 runs the rest, and this spec checks only their
  rendered text.
- **A3.** Running the privacy search by hand before each push is enough until CI
  arrives in scope 4. No hook or workflow enforces it, and a search cannot catch
  private prose that nobody has identified. This is an accepted residual.

## Decomposition

**SPIDR axis: Interface.** SPIDR is jig's split of work by Spike, Path,
Interface, Data or Rules. The split here is by install channel. A local
`--plugin-dir` load is the minimal channel, and the marketplace from GitHub
follows it. Both slices end with a person running `capture` and reading a
dossier.

Packaging uses the family's `hosts/claude` layout, but the build does more than
the family's Claude builds do. Source stays host-neutral, and the build renders
each skill into one self-contained file. See Decisions for why that was accepted.

## Slices

- [001-01 — capture from the built package](slice-01-built-package.md)
- [001-02 — install from GitHub](slice-02-install-from-github.md)

## Deferred decisions this spec reaches

| Entry in `docs/refinement-todo.md` | What happens |
|---|---|
| Tech stack | 001-01's ADR resolves the packaging part. |
| Module boundaries | The plugin manifest is the first contract, and source versus rendered package is a new boundary. 001-01 adds both to `docs/architecture.md`. Its statement that skills couple by relative paths still holds for source. |
| Skill file access in claude.ai | Its trigger names the first packaging spec, but chat packaging is deferred. Self-contained skills may also suit chat, which is untested. The trigger narrows to R-02. |
| "Nothing to install or run" as the lead claim | Julien decides in 001-02, since a Claude Code user now installs a plugin. |
| CI/CD setup | This spec crosses a deploy boundary. The release plan says CI is "Needed once the repository is public", and its release check requires CI before the tag, which comes after the repository is public. Until then the privacy search runs by hand (A3). The trigger moves to scope 4. |
