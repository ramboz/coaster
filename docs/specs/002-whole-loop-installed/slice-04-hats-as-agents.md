---
status: READY_FOR_IMPLEMENTATION
dependencies: [adr-0003]
last_verified:
frame_review: true
arch_review: true
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
| 1 | 1 | Three agent files, each part byte-identical to `challenge`'s; `--check` catches a stale or missing agent; under 200 lines | | not-run | |
| 2 | 2, 3 | The brief and `challenge`'s wording as specified; nothing pasted | | not-run | |
| 3 | 4 | Valid, and shipped as `0.1.0-pre.12` | | not-run | |
| 4 | 5 | The local Sonnet and Opus runs: the agents started with prompts that carry only the run's details, each with its file as its system prompt, none writing or running Bash, no denials, and research set beside `a1e` and `a1g` | | not-run | |
| 5 | Preserved | The other five skills render unchanged | | not-run | |

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
