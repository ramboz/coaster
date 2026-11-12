---
slice: 002-04 — the hats as plugin agents
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T17:30:54Z
prompt_source: review.py frame-critique docs/specs/002-whole-loop-installed/spec.md 002-04 <8 supporting files>
---

Frame-critique pass from one fresh reviewer.

The reviewer attacked the frame's main assumption: Claude Code loads a plugin agent's file body intact as its system prompt, keeps it to its `tools` line and runs it on the session's model. That rests on the 2.1.322 probe in ADR-0003's Context, and AC 5 checks it again before anything ships. The reviewer found no concrete way it fails.

The secondary notes were applied after the verdict:
- the tool limit is now grounded in the probe agent's calls, not its own report;
- AC 5 sets each hat's research and reply checks beside `a1e` and `a1g`, and adds an Opus run, since an Opus parent searched for the link-check helper;
- the proposed amendment to 002-02's AC 5 defines "traces to", and AC 3 asks the parent to copy each hat's section as the hat replied it;
- ADR-0003's B1 cites ADR-0001's note that the sibling packs ship plugin agents.

AC 3 and AC 5 also gained the `Agent` prompt allowlist that ADR-0003's own frame-critique asked for. The DoR still waits on ADR-0003's acceptance and Julien's agreement to the amendments.
