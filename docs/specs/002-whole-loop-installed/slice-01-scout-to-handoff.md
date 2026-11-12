---
status: IN_PROGRESS
dependencies: [001-02]
last_verified:
frame_review: true
arch_review: true
claimed_by: claude/spec-002-01-scout-to-handoff
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 002-01 — scout to handoff, installed

**Goal:** Take a dossier from coaster installed from GitHub through `scout`'s
quick pass, `frame`, `name` and `handoff`, with both helpers running from the
installed plugin after the user's ordinary Bash permission, and no packaged
file read.

**DoR:**
- ✅ Spec 001 is DONE, and `0.1.0-pre.2` is on `origin/main`.
- ✅ Probes on 2026-11-11 showed the default denials and the helpers' file
  mode (see the spec's Current state).
- Julien has signed in to a new disposable profile with coaster installed from
  GitHub. 001-02's profile is not reused, because synced plugins joined it.
- ✅ Julien accepted the spec's decisions on 2026-11-11.

**Acceptance Criteria:**

1. **Helpers run through an interpreter.** In `skills/scout/SKILL.md` and
   `skills/name/SKILL.md` each helper is run as `python3 scripts/<file>`. The
   build's `HELPERS` map matches that form, and the rendered skills say
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"`, the form
   jig uses for its own helpers. The build's
   rewrite and its guard against an unrewritten helper reference work on the
   new form, shown by a build that fails when one reference is left in source
   form. `--check` exits
   0, `claude plugin validate --strict hosts/claude` exits 0, a search of the
   rendered skills for `` `scripts/ `` and `allowed-tools` finds nothing, and the
   script stays under 200 lines.
2. **A refused helper is not worked around, and nothing is filled in.**
   `scout` and `name` each say what to do when the helper is refused or fails:
   try no other command to the same end, take the web route the skill already
   gives for chat if those tools are allowed and say so, and otherwise record
   "not run", the reason and the command to run by hand. In one `scout` run and
   one `name` run with the helper withheld and the web tools granted:
   - the only `Bash` calls denied are the helper command, and no other `Bash`
     call makes a network request;
   - every link-check, registry or GitHub result recorded in the dossier or
     `naming.md` traces to a `WebFetch` or `WebSearch` call in the log, and says
     it came from the web route;
   - every check with no such call is marked "not run" with the reason and the
     command.

   **Amended by Julien, 2026-11-11:** a denied `Bash` command that only writes
   inside the run folder, and that the run then makes with `Write` or `Edit`,
   is allowed and recorded. Sonnet tried such a heredoc in every `scout` run on
   `0.1.0-pre.2` and `0.1.0-pre.4`, a habit of the model rather than of the
   package. `scout` was also told to create its files with the file-writing
   tool.
3. **Helpers run from the installed plugin, on something to check.** `<root>` is
   the `path` the run's `init` event gives for `coaster`. `scout`'s Process step
   checks the links after the entries are filed, since `link_check.py` reads
   only Markdown already on disk. With each helper granted by its full path, the
   `scout` run's log shows `python3 "<root>/skills/scout/scripts/link_check.py"`
   run on the dossier folder after the `scout/` files are written. Its summary
   line counts more than zero URLs, as many as the unique URLs cited in that
   folder's Markdown at that point, and the dossier's Evidence section records
   it with the date. The `name` run's log shows
   `python3 "<root>/skills/name/scripts/name_check.py"` run on the candidates,
   and `naming.md` carries its rows with the date.
4. **`scout`'s quick pass files evidence by the rules.** On a dossier written by
   the installed `capture` for spec 001's sample idea, one `scout` run asked for
   the Landscape and Demand lanes:
   - writes one file per lane under `scout/`, with the entries labelled as a
     quick pass and at most ten per lane;
   - gives every entry its lane prefix, a number, a tag from the evidence rules,
     and the source fields that tag requires;
   - cites, for every entry tagged `grounded`, a URL that a `WebFetch` call in
     the log opened;
   - adds an index line to the dossier's Evidence section for each load-bearing
     entry, sets `status: scouted`, and sets `last_scouted` to today.
5. **Without web tools, `scout` says so.** In one run with `WebSearch` and
   `WebFetch` withheld, `scout` states that the quick pass could not search,
   and adds no entry whose source no tool call returned.
6. **`frame` reads, suggests, and records only the user's call.** On the
   scouted dossier, a first turn asking for the Open and Wanted lenses refreshes
   `## At a glance` with a one-word summary for those two, "not looked at" for
   the other four, the count of `grounded` entries out of the total, and a call
   labelled as a suggestion. It sets `status: framed` and leaves `## Decisions`
   unchanged. A second turn that says "Go." appends a dated go with every open
   risk carried forward, and sets `decision: go` and `status: decided`.
7. **`name` shortlists with its checks.** One run with a naming brief in the
   prompt writes `naming.md` with every heading of the packaged naming template
   in order, at least five shortlisted candidates each with its strongest
   argument and its main collision, and a plain statement that this is not
   trademark clearance. A second turn that picks one records the pick and its
   reason under `## Decisions` in the dossier.
8. **`handoff` writes one file.** One run on the decided dossier writes
   `handoff.md` with every heading of the packaged handoff template in order,
   Appetite left `TBD`, and no use case that the dossier does not state. The run
   writes no other file and starts no other skill.
9. **No packaged file is read, and only withheld tools are denied.** In every
   run of this slice:
   - `permission_denials` holds only calls to the tools that run deliberately
     withheld: the helper command in AC 2's runs, and `WebSearch` and
     `WebFetch` in AC 5's;
   - no tool call reads, lists or searches `<root>`, other than the two helper
     commands;
   - every new or changed file is under `docs/prospects/<slug>/`;
   - the `init` event lists `coaster` from the `coaster` marketplace at the
     version under test, Claude Code's built-in plugins, and nothing else, and
     its skills list holds no research or grilling skill other than coaster's
     that the profile does not block. A run that falls short is void and
     repeated, as the spec's Decisions say, and the void run is recorded;
   - no `Skill` call names a skill outside coaster;
   - no `Agent` call starts a hat, and the challenge round is mentioned at most
     once in the session.

   **Amended by Julien, 2026-11-11:** as in AC 2, a denied `Bash` command that
   only writes inside the run folder, and that the run then makes with `Write`
   or `Edit`, is allowed and recorded.
10. **The permission choice is recorded.** An ADR written with
    `/jig:adr-workflow new` records that the helpers ask for Bash like any
    other command, that coaster grants itself nothing, and that a refused
    helper is not worked around. It states the costs, that a user is asked again
    in each new idea folder and after each update, and the two alternatives set
    aside: a README allow rule, whose version wildcard also admitted a `..` path
    in the spec's probe, and a rendered `allowed-tools` grant. It cites A2, what
    "don't ask again" saves, as unverified. The README's "What's inside" says
    how the helpers get permission, and recommends no wildcard rule.

    **Amended by Julien, 2026-11-11:** his interactive probe settled A2, and
    "don't ask again" saves `Bash(python3 *)`. The ADR records A2 as settled
    rather than unverified, and the costs as they are: that option allows any
    Python command in the project. He kept jig's form, so the README, `scout`
    and `name` warn users to answer Yes instead.
11. **The fixes ship before the runs that judge them.** The changes go out as
    `0.1.0-pre.3`, after the path and term searches, as an ordinary commit on
    `main`. The test profile is updated, and the runs for ACs 2 to 9 and 12 are
    on the installed `0.1.0-pre.3`.
12. **The user's choice of research option wins.** `scout`'s Run step takes
    the option the user asks for before "the first option that applies", as
    `challenge` does for the hats. In one run in a profile where a research
    skill is installed and not blocked, a request for the quick pass gets the
    quick pass: the log shows `scout`'s own searches and no `Skill` call to the
    research skill. Without such a request, `scout` still hands research to the
    installed skill, which is scope 3's path and is not judged here.

### Verification scenario

**Preconditions:** Claude Code 2.1.322 or later. A new empty folder as
`CLAUDE_CONFIG_DIR`, with `claude plugin marketplace add ramboz/coaster` and
`claude plugin install coaster@coaster`, and Julien signed in there by hand.
Before each step, `claude plugin list` under the profile shows only coaster,
and any other plugin is disabled first. Any research or grilling skill in the
profile's `skills/synced/` folder is blocked with a `Skill(...)` deny rule in
that profile's settings, or turned off on the account for the test. Each run
starts in a new empty folder made with `git init`, into which the previous
step's `docs/` is copied. No secrets.

**Invocation:** Every command runs with `CLAUDE_CONFIG_DIR` set to that folder,
with `--model sonnet --permission-mode acceptEdits --output-format stream-json
--verbose`, and without `--plugin-dir`. `$ROOT` is coaster's `path` from the
`init` event of the first run on each installed version, because the path
changes with the version. The grants are the ones each step needs, and never
`Read`. A helper grant quotes the path as the command does, since an unquoted
rule did not match a quoted command in the probes: `$SCOUT_GRANT` is
`Bash(python3 "$ROOT/skills/scout/scripts/link_check.py":*)` and `$NAME_GRANT`
is `Bash(python3 "$ROOT/skills/name/scripts/name_check.py":*)`. Each run's
`init` event is checked before its output is judged.

1. The baseline: steps 2 to 7 on the installed `0.1.0-pre.2`, recorded as found
   and not judged.
2. The sample dossier, as in spec 001:
   `claude -p '/coaster:capture A small app that reminds me when my houseplants need water. Skip the other questions.'`
3. `scout`, granted
   `--allowedTools "WebSearch,WebFetch,$SCOUT_GRANT"`:
   `claude -p '/coaster:scout Run the Landscape and Demand lanes as a quick pass, and skip the other lanes.'`
   The same prompt again with only `WebSearch,WebFetch` granted (AC 2), and
   once with nothing granted (AC 5), each on a copy of step 2's output.
4. `frame` on step 3's first output, no grant:
   `claude -p '/coaster:frame Read the Open and Wanted lenses, and skip the others.'`,
   then `claude -p --resume "$SESSION_ID" 'Go.'`
5. `name`, granted
   `--allowedTools "WebSearch,WebFetch,$NAME_GRANT"`:
   `claude -p '/coaster:name It reminds forgetful plant owners to water their plants. Botany, warm and playful, short and lowercase, and it must read well as a command. Skip the other questions.'`,
   then `claude -p --resume "$SESSION_ID" 'I pick the first one on the shortlist.'`
   The first turn again with only `WebSearch,WebFetch` granted (AC 2).
6. `handoff`, no grant: `claude -p '/coaster:handoff'`
7. For AC 12, in a copy of the profile where a research skill is installed and
   not blocked, step 3's first command runs again.
8. Collect each run's `permission_denials`, `init` event and tool calls.

**Preserved behavior:** `capture` still meets spec 001's AC 7 from the installed
plugin. `claude --plugin-dir hosts/claude` still lists six `coaster:` skills.

**Code revision / dirty-change identity:** Record the commit on `origin/main`
that was installed and the installed version, for the baseline and for the
judged runs. Raw logs stay out of the repository, because they hold home
directory paths. The evidence is the table below and a list of each run's tool
calls with those paths trimmed, in `evidence/slice-01-tool-calls.md`.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | — | The baseline on `0.1.0-pre.2` is recorded | | not-run | |
| 2 | 1 | Source, map and rendered form agree; `--check` and strict validation pass | | not-run | |
| 3 | 2 | A withheld helper is not worked around; each result traces to a web call or is marked not run | | not-run | |
| 4 | 3, 4 | The quick pass files entries by the rules, and the link check runs from `<root>` | | not-run | |
| 5 | 5 | With no web tools, `scout` says it could not search and invents nothing | | not-run | |
| 6 | 6 | `frame` suggests, then records the go only on the second turn | | not-run | |
| 7 | 3, 7 | `naming.md` is complete, `name_check.py` runs from `<root>`, and the pick is recorded | | not-run | |
| 8 | 8 | `handoff.md` is complete and is the only file written | | not-run | |
| 9 | 9 | No packaged file read, and only withheld tools denied, in every run | | not-run | |
| 10 | 10 | The ADR records the choice, its costs and both alternatives; the README says how helpers get permission | | not-run | |
| 11 | 11 | `0.1.0-pre.3` is installed for the judged runs | | not-run | |
| 13 | 12 | A requested quick pass beats an installed research skill | | not-run | |
| 12 | Preserved | `capture` and `--plugin-dir` still work | | not-run | |

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

**Anti-horizontal-phasing check:** After this slice, someone who installs
coaster from GitHub can scout, frame, name and hand off an idea, and both
helpers run from the plugin once they allow them.
