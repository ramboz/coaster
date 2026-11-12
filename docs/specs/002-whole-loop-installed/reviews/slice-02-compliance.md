---
slice: 002-02 — the challenge round, installed
pass: compliance
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T22:10:41Z
prompt_source: review.py implementation, then two re-checks by the same reviewer
---

Compliance pass on the second re-check by the same reviewer, not a fresh review.

The first pass, on `b760162`, returned needs-changes:
- AC 5's row did not judge `i1o`'s "Parent's notes on the evidence";
- the evidence file still showed S-01's hat as `CHECK` and left S-01 out of the count;
- AC 7 had no row;
- row 6 called the lane-file note a recurrence while its outcome passed it;
- the record did not say that every reading the round touches got a note.

Fixed in `511e0e8`. Julien then ruled the parent's notes on the ledger allowed (`6e2703a`). The first re-check returned needs-changes on one point: `i1s` passed AC 5 only on the recorder's own reading of "touches". `a2a9945` corrected the record: the shapes are not readings, and the open question was the four lenses skipped at the user's request. Julien ruled that a round needs no note under a lens that was not looked at (`ddd1dcd`).

On the second re-check, every AC is met as amended and ruled, and the record is accurate. Reconciliation notes to log:
- AC 1 ran on the profile itself with `--settings`;
- AC 1's builds were not version-bumped, and it had two extra runs;
- the installed runs came before 002-04 was DONE;
- B4 held in 4 of 6 runs on the agents, and B1 is settled;
- ADR-0003 has no pointer to the ruling;
- two of AC 5's points pass only by Julien's rulings.
