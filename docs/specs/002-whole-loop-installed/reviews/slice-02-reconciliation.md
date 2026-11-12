---
slice: 002-02 — the challenge round, installed
pass: reconciliation
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T22:28:21Z
prompt_source: review.py reconciliation (changed-files list corrected to d81ea3a^..HEAD), then a re-check by the same reviewer
---

Reconciliation pass on a re-check by the same reviewer, not a fresh review. The prompt from `review.py reconciliation` listed changed files from `main...HEAD`. Local `main` is stale, so that list mixed in specs 001, 002-01 and 003. The orchestrator replaced it with `git log d81ea3a^..HEAD`, which splits out 002-04's commits; those were reconciled in 002-04's own sweep.

The first pass returned needs-changes:
- the sweep called the status board updated while it still showed IN_PROGRESS;
- the ADR-0003 row called an Accepted record immutable, which the conventions contradict (they make it append-only);
- the log said the release plan pointed at the ruling, when it points at this slice's record;
- deviation 7 attributed `i1o`'s headings and notes to every Opus parent;
- the claim that each inbox item names the ruling it could retire held for one item only;
- the release-plan close-out box was unticked;
- B2 was missing.

Fixed:
- Julien chose to append a dated note to ADR-0003, after its remedy line, pointing at the AC 6 ruling; `adr.py check-index` is clean.
- The log and sweep were reworded, the close-out item ticked, deviation 10 added for B2, and the inbox item given its retire check.

On re-check, all seven are fixed and the log, sweep, close-out, ADR note and inbox agree. Two non-blocking nits:
- the board regenerates at the next transition, which was done at RECONCILED;
- inbox item 22 was broader than the record, and is now narrowed to the judged runs.
