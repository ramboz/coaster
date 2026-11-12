---
slice: 002-02 — the challenge round, installed
pass: arch
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T22:10:41Z
prompt_source: review.py arch-review --richer-skill arch-review
substrate: non-interactive
---

Arch pass on the first review, of `b760162`. The installed runs confirm ADR-0003's design. The build cuts the skill's and the agents' four parts from one `_section`, the installed folder matched `hosts/claude`, and each hat's system prompt matched its installed agent file. The `tools` line now enforces "write nothing": no installed hat called Bash or a write tool, against 9 of 15 hats denied Bash in AC 1's runs. That confirms ADR-0003's B1 on the installed plugin.

Nits:
- ADR-0003 has no pointer to the lane-file ruling, which changes how its prompt list and remedy line read. The reviewer suggests a dated note in the ADR and a pointer from `docs/architecture.md`.
- `challenge` still says "and nothing else: no notes", which is stricter than the check now is.
- The hats' read scope differs between `challenge` and the brief, parked in `docs/inbox.md`.
- The round template has no place for the grouping of concerns or the parent's notes.

Reconciliation notes: log the ruling's relation to ADR-0003, link the read-scope item to the ruling, record that B4 held in 4 of 6 runs on the agents, and record the two readings of "into the ledger". B2 stays untested until R-04's activation test.
