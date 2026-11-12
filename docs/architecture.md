> Status: Draft (elicited)
>
> Technical mechanics. Vision and design principles live in
> [product-vision.md](product-vision.md). Update via reconciliation after each
> spec slice completes.

# Architecture: coaster

> For *what this project is*, *who it's for*, and *why*, see
> [product-vision.md](product-vision.md). This document covers the technical
> mechanics: repository structure, tech stack, decisions, modules, data.

## Repository structure

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:64d7bbf4d4ac -->

```
coaster/
├── .claude-plugin/    # the source manifest; the root is not a supported plugin target
├── skills/            # the six skills, _shared/ (evidence rules, lenses, hats), two Python helpers
├── templates/         # dossier, research brief, challenge round, naming, handoff
├── scripts/           # build_host_packages.py renders hosts/claude from source
├── hosts/claude/      # the generated, committed Claude Code package, with challenge's hat agents; never edit by hand
├── docs/prospects/    # one dossier folder per idea
├── docs/dogfood/      # what each run on its own idea taught
└── docs/              # jig's vision, architecture, specs, decisions
```

## Tech stack

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:1f659fce3877 -->

- **Runtime / language:** Markdown skills and templates, plus two
  standard-library Python helpers that run only in Claude Code or a terminal.
  Locked.
- **Platform commitments:** Claude chat and Claude Code first, then Codex
  and Copilot later, as v1. Locked.
- **Package manager:** none. The Claude Code package is a generated
  `hosts/claude`, rendered by a standard-library script
  ([ADR-0001](decisions/adr-0001-rendered-claude-package.md)).
- **Database / state:** none.
- **Key external services:** GitHub for marketplace install; claude.ai Projects
  and Research; npm, PyPI, crates.io and GitHub for name checks.

## Core architecture decisions

> _One H3 subsection per decision. Each decision should reference its ADR
> (when one exists) and split into Principle (from
> [product-vision.md](product-vision.md) where applicable) + Mechanics
> (technical detail). This section is the running summary; decisions
> themselves live in `docs/decisions/`._

### Rendered Claude package ([ADR-0001](decisions/adr-0001-rendered-claude-package.md))

**Principle:** one place to edit, and an installed skill that needs no extra
permission to read its own text.

**Mechanics:** `scripts/build_host_packages.py` renders `hosts/claude/` from
`skills/` and `templates/`, appending each skill's packaged files under
`## Packaged:` headings from an explicit map, and renders challenge's three hat
agents (ADR-0003). After any change to `skills/`, `templates/`, `README.md` or
the manifest, run the script and commit the result. `--check` fails when the
committed package is stale.

### The hats are plugin agents ([ADR-0003](decisions/adr-0003-hats-as-plugin-agents.md))

**Principle:** each hat works from the full rules and stays independent of the
conversation, and "write nothing" is enforced rather than asked for.

**Mechanics:** the build renders `hosts/claude/agents/skeptic.md`, `rival.md`
and `customer.md` from `skills/challenge/hat-agent.md`, a Claude-only brief,
followed by the hats' rules, that hat's own section, the evidence rules and the
round template, cut from the same rendered sections `challenge` carries. Each
agent has `tools: Read, Grep, Glob, WebSearch, WebFetch` and `model: inherit`.
`challenge` starts `coaster:skeptic`, `coaster:rival` and `coaster:customer`
in one message, with only the hat's name, the dossier path, earlier rounds and
the date in each prompt, and writes the round from their replies. The release
check reads each hat's system prompt from its subagent transcript and checks
each `Agent` prompt against that list. The chat path still pastes the full
text into one prompt per hat. A later chat or Codex build must skip
`hat-agent.md`.

### Helpers ask for Bash ([ADR-0002](decisions/adr-0002-helpers-ask-for-bash.md))

**Principle:** coaster grants itself no permissions. Running a script that
makes network requests is the user's call.

**Mechanics:** source runs each helper as `python3 scripts/<file>`, and the
build renders it in jig's form,
`python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"`. Claude Code
asks before each run. Answering "don't ask again" saves `Bash(python3 *)`
(Claude Code 2.1.322), so the README, `scout` and `name` tell users to answer
Yes instead. A refused helper is never worked around with another command: the
skill takes the web route when it can, and otherwise records the check as not
run.

## Module boundaries

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:db97279b6ea5 -->

- **skills:** one step of the loop each, reading and updating the dossier
- **_shared:** the rules every skill follows
- **templates:** the file shapes the skills write
- **helpers:** link and name-collision checks
- **package:** the generated `hosts/claude`, built only from the source above

Coupling: in source, skills couple only through the dossier and by relative
paths to `_shared/` and `templates/`. In the package those paths are replaced by
text built into each skill, and into each of challenge's hat agents.

## Data model

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:857835d0fd84 -->

Near-stateless: the pack owns no runtime state. Each idea is one Markdown
dossier plus sibling files, in `docs/prospects/<slug>/` or as artifacts in a
Claude Project.

## Contract surfaces

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:a78d53a5b212 -->

- **Internal data shapes** (artifact: dossier template at
  `templates/dossier.md`) — the dossier and its sibling files, read by later
  skills
- **Internal data shapes** (artifact: handoff template at
  `templates/handoff.md`) — `handoff.md`, read by jig's vision step and shaper
- **CLI output** (no artifact yet) — `link_check.py` and `name_check.py`
- **Plugin manifest** (artifact: `.claude-plugin/plugin.json`) — the plugin name,
  the version installers update on, and the `/coaster:<skill>` commands. From
  `v0.1.0`, release-please sets the version in it and in the package's copy
  ([spec 003](specs/003-commits-and-releases/spec.md))
- **Plugin agents** (artifact: `hosts/claude/agents/*.md`, rendered from
  `skills/challenge/hat-agent.md`) — `coaster:skeptic`, `coaster:rival` and
  `coaster:customer`, listed in every session that has coaster installed and
  started only by `challenge` ([ADR-0003](decisions/adr-0003-hats-as-plugin-agents.md))
- **Marketplace manifest** (artifact: `.claude-plugin/marketplace.json`) — the
  marketplace name and the `coaster@coaster` install id, with its `git-subdir`
  source
- **Release asset** (artifact: `.github/workflows/release.yml`) —
  `coaster-claude-vX.Y.Z.zip` on each GitHub release from `v0.1.0`, the
  package as a plugin folder for `claude --plugin-dir`
  ([spec 003](specs/003-commits-and-releases/spec.md))

## Open questions

> Deferred items live in [refinement-todo.md](refinement-todo.md).
