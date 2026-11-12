---
status: DONE
dependencies: [001-02]
last_verified: 2026-11-11
frame_review: true
arch_review: true
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

   **Amended again by Julien, 2026-11-11:** any denied `Bash` command confined
   to the run folder, whether it reads or writes, is allowed and recorded. A
   command that reads, lists or searches the installed plugin's folder, other
   than the helper commands, still fails this AC even when it is denied.
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

**Recorded revision:** the judged runs used coaster installed from GitHub into a disposable profile, with Claude Code 2.1.322 and Sonnet. Each skill was judged on a version whose text for that skill is byte-identical in `0.1.0-pre.11`:
- `scout` on `0.1.0-pre.11` (`ac1f86f`);
- `name` and `handoff` on `0.1.0-pre.10` (`2fc2016`);
- `capture` and `frame` on `0.1.0-pre.9` (`3189b90`).

Their text and both helpers are byte-identical in `0.1.0-pre.11`, which ships. After each update the installed folder matched `hosts/claude` (`diff -rq`), and `cmp` confirmed which skills changed between versions. The run IDs below are the headings in [evidence/slice-01-tool-calls.md](evidence/slice-01-tool-calls.md), which also describes how the checks were made.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | — | The baseline on `0.1.0-pre.2` is recorded | Recorded as found:<br>- The rendered helper commands had no `python3`. The model wrote `python3 -I <path> … 2>&1` itself, which the quoted grant did not match, so the helper was refused even when granted.<br>- `name` wrote `naming.md` outside the dossier folder.<br>- Most runs first tried a Bash heredoc or inline-Python edit that `acceptEdits` denied.<br>- With no web tools, `scout` already said it could not search.<br>- Account-synced plugins joined the profile after the first run and were then disabled. | recorded | `b2` to `b6` |
| 2 | 1 | Source, map and rendered form agree; `--check` and strict validation pass | Source runs `python3 scripts/<file>`. The `HELPERS` keys, the rewrite and the `FORBIDDEN` guard use that form, and the rendered skills say `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"`.<br>Each guard fails the build:<br>- a stray `python3 scripts/` in `frame`, inside or outside backticks: "unmapped reference";<br>- an old-form reference in `scout`: "helper reference not found".<br>`--check` exits 0 and `claude plugin validate --strict hosts/claude` passes. The rendered skills hold no `` `scripts/ `` or `allowed-tools`, `skills/` holds no `${CLAUDE_PLUGIN_ROOT}`, and the script is 161 lines. | pass | the build; the guard runs |
| 3 | 2 | A withheld helper is not worked around; each result traces to a web call or is marked not run | **`t3b` (`scout`):** the only denial is the helper. It tried no other command, opened the sources behind its 8 `grounded` entries on the web, and says so in the Evidence section, with the command to run by hand. Every `grounded` entry cites a fetched URL, and the `unverified` ones are named as not opened.<br>**`s5b` (`name`):** the only denial is the helper. It tried nothing else, marked the npm, PyPI, crates.io and GitHub columns "not checked", which is `name`'s word for AC 2's "not run", and gave the reason and the command to run by hand. Web tools were granted, but it used them only for product searches and did not do the registry lookups on the web, as its text says to. AC 2's bullets still hold, because nothing unchecked is reported as checked. | pass | `t3b`, `s5b` |
| 4 | 3, 4 | The quick pass files entries by the rules, and the link check runs from `<root>` | **`t3a`:** no denials. The warning came before the helper.<br>- The lane files were written first. Then `python3 "<root:0.1.0-pre.11>/skills/scout/scripts/link_check.py"` ran on the dossier folder, after the model's own edits, and reported 12 URLs (10 resolve, 2 refuse automated requests), matching the folder's 12 unique URLs. The Evidence section records it with the date.<br>- The lanes hold 5 and 7 entries, labelled quick pass. Every entry has its prefix, number, a known tag and the fields that tag needs, and every `grounded` entry cites a fetched URL. The Evidence index lists the load-bearing entries.<br>- `status: scouted`, and `last_scouted` is today. | pass | `t3a` |
| 5 | 5 | With no web tools, `scout` says it could not search and invents nothing | **`t3c`:** the only denials are `WebSearch`. It said the quick pass could not run and tried no other route. It wrote only a brief, beside the dossier, plus a status note in the dossier saying no searches ran, and no URL appears anywhere in the folder. | pass | `t3c` |
| 6 | 6 | `frame` suggests, then records the go only on the second turn | **`r4`:** At a glance gives one-word readings for Open and Wanted, "not looked at" for the other four, "5 of 19 lane entries `grounded`", and a call labelled "a suggestion, not the decision". It sets `status: framed`, and `## Decisions` is unchanged.<br>**`r4t2` ("Go."):** a dated go with the open risks carried forward, `decision: go` and `status: decided`. | pass | `r4`, `r4t2` |
| 7 | 3, 7 | `naming.md` is complete, `name_check.py` runs from `<root>`, and the pick is recorded | **`s5a`:** no denials. `python3 "<root:0.1.0-pre.10>/skills/name/scripts/name_check.py"` ran on the candidates. `naming.md` sits in the dossier's folder with all 6 template headings in order and the helper's rows dated 2026-11-11. It has a shortlist of 6, each with its strongest argument and main risk, and states it is not trademark clearance.<br>**`s5at2`:** records the pick under `## Decisions` with why it ranked first, noting that the user gave no reason. | pass | `s5a`, `s5at2` |
| 8 | 8 | `handoff.md` is complete and is the only file written | **`s6`:** one `Write`, of `handoff.md` beside the dossier. It has all 21 template headings in order, Appetite "TBD, the user's call", and use cases "None stated by the user. TBD." A denied in-folder `sed` tried to add a hand-off line to the dossier, so nothing else changed. Apart from reading the folder, it made no other tool call, and no `Agent` or `Skill` call. | pass | `s6` |
| 9 | 9 | No packaged file read, and only withheld tools denied, in every run | **In every judged run:**<br>- the `init` event lists coaster at the version under test and Claude Code's built-in plugins only, with `deep-research` blocked by the profile's deny rules except in AC 12's run;<br>- no tool call reads, lists or searches the installed plugin's folder other than a helper command;<br>- every new or changed file is in `docs/prospects/houseplant-watering-reminder/`;<br>- no `Agent` or `Skill` call is made, and the challenge round is mentioned at most once a session.<br>**Denials:** the withheld tools, plus in-folder Bash edits in `r4`, `r4t2` and `s6`, which the widened amendment allows. | pass (as amended) | all judged runs |
| 10 | 10 | The ADR records the choice, its costs and both alternatives; the README says how helpers get permission | **ADR-0002, Accepted:** records the choice, the A2 probe ("don't ask again" saves `Bash(python3 *)`), the costs, and Options B, C and D set aside, with the scope-4 trigger. Its frame review passed after two re-checks.<br>**The README** says coaster grants itself nothing, that Claude Code asks before each helper, and to answer Yes rather than "don't ask again". It recommends no wildcard rule.<br>**`scout` and `name`** carry the same warning, as AC 10's amendment requires, in its own paragraph before the helper command (`skills/scout/SKILL.md`, `skills/name/SKILL.md`). | pass (as amended) | ADR-0002; `README.md`; the two skills |
| 11 | 11 | `0.1.0-pre.3` is installed for the judged runs | Shipped as nine pre-releases, `0.1.0-pre.3` to `0.1.0-pre.11`. Each went out as an ordinary commit on `main` after the path and term searches, under Julien's standing go-ahead for this slice. The judged runs used the versions under Recorded revision. | pass, with deviation | `git log` |
| 12 | Preserved | `capture` and `--plugin-dir` still work | **`r2` (`capture`):** one `Write`, all 24 headings in order, the frontmatter right, the idea quoted word for word, four questions under Unstated, empty lenses and no placeholder.<br>**`--plugin-dir hosts/claude`:** loads coaster with all six skills. | pass | `r2`; the `init` skills list |
| 13 | 12 | A requested quick pass beats an installed research skill | **`t12`, with `deep-research` unblocked:** asking for a quick pass got `scout`'s own six searches and no `Skill` call. | pass | `t12` |

**DoD:**
- [x] All ACs pass, with the table above filled in from real runs.
- [x] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [x] Implementation review passed.
- [x] Deviation log produced under this slice heading.
- [x] Reconciliation sweep produced under this slice heading.
- [x] Reconciliation review passed.
- [x] `docs/refinement-todo.md` updated if any decisions were deferred during
      implementation.

### Close-out (post-DONE)

- [x] `docs/specs/README.md` regenerated by `workflow.py status-board`.

**Anti-horizontal-phasing check:** After this slice, someone who installs
coaster from GitHub can scout, frame, name and hand off an idea, and both
helpers run from the plugin once they allow them.

### Deviation log (after reconciliation)

The original slice is preserved above. Implementation notes:

1. **Nine pre-releases instead of one.** AC 11 named `0.1.0-pre.3`. Each round of runs found something the last had not, and every fix changed the package's bytes. Each shipped as an ordinary commit on `main` after the path and term searches, under Julien's standing go-ahead for this slice:
   - `pre.3`: the helper form, the no-workaround rule, `scout`'s choice and link order, and the README.
   - `pre.4`: `name` and `handoff` say where their files go.
   - `pre.5`: `scout` creates lane files with its file tool.
   - `pre.6`: `link_check.py` no longer crashes on mixed statuses, a bug in every earlier published version.
   - `pre.7`: the README warning.
   - `pre.8`: the in-session warning.
   - `pre.9`: the warning comes before the helper command, the file-tool rule covers dossier edits, and the build guard catches references outside backticks. These came from the reviews.
   - `pre.10`: `name` finds the dossier first, and `scout` writes every file beside it.
   - `pre.11`: the limit of ten entries per lane counts absences, and a gap is not an entry.
2. **Julien amended ACs 2, 9 and 10.**
   - **ACs 2 and 9:** first, to allow a denied Bash write inside the run folder; then, for AC 9, any denied Bash command confined to the run folder. A command touching the plugin's folder still fails, even when denied. The first amendment says Sonnet tried a heredoc in every `scout` run on pre.2 and pre.4. The accurate count is every `scout` run that wrote lane files: four of six. The two runs without web tools wrote none.
   - **AC 10:** A2 is settled. Julien's interactive probe showed that "don't ask again" saves `Bash(python3 *)`. That fired ADR-0002's kill criterion. Julien weighed Option D and chose to keep jig's form and warn users. The scope-4 release check revisits it, as `docs/refinement-todo.md` tracks.
3. **The in-session warning is in the text, but its display is not reliable.** AC 10's amendment requires the warning in `scout`'s and `name`'s text, and the text that ships carries it. No AC requires a run to show it. In the final runs `scout` showed it before every helper call, and `name` before neither of its two, as on pre.8, even after pre.9 moved it before the command. ADR-0002 and refinement-todo record this.
4. **Each skill was judged on text byte-identical in pre.11.** Recorded revision gives the versions:
   - `capture` and `frame` ran on pre.9, with `frame` (`r4`) reading the output of pre.9's `scout` run `r3a`;
   - `name` ran on pre.10 from that `frame` output, and `handoff` on pre.10 from that `name` output;
   - `scout` ran on pre.11 from pre.9's `capture`.

   Each update was compared byte for byte.
5. **The test profile needed isolating.** Account-synced plugins joined it after its first run, and the synced `deep-research` skill appeared at the first session. The plugins were disabled with `claude plugin disable`. `deep-research` was blocked with `Skill(...)` deny rules in the profile's settings, lifted only for AC 12's run, which reused the profile because a copy would not carry the sign-in. Julien's own settings were not touched. This settles A7. A1 is settled too: every helper command in the logs ran from the installed path, with `${CLAUDE_PLUGIN_ROOT}` filled in.
6. **Earlier runs are kept as history.** The intermediate runs are summarized in the evidence. They include the pre.4 `frame` turn whose denied command named `/tmp/x`, outside the run folder, which no judged run repeats. They also include `DEM-02`, tagged `grounded` in a pre.5 run with only "same thread as DEM-01" as its source. The final runs cite a fetched URL for every `grounded` entry.
7. **The first reviews were redone.** Compliance and craft returned needs-changes on pre.8. The fixes went into pre.9 to pre.11, and the runs were repeated as above. The checks that support the table are described in the evidence file. The scripts stay outside the repository, which keeps the release plan's no-test-harness rule.
8. **Two wording gaps and one behaviour gap against AC 2.**
   - `scout` and `name` now say "If the helper is refused, try no other command", while AC 2 says "refused or fails". On a failure the text sends the model to the web route or to "not run", which excludes another command only by implication.
   - `name` writes "not checked" where AC 2 says "not run".
   - A behaviour gap: in `s5b`, `name` had web tools but did not do the registry lookups on the web, though its text says to.

   None makes a result up. The first and third are parked in `docs/inbox.md`.
9. **The baseline skipped one step.** Scenario step 1 covered steps 2 to 7, but AC 12's run (step 7) was not part of the baseline on pre.2. Only the judged runs exercise it.
10. **Both synced research skill names were blocked.** Every judged run's skills list showed `deep-research` and `anthropic-skills:deep-research`. The profile's deny rules named both, and no run called either.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `updated` | "What's inside" says coaster grants itself nothing, that Claude Code asks before each helper, and to answer Yes rather than "don't ask again". It ships in the package. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board`. |
| `docs/product-vision.md` | `no-op` | Scope and use cases are unchanged. |
| `docs/architecture.md` | `updated` | The helpers' command form and how they get permission, with ADR-0002. |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `no-op` | `CLAUDE.md`'s Active specs lists only the worked example, by its own convention, and spec 001 had no entry either. There is no `AGENTS.md`. |
| `docs/inbox.md` | `updated` | Four follow-ups: `frame`'s Bash edits and `handoff`'s one-file rule; `scout` once citing another entry's source in place of its own link; the "refused or fails" wording in `scout` and `name`; and `name` skipping the web route for registries. The CONTRIBUTING-pointer item stays parked: its rule ties it to the next PR that changes the package, and 002-02 will. The `challenge` item belongs to 002-02. |
| `docs/refinement-todo.md` | `updated` | New entry for the "don't ask again" exposure, triggered at the scope-4 release check, noting the unreliable in-session warning and the model's own inline `python3` edits. |
| `docs/memory/**` | `updated` | Learnings on synced plugins and skills in a disposable profile, and on what "don't ask again" saves. |
| `docs/decisions/README.md` / ADR index | `updated` | ADR-0002 accepted, and the index regenerated and checked clean. |
| `docs/specs/002-whole-loop-installed/spec.md` | `updated` | A1, A2 and A7 settled, the helpers Decision amended, and the new "don't ask again" exposure added to the deferred-decisions table. |
| `slice-03-next-real-idea.md` | `updated` | AC 4 now records A2 again rather than settling it. |
| `hosts/claude/**`, `.claude-plugin/plugin.json` | `updated` | Rebuilt for each pre-release, now `0.1.0-pre.11`, and in sync by `--check`. |
| `evidence/slice-01-tool-calls.md`, `reviews/slice-01-*.md`, `docs/decisions/reviews/adr-0002-frame-critique.md` | `updated` | The slice's own evidence and the recorded review verdicts. |
| `skills/scout/SKILL.md`, `skills/name/SKILL.md`, `skills/handoff/SKILL.md`, `skills/scout/scripts/link_check.py`, `scripts/build_host_packages.py`, `docs/decisions/adr-0002-helpers-ask-for-bash.md` | `updated` | The slice's implementation and its ADR, as the deviation log describes. |
| `docs/releases/claude-code-first-release.md` | `updated` | The release check gains a line to revisit the "don't ask again" exposure before `v0.1.0`, so the trigger in ADR-0002 and refinement-todo has a gate. |
| `docs/bugs/README.md` | `no-op` | The `link_check.py` crash was found and fixed inside this slice, in pre.6, and the deviation log records it, so no bug record was opened. |
| `docs/conventions.md`, `CONTRIBUTING.md`, `.github/**`, spec 003 | `no-op` | These came from spec 003 (PR #2, #4), which landed on `main` while this slice was in flight. This branch was rebased onto them, and its commits follow the new conventional-commit rule. |
