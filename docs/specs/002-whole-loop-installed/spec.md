---
status: IN_PROGRESS
skill:
use_cases: [UC-1, UC-2, UC-3, UC-4, UC-5, UC-6, UC-9, UC-10, UC-11]
---

<!-- jig self-defining vocabulary (soft, forward-only): expand each acronym on first use and link the term to docs/memory/glossary.md (or jig's lexicon). See docs/workflow.md "Self-defining vocabulary". -->

# Spec 002: The whole loop, installed

> Reserved on 2026-11-11 as a local provisional number with `workflow.py new
> --no-push`, so that pushing the reservation to the public `main` stays
> Julien's call. `origin/main` held only specs 000 and 001 at the time. Serves
> scope 2 of the
> [Claude Code first release](../../releases/claude-code-first-release.md).

## Overview

Spec 001 published coaster and showed that `capture`, installed from GitHub,
writes a correct dossier. The other five skills have never run from the
rendered package, installed or local. This spec runs `scout`, `frame`,
`challenge`, `name` and `handoff` from coaster installed from
github.com/ramboz/coaster, starting from the published `0.1.0-pre.2`. Both
helpers run through `${CLAUDE_PLUGIN_ROOT}`, the spec settles the Bash permission
they need, and it makes the check that ADR-0001 and the release plan require
before the `v0.1.0` tag: in a `challenge` run's log, each hat's prompt holds the
hats' rules, its own hat section, the evidence rules and the round shape,
intact. Last, Julien runs the whole loop on his next real idea.

### Current state (verified 2026-11-11)

**The installed package**

- `origin/main` is at `bbeda54`, and its `hosts/claude/.claude-plugin/plugin.json`
  says `0.1.0-pre.2`. 001-02 installed `0.1.0-pre.1` from GitHub and ran only
  `capture` from it.
- Rendered lengths: `scout` 258 lines, `frame` 196, `challenge` 319, `name` 116,
  `handoff` 135. `challenge` is 13,492 bytes, about 3,400 tokens at four
  characters a token, so it fits inside the 5,000 tokens that ADR-0001 says an
  invoked skill keeps after compaction.

**The helpers**

- `scout`'s `link_check.py` and `name`'s `name_check.py` use only the standard
  library and need network access. `name_check.py` also calls `gh` when it is
  signed in, and otherwise writes "not checked" in the GitHub column.
- Both are mode `100644` in git, so neither is executable. The rendered skills
  tell the model to run `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>`
  with no interpreter, while each script's own usage line says
  `python3 <file>`. Run as written, the shell refuses a file without the
  execute bit.
- `scripts/build_host_packages.py` finds the two references by their source
  form, `` `scripts/link_check.py `` and `` `scripts/name_check.py ``, in its
  `HELPERS` map, and fails when one is missing. Its rewrite replaces
  `` `scripts/ `` inside each key, and its `FORBIDDEN` guard looks for
  `` `scripts/ `` in the rendered text. A key of the form
  `` `python3 scripts/link_check.py `` holds neither, so rewording the source
  means changing the keys, the rewrite and the guard together. That stays
  inside ADR-0001's bound of "the two helper paths".
- A probe on Claude Code 2.1.322 (Haiku, headless `-p`,
  `--permission-mode acceptEdits`, no `--allowedTools`, a profile with no allow
  rules) was denied all three of `python3 <checkout>/hosts/claude/skills/name/scripts/name_check.py`,
  `WebSearch` and `WebFetch`. A headless run of `scout` with no grant cannot
  search at all, and an interactive user is asked before each of those tools.
- No `SKILL.md` in the installed jig plugin has an `allowed-tools` line (a
  search of every `SKILL.md` in that plugin's folder). jig's helpers run through
  the user's ordinary Bash permission.
- Installed from GitHub into a scratch profile, without signing in, the
  helpers land at
  `$CLAUDE_CONFIG_DIR/plugins/cache/coaster/coaster/0.1.0-pre.2/skills/<skill>/scripts/<file>`,
  so the installed path names the version. The marketplace's own clone of the
  whole repository sits beside it.
- An allow rule with wildcards for the folders and the version,
  `Bash(python3 */coaster/coaster/*/skills/name/scripts/name_check.py *)`,
  let a headless Haiku run start `name_check.py` from that cache path with no
  denial (probe, 2.1.322). The same rule refused a lookalike
  `python3 -c '...' .../coaster/coaster/.../name_check.py`. But a rule anchored
  at the cache folder, `Bash(python3 <cache>/coaster/coaster/*/skills/name/scripts/name_check.py *)`,
  let a script outside the plugin run with no prompt, through a path of the
  form `<cache>/coaster/coaster/../../../../../<elsewhere>/skills/name/scripts/name_check.py`.
  A wildcard for the version therefore also admits `..`, and with it any script
  the model can write at a matching path.
- `${CLAUDE_PLUGIN_ROOT}` resolves in a skill body under `--plugin-dir`
  (spec 001). jig, whose skills work this way in daily use, writes 88 of the 94
  plugin-root references in its installed skills as
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/<file>.py"`: an interpreter,
  and the path in double quotes, with no `allowed-tools` grant (a count over
  every `SKILL.md` in its installed plugin). In the CLI, a jig skill loaded with
  the Skill tool showed that path with the plugin's absolute folder in place of
  the variable (probe, Haiku). That jig was synced from Julien's account rather
  than installed from a marketplace.
- An allow rule written without the quotes, `Bash(python3 <path>:*)`, did not
  match the quoted command `python3 "<path>" ...` and was denied. The same rule
  with the quotes, `Bash(python3 "<path>":*)`, matched (probes, Haiku).

**`challenge`**

- The source says to start three "read-only subagents", that each "writes its
  own section file", and then to delete the per-hat files. `docs/inbox.md`
  parked that contradiction for this scope.
- A second probe on 2.1.322 (Haiku, headless, `--output-format stream-json
  --verbose`, `--allowedTools WebSearch`) started one `Explore` subagent. The
  log carried its full prompt in the `Agent` call's input, beside its
  `subagent_type`, and each of the subagent's own tool calls carried that call's
  id as `parent_tool_use_id`. The subagent's `WebSearch` ran under the session's
  grant, with no denial. Claude Code's `Explore` agent has no `Write` or `Edit`.
- A third probe (Sonnet, the same flags, `--allowedTools WebSearch,WebFetch`)
  used the skill's own wording: "start three fresh read-only subagents in
  parallel", with a marker line to paste. The parent chose `general-purpose` for
  all three, which has `Write`, `Edit` and `Bash`, so "read-only" was only a
  request. The three `Agent` calls shared one `message.id`, all three prompts
  held the marker, the hats ran on the session's Sonnet, and one of them read
  the dossier with `cat` through `Bash`.
- A fourth probe (Sonnet) asked for an `Explore` subagent by name. It ran on the
  session's Sonnet, not on a smaller model, and read the file with `Read`.
- So the hat-prompt check can read each hat's prompt from a run's log, and a
  hat needs no grant of its own to search. Naming `Explore` takes `Write` and
  `Edit` away from a hat, but it keeps `Bash`, so a check of what each hat ran
  is still needed.

**Profiles and other skills**

- A stream-json run's `init` event lists the loaded plugins with their source
  and version, and the skills. The probes ran in Julien's normal profile, which
  loaded three account-synced plugins besides the built-in ones.
- The same `init` event's skills list held `deep-research` and
  `anthropic-skills:deep-research`. These are standalone skills synced from
  Julien's account, not plugins, so `claude plugin list` does not show them.
  Claude Code downloads account-enabled skills into `skills/synced/` in any
  signed-in terminal session (`ENB-15` in coaster's field research).
- A disposable `CLAUDE_CONFIG_DIR` needs Julien to sign in by hand, and 001-02
  found account-synced plugins joining such a profile on resume.
- `scout` hands research to an installed research skill, and `challenge` hands
  the round to an installed grilling skill, when one is present. That deferral
  is scope 3. `scout`'s Run step takes "the first option that applies", and
  its first option is such a skill, called when Claude can call it. Unlike
  `challenge`, which also runs the hats "when the user prefers them", `scout`
  has no clause for a user who asks for the quick pass.

## Decisions

Julien accepted each of these on 2026-11-11, as the draft proposed them.

- **Helpers ask for Bash like any other command (Julien, 2026-11-11).** coaster grants
  itself nothing. The rendered command follows jig's form,
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"`, rendered from
  `python3 scripts/<file>` in source, so it does not depend on the execute bit.
  The helpers stay in each skill's `scripts/` folder, where spec 001 put them,
  rather than beside `SKILL.md` as jig's do. Claude Code asks before each helper
  runs, as it does for jig's helpers.
  Running a script that makes network requests is a fair moment to ask, which
  reading the package's own text was not. The cost is that "don't ask again" is
  saved per project and names the versioned path, so a user is asked again in
  each new idea folder and after each update. Two alternatives are set aside.
  A version-independent allow rule in the README would end the repeat prompts,
  but its wildcard also matched a `..` path to a script outside the plugin, so
  publishing it would invite users to allow more than coaster's helpers. A
  rendered `allowed-tools` grant would name the exact installed path and is
  narrower than any rule a user writes. It is set aside because it adds a build
  text change beyond ADR-0001's bound, has only been seen lasting for the turn
  that invoked the skill, which misses the link check `scout` often runs in a
  later turn, and because no sibling pack grants itself Bash. 002-01 records
  the choice and its costs in an ADR. What "don't ask again" saves, the versioned script path or a broader
  `python3` prefix, has not been run (A2), and decides both the cost and
  whether asking stays the narrow choice. The ADR cites it as unverified, and
  002-03 records the rule the prompt offers. **Amended by Julien, 2026-11-11:**
  his interactive probe settled A2. "Don't ask again" saves `Bash(python3 *)`,
  not the script's path, so the cost above is wrong: a user who picks it allows
  any Python command in the project. He kept jig's form and chose to warn users,
  in the README and in `scout` and `name` just before each helper runs
  (ADR-0002).
- **A refused helper is not worked around, and nothing is filled in
  (Julien, 2026-11-11).** When a helper is refused, the skill does not try another
  command to the same end, such as `curl` or an inline script, because the user
  declined running code. It may take the route its text already gives for chat,
  opening the sources or searching the registries on the web, when those tools
  are allowed, and it says which route ran. Otherwise it records "not run", the
  reason, and the command to run by hand. It never states a result that no tool
  call returned. A refused read degraded `capture` without any error in spec
  001, and the same could happen here.
- **Hats write nothing and reply with their section (Julien, 2026-11-11).** In Claude
  Code, `challenge` names the subagent type for its hats. `Explore`, the
  built-in type with no `Write` or `Edit`, which in the probes searched under
  the session's grant and ran on the session's model, is kept only if, run side
  by side with `general-purpose` hats, its hats meet the hats' rules, read the
  whole dossier and research about as much (002-02's AC 1). Otherwise the hats
  are `general-purpose` and told to write nothing, which the runs then check.
  Each hat replies with its section in the round template's shape, and the
  parent writes `challenge/round-N.md` from the replies, adding only the
  summary, the grouping and the proposed dispositions. There are no per-hat
  files to write or delete, and the chat path, where the user pastes each answer
  back, already works this way. Three alternatives are set aside. Leaving the
  type to the parent got `general-purpose` hats in the probe, which could write,
  with "read-only" only a request. Hats that write their own section files leave
  files to delete and nothing to stop a hat editing the dossier. Option F, each
  hat as a plugin agent with its own tools and model, would enforce both, but
  widens the package and the script, and ADR-0001 holds it for a failed paste.
  **Amended by Julien, 2026-11-12:** 002-02's comparison found the paste
  condensed in one run of five, which fired ADR-0001's kill criterion. Julien
  chose Option F, recorded in ADR-0003: the hats are coaster's own plugin
  agents, `coaster:skeptic`, `coaster:rival` and `coaster:customer`, rendered
  by the build with their rules, limited to `Read`, `Grep`, `Glob`,
  `WebSearch` and `WebFetch`, and on the session's model. Each hat's prompt
  carries only the run's details. Slice 002-04 builds it. Julien ruled on
  2026-11-12 that a note in a hat's prompt that only says where the dossier's
  own files are counts as part of the dossier path, so ADR-0003 stands
  ([lightweight decisions](../../decisions/lightweight-decisions.md)).
- **What a verification run grants (Julien, 2026-11-11).** Spec 001's lesson was to test
  with no `--allowedTools` grant, because a `Read` grant hid a refused read of
  the package. In this scope `WebSearch`, `WebFetch` and the helpers are tools a
  user is asked about and would approve, so a headless run grants exactly those
  for its step, with the helper granted by its full installed path. It never
  grants `Read` and never uses a bypass mode. Each run checks that
  `permission_denials` holds only what it deliberately withheld, and that the
  log shows no read of the installed plugin's folder.
- **The floor, not deferral, in a profile that holds only coaster.** This
  scope runs `scout`'s quick pass and the three hats. Deferral to richer skills
  is scope 3. Signing in to a disposable profile can bring in account-synced
  plugins, which in 001-02 arrived on an interactive resume and whose hooks
  wrote files into the run folder, and synced skills such as `deep-research`
  arrive the same way without being plugins. So every headless run is judged
  only if its `init` event lists coaster and Claude Code's built-in plugins and
  nothing else, and its skills list holds no research or grilling skill other
  than coaster's, or only ones blocked by a deny rule in that profile's
  settings. A run that falls short is void: the plugin is disabled or the skill
  blocked in the profile, or the profile is recreated, and the run is repeated.
  Julien's own settings are not changed. 001-02's profile is not reused.
  002-03's interactive run is judged by its log instead (its AC 3). Separately,
  `scout` honours a user who asks for a particular option, as `challenge`
  already does (002-01).
- **Start from `0.1.0-pre.2`, ship fixes as pre-releases.** 002-01 opens with a
  baseline run of the four skills on the installed `0.1.0-pre.2`, recorded as
  found. Every change to the package's bytes bumps the pre-release number (spec
  001), goes out as an ordinary commit after the path and term searches (spec
  001, A3), and is then updated in the test profile before the runs that judge
  the acceptance criteria.
- **The real idea stays out of this repository** (spec 001's Decisions).
  002-03's evidence records only the shape of the run, not the idea.
- **The release check "a fresh install from GitHub runs the whole loop" is met
  by the three slices together.** 002-01 and 002-02 run every skill from an
  install from GitHub, and 002-03 runs a real idea as far as Julien's decision
  takes it. The test must not lean on that decision: a real idea that ends in a
  no-go or a park is coaster working as designed. The release plan's scope 2
  line points here.

## Non-goals

- Deferral to richer research and grilling skills (scope 3, R-03).
- R-04's activation test and the six-or-three call, which land before the tag.
- The `v0.1.0` tag, the ai-pegboard listing, `CHANGELOG` and CI (scope 4).
- The claude.ai chat path, Codex and Copilot.
- Option F, plugin agents for the hats, unless the hat-prompt check fails
  (002-02's AC 7). It failed on 2026-11-12, so 002-04 builds Option F
  (ADR-0003).
- `capture`'s two follow-ups in `docs/inbox.md`, unless the real-idea run trips
  on one of them.
- A test harness for the Markdown skills, which the release plan rules out. The
  checks here are recorded runs, and the hat-prompt comparison runs as a short
  command kept outside the repository.

## Assumptions

- **A1.** A plugin installed from a marketplace gets `${CLAUDE_PLUGIN_ROOT}`
  replaced in the skill body as jig's account-synced plugin does in the CLI and
  in the desktop app. Julien's call is to follow jig here, since jig's form has
  worked reliably. The residual is only the marketplace install itself, which
  the first `scout` run in 002-01 shows in the helper command it runs.
  **Settled on 2026-11-11:** in every 002-01 run from a marketplace install,
  the helper command ran from the installed path with the variable filled in.
- **A2.** An interactive session in the default permission mode asks once for
  each helper, and allowing it for the project covers later runs until the next
  version changes the path. **Settled on 2026-11-11, and wrong:** in Julien's
  interactive probe, "don't ask again" saved `Bash(python3 *)`, which allows
  any Python command in the project. Julien chose to keep jig's form and have
  the README tell users to answer Yes instead (ADR-0002). He judges the
  friction in 002-03.
- **A3.** The parent pastes the packaged sections into each hat's prompt
  intact. This is ADR-0001's open assumption, and 002-02's AC 6 tests it. If it
  fails, ADR-0001's kill criterion applies. **Settled on 2026-11-12, and
  wrong:** in one of 002-02's five comparison runs, the parent condensed the
  evidence rules and the round template. ADR-0003 replaces the paste.
- **A4.** Hats started as `Explore` subagents inherit the session's grants and
  its model, as they did in one Haiku and one Sonnet probe. No Opus session has
  been probed, and Claude Code's documentation has at times described
  `Explore` as running on a smaller model. If a hat's search is denied, the run
  records it and grants nothing more. 002-02's AC 1 runs `Explore` hats on Opus
  before anything ships, and if one runs on another model, the hats move to
  `general-purpose` (002-02's ACs 1 and 3). **Settled on 2026-11-12:**
  `Explore` hats ran on Opus in 002-02's `a1o`, and a plugin agent with
  `model: inherit` ran on Sonnet and on Opus in ADR-0003's probes. Every hat
  search ran under the session's grant.
- **A5.** Julien has time for one interactive loop on his next real idea,
  which he confirmed on 2026-11-11 is ready. If the time does not come, 002-03
  is parked as DEFERRED until it does. What he decides about
  the idea does not matter: 002-03 passes on a no-go or a park, and 002-01's
  installed runs are the evidence for `name` and `handoff` if his loop stops
  before them.
- **A6.** Spec 001's A3 still holds: the path and term searches run by hand
  before each push, until CI arrives in scope 4.
- **A7.** A new disposable profile can be kept to coaster and the built-in
  plugins for a series of headless runs, including `--resume` turns, and a
  `Skill(...)` deny rule in that profile keeps a synced research skill from
  being called. 001-02's headless run loaded only coaster, but synced plugins
  later joined that profile on an interactive resume, and what triggers the
  sync is unknown. That a deny rule also blocks a synced skill comes from
  coaster's research notes and has not been run. The `init` check and the log
  catch either failure after the fact. If disabling or blocking does not keep
  them out, Julien turns the skill off on his account for the test, or chooses
  another way to sign the profile in. **Settled on 2026-11-11:** synced plugins
  joined 002-01's profile after its first run and stayed out once disabled with
  `claude plugin disable`. `deep-research` arrived at the first session, and
  with the deny rules no judged run called it.
- **A8.** An `Explore` hat writes a section as full as a `general-purpose` hat
  would. Claude Code describes `Explore` as a search agent that reads excerpts
  rather than whole files and locates rather than reviews, while a hat must read
  the whole dossier and review it. 002-02's AC 1 compares the two types hat by
  hat, on their replies, their reading and their research, before the change
  ships, and its AC 4 judges every hat's reply, not only the assembled round.
  **Settled on 2026-11-12:** at Sonnet, `Explore` and `general-purpose` hats
  researched the same amount, and every reply met AC 4. The choice is moot
  under ADR-0003, and 002-04 sets its agents beside these runs.

## Decomposition

**SPIDR axis: Path, then Interface.** SPIDR is jig's split of work by Spike,
Path, Interface, Data or Rules. The first split is by path through the loop.
002-01 takes the main path, `scout` to `handoff` with both helpers, and 002-02
takes the opt-in branch, a challenge round and the hat-prompt check. Both are
judged on headless runs of a sample idea in a disposable profile with coaster
installed from GitHub. The second split is by channel: in 002-03, Julien runs
the whole loop interactively on a real idea from a fresh install. Each slice
ends with someone reading a dossier, round or handoff written by the installed
plugin.

## Slices

- [002-01 — scout to handoff, installed](slice-01-scout-to-handoff.md)
- [002-02 — the challenge round, installed](slice-02-challenge-round.md)
- [002-03 — the next real idea](slice-03-next-real-idea.md)
- [002-04 — the hats as plugin agents](slice-04-hats-as-agents.md), added
  on 2026-11-12 when 002-02's AC 6 failed (ADR-0003). It lands before 002-02's
  installed runs.

## Deferred decisions this spec reaches

| Entry in `docs/refinement-todo.md` | What happens |
|---|---|
| Module boundaries | The hats' reply shape is a contract between `challenge` and its own subagents, not between skills. The entry is unchanged. |
| Testing framework | The checks are recorded runs and a comparison kept outside the repository, so the trigger is not reached. |
| CI/CD setup | Pushes in this scope run the searches by hand (A6). The trigger stays with scope 4. |
| The helpers' "don't ask again" exposure (new) | 002-01 created it: "don't ask again" saves `Bash(python3 *)`. ADR-0002 keeps jig's form with warnings, and the scope-4 release check revisits it. |
