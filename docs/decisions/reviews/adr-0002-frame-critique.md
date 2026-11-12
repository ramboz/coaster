---
adr: 0002
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T01:10:10Z
prompt_source: review.py frame-critique docs/decisions/adr-0002-helpers-ask-for-bash.md, then two re-checks by the same reviewer
---

Frame-critique pass, reached by one reviewer in three steps. The second and third were re-checks by the same reviewer, not fresh reviews.

- Round 1 (needs-changes): the ADR stated A2's cost as fact while calling A2 unrun, and Claude Code's "don't ask again" might offer a bare `python3` prefix. It left out Option D (executable helpers run by their own path), and its fallback, Option B, was hollow. Julien then ran the interactive probe: "don't ask again" saved `Bash(python3 *)`. The ADR now records that, adds Option D, and states Julien's choice to keep jig's form and warn users.
- Re-check 1 (needs-changes): the README warning is out of view at the prompt, the new kill criterion could not fire, and spec 002, 002-01 AC 10 and 002-03 still described A2 the old way. Fixed: `scout` and `name` warn just before each helper runs (0.1.0-pre.8); the scope-4 release check is the standing trigger, tracked in refinement-todo; the three records carry dated amendments.
- Re-check 2 (pass): all three resolved. Notes: nothing yet checks that the in-session warning is shown, which 002-01's pre.8 runs now check; the warning's claim rests on Claude Code 2.1.322, and the scope-4 review can re-probe it; and one wording nit, fixed after the verdict.
