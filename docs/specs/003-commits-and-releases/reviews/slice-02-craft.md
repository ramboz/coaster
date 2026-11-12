---
slice: 003-02 — releases from main
pass: craft
verdict: pass
reviewer: jig:reviewer (pr-review rubric)
reviewed_at: 2026-11-12T01:19:00Z
prompt_source: review.py pr-review --richer-skill pr-review
substrate: shown
applied_skill: pr-review
shown_candidates: [independent-review:high-confidence, pr-review:high-confidence, scout-pr-review:high-confidence, access:speculative, adr-workflow:speculative, agent-development:speculative, analyze:speculative, arch-review:speculative, bug-fix:speculative, build-dashboard:speculative, build-mcp-app:speculative, build-mcp-server:speculative, build-mcpb:speculative, cardputer-buddy:speculative, clarify:speculative, claude-automation-recommender:speculative, claude-md-improver:speculative, code-health:speculative, command-development:speculative, configure:speculative, contracts:speculative, cowork-plugin-customizer:speculative, create-cowork-plugin:speculative, create-viz:speculative, data-context-extractor:speculative, data-visualization:speculative, example-command:speculative, example-skill:speculative, explain:speculative, explore-data:speculative, frontend-design:speculative, hook-development:speculative, m5-onboard:speculative, math-olympiad:speculative, mcp-integration:speculative, memory-sync:speculative, migrate:speculative, orient:speculative, playground:speculative, plugin-settings:speculative, plugin-structure:speculative, project-artifact:speculative, reframe:speculative, scaffold-init:speculative, scout-autotune:speculative, scout-bench-create:speculative, scout-memory-init:speculative, scout-scrum-master:speculative, security-review:speculative, session-report:speculative, skill-creator:speculative, skill-development:speculative, slice-land:speculative, spec-workflow:speculative, sql-queries:speculative, statistical-analysis:speculative, tdd-loop:speculative, validate-data:speculative, vision-elicitation:speculative, write-query:speculative, writing-hookify-rules:speculative]
---

Craft pass: pass, with no blockers.

- Strengths: tag and version passed through `env:`, not inline as in jig; cheap checks before the npm install; an install note that says the marketplace follows `main`; the `0.0.0` seed with `initial-version` needing no follow-up PR; a CONTRIBUTING table that matches release-please's real behaviour.
- Nits, all applied: permissions per job, with a `{}` default; `persist-credentials: false` on the package checkout; `--clobber` on the upload and a guard against a second install note, so the job can be re-run; a `0.1.0` → `1.0.0` example on the `!` row; the merge rule scoped to the first release plan for `v0.1.0`.
