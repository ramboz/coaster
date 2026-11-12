---
slice: 002-04 — the hats as plugin agents
pass: craft
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T17:51:56Z
prompt_source: review.py pr-review --richer-skill pr-review
substrate: shown
applied_skill: pr-review
shown_candidates: [independent-review:high-confidence, pr-review:high-confidence, scout-pr-review:high-confidence, access:speculative, adr-workflow:speculative, agent-development:speculative, analyze:speculative, arch-review:speculative, bug-fix:speculative, build-dashboard:speculative, build-mcp-app:speculative, build-mcp-server:speculative, build-mcpb:speculative, cardputer-buddy:speculative, clarify:speculative, claude-automation-recommender:speculative, claude-md-improver:speculative, code-health:speculative, command-development:speculative, configure:speculative, contracts:speculative, cowork-plugin-customizer:speculative, create-cowork-plugin:speculative, create-viz:speculative, data-context-extractor:speculative, data-visualization:speculative, example-command:speculative, example-skill:speculative, explain:speculative, explore-data:speculative, frontend-design:speculative, hook-development:speculative, m5-onboard:speculative, math-olympiad:speculative, mcp-integration:speculative, memory-sync:speculative, migrate:speculative, orient:speculative, playground:speculative, plugin-settings:speculative, plugin-structure:speculative, project-artifact:speculative, reframe:speculative, scaffold-init:speculative, scout-autotune:speculative, scout-bench-create:speculative, scout-memory-init:speculative, scout-scrum-master:speculative, security-review:speculative, session-report:speculative, skill-creator:speculative, skill-development:speculative, slice-land:speculative, spec-workflow:speculative, sql-queries:speculative, statistical-analysis:speculative, tdd-loop:speculative, validate-data:speculative, vision-elicitation:speculative, write-query:speculative, writing-hookify-rules:speculative]
---

Craft pass (pr-review rubric) on `b6052c4`, with no blockers.

Strengths: the agents reuse `_section`, `FILES` and `INTRO`, so a skill and its agents cannot drift; the `{name}`/`{Hat}` guard fails the build on an unrendered placeholder; the `tools` line enforces "write nothing" and "run no helper" in config; the evidence reports the full `Agent` prompts and the Sonnet parent's shortening honestly.

Nits, and what became of them:
- `_part`'s bare `next()` and the `[1:]` dependency on the order of challenge's files: fixed in `cbe06fc` (a named `ERROR:` and an explicit filter). The `## Packaged: hats` literal now comes from the rendered section's own heading.
- The brief's split ownership of the link check and dossier changes: reworded in `cbe06fc` (the link check belongs to `scout`, dossier changes to the parent).
- "Under each hat's heading" was ambiguous: `challenge` now says to copy each section from its own `## ` heading on, without shortening it (`cbe06fc`).
- The `f1s` prompts' lane-file note, and the missing build identity: met by tightening the wording and re-running both models from the recorded commit `cbe06fc`.
- The brief's lane files beside hats rule 1, an automatic byte-identity assert, and the architecture doc: deviation log and reconciliation sweep.
