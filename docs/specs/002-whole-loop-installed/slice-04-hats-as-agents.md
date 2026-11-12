---
status: RECONCILED
dependencies: [adr-0003]
last_verified: 2026-11-12
frame_review: true
arch_review: true
claimed_by: claude/trusting-blackburn-a5b423
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 002-04 — the hats as plugin agents

**Goal:** `challenge`'s three hats run as coaster's own plugin agents. Each
carries its rules, has no tool that writes or runs commands, and runs on the
session's model, so a challenge round no longer depends on the parent pasting
the rules.

**DoR:**
- ✅ 002-02's AC 1 runs are recorded, with the failing log (`a1e`), in
  `evidence/slice-02-tool-calls.md`.
- ✅ Julien chose Option F on 2026-11-12.
- ✅ ADR-0003 is Accepted (2026-11-12).
- ✅ Julien agreed the amendments to 002-02 listed at the end of this slice on
  2026-11-12, and they are applied there.

**Acceptance Criteria:**

1. **The build renders three hat agents.** `scripts/build_host_packages.py`
   renders `hosts/claude/agents/skeptic.md`, `rival.md` and `customer.md`
   from source. Each file is frontmatter, then a short brief kept in source
   under `skills/challenge/`, then the four parts as 002-02's AC 6 cuts them,
   each byte-identical to the same part in the rendered `challenge`
   `SKILL.md`:
   - the hats' rules: `## Rules every hat follows` under `## Packaged: hats`,
     up to the next `## ` heading;
   - that hat's own section, from its `## ` heading up to the next `## `
     heading;
   - the whole `## Packaged: evidence rules` section;
   - the whole `## Packaged: challenge round template` section.

   The frontmatter gives the agent's `name`, a description that says it is
   started only by coaster's `challenge`, `tools: Read, Grep, Glob, WebSearch,
   WebFetch` and `model: inherit`. `--check` reports an agent file that is
   stale or missing, shown by a check that fails after one agent file is
   edited by hand and after one is deleted. The script stays under 200 lines.
2. **The brief.** Each agent's brief names its hat and tells it to read the
   whole dossier and any earlier rounds, to write nothing, and to use the
   evidence rules only to format its own new entries. It says that the link
   check and every change to the dossier belong to the parent and `scout`, and
   tells the hat to reply with its section only, in the shape of its part of the round
   template.
3. **`challenge` starts the agents and pastes nothing.** In Claude Code,
   `skills/challenge/SKILL.md` starts `coaster:skeptic`, `coaster:rival` and
   `coaster:customer` in one message. Their prompts carry only the hat's name,
   the dossier path, the paths of earlier round files and today's date, and
   restate, shorten or add to none of the hats' rules. It says that
   `challenge` does not run the link check, which belongs to `scout`. The
   parent writes `challenge/round-N.md` from the replies, with each hat's
   section under its heading as the hat replied it. Neither
   that file nor `templates/challenge-round.md` speaks of per-hat files any
   more. The chat path still writes one paste-in prompt per hat. The
   `challenge` item in `docs/inbox.md` is struck through with a pointer to
   this slice.
4. **Valid, and shipped as a pre-release.** `--check` and `claude plugin
   validate --strict hosts/claude` exit 0. After the path and term searches,
   the change ships as `0.1.0-pre.12`, with Julien's go-ahead for the push.
5. **Local runs before it ships.** One Sonnet run and one Opus run of
   `/coaster:challenge challenge this` from a `--plugin-dir` build of this
   slice, set up as 002-02's AC 1 runs were, each show:
   - three `Agent` calls with the `subagent_type`s `coaster:skeptic`,
     `coaster:rival` and `coaster:customer`, sharing one `message.id`;
   - each `Agent` prompt, recorded in full with local paths trimmed, carrying
     only the hat's name, the dossier path, the paths of earlier round files,
     today's date and at most one line asking the hat to begin, and stating no
     rule, limit, lens instruction or reply shape of its own;
   - in each hat's own transcript in the profile, a `prompt_snapshot` whose
     system prompt holds that agent file's body, apart from surrounding
     whitespace;
   - no `Bash`, `Write`, `Edit` or `NotebookEdit` call by any hat, every hat on
     the session's model, and each hat reading the whole dossier;
   - an empty `permission_denials`, and no tool call by the parent or a hat
     that reads, lists or searches `<root>`;
   - one `challenge/round-1.md` written by the parent.

   The record sets each hat beside the `a1e` and `a1g` rows of 002-02's
   comparison: whether its reply passes 002-02's AC 4, its `WebSearch` and
   `WebFetch` calls, its new entries, and its tokens and time. If a part of a
   hat's system prompt differs from its agent file, an `Agent` prompt breaks
   the list above, or a hat runs on another model, ADR-0003's kill criterion
   applies and nothing ships.

### Verification scenario

**Preconditions:** As in 002-02's AC 1 runs: 002-01's disposable profile,
signed in, with coaster `0.1.0-pre.11` installed and disabled for the run with
`--settings '{"enabledPlugins":{"coaster@coaster":false}}'`, because a copied
profile is not signed in. The run starts in a new empty `git init` folder
holding the framed copy of 002-01's dossier. No secrets.

**Invocation:**

```bash
claude -p '/coaster:challenge challenge this' --model sonnet --permission-mode acceptEdits --allowedTools "WebSearch,WebFetch" --output-format stream-json --verbose --plugin-dir hosts/claude --settings '{"enabledPlugins":{"coaster@coaster":false}}'
```

Then the same with `--model opus`, in its own folder.

Each hat's transcript is under the profile's `projects/` folder, in the run's
session folder, at `subagents/agent-<id>.jsonl`. Its `prompt_snapshot`
attachment holds the system prompt.

**Preserved behavior:** `capture`, `scout`, `frame`, `name` and `handoff`
render byte for byte as in `0.1.0-pre.11`. The chat path still writes one
paste-in prompt per hat. `challenge` runs only on an explicit request.

**Code revision / dirty-change identity:** Record the commit the local build
was made from. Raw logs and transcripts stay out of the repository. The
evidence is the table below and the run's tool calls, added to
`evidence/slice-02-tool-calls.md`.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1 | Three agent files, each part byte-identical to `challenge`'s; `--check` catches a stale or missing agent; under 200 lines | `hosts/claude/agents/skeptic.md`, `rival.md` and `customer.md` are rendered from `skills/challenge/hat-agent.md` and the challenge files. In each, the hats' rules, its own section, the evidence rules and the round template equal the same parts of the rendered `challenge` `SKILL.md` byte for byte. Each frontmatter has its `name`, a description that says only `challenge` starts it, `tools: Read, Grep, Glob, WebSearch, WebFetch` and `model: inherit`. On a scratch copy, `--check` names `agents/rival.md` after a hand edit and `agents/customer.md` after a deletion, and exits 1 both times. A renamed hat heading in `hats.md` stops the build with a named `ERROR:`. The script is 192 lines. | pass | the build; the guard runs |
| 2 | 2, 3 | The brief and `challenge`'s wording as specified; nothing pasted | The brief names the hat and says to read the whole dossier and earlier rounds, to write nothing, and to use the evidence rules only for its own new entries. It says the link check belongs to `scout` and every change to the dossier to the skill that started it, and to reply with its section only. `challenge` starts the three agents in one message, with prompts that hold the hat's name, the dossier path, earlier rounds and the date, "and nothing else". It says `challenge` does not run the link check, and has the parent copy each hat's section from its own heading on, without shortening it. The template says the parent writes the round from each hat's reply, and the chat path still pastes the full text into one prompt per hat. The inbox's `challenge` item is struck through. | pass | `skills/challenge/`; `templates/challenge-round.md`; `docs/inbox.md` |
| 3 | 4 | Valid, and shipped as `0.1.0-pre.12` | `--check` prints "in sync" and `claude plugin validate --strict hosts/claude` passes. The path search (bracketed home path, with no review sidecars present) and the 27-term search from the local `pre-publication` branch find nothing in the 27 changed files or the commit messages, and every subject is conventional. With Julien's go-ahead on 2026-11-12, the branch was pushed to `main` as a fast-forward, `c8480fa..8dbc2f7`. The test profile then updated from `0.1.0-pre.11` to `0.1.0-pre.12` at `8dbc2f7`, and its installed folder matches `hosts/claude` (`diff -rq`). | pass | the build; the searches; `git log origin/main` |
| 4 | 5 | The local Sonnet and Opus runs: the agents started with prompts that carry only the run's details, each with its file as its system prompt, none writing or running Bash, no denials, and research set beside `a1e` and `a1g` | **Judged: `f2s` (Sonnet) and `f2o` (Opus), built from `cbe06fc`:**<br>- the three agents started in one message;<br>- each prompt holds the hat's name, the dossier path, "Earlier rounds: none" and the date, and nothing else;<br>- every hat's system prompt equals its agent file's body, and all four parts match exactly;<br>- no hat ran Bash or wrote, each ran on the session's model and read the whole dossier;<br>- `permission_denials` is empty, nothing touched the build folder, and neither parent looked for the helper;<br>- one round file each, with the hats' sections copied as they replied.<br>At Sonnet the agents made more searches and returned more entries than the built-in types (2 and 4.3 a hat, against 1.5 to 1.7 and 3) but opened fewer pages and returned fewer `grounded` entries (0.3 and 0.3, against 0.5 and 0.5), on 23k tokens against 33k to 49k. At Opus they matched or passed `Explore` on every research measure: 3.7 searches, 7 pages and 8 entries (6.3 `grounded`).<br>**First runs at `b6052c4` (`f1s`, `f1o`), not judged:** the Sonnet prompts added a note on the lane files, which led to `cbe06fc` and the repeat. | pass | [evidence](evidence/slice-02-tool-calls.md#slice-002-04-the-hat-agents-local-runs-2026-11-12) |
| 5 | Preserved | The other five skills render unchanged | Against the installed `0.1.0-pre.11`, `diff -rq` finds `capture`, `scout`, `frame`, `name` and `handoff`, with both helpers, identical. Only the manifest, the README, `challenge`'s `SKILL.md` and the new `agents/` folder differ. | pass | `diff -rq` |

**DoD:**
- [x] All ACs pass, with the table above filled in from real runs.
- [x] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [x] Implementation review passed.
- [x] Deviation log produced under this slice heading.
- [x] Reconciliation sweep produced under this slice heading.
- [x] Reconciliation review passed.
- [x] `docs/refinement-todo.md` updated if any decisions were deferred during
      implementation. None was; the read-scope fold is parked in the inbox.

### Close-out (post-DONE)

- [ ] `docs/specs/README.md` regenerated by `workflow.py status-board`.

**Anti-horizontal-phasing check:** After this slice, someone running coaster
from a local build can ask for a challenge round and get one from three hats
that carry their own rules and cannot write.

### Amendments this slice proposes to 002-02

Proposed on 2026-11-12, agreed by Julien the same day, and applied to 002-02
as dated amendments under each AC.

- **Dependencies:** `[002-01, 002-04]`. 002-02's installed runs check this
  slice's change.
- **AC 1:** closed by the recorded comparison. The paste condensed in one run
  of five, so ADR-0003 replaces both built-in types with coaster's agents.
- **AC 2:** replaced by this slice's ACs 1 to 4.
- **AC 3:** the three `Agent` calls have the `subagent_type`s
  `coaster:skeptic`, `coaster:rival` and `coaster:customer`. The bullet about
  `Explore` hats moving to `general-purpose` is dropped. A hat on another model
  is ADR-0003's kill criterion.
- **AC 4:** a hat's reply is the `tool_result` of its `Agent` call or, when
  the hat runs in the background, the `summary` of the `task_notification`
  that names that call.
- **AC 5:** a concern or lens line in the round traces to a hat's reply when
  it keeps that concern's claim, cheapest test and urgency, or that lens's
  line. Shorter wording is allowed and recorded. In AC 1's four Sonnet runs the
  parent wrote the hats' concerns in fewer words than their replies, and this
  slice now asks it to copy each section as the hat replied it.
- **AC 6:** it has two halves. Each hat's system prompt is the
  `prompt_snapshot` in its own transcript in the profile, and the four parts
  are cut from the installed agent file. The allowed differences are
  unchanged. And each hat's `Agent` prompt, recorded in full with local paths
  trimmed, carries only what this slice's AC 5 lists.
- **AC 7:** met by ADR-0003. The `a1e` log stays the evidence. A failure of
  the amended AC 6 is ADR-0003's kill criterion.
- **Verification scenario:** coaster is updated to `0.1.0-pre.12` before the
  runs. AC 1's runs are done.

### Deviation log (after reconciliation)

The original slice is preserved above. Implementation notes:

1. **The first local runs were repeated.** In `f1s`, the Sonnet parent added "(lane files are under scout/ beside it)" to every hat's prompt. That is not on AC 5's list, and the record first judged it allowed. The compliance review held it to the list. ADR-0003's remedy was applied for the first time: `challenge` now says the prompt holds the four items "and nothing else" (`cbe06fc`), and both runs were repeated from that commit (`f2s`, `f2o`). The `f1` runs stay on record, unjudged. The same commit has the parent copy each hat's section from its own heading on, without shortening it, because the `f1s` parent had shortened them. In both judged runs the parent copied them.
2. **The brief splits the two jobs more plainly.** AC 2 says the link check and every change to the dossier "belong to the parent and `scout`". The brief says the link check belongs to `scout` and every change to the dossier to the skill that started the hat. The meaning is the same. The craft review asked for the plainer split.
3. **The agent files carry two more lines than AC 1 lists.** Between the brief and the four parts, the build adds the `INTRO` line, which says where each `## Packaged:` section ends, and the `## Packaged: hats` heading. Both come from the build, as in every skill, and the four parts are unchanged.
4. **The brief also sends hats to the lane files.** It tells each hat to read "the lane files the dossier links to", which AC 2 does not list. Hats rule 1 in `skills/_shared/hats.md` and the round template's opening note both say the hats read only the dossier and earlier rounds, and both are in each agent's system prompt, as is the brief. `challenge`'s own text says the same. So a hat sees two read scopes. Every hat in AC 1's runs read the lane files too. `docs/inbox.md` parks aligning all three places, which also reaches the chat path and the grilling hand-off.
5. **The README changed beyond the ACs.** It said coaster had "no agents", which became false, so it now describes the three hats. It also gained the pointer to `CONTRIBUTING.md` that 002-01's sweep left for the next change to the package, which this was.
6. **The build gained two small guards from the reviews.** A missing hat heading in `hats.md` stops the build with a named error, and the agents no longer depend on the order of `challenge`'s files. The four parts match the skill's by construction, since the agents and the skill both take them from the same `_section` output. No separate assertion checks it, which keeps the script at 192 lines.
7. **It shipped with the records before it.** The push to `main` was a fast-forward of eight commits, `c8480fa..8dbc2f7`: 002-02's comparison record, ADR-0003, this slice and the package change. All subjects are conventional, and the searches covered every changed file.
8. **Two small things in the judged Sonnet run.** Its round ends by saying the "Round 1 proposes:" notes "are not yet added", although its dossier has them. Its parent read the dossier with one compound Bash command, `cd … && cat … && ls -R`, which ran. Neither breaks an AC of this slice. 002-02 judges the rounds.
9. **The "nothing else" wording did not hold in the next Sonnet run.** In 002-02's installed Sonnet run, `i1s`, on `0.1.0-pre.12`, the parent again added a note on where the lane files are to every hat's prompt. That is 2 of 3 Sonnet runs on the agents (`f1s`, `i1s`; not `f2s`) and none of 3 Opus runs. ADR-0003 says a breach of the `Agent` prompt list "is met first by tightening `challenge`'s wording and running again. It reopens this choice only if it recurs after that." `i1s` is that recurrence, so under the ADR's own words Option F1 is reopened, although the note adds no rule, limit, lens instruction or reply shape, which is what the kill criterion names. Julien's ruling in 002-02 decides whether ADR-0003 stands as it is, with the list read to allow a note that only locates the dossier's own files, or is reopened. This slice's ACs are about what `challenge` says and the pre-ship runs, which passed.
10. **Two reviews were re-checks, and two were not repeated.** Compliance passed on a re-check by the reviewer that first returned needs-changes, not a fresh reviewer, as its record says. The craft and arch verdicts were given on `b6052c4`. Their nits were fixed in `cbe06fc` and not reviewed again by those passes; compliance's re-check covered `cbe06fc`.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `updated` | Describes the three hat agents and points at `CONTRIBUTING.md`. It ships in the package. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board`. |
| `docs/product-vision.md` | `no-op` | Scope and use cases are unchanged. |
| `docs/architecture.md` | `updated` | An ADR-0003 section, the agents in the package layout, the build's mechanics and the coupling, and the three agent types as a contract surface. |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `no-op` | `CLAUDE.md`'s Active specs lists only the worked example, by its own convention. There is no `AGENTS.md`. |
| `docs/inbox.md` | `updated` | The `challenge` item and the CONTRIBUTING-pointer item are struck through. A new item parks the hats' read scope. |
| `docs/refinement-todo.md` | `no-op` | No decision was deferred there. Aligning the hats' read scope is parked in `docs/inbox.md` (deviation 4), and the build's headroom under its 200-line bound is a kill criterion in ADR-0003. |
| `docs/memory/**` | `updated` | Learnings on background subagents and their replies, where a subagent's system prompt is recorded, and why a copied profile is not signed in. |
| `docs/decisions/adr-0003-hats-as-plugin-agents.md`, `docs/decisions/README.md` / ADR index | `updated` | ADR-0003 written, frame-reviewed and accepted, and the index regenerated and checked clean. |
| `docs/decisions/adr-0001-rendered-claude-package.md` | `no-op` | It is Accepted and immutable. ADR-0003 replaces only its paste for the hats, which ADR-0001's kill criterion names, and says so. |
| `docs/releases/claude-code-first-release.md` | `updated` | R-04's retirement path covers prompts that could start the hats, and the evidence line names both halves of the hat check. |
| `docs/specs/002-whole-loop-installed/spec.md`, `slice-02-challenge-round.md` | `updated` | The slice list, the hats decision, the Option F non-goal, A3, A4 and A8; and 002-02's amendments. |
| `hosts/claude/**`, `.claude-plugin/plugin.json` | `updated` | Rebuilt as `0.1.0-pre.12` and in sync by `--check`. |
| `skills/challenge/`, `templates/challenge-round.md`, `scripts/build_host_packages.py` | `updated` | The slice's implementation. |
| `evidence/slice-02-tool-calls.md`, `reviews/slice-04-*.md`, `docs/decisions/reviews/adr-0003-frame-critique.md` | `updated` | The local runs and the review verdicts. |
| `CONTRIBUTING.md` | `no-op` | Its build steps already cover anything under `skills/`, which now includes the agents' brief. |
| `docs/bugs/README.md` | `no-op` | No defect was found outside the slice's own scope. |
