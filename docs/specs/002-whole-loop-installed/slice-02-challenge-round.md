---
status: RECONCILED
dependencies: [002-01, 002-04]
last_verified: 2026-11-12
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
- ✅ 002-01 is DONE, and its framed sample dossier is kept outside the repository.
- ✅ Julien accepted the decision that hats write nothing, with the type
  chosen by comparison, on 2026-11-11.
- ✅ 002-04 is DONE, so `0.1.0-pre.12` with the hats as plugin agents is on
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

   **Ruled by Julien, 2026-11-12:** an entry whose tag is not one of the five
   but whose own text names its provenance, as `i1s`'s S-01
   (`[grounded-lead, unverified until opened]`, with "they stay `unverified`"
   and its links and date), is a format slip that is allowed and recorded,
   not a failure. An entry with no tag, or one that claims more than its
   source supports, still fails.
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

   **Ruled by Julien, 2026-11-12:** the parent's own notes on the ledger, as
   in `i1o`'s "Parent's notes on the evidence", are allowed and recorded. They
   are part of putting the hats' new evidence into the ledger, which
   `challenge` asks of the parent. They can say which entries share a source,
   which entry updates an earlier one, and which entries rest on thin
   listings, and they can propose a strike. A note that changes a hat's
   concern or lens line, or that strikes or changes a dossier entry rather
   than proposing it, still fails.

   **Ruled by Julien, 2026-11-12:** the readings a round touches are the
   readings with content that the round affects, as `challenge`'s "each
   affected reading" says. A lens that was not looked at has no reading to
   change, so `i1s` meets this AC without a note under "Not looked at". A note
   there, as in `i1o`, is allowed. A reading with content that a disposition
   proposes to change, left without a note, still fails.
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

   **Ruled by Julien, 2026-11-12:** a note that only says where the dossier's
   own files are, such as `i1s`'s "(lane files are in the scout/ folder beside
   it)", counts as part of the dossier path. It is allowed and recorded.
   ADR-0003 stands: the recurrence in `i1s` after `cbe06fc` does not reopen
   Option F1, because the note adds nothing the list guards against. A note
   that states a rule, limit, lens instruction or reply shape still fails.
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

**Recorded revision:** ACs 3 to 8 were judged on coaster `0.1.0-pre.12`, installed from GitHub at `8dbc2f7` into 002-01's disposable profile, with Claude Code 2.1.322: one Sonnet run (`i1s`) and one Opus run (`i1o`). The installed folder matched `hosts/claude` (`diff -rq`). AC 1's five runs used local builds of the draft wording on top of `c8480fa`, which differed only in the subagent type. The run IDs are the headings in [evidence/slice-02-tool-calls.md](evidence/slice-02-tool-calls.md). Raw logs, and the long prompts AC 1's parents pasted, stay out of the repository. The hat agents' short `Agent` prompts are quoted there in full, as ADR-0003 asks.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1 | The two types compared hat by hat; the choice follows the comparison | Five runs from local builds: `Explore` on Sonnet (`a1e`, `a2e`) and Opus (`a1o`), and `general-purpose` on Sonnet (`a1g`, `a2g`). Every `Explore` hat passes AC 3's checks on writes, Bash, the model and reading the whole dossier, every reply of either type meets AC 4, and at Sonnet both types research the same amount, with `Explore` on about two thirds of the tokens. On Opus, `Explore` hats ran on Opus. The rule would keep `Explore`, but both types fail AC 8 (step 7), and one run fails AC 6 (step 6). So AC 2 waits for Julien. | pass, as amended: Julien saw the comparison and chose Option F (ADR-0003) | [evidence](evidence/slice-02-tool-calls.md#ac-1-the-two-types-hat-by-hat-2026-11-12) |
| 2 | 2 | Source and template speak only of replies; rebuilt, valid and shipped | Replaced by 002-04's ACs 1 to 4 (amendment). `challenge` and the template speak only of the hats' replies, the inbox item is struck through, and `0.1.0-pre.12` shipped at `8dbc2f7` after the searches. | pass, as amended | [002-04](slice-04-hats-as-agents.md) |
| 3 | 3 | Three hats of the chosen type started together on the session's model, none writing; one round file per run | **`i1s` (Sonnet) and `i1o` (Opus), installed `0.1.0-pre.12`:** the three `Agent` calls are `coaster:skeptic`, `coaster:rival` and `coaster:customer`, sharing one `message.id`. No hat called `Bash`, `Write`, `Edit` or `NotebookEdit`. Each ran on the session's model and read the whole dossier with `Read`. Each run wrote one `challenge/round-1.md`, and nothing else under `challenge/`. | pass | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 4 | 4 | Every hat's reply follows the hats' rules | All six replies, from their `task_notification`s, lead with what holds up, cover the six lenses, hold at most five concerns with why, test and urgency, and use no word from the list. Every entry carries its hat's prefix. One entry breaks the evidence rules' format: `i1s`'s Skeptic tagged S-01 `[grounded-lead, unverified until opened]` rather than `[unverified]`. The entry says itself that it stays unverified, and carries links and a date. | pass, as ruled: S-01's tag is a recorded format slip | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 5 | 5 | Each round traces to its hats' replies | Both rounds have the template's headings in order and open with "What holds up". Every concern and lens line under a hat's heading appears in its reply, and each round says all its dispositions are proposed. In each dossier no line was removed or changed. `i1s` added "Round 1 proposes:" notes under Open and Wanted, the only readings with content, since the other four lenses were skipped at the user's request. Its round also bears on those four (G5 on the business model, G7 on setup, trust and iOS push), but it added no note under "Not looked at". `i1o` added notes under Open, Wanted and "Not looked at", and one under shape A, and indexed the hats' new entries in the Evidence section. `i1o`'s round also adds "Concern groups", the grouping AC 5 allows, and "Parent's notes on the evidence", which AC 5's three additions do not cover. It notes duplicate sources, one price update, one proposed strike, and thin listings. | pass, as ruled: `i1o`'s notes on the evidence are allowed, and `i1s` needs no note under a lens that was not looked at | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 6 | 6 | All four parts intact in every hat prompt, allowed differences listed | **System prompts:** in both installed runs, the first block of every hat's system prompt equals its installed agent file's body, apart from surrounding whitespace. All four parts match exactly, with no difference to allow. **`Agent` prompts:** `i1o`'s hold only the hat's name, the dossier path, the earlier rounds and the date. Each `i1s` prompt also says "(lane files are in the scout/ folder beside it)", although `cbe06fc` told the parent "nothing else". The note adds no rule, limit, lens instruction or reply shape. Before the ruling it was recorded as a recurrence that, under ADR-0003's remedy line, would reopen Option F1. AC 1's `a1e` failure stays the evidence for ADR-0003. | pass, as ruled: the lane-file note counts as part of the dossier path, and ADR-0003 stands | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |
| 6a | 7 | A failed check stops the slice until Julien decides in a new ADR | AC 1's `a1e` failed AC 6. Julien chose Option F on 2026-11-12, recorded and accepted in ADR-0003, and slice 002-04 built it. The `a1e` log stays the evidence. | pass, as amended | [ADR-0003](../../decisions/adr-0003-hats-as-plugin-agents.md) |
| 7 | 8 | No denials, no read of `<root>`, only coaster loaded, hats searched under the grant | Every `init` lists `coaster@coaster` `0.1.0-pre.12` and the built-in plugins only, with both research skills blocked by the profile's deny rules and no grilling skill. `permission_denials` is empty in every `result` event, nothing reads, lists or searches `<root>`, no `Skill` call was made, and every hat search ran. AC 1's runs failed this AC, and their denials led to ADR-0003. | pass | [evidence](evidence/slice-02-tool-calls.md#slice-002-02-the-installed-runs-2026-11-12) |

**DoD:**
- [x] All ACs pass, with the table above filled in from real runs.
- [x] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [x] Implementation review passed.
- [x] Deviation log produced under this slice heading.
- [x] Reconciliation sweep produced under this slice heading.
- [x] Reconciliation review passed.
- [x] `docs/refinement-todo.md` updated if any decisions were deferred during
      implementation. None was; the follow-ups are parked in the inbox.

### Close-out (post-DONE)

- [ ] `docs/specs/README.md` regenerated by `workflow.py status-board`.
- [x] The release plan's check that each hat received the packaged rules intact
      points at this slice's record. Done when the AC 6 ruling was recorded.

**Anti-horizontal-phasing check:** After this slice, someone who installs
coaster from GitHub can ask for a challenge round and get one written from
three independent hats, each working from the full rules.

### Deviation log (after reconciliation)

The original slice is preserved above, with each amendment and ruling dated under its AC. Implementation notes:

1. **The slice changed course after AC 1.** AC 1's comparison found the paste condensed in one run of five (`a1e`, AC 6), and both built-in types failed AC 8. Julien chose Option F, recorded in ADR-0003, and slice 002-04 built the hats as plugin agents. 002-04 became a dependency, AC 2 was replaced by its ACs 1 to 4, and ACs 1, 3 to 7 and the verification scenario carry Julien's dated amendments. ACs 3 to 8 were judged on the installed `0.1.0-pre.12`. "Option F" is ADR-0001's name for the remedy, and ADR-0003 calls its version Option F1. AC 7's amendment and ADR-0003's Status line use the first name, and the rulings the second, for the same choice.
2. **AC 1 ran more runs than it asked for, on the profile itself.** AC 1 asked for three runs. Two more were made, `a2e` and `a2g`, a second Sonnet run of each type, to see how often each result recurs. A copied profile is not signed in, so each AC 1 run loaded the local build with `--plugin-dir` and disabled the installed coaster for that run alone with `--settings`, in place of the copy the Preconditions describe. The local builds were not version-bumped, so their manifests say `0.1.0-pre.11`. The record names the commit they were built on and the one line that differs between them. The installed runs used neither flag.
3. **The hats ran in the background.** In Claude Code 2.1.322, each `Agent` call's `tool_result` was only a launch notice, and the reply came later in a `task_notification`. AC 4 was amended to read the reply there. A background hat cannot ask for permission, so in AC 1's runs every compound Bash command a hat tried was denied, which is how both built-in types failed AC 8.
4. **The installed runs came before 002-04 was DONE.** The DoR asks for 002-04 to be DONE. `0.1.0-pre.12` was on `main` at `8dbc2f7` when `i1s` and `i1o` ran, but 002-04 was REVIEWED; it was reconciled and closed after the runs were recorded. No package byte changed between `8dbc2f7` and 002-04's close at `c42dd27` (`git diff --stat` over the package paths is empty), so the runs judged the package 002-04 closed with. Its deviation 9 records what `i1s` showed about its wording.
5. **Four points pass only by Julien's rulings.** S-01's off-list evidence tag (AC 4), `i1o`'s notes on the evidence (AC 5), `i1s` leaving no note under the lenses that were not looked at (AC 5) and `i1s`'s lane-file note in each hat prompt (AC 6) are allowed and recorded. Each ruling is a dated note under its AC and an entry in `docs/decisions/lightweight-decisions.md`, and each says what still fails. That file describes itself as holding decisions outside spec slices, and its rubric sends a load-bearing choice with rejected alternatives to an ADR. The four are scoped to this slice and were recorded there knowingly: the AC 6 ruling reads ADR-0003's list and remedy line without changing its decision, and ADR-0003 now carries a dated note pointing at it (deviation 6).
6. **ADR-0003's wording assumption held in four of six runs on the agents.** Its B4 assumes the parent keeps each hat's prompt to the run's details. The Sonnet parent added a lane-file note in `f1s` and again in `i1s`, after `cbe06fc` said "nothing else"; `f2s` and the three Opus runs did not. ADR-0003's remedy line would treat `i1s` as reopening Option F1. Julien's AC 6 ruling settles it: the note counts as part of the dossier path, and ADR-0003 stands. `challenge` still says "and nothing else: no notes", stricter than the check now is. Changing it is a package change, so it waits for the read-scope item in `docs/inbox.md`, which may remove the note's cause. ADR-0003's B1 held in both installed runs: each hat was listed as `coaster:<name>`, ran on the session's model, used only its tools and had its agent file's body as its system prompt. Read alone, ADR-0003's remedy line said the opposite of the ruling. The arch and reconciliation reviews flagged the missing pointer, and on Julien's go-ahead a dated note after that line now points at the ruling, as `docs/conventions.md` allows for an Accepted record. The spec's hats decision and `docs/architecture.md` point at the ruling too, and the release plan points at this slice's record.
7. **The two models assemble the round differently.** The judged Opus parents (`a1o`, `f2o`, `i1o`) indexed the hats' new entries in the dossier's Evidence section before the user confirmed anything, and the record shows no Sonnet parent doing so. `i1o` also added headings of its own for the grouping and the notes on the evidence, and noted "Not looked at" and shape A; `i1s` did neither. `challenge` does not say where or when new evidence goes into the ledger, the template has no heading for the grouping, and "each affected reading" left the two installed runs placing notes differently. All three are parked in one `docs/inbox.md` item, beside the hats' read scope, the likely cause of the Sonnet lane-file note. Each item names the rulings it could retire.
8. **The record was corrected after review.** The evidence file was written before Julien's rulings, so it still called the lane-file note a breach and left S-01 at `CHECK`. `i1o`'s AC 5 was first marked a pass before its notes on the evidence were judged. And row 5 first said the shapes went without a note, when the shapes are not readings and the open question was the skipped lenses. The compliance and craft reviews caught these; `511e0e8`, `a2a9945` and the ruling commits fixed the record. Both passes were re-checked by the reviewers that returned needs-changes, not by fresh reviewers. Arch passed on the first review.
9. **One close-out item was done before DONE.** The release plan's check that each hat received the packaged rules intact was pointed at this slice's record, which carries the AC 6 ruling, when the ruling was recorded.
10. **ADR-0003's B2 is still untested.** It assumes the main model does not start the hats for work outside `challenge`. Only R-04's activation test, which the release plan tracks before the tag, can show a leak. Every run in this slice asked for a challenge round.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `no-op` | 002-04 already describes the three hat agents. Nothing in the package changed in this slice. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board` at RECONCILED and again at DONE. |
| `docs/product-vision.md` | `no-op` | Scope and use cases are unchanged. |
| `docs/architecture.md` | `updated` | The ADR-0003 section points at the AC 6 ruling. |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `no-op` | `CLAUDE.md`'s Active specs lists only the worked example, by its own convention. There is no `AGENTS.md`. |
| `docs/inbox.md` | `updated` | Two items: the hats' read scope, and how `challenge` assembles a round (ledger entries, parent notes, the grouping, which readings get a note). Each names the rulings it could retire. |
| `docs/refinement-todo.md` | `no-op` | No decision was deferred there. Both follow-ups are parked in the inbox. |
| `docs/memory/**` | `no-op` | The learnings from these runs (background subagents, system prompts in transcripts, copied profiles) were recorded with 002-04. |
| `docs/decisions/lightweight-decisions.md` | `updated` | Julien's four rulings on ACs 4, 5 (two) and 6. |
| `docs/decisions/adr-0003-hats-as-plugin-agents.md` | `updated` | Accepted, so append-only. A dated note after its remedy line points at the AC 6 ruling, added on Julien's go-ahead. The decision is unchanged. |
| `docs/releases/claude-code-first-release.md` | `updated` | The release check that each hat received the rules intact points at this slice's record, which carries the rulings, and its evidence. |
| `docs/specs/002-whole-loop-installed/spec.md` | `updated` | The hats decision points at the AC 6 ruling. |
| `evidence/slice-02-tool-calls.md`, `reviews/slice-02-*.md` | `updated` | The comparison runs, the installed runs with the rulings, and the review verdicts. |
| `hosts/claude/**`, `skills/**`, `templates/**`, `scripts/**` | `no-op` | No package change in this slice; 002-04 shipped `0.1.0-pre.12`. |
| `docs/bugs/README.md` | `no-op` | No defect was found outside the slice's own scope. |
