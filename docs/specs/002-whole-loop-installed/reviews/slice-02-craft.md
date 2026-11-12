---
slice: 002-02 — the challenge round, installed
pass: craft
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T22:10:41Z
prompt_source: review.py pr-review --richer-skill pr-review, then a re-check by the same reviewer
substrate: non-interactive
---

Craft pass on a re-check by the same reviewer, not a fresh review.

The first pass, on `b760162`, returned needs-changes. Its blocker was that the evidence file predated Julien's rulings: it still showed `CHECK` and the breach wording. Its record nits were the row 6 wording, row 5's extra headings, the missing AC 7 row, and which prompts stay out of the repository. Two package nits went to `docs/inbox.md`: the hats' read scope, and where new ledger entries and parent notes go.

All were fixed in `511e0e8`, and Julien's AC 5 ruling was recorded in `6e2703a`. On re-check the rulings read the same in the slice, the evidence, `lightweight-decisions.md` and the inbox. Three wording nits remained, all fixed in `a2a9945`:
- row 5's "add" for what `i1s` proposed;
- naming both Sonnet runs in the read-scope item;
- separating the two causes in the ledger item.

The F and F1 naming drift between ADR-0003's Status line, AC 7 and the rulings goes to the deviation log.
