---
slice: 003-02 — releases from main
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T00:50:50Z
prompt_source: review.py frame-critique, two fresh rounds
---

Second frame-critique round: pass, reached through two fresh reviewers.

- Round 1 (needs-changes): a manifest seeded at `0.0.0` does not give `0.1.0`. In release-please's source, `manifest.ts` uses the manifest's version as a stand-in previous release only when it is not `0.0.0`, and `base.ts` then falls back to `initial-version`, `1.0.0` by default. servo's evidence fits a non-zero seed, not `0.0.0`. The source was read and confirmed. Fixed with `initial-version: "0.1.0"` beside the `0.0.0` seed, with `release-as` and a non-zero seed recorded as rejected. A4 was reworded: release-please's PR will probably get no checks, so the by-hand fallback is the expected path.
- Round 2 (pass): the frame survives, because `0.1.0` comes out on either code path and AC 7 reads the version before the merge. Two notes were applied after the verdict. AC 7 now also requires that the first changelog heading has no compare link, which would reveal the `0.0.0`-as-previous path. The package job's validation is no longer counted as the release plan's pre-ship check, since it runs after the tag. The by-hand fallback adds `claude plugin validate --strict` to `--check`, and a failed first package run is named as a residual.

Residuals: A2 was read in the source, not run, and the first release PR shows it. A5 holds on macOS, not yet on the Ubuntu runner, and the package job first runs at `v0.1.0`.
