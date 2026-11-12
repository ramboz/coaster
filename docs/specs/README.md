# Spec Status Board

> Status: Draft (wizard-generated)
>
> Current state of all specs for coaster. Update after each slice transition.
>
> A leading 🔬 in the Slice column flags slices marked `kind: spike` in
> their frontmatter — timeboxed investigation, not feature work. The
> marker is recomputed from each slice's `kind:` field on every regen
> by `workflow.py status-board`; it is never stored separately in this
> file.
>
> Related: [Bug Status Board](../bugs/README.md). Check both boards before
> folding reported defects into spec acceptance criteria.

| Spec | Slice | Status | Notes |
|------|-------|--------|-------|
| [000-adopt-jig](000-adopt-jig/spec.md) | 000-01 — bootstrap | **DONE** | genesis worked example; review boxes satisfied by deterministic completion check |
| [001-install-and-capture](001-install-and-capture/spec.md) | 001-01 — capture from the built package | **DONE** |  |
| [001-install-and-capture](001-install-and-capture/spec.md) | 001-02 — install from GitHub | **DONE** |  |
| [002-whole-loop-installed](002-whole-loop-installed/spec.md) | 002-01 — scout to handoff, installed | READY_FOR_IMPLEMENTATION |  |
| [002-whole-loop-installed](002-whole-loop-installed/spec.md) | 002-02 — the challenge round, installed | READY_FOR_IMPLEMENTATION |  |
| [002-whole-loop-installed](002-whole-loop-installed/spec.md) | 002-03 — the next real idea | READY_FOR_IMPLEMENTATION |  |
| [003-commits-and-releases](003-commits-and-releases/spec.md) | 003-01 — every PR checked | DRAFT |  |
| [003-commits-and-releases](003-commits-and-releases/spec.md) | 003-02 — releases from main | DRAFT |  |

## Richer-skill selection audit (spec 096-05)

Advisory (ADR-0040 auditability — never blocks). Regenerated from `reviews/slice-*.md` `substrate:` fields.

- **0** pass(es) recorded `not-shown` (selection step did not run — the kill-criterion-1 defect signal).
- **3** pass(es) recorded `non-interactive` (declared no-orchestrator / CI).
- **0** shown-and-declined anomaly(ies) (a high-confidence richer skill was shown and not applied):
