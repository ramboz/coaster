---
status: Proposed
dependencies: [adr-0001]
last_verified:
frame_review: true
---

# ADR-0002: Helpers ask for Bash like any other command

## Status

Proposed (2026-11-11). Julien chose this option in spec 002's Decisions on 2026-11-11.

## Context

ADR-0001 builds the packaged text into each skill, so reading it needs no permission. The two helpers are different: `scout`'s `link_check.py` and `name`'s `name_check.py` are Python scripts that make network requests, and they run through Bash. ADR-0001 left their permission to scope 2. Spec 002 settles it.

Probes on Claude Code 2.1.322, recorded in spec 002's Current state, set the terms:

- A headless run with no grant was denied Bash, WebSearch and WebFetch. An interactive user is asked before each.
- jig writes 88 of the 94 plugin-root references in its installed skills as `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/<file>.py"`, with no `allowed-tools` grant. In the CLI, a jig skill loaded with that root already replaced by the plugin's absolute folder. Julien asked coaster to follow jig.
- Installed from GitHub, the helpers land at `$CLAUDE_CONFIG_DIR/plugins/cache/coaster/coaster/<version>/skills/<skill>/scripts/<file>`, so the path names the version.
- An allow rule must quote the path the way the command does. An unquoted rule did not match a quoted command.
- An allow rule with a wildcard for the version, anchored at the plugin cache, also let a script outside the plugin run with no prompt, through a `../../` path.
- In an interactive session, answering "Yes, and don't ask again" to `python3 "<plugin>/skills/name/scripts/name_check.py" ...` saved `Bash(python3 *)` in the project's `.claude/settings.local.json` (probe by Julien, 2026-11-11). That rule allows any Python command in the project. jig's helpers, written the same way, have the same exposure.

## Decision Options Considered

### Option A: Ask, like jig's helpers
- **Pros:** coaster grants itself nothing, which matches jig, servo and shaper. Running a network script is a fair moment to ask. The build needs no new text change.
- **Cons:** "Don't ask again" saves `Bash(python3 *)`, which allows any Python command in the project, far broader than coaster needs. A user who declines it is asked before every helper run.

### Option B: A rendered `allowed-tools` grant naming the exact installed path
- **Pros:** No prompt, and narrower than any rule a user writes.
- **Cons:** Adds a build text change beyond ADR-0001's bound. A frontmatter grant has only been seen lasting for the turn that invoked the skill, and `scout` often checks links in a later turn. No sibling pack grants itself Bash.

### Option C: An allow rule in the README, with a wildcard for the version
- **Pros:** Written once, it outlives version changes.
- **Cons:** Its wildcard also admitted a `..` path to a script outside the plugin, so publishing it would invite users to allow more than coaster's helpers.

### Option D: Executable helpers, run by their quoted path
- **Pros:** The command starts with coaster's own script path, so any rule "don't ask again" derives from it names that script rather than an interpreter.
- **Cons:** Departs from jig's form, which Julien chose to follow. Depends on the execute bit surviving the build, git and the plugin install, which has not been checked.

## Recommended Decision

Option A, chosen by Julien on 2026-11-11.

- **The command.** The source runs each helper as `python3 scripts/<file>`. The build renders it in jig's form, `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"`, so it does not depend on the execute bit. The build's `HELPERS` keys, rewrite and `FORBIDDEN` guard follow that form, which stays inside ADR-0001's bound of "the two helper paths".
- **No workaround.** When a helper is refused, the skill tries no other command to the same end, because the user declined running code. If web tools are allowed, it takes the web route its text already gives for chat, and says so. Otherwise it records the check as not run, with the reason and the command to run by hand. It never records a result that no tool returned.
- **The warning.** The README says that coaster grants itself no permissions and that Claude Code asks before each helper runs. It tells users to answer Yes rather than "don't ask again", because that option saves `Bash(python3 *)`, and it recommends no allow rule. `scout` and `name` give the same warning in the session, just before each helper runs, since a user who installed from the marketplace may never open the README.

The probe fired this ADR's first kill criterion. Julien weighed Option D, executable helpers run by their own path, and chose on 2026-11-11 to keep jig's form and warn users instead.

## Consequences

**Becomes easier:**
- Trusting the plugin: it pre-approves nothing, and a refused helper leaves an honest record.
- Keeping the build within ADR-0001's bound.

**Becomes harder:**
- Using the helpers without prompts: a careful user answers each helper prompt, and one who picks "don't ask again" allows any Python command in that project. The warnings in the README and in the session are the only guard.
- Testing headless: a run must grant the helper by its exact, quoted, installed path.

## Assumptions

- **Settled: what "don't ask again" saves** (spec 002, A2). It saved `Bash(python3 *)`, as recorded under Context. 002-03 records it again in a real session.
- **A plugin installed from a marketplace gets `${CLAUDE_PLUGIN_ROOT}` filled in** as jig's account-synced plugin does (spec 002, A1). The first `scout` run in 002-01 shows it.

## Kill criteria

- ~~"Don't ask again" turns out to offer a bare `python3` rule.~~ Fired on 2026-11-11. Julien chose the README warning over Option D, and Option B stays set aside for its own reasons.
- An issue report shows users accepting the broad rule despite the warning. coaster has no telemetry, so the standing trigger is the scope-4 release check before `v0.1.0`, which reviews this exposure again (tracked in `docs/refinement-todo.md`). Option D is then the next step, after checking that the execute bit survives the build, git and the plugin install.
- Users find the repeat prompts bad enough to stop using the helpers, as 002-03 or later use shows.

## Open questions

None.
