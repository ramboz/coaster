---
slice: 003-01 — every PR checked
pass: craft
verdict: pass
reviewer: jig:reviewer (pr-review rubric)
reviewed_at: 2026-11-12T01:18:59Z
prompt_source: review.py pr-review --richer-skill pr-review
substrate: shown
applied_skill: pr-review
shown_candidates: [independent-review:high-confidence, pr-review:high-confidence, scout-pr-review:high-confidence, access:speculative, adr-workflow:speculative, agent-development:speculative, analyze:speculative, arch-review:speculative, bug-fix:speculative, build-dashboard:speculative, build-mcp-app:speculative, build-mcp-server:speculative, build-mcpb:speculative, cardputer-buddy:speculative, clarify:speculative, claude-automation-recommender:speculative, claude-md-improver:speculative, code-health:speculative, command-development:speculative, configure:speculative, contracts:speculative, cowork-plugin-customizer:speculative, create-cowork-plugin:speculative, create-viz:speculative, data-context-extractor:speculative, data-visualization:speculative, example-command:speculative, example-skill:speculative, explain:speculative, explore-data:speculative, frontend-design:speculative, hook-development:speculative, m5-onboard:speculative, math-olympiad:speculative, mcp-integration:speculative, memory-sync:speculative, migrate:speculative, orient:speculative, playground:speculative, plugin-settings:speculative, plugin-structure:speculative, project-artifact:speculative, reframe:speculative, scaffold-init:speculative, scout-autotune:speculative, scout-bench-create:speculative, scout-memory-init:speculative, scout-scrum-master:speculative, security-review:speculative, session-report:speculative, skill-creator:speculative, skill-development:speculative, slice-land:speculative, spec-workflow:speculative, sql-queries:speculative, statistical-analysis:speculative, tdd-loop:speculative, validate-data:speculative, vision-elicitation:speculative, write-query:speculative, writing-hookify-rules:speculative]
---

Craft pass: pass, with no blockers.

- Strengths: least-privilege permissions; `pull_request`, not `pull_request_target`; push SHAs passed through `env:`; `pr-title.yml` equal to jig's apart from its header; comments that explain each choice; a failing example and a fix-forward command in CONTRIBUTING.
- Nits, applied: the path search now fails on a `git grep` error rather than taking it as "no match"; the subject check fails when `git log` fails and warns when it falls back to the newest commit; CONTRIBUTING gives the path-search command and names `/usr/bin/python3` for the 3.9 floor.
- Nits, not applied: pinning Node with `actions/setup-node`, and pinning actions by SHA, since the spec mirrors jig's tags.
- Noted: the nine types and the subject rule live in four places. CONTRIBUTING now says to change them together.
