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

## Decision Options Considered

### Option A: Ask, like jig's helpers
- **Pros:** coaster grants itself nothing, which matches jig, servo and shaper. Running a network script is a fair moment to ask. The build needs no new text change.
- **Cons:** "Don't ask again" is saved per project and names the versioned path, so a user is asked again in each new idea folder and after each update.

### Option B: A rendered `allowed-tools` grant naming the exact installed path
- **Pros:** No prompt, and narrower than any rule a user writes.
- **Cons:** Adds a build text change beyond ADR-0001's bound. A frontmatter grant has only been seen lasting for the turn that invoked the skill, and `scout` often checks links in a later turn. No sibling pack grants itself Bash.

### Option C: An allow rule in the README, with a wildcard for the version
- **Pros:** Written once, it outlives version changes.
- **Cons:** Its wildcard also admitted a `..` path to a script outside the plugin, so publishing it would invite users to allow more than coaster's helpers.

## Recommended Decision

Option A, chosen by Julien on 2026-11-11.

- **The command.** The source runs each helper as `python3 scripts/<file>`. The build renders it in jig's form, `python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"`, so it does not depend on the execute bit. The build's `HELPERS` keys, rewrite and `FORBIDDEN` guard follow that form, which stays inside ADR-0001's bound of "the two helper paths".
- **No workaround.** When a helper is refused, the skill tries no other command to the same end, because the user declined running code. If web tools are allowed, it takes the web route its text already gives for chat, and says so. Otherwise it records the check as not run, with the reason and the command to run by hand. It never records a result that no tool returned.
- **The README** says that coaster grants itself no permissions and that Claude Code asks before each helper runs. It recommends no allow rule.

## Consequences

**Becomes easier:**
- Trusting the plugin: it pre-approves nothing, and a refused helper leaves an honest record.
- Keeping the build within ADR-0001's bound.

**Becomes harder:**
- Using the helpers without prompts: a user is asked again in each new idea folder and after each update.
- Testing headless: a run must grant the helper by its exact, quoted, installed path.

## Assumptions

- **What "don't ask again" saves has not been run** (spec 002, A2). If it saves a broad `python3` prefix rather than the script's path, asking stops being the narrow choice. 002-03 records the rule the prompt offers.
- **A plugin installed from a marketplace gets `${CLAUDE_PLUGIN_ROOT}` filled in** as jig's account-synced plugin does (spec 002, A1). The first `scout` run in 002-01 shows it.

## Kill criteria

- "Don't ask again" turns out to save a broad `python3` rule. Option B then becomes the narrower choice and is reconsidered.
- Users find the repeat prompts bad enough to stop using the helpers, as 002-03 or later use shows.

## Open questions

None.
