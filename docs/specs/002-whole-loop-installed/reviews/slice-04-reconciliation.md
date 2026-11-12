---
slice: 002-04 — the hats as plugin agents
pass: reconciliation
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T18:22:21Z
prompt_source: review.py reconciliation (changed-files list corrected to c8480fa..), then two re-checks by the same reviewer
---

Reconciliation pass, reached by one reviewer in three steps. The second and third were re-checks by the same reviewer, not fresh reviews.

- Round 1 (needs-changes): table row 4 overstated the Sonnet agents' research, since they opened fewer pages and returned fewer `grounded` entries than the built-in types; deviation 4 and its inbox item named only hats rule 1, while the round template's note and `challenge` say the same; the refinement-todo row claimed nothing was deferred; ADR-0003 had no sweep row. Process note: compliance was a same-reviewer re-check, and craft and arch were not repeated after `cbe06fc`. All fixed, with new deviations 9 and 10.
- Re-check 1 (needs-changes): deviation 9 left out that ADR-0003's remedy line makes a recurrence after tightening reopen Option F1. Fixed in deviation 9 and in 002-02's AC 6 row.
- Re-check 2 (pass): the deviation log and sweep are faithful, every changed path is accounted for, no over-build, the new contract surface is declared, and no principle is violated. Open at closure: Option F1 is reopened under ADR-0003 until Julien rules in 002-02.
