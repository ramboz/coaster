---
status: IN_PROGRESS
dependencies: [002-01, 002-04]
last_verified:
frame_review: true
arch_review: true
claimed_by: claude/trusting-blackburn-a5b423
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 002-02 — the challenge round, installed

**Goal:** Run a challenge round from coaster installed from GitHub, with three
hats that write nothing and reply with their sections, and show from the run
logs that each hat received the packaged rules intact.

**DoR:**
- 002-01 is DONE, and its framed sample dossier is kept outside the repository.
- ✅ Julien accepted the decision that hats write nothing, with the type
  chosen by comparison, on 2026-11-11.
- 002-04 is DONE, so `0.1.0-pre.12` with the hats as plugin agents is on
  `main` (added by Julien's amendment, 2026-11-12).

**Acceptance Criteria:**

1. **The hats' subagent type is chosen by comparison.** Before the change
   ships, runs of `challenge` from local builds loaded with `--plugin-dir`, on
   the same copy of 002-01's framed dossier, start the hats one way each. The
   builds carry AC 2's draft wording and differ only in the subagent type: as
   `Explore` subagents, in one Sonnet run and one Opus run, and as
   `general-purpose` subagents told to write nothing, in one Sonnet run. AC 3's
   checks on writes, `Bash`, the model and reading the whole dossier, and AC 8's
   checks, apply to every one of these runs. The record sets the two types side
   by side, hat by hat: whether each reply passes AC 4, whether each hat read
   the whole dossier, its `WebSearch` and `WebFetch` calls and the sources it
   opened, the new evidence entries it returned, and its tokens and time.
   `Explore` is kept only if every one of its hats passes AC 3 and AC 4 and its
   research, in searches, sources opened and new entries, is not clearly below
   the `general-purpose` hats'. Otherwise the hats are `general-purpose`, and
   "write nothing" is an instruction that AC 3 checks rather than a missing
   tool. If the `general-purpose` hats also fail AC 3 or AC 8, AC 2 waits for
   Julien's decision. Julien sees the comparison before AC 2 ships the
   choice.

   **Amended by Julien, 2026-11-12:** closed by the recorded comparison
   ([evidence](evidence/slice-02-tool-calls.md#ac-1-the-two-types-hat-by-hat-2026-11-12)).
   The paste condensed in one run of five, so ADR-0003 replaces both built-in
   types with coaster's own agents, `coaster:skeptic`, `coaster:rival` and
   `coaster:customer` (002-04). AC 1's runs stay the evidence for ADR-0003.
   ACs 6 and 8 are judged on the runs of 002-04's change.
2. **Hats write nothing and reply with their section.** In Claude Code,
   `skills/challenge/SKILL.md` starts the three hats in parallel as subagents of
   the type AC 1 chose, tells the parent to paste the packaged sections
   unchanged, placeholders included, and has each hat reply with its section in
   the shape of the round template. Outside the pasted sections, it tells each
   hat that it uses the evidence rules only to format its own new entries, and
   that the link check and every change to the dossier belong to the parent and
   `scout`, so a hat neither runs a helper nor edits a file. The parent writes `challenge/round-N.md`
   from the replies. Neither that file nor `templates/challenge-round.md` speaks
   of per-hat files any more. The `challenge` item in `docs/inbox.md` is struck
   through with a pointer to this slice. The package is rebuilt, `--check` and
   strict validation exit 0, and the change ships as the next pre-release after
   the path and term searches.

   **Amended by Julien, 2026-11-12:** replaced by 002-04's ACs 1 to 4.
3. **Two rounds from the installed plugin.** On copies of 002-01's framed
   dossier, one Sonnet run and one Opus run of `/coaster:challenge challenge
   this` each show, in the log:
   - three `Agent` calls with the `subagent_type` AC 1 chose, sharing one
     `message.id`, so started together;
   - no `Write`, `Edit` or `NotebookEdit` call carrying one of those calls' ids
     as its `parent_tool_use_id`, and every `Bash` call that does carry one only
     reads, with each such command listed in the record;
   - each hat's own assistant events on the session's model;
   - each hat reading the whole dossier, by `Read` calls or a reading `Bash`
     command that together cover every line of it;
   - if `Explore` hats run on another model or skip part of the dossier, the
     hats move to `general-purpose` as in AC 1, the change ships as a
     pre-release, and both runs are repeated;
   - one `challenge/round-1.md` written by the parent, and no other new file
     under `challenge/`.

   **Amended by Julien, 2026-11-12:** the three `Agent` calls have the
   `subagent_type`s `coaster:skeptic`, `coaster:rival` and `coaster:customer`.
   The bullet about `Explore` hats moving to `general-purpose` is dropped. A hat
   on a model other than the session's is ADR-0003's kill criterion.
4. **Each hat's reply follows the hats' rules.** A hat's reply is the
   `tool_result` of its `Agent` call in the log. Each reply holds that hat's
   section in the round template's shape: what holds up before any concern, a
   line for each of the six lenses (a concern, or "nothing serious from this
   hat"), at most five concerns, each with why it matters, its cheapest test
   and a suggested urgency, and none of "fatal", "kill" or "will fail". New
   evidence carries the hat's prefix, `S`, `V` or `C`, in the evidence rules'
   format.

   **Amended by Julien, 2026-11-12:** a hat's reply is the `tool_result` of
   its `Agent` call or, when the hat runs in the background, the `summary` of
   the `task_notification` that names that call. In Claude Code 2.1.322 the
   hats ran in the background, and the `tool_result` was only a launch notice.
5. **The round is assembled from the replies, not written over them.** Each
   `round-1.md` has the headings of the packaged round template in order and
   opens with a "What holds up" summary. Every concern and lens line under a
   hat's heading traces to that hat's reply. The parent adds only the summary,
   the grouping of concerns that land on one risk, and the dispositions, each
   marked proposed. The readings in the dossier are unchanged except for a
   "Round 1 proposes:" note under each one the round touches.

   **Amended by Julien, 2026-11-12:** a concern or lens line in the round
   traces to a hat's reply when it keeps that concern's claim, cheapest test
   and urgency, or that lens's line. Shorter wording is allowed and recorded.
   In AC 1's four Sonnet runs the parent wrote the hats' concerns in fewer
   words than their replies, and 002-04 now asks it to copy each section as the
   hat replied it.
6. **Each hat received the packaged text intact.** This is the check ADR-0001
   and the release plan require before the tag. For every hat in every
   challenge run of this spec, its prompt is the `prompt` input of its `Agent`
   call in the log. The prompt must hold each of these, taken from the
   `challenge` `SKILL.md` that run loaded (the installed one, or for AC 1's
   runs the local build's), as one unbroken run of text:
   - the hats' rules: `## Rules every hat follows` under `## Packaged: hats`, up
     to the next `## ` heading;
   - that hat's own section, from its `## ` heading up to the next one or the
     end of `## Packaged: hats`;
   - the evidence rules: the whole `## Packaged: evidence rules` section, less
     its `## Packaged:` heading;
   - the round shape: the whole `## Packaged: challenge round template` section,
     less its `## Packaged:` heading.

   Three kinds of difference are allowed and recorded: whitespace, Markdown
   markup alone (a heading's level, a list marker, a code fence line), and a
   template placeholder such as `N` or `YYYY-MM-DD` filled with a value. Any
   other difference, a word left out, added or changed, is an omission or a
   condensation, and fails. The record lists each hat and part as found, with
   every allowed difference, or gives the first line that fails. The
   comparison runs as a short command kept outside the repository, and the
   record says what it did.

   **Amended by Julien, 2026-11-12:** the check has two halves (ADR-0003).
   Each hat's system prompt is the `prompt_snapshot` in its own transcript in
   the profile, and the four parts are cut from the installed agent file under
   `<root>/agents/`, not from the `Agent` call's `prompt`. The allowed
   differences are unchanged. And each hat's `Agent` prompt, recorded in full
   with local paths trimmed, carries only what 002-04's AC 5 lists: the hat's
   name, the dossier path, the paths of earlier round files, today's date and
   at most one line asking the hat to begin, with no rule, limit, lens
   instruction or reply shape of its own.
7. **A failed check stops here.** If any part of any hat's prompt fails AC 6,
   ADR-0001's kill criterion applies. This AC cannot pass until Julien has
   decided, in a new ADR, between Option F (each hat as a plugin agent, with its
   own slice in this spec) and another remedy. The failing log stays the
   evidence.

   **Amended by Julien, 2026-11-12:** met by ADR-0003, which chose Option F.
   The `a1e` log stays the evidence. A failure of the amended AC 6 is
   ADR-0003's kill criterion.
8. **Nothing else is read or denied.** In every run, `permission_denials` is
   empty, no tool call reads, lists or searches `<root>`, the `init` event lists
   coaster, Claude Code's built-in plugins and nothing else, its skills list
   holds no grilling or research skill that the profile does not block, no
   `Skill` call names a skill outside coaster, and every hat's
   `WebSearch` or `WebFetch` call ran under the session's grant. A run whose
   `init` event lists more is void and repeated, as the spec's Decisions say. A
   hat's denied search is recorded as such, and the run is not given a wider
   grant.

### Verification scenario

**Preconditions:** As in 002-01: the disposable profile, coaster updated to the
pre-release from AC 2, Julien signed in, `claude plugin list` showing only
coaster before each run, and any synced research or grilling skill blocked as
in 002-01. AC 1's three runs use local builds with `--plugin-dir` in a copy of
the profile with the installed coaster disabled, so their `init` event lists
the `--plugin-dir` copy in its place, which AC 8 expects. The rest use the
installed plugin. `<root>` is coaster's `path`
from the `init` event of the first run on that version. Each run starts in a
new empty `git init` folder holding a copy of 002-01's framed dossier. No
secrets.

**Invocation:** With `CLAUDE_CONFIG_DIR` set, and for ACs 3 to 8 without
`--plugin-dir`:

```bash
claude -p '/coaster:challenge challenge this' --model sonnet --permission-mode acceptEdits --allowedTools "WebSearch,WebFetch" --output-format stream-json --verbose
```

Then the same with `--model opus`. For AC 4, take each `Agent` call's
`tool_result` from the logs. For AC 6, take each `Agent` call's `prompt`, and
the four parts from the installed `challenge` `SKILL.md` under `<root>`.

**Amended by Julien, 2026-11-12:** coaster is updated to `0.1.0-pre.12` before
the runs, and AC 1's runs are done. For AC 4, a background hat's reply is the
`summary` of its `task_notification`. For AC 6, each hat's system prompt is in
its transcript under the profile's `projects/` folder, at
`<session>/subagents/agent-<id>.jsonl`, and the four parts come from
`<root>/agents/<hat>.md`.

**Preserved behavior:** `challenge` runs only on an explicit request (002-01's
AC 9 covers the runs where it was not asked for). The chat path still writes one
paste-in prompt per hat.

**Code revision / dirty-change identity:** Record the commit on `origin/main`
that was installed and the installed version. Raw logs and hat prompts stay out
of the repository. The evidence is the table below, the per-hat results of
ACs 4 and 6, and a list of each run's tool calls with home directory paths
trimmed, in `evidence/slice-02-tool-calls.md`.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1 | The two types compared hat by hat; the choice follows the comparison | Five runs from local builds: `Explore` on Sonnet (`a1e`, `a2e`) and Opus (`a1o`), and `general-purpose` on Sonnet (`a1g`, `a2g`). Every `Explore` hat passes AC 3's checks on writes, Bash, the model and reading the whole dossier, every reply of either type meets AC 4, and at Sonnet both types research the same amount, with `Explore` on about two thirds of the tokens. On Opus, `Explore` hats ran on Opus. The rule would keep `Explore`, but both types fail AC 8 (step 7), and one run fails AC 6 (step 6). So AC 2 waits for Julien. | pass, as amended: Julien saw the comparison and chose Option F (ADR-0003) | [evidence](evidence/slice-02-tool-calls.md#ac-1-the-two-types-hat-by-hat-2026-11-12) |
| 2 | 2 | Source and template speak only of replies; rebuilt, valid and shipped | Replaced by 002-04's ACs 1 to 4 (amendment). `challenge` and the template speak only of the hats' replies, the inbox item is struck through, and `0.1.0-pre.12` shipped at `8dbc2f7` after the searches. | pass, as amended | [002-04](slice-04-hats-as-agents.md) |
| 3 | 3 | Three hats of the chosen type started together on the session's model, none writing; one round file per run | **`i1s` (Sonnet) and `i1o` (Opus), installed `0.1.0-pre.12`:** the three `Agent` calls are `coaster:skeptic`, `coaster:rival` and `coaster:customer`, sharing one `message.id`. No hat called `Bash`, `Write`, `Edit` or `NotebookEdit`. Each ran on the session's model and read the whole dossier with `Read`. Each run wrote one `challenge/round-1.md`, and nothing else under `challenge/`. | pass | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 4 | 4 | Every hat's reply follows the hats' rules | All six replies, from their `task_notification`s, lead with what holds up, cover the six lenses, hold at most five concerns with why, test and urgency, and use no word from the list. Every entry carries its hat's prefix. One entry breaks the evidence rules' format: `i1s`'s Skeptic tagged S-01 `[grounded-lead, unverified until opened]` rather than `[unverified]`. The entry says itself that it stays unverified, and carries links and a date. | `i1o` pass; `i1s` fails on one tag, awaiting Julien's ruling | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 5 | 5 | Each round traces to its hats' replies | Both rounds have the template's headings in order and open with "What holds up". Every concern and lens line under a hat's heading appears in its reply. Every disposition is marked proposed. In each dossier no line was removed or changed: only "Round 1 proposes:" notes were added, and in `i1o` an index of the hats' new entries in the Evidence section. | pass | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 6 | 6 | All four parts intact in every hat prompt, allowed differences listed | **System prompts:** in both installed runs, every hat's system prompt equals its installed agent file's body, and all four parts match exactly, with no difference to allow. **`Agent` prompts:** `i1o`'s hold only the hat's name, the dossier path, the earlier rounds and the date. Each `i1s` prompt also says "(lane files are in the scout/ folder beside it)", which is not on the list, although `cbe06fc` told the parent "nothing else". It adds no rule, limit, lens instruction or reply shape. ADR-0003 says a breach of this list that recurs after the wording is tightened reopens its choice, and this is that recurrence. AC 1's `a1e` failure stays the evidence for ADR-0003. | `i1o` pass; `i1s` fails the prompt list, awaiting Julien's ruling on ADR-0003 | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 7 | 8 | No denials, no read of `<root>`, only coaster loaded, hats searched under the grant | Every `init` lists `coaster@coaster` `0.1.0-pre.12` and the built-in plugins only, with both research skills blocked by the profile's deny rules and no grilling skill. `permission_denials` is empty in every `result` event, nothing reads, lists or searches `<root>`, no `Skill` call was made, and every hat search ran. AC 1's runs failed this AC, and their denials led to ADR-0003. | pass | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |

**DoD:**
- [ ] All ACs pass, with the table above filled in from real runs.
- [ ] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [ ] Implementation review passed.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [ ] Reconciliation review passed.
- [ ] `docs/refinement-todo.md` updated if any decisions were deferred during
      implementation.

### Close-out (post-DONE)

- [ ] `docs/specs/README.md` regenerated by `workflow.py status-board`.
- [ ] The release plan's check that each hat received the packaged rules intact
      points at this slice's record.

**Anti-horizontal-phasing check:** After this slice, someone who installs
coaster from GitHub can ask for a challenge round and get one written from
three independent hats, each working from the full rules.
