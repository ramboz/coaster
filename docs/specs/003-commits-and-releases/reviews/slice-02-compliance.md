---
slice: 003-02 — releases from main
pass: compliance
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T01:18:59Z
prompt_source: review.py implementation
---

Compliance pass: pass. ACs 1 to 6 are met, and AC 7 is pending by design until the merge.

- `release.yml` has the triggers, permissions, outputs and package steps in the required order.
- The config equals jig's settings and changelog sections, plus two `extra-files` entries and `initial-version: "0.1.0"`; the manifest is `0.0.0`.
- CONTRIBUTING's table matches the config.
- The refinement-todo entry is struck in the file's style, and the release plan stays `candidate`.
- Notes, applied: AC 4 re-run on the rebased `0.1.0-pre.8` tree (deviation log item 4); CONTRIBUTING says what to do when `package` fails; the architecture doc's plugin-manifest entry points to release-please.
