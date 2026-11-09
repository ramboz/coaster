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
├── skills/            # the six skills, _shared/ (evidence rules, lenses, hats), two Python helpers
├── templates/         # dossier, research brief, challenge round, naming, handoff
├── docs/prospects/    # one dossier folder per idea
├── docs/dogfood/      # what each run on its own idea taught
└── docs/              # jig's vision, architecture, specs, decisions
```

## Tech stack

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:1f659fce3877 -->

- **Runtime / language:** Markdown skills and templates, plus two
  standard-library Python helpers that run only in Claude Code or a terminal.
  Locked.
- **Platform commitments:** "Claude Chat/Code first, then Codex/Copilot later
  as v1." Locked.
- **Package manager:** none. Packaging is open; the family convention is a
  generated `hosts/claude`.
- **Database / state:** none.
- **Key external services:** GitHub for marketplace install; claude.ai Projects
  and Research; npm, PyPI, crates.io and GitHub for name checks.

## Core architecture decisions

> _One H3 subsection per decision. Each decision should reference its ADR
> (when one exists) and split into Principle (from
> [product-vision.md](product-vision.md) where applicable) + Mechanics
> (technical detail). This section is the running summary; decisions
> themselves live in `docs/decisions/`._

_(No decisions recorded yet. Add the first H3 when the first ADR accepts.)_

## Module boundaries

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:db97279b6ea5 -->

- **skills:** one step of the loop each, reading and updating the dossier
- **_shared:** the rules every skill follows
- **templates:** the file shapes the skills write
- **helpers:** link and name-collision checks

Coupling: skills couple only through the dossier and by relative paths to
`_shared/` and `templates/`. No formal contracts yet.

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

## Open questions

> Deferred items live in [refinement-todo.md](refinement-todo.md).
