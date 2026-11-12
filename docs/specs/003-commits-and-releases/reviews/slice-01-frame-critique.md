---
slice: 003-01 — every PR checked
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T00:57:13Z
prompt_source: review.py frame-critique, three fresh rounds
---

Third frame-critique round: pass, reached through three fresh reviewers.

- Round 1 (needs-changes): the claim that squash-merge makes the PR title the commit on `main` was asserted, not known. GitHub's defaults allow all three merge methods and use `COMMIT_OR_PR_TITLE`, and PR #1 could not tell the cases apart. It had 5 commits, and its landed subject was typed at merge, matching neither its title nor a commit. Fixed: the DoR now names servo's four merge settings and blocks until they hold, A3 was rewritten, and AC 7 records the settings.
- Round 2 (needs-changes): most commits reach `main` by direct push. 16 of the 17 did, and jig's `workflow.py new` pushes reservations by default. A rule about PR titles alone does not cover them. Fixed: CI's run on each push to `main` checks every new subject against the title check's rules, and the rule text covers direct pushes. A rule forbidding direct pushes was rejected, since only branch protection could enforce it. `squash_merge_commit_message: BLANK` was added as a fifth gated setting, so branch commit footers cannot reach release-please.
- Round 3 (pass): the frame survives. Five notes were applied after the verdict. The subject check now runs before a push too (DoD, CONTRIBUTING), and a red `main` is fixed forward with a correctly worded empty commit. AC 7 expects GitHub's ` (#N)` suffix. The `main` check fetches full history. AC 5 expects `jig-governance` to fail on this PR, by design.

Residuals: A1 (plugin validation on an Ubuntu runner) and the `main` subject check's first live run are settled by this spec's own PR and its merge. A subject edited at merge or a direct push is caught only after it lands.
