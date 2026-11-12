---
slice: 002-04 — the hats as plugin agents
pass: arch
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T17:51:56Z
prompt_source: review.py arch-review --richer-skill arch-review
substrate: shown
applied_skill: arch-review
shown_candidates: [arch-review:high-confidence, access:speculative, adr-workflow:speculative, agent-development:speculative, analyze:speculative, bug-fix:speculative, build-dashboard:speculative, build-mcp-app:speculative, build-mcp-server:speculative, build-mcpb:speculative, cardputer-buddy:speculative, clarify:speculative, claude-automation-recommender:speculative, claude-md-improver:speculative, code-health:speculative, command-development:speculative, configure:speculative, contracts:speculative, cowork-plugin-customizer:speculative, create-cowork-plugin:speculative, create-viz:speculative, data-context-extractor:speculative, data-visualization:speculative, example-command:speculative, example-skill:speculative, explain:speculative, explore-data:speculative, frontend-design:speculative, hook-development:speculative, independent-review:speculative, m5-onboard:speculative, math-olympiad:speculative, mcp-integration:speculative, memory-sync:speculative, migrate:speculative, orient:speculative, playground:speculative, plugin-settings:speculative, plugin-structure:speculative, pr-review:speculative, project-artifact:speculative, reframe:speculative, scaffold-init:speculative, scout-autotune:speculative, scout-bench-create:speculative, scout-memory-init:speculative, scout-pr-review:speculative, scout-scrum-master:speculative, security-review:speculative, session-report:speculative, skill-creator:speculative, skill-development:speculative, slice-land:speculative, spec-workflow:speculative, sql-queries:speculative, statistical-analysis:speculative, tdd-loop:speculative, validate-data:speculative, vision-elicitation:speculative, write-query:speculative, writing-hookify-rules:speculative]
---

Arch pass (arch-review rubric) on `b6052c4`. The change follows ADR-0003's Option F1 and stays inside ADR-0001's bounds: `hosts/claude` is still generated only from source, the build is standard-library, Claude-only and under 200 lines, and `--check` covers the agents through its whole-tree diff. Each agent's parts come from the same `_section` output the skill uses, so they match by construction.

Nits: the `[1:]` order dependency and `_part`'s bare `StopIteration` (fixed in `cbe06fc`); the brief's lane files beside hats rule 1, which lives only in the Claude-only brief (deviation log).

Reconciliation notes: `docs/architecture.md` needs an ADR-0003 entry and the three agent types as a contract surface; ADR-0001 still describes the paste, which ADR-0003 replaces (ADR-0001 is Accepted and immutable, so ADR-0003 carries the reference); `skills/challenge/hat-agent.md` is a Claude-only file in the host-neutral tree that a later chat or Codex build must skip; the script has a few lines of headroom; and the parent's condensation has moved from the hats' input to the round's output.
