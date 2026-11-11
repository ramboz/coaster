---
slice: 002-03 — the next real idea
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-11T23:47:12Z
prompt_source: review.py frame-critique, three fresh rounds, then a re-check by the round-3 reviewer
---

Third frame-critique round: pass, reached through three fresh reviewers and a re-check by the third. The re-check was not a fresh review.

- Round 1 (needs-changes): the real-idea run had no guard against account-synced plugins taking over `scout` or `challenge`, and the push-time search covered only the tip, not the pushed history. Fixed with a log-judged floor check and a search of `git log -p origin/main..HEAD`.
- Round 2 (needs-changes): Julien's account syncs a standalone `deep-research` skill, which `claude plugin list` does not show and which `scout` would call by default. Confirmed in a probe's `init` skills list. Fixed by recording `skills/synced/`, blocking such skills in the test profile, adding a "user's choice wins" rule to `scout` (002-01 AC 12), and giving the one-shot real idea a recovery path.
- Round 3 (needs-changes): the slice required a `handoff.md`, but coaster correctly stops at a no-go or park, so the test leaned on Julien's decision. Fixed: the loop runs as far as his decision takes it, no outcome is required, and the release check is met by the three slices together. Other plugins are disabled before each session.
- Re-check (pass): both findings resolved. Notes applied after the verdict: a declined helper is handled as 002-01's AC 2 requires, "end of the run", how the hat check reads an interactive log, and a release-plan pointer if Julien accepts the decision.

Residuals: A5 (an idea and the time) and the unprobed interactive log format apply only if Julien asks for a round.
