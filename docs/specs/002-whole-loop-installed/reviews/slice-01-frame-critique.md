---
slice: 002-01 — scout to handoff, installed
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-11T23:47:11Z
prompt_source: review.py frame-critique, three fresh rounds, then a re-check by the round-3 reviewer
---

Third frame-critique round: pass, reached through three fresh reviewers and a re-check by the third. The re-check was not a fresh review.

- Round 1 (needs-changes): a signed-in disposable profile may not stay isolated, since synced plugins joined 001-02's profile on resume. `$ROOT` was read from the pre.2 baseline. "Allow for the project" expires with each version, the same flaw the spec held against the README rule. Fixed with an `init` check that voids contaminated runs, `$ROOT` taken per installed version, and an honest statement of the cost.
- Round 2 (needs-changes): a refused helper has a web route the skills already give, so "not run" was the wrong rule, and the version-path argument was unprobed. Fixed with the rule that a refused helper is not worked around, and that each result traces to a tool call or is marked not run. Probes showed the cache path holds the version, and that a wildcard rule matches the installed helper.
- Round 3 (needs-changes): the README wildcard rule might admit more than coaster's helpers, and the link check could run before any link is on disk. A probe showed a `python3 -c` lookalike refused, but a `..` path through a cache-anchored rule ran a script outside the plugin. The README rule was dropped and recorded as rejected, and the rendered grant is described as narrower and left to Julien. The link check now runs after filing and must count more than zero URLs.
- Re-check (pass): both findings resolved. Three consistency notes were applied after the verdict: the grant branch also amends AC 1 and the build's `FORBIDDEN` list and adds a two-turn run; the ADR cites A2 as unverified, and 002-03 records the rule "don't ask again" offers; the build's rewrite and guard change with the keys.

Residuals: A1 (`${CLAUDE_PLUGIN_ROOT}` in a CLI-installed skill) and A2 (what "don't ask again" saves) stay open, and the first runs settle them.
