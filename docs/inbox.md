# Inbox

> Status: Draft (wizard-generated)
>
> Thin capture layer for unresolved ideas, observations, and items that surfaced during
> sessions but aren't ready for a spec. Triage during reconciliation or session end:
> (a) promote to a spec, (b) promote to an ADR, (c) drop.
>
> This is NOT a task list. Items here are parked thoughts, not committed work.

<!-- Add items below. Format: - [date] description -->
- ~~[2026-11-11] Add a pointer to `CONTRIBUTING.md` in the README (spec 003's sweeps). `README.md` is copied into the package, so do it in the next PR that changes the package anyway, with that PR's pre-release bump or release.~~ Done in slice 002-04's `0.1.0-pre.12`.
- [2026-11-11] The elicitation hashes in `docs/product-vision.md` and `docs/architecture.md` no longer match sections edited in spec 001. Refresh them on the next `/jig:vision-elicitation` run, choosing skip so the edits become the baseline.
- [2026-11-09] `capture` step 2 sends question 5's answer to Intent, while step 3 and the evidence rules send a claim such as "nothing does this" to Evidence. One sentence should say which wins.
- ~~[2026-11-09] `challenge` starts "read-only subagents" and then has each one write a section file. Settle this in scope 2.~~ Settled by [slice 002-04](specs/002-whole-loop-installed/slice-04-hats-as-agents.md): the hats are plugin agents that cannot write, and reply with their sections (ADR-0003).
- [2026-11-09] `capture`'s rule that a briefly answered question is not unstated is stricter than 001-01's amended AC 8. Align them when `capture` next changes.
- [2026-11-11] `frame` still tries Bash edits (inline `python3 -`, `sed -i`) before its file tools, which an interactive user is asked about; `scout`'s file-tools line may help it. `handoff` is different: in 002-01's final run it tried a `sed -i` that added a `handoff.md` line to the dossier, a second write its "writes one file and stops" rule forbids, and AC 8 held only because the command was denied. The fix there is to keep `handoff` to its one file, and to settle who records `handoff.md` in the dossier's sibling index, not to give it file tools.
- [2026-11-11] In one of 002-01's pre.5 runs, `scout` tagged an entry `grounded` with "same thread as DEM-01" in place of its own link. The evidence rules want a link on every `grounded` entry; consider saying so in `scout`'s Extract step.
- [2026-11-11] `scout` and `name` say "If the helper is refused, try no other command", while 002-01's AC 2 says "refused or fails". On a failure the text routes to the web or to "not run", which excludes another command only by implication. Say "refused or fails" in the next change to either skill.
- [2026-11-11] In 002-01's run `s5b`, `name` had web tools but marked the registry and GitHub columns "not checked" instead of doing those lookups on the web, as its text says to. Consider making the web route for registries explicit.
- [2026-11-12] The hats' brief (`skills/challenge/hat-agent.md`) sends each hat to the lane files the dossier links to, while three places say the hats read only the dossier and earlier rounds: hats rule 1 in `skills/_shared/hats.md`, the opening note of `templates/challenge-round.md` (both in each agent's system prompt), and `skills/challenge/SKILL.md`. Align all three with the brief the next time any of them changes, so the agents, the chat path and the grilling hand-off get one scope (slice 002-04's deviation 4).
