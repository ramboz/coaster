---
slice: 002-01 — scout to handoff, installed
pass: compliance
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T01:58:13Z
prompt_source: review.py implementation, then a re-check by the same reviewer
---

Compliance pass on a re-check by the same reviewer, not a fresh review. The first pass, on the record for pre.8, returned needs-changes:
- a judged `frame` turn's denied command named `/tmp/x`, outside AC 9's amendment;
- Recorded revision claimed `name`'s text was unchanged through pre.8;
- the AC 2 and AC 5 runs predated the shipped text;
- several AC sub-points were unstated, and the check scripts were undescribed;
- two breaches of `scout`'s own text were untracked.

The fixes went into pre.9 to pre.11. The judged runs were repeated so that each skill was judged on text byte-identical in pre.11. Julien widened AC 9's amendment to any denied Bash command confined to the run folder, and the evidence file now describes its checks. On re-check all six findings were resolved and nothing failed an AC. Three medium items were applied in reconciliation: the `handoff` inbox remedy, `s5b`'s skipped web route for registries, and the pre.10 warning gap in ADR-0002 and refinement-todo.
