---
slice: 002-02 — the challenge round, installed
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-11T23:47:11Z
prompt_source: review.py frame-critique, three fresh rounds, then a re-check by the round-3 reviewer
---

Third frame-critique round: pass, reached through three fresh reviewers and a re-check by the third. The re-check was not a fresh review.

- Round 1 (needs-changes): "read-only subagents" was only prose. A probe showed a Sonnet parent picking `general-purpose` hats, which can write, and one hat using `cat` through Bash. The three calls shared one `message.id`. A second probe showed an `Explore` hat running on the session's Sonnet. Fixed by naming the subagent type, checking parallel starts by `message.id`, and banning writes rather than all Bash.
- Round 2 (needs-changes): the round file is the parent's, so it could pass while the hats' replies were thin, and A8's fallback had no trigger. AC 4's "any other difference fails" was stricter than ADR-0001's "omits or condenses". Fixed with an AC on each hat's reply (the `Agent` call's `tool_result`), an AC that the round traces to the replies, and allowed difference classes (whitespace, markup alone, a filled placeholder).
- Round 3 (needs-changes): choosing `Explore` on reply shape alone cannot catch shallow research, and the pasted evidence rules tell the reader to run the link check. Fixed with AC 1 as a hat-by-hat comparison against `general-purpose` on reading, searches, sources, entries, tokens and time, including an Opus `Explore` run. Wording outside the pasted sections keeps hats from running helpers or editing files.
- Re-check (pass): both findings resolved. Setup notes were applied after the verdict: AC 1's runs compare against the local build they loaded, run with the installed coaster disabled, carry AC 2's draft wording, and block AC 2 if both types fail.

Residuals: A3 (the paste is intact) is ADR-0001's open assumption, tested by AC 6, with AC 7 as its kill path. A8 is settled by AC 1's comparison.
