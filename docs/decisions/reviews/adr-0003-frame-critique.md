---
adr: 0003
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T17:34:17Z
prompt_source: review.py frame-critique docs/decisions/adr-0003-hats-as-plugin-agents.md, then a re-check by the same reviewer
---

Frame-critique pass, reached by one reviewer in two steps. The second was a re-check by the same reviewer, not a fresh review.

- Round 1 (needs-changes): the ADR said nothing could be condensed because nothing is pasted, but the parent still writes each hat's prompt and still holds the full rules. Checking only the system prompt would pass by construction and miss a parent that adds an edited restatement. Secondary notes: the hats keep `Glob`/`Grep`/`Read`, which could search the plugin's folder; and R-04's activation test might never see a hat started for other work. Fixed: the release check has a second half, each `Agent` prompt recorded in full and held to a list of what it may carry; two new kill criteria cover a prompt that breaks that list and a hat that searches the plugin's folder; B4 states the wording dependence; the release plan's R-04 line asks for prompts that could pull in the hats and a record of `Agent` calls. A second probe settled the Opus case, and the tool limit is grounded in the calls the agent made.
- Re-check (pass): all findings resolved. Two follow-ups were applied after the verdict: the release plan's "evidence to inspect" line now names both halves of the check, and the kill criteria say that a breach of the prompt list is met first by tightening `challenge`'s wording.
