# Learnings

> Status: Draft (wizard-generated)
>
> Dead ends, failed approaches, and "we tried X and here's why it didn't work."
> The institutional memory that ADRs don't capture — these are not decisions,
> they're anti-patterns and gotchas discovered in practice.
>
> Update via `/jig:memory-sync` during reconciliation.

<!-- Learnings below. Format: ## Title, followed by what happened and what to do instead. -->

## A refused read can degrade a skill without any error

A headless `capture` run was refused the plugin's own template, carried on, and wrote 9 of the template's 22 headings without reporting a problem. An earlier 3 of 3 result had hidden this because those runs were granted `Read`. Test a skill with no `--allowedTools` grant and check `permission_denials` in the result, not the model's summary.

## Write searches for private strings so they cannot match themselves

A check for a home path written literally in a spec matches the spec once it is pushed. Use a bracketed form in the pattern, such as `[r]amboz`. Run the search over every review sidecar too, since jig's `reviews/.candidates/` files hold absolute paths and are git-ignored for that reason.

## Check the remote right before any publishing step

Another session published this repository, public and with its full history, while a review for publishing it was still running. Right before creating or pushing a repository, run `git remote -v` and `gh repo view`, because their state can change between steps.

## Python bytecode carries absolute paths

A `.pyc` file committed by accident held the absolute path of its source file. Ignore `__pycache__/` and `*.pyc` from the start, and include binary files in any search for private strings.

## A signed-in disposable profile picks up synced plugins and skills

A new `CLAUDE_CONFIG_DIR` was clean at sign-in, and coaster was its only plugin. By the second run, account-synced plugins (jig, data, cowork-plugin-management) had joined it. The synced `deep-research` skill was there from the first session's start, which `scout` would hand research to. Check every run's stream-json `init` event (`plugins` and `skills`), and disable such plugins with `claude plugin disable`. Block skills with `Skill(...)` deny rules in that profile's settings, not in your own.

## "Don't ask again" on `python3 "<path>"` saves `Bash(python3 *)`

In Claude Code 2.1.322, answering "Yes, and don't ask again" to a helper run as `python3 "<script>" ...` saved `Bash(python3 *)` in the project's `.claude/settings.local.json`. That rule allows any Python command. An allow rule must also quote a path the way the command does: an unquoted rule did not match a quoted command. A wildcard for a version folder also matches a `../..` path out of it. Probe the saved rule before relying on a prompt being narrow.

## A release-please manifest at `0.0.0` means "never released"

Seeding `.release-please-manifest.json` at `0.0.0` does not make the first release `0.1.0`. release-please uses the manifest's version as a stand-in previous release only when that version is not `0.0.0`; otherwise it takes the package's `initial-version`, which defaults to `1.0.0`. A frame review caught this before spec 003 merged. Set `initial-version` beside a `0.0.0` seed, and read the version in the release PR's title before merging it.

## A docs-only merge opens a release PR

jig's and servo's CONTRIBUTING tables say `docs` does not release. Their configs show `docs` in the changelog, and servo's `v0.2.1` holds only a Documentation section. With that config, a docs-only merge such as a new spec opens a patch release PR. Describe release behaviour from the config and the tags, not from a sibling's prose.

## Validate the plugin folder, not the repository root

`claude plugin validate --strict .` fails at coaster's root, because `--strict` turns the warning about the root `CLAUDE.md` into an error. Validate `hosts/claude` and `.claude-plugin/marketplace.json` instead. Neither needs a sign-in: both pass with an empty `CLAUDE_CONFIG_DIR`, on macOS and on GitHub's Ubuntu runner.

## release-please's PR gets no checks, and a blank squash body still gets trailers

coaster's first release PR, opened by `github-actions` with the default token, ran no workflow, because events made with `GITHUB_TOKEN` start none. Run `--check` and `claude plugin validate --strict hosts/claude` on its branch by hand before merging it. Separately, with `squash_merge_commit_message: BLANK`, GitHub still appends `Co-authored-by:` trailers from the squashed commits; release-please ignores them, but "empty body" is not literally true.

## Headless subagents run in the background, and cannot ask

In Claude Code 2.1.322, a headless `claude -p` parent started its subagents in the background. The `Agent` call's `tool_result` is only a launch notice. The subagent's reply arrives later as a `system` event of subtype `task_notification` with the same `tool_use_id`: its `summary` is the reply, identical to the subagent transcript's last message, and its `usage` holds tokens, tool uses and time. Such a run ends with several `result` events, so collect `permission_denials` from all of them. A background subagent cannot ask for permission, so a Bash command that `acceptEdits` does not allow by itself, such as `ls -R …; cat …; for f in …`, is denied. Slice 002-02 found this in nine of fifteen built-in hats.

## A subagent's system prompt is in its transcript, not in the stream

The stream-json log carries each `Agent` call's `prompt`, not the subagent's system prompt. The subagent's own transcript does, at `$CLAUDE_CONFIG_DIR/projects/<run folder>/<session>/subagents/agent-<task id>.jsonl`, in an attachment of type `prompt_snapshot`. Match an `Agent` call to its task with the `task_started` event. For a plugin agent, the first block equals the agent file's body, apart from surrounding whitespace (2.1.322). Its `tools` line held: a hat limited to `Read, Grep, Glob, WebSearch, WebFetch` made no other call, and `model: inherit` ran on the session's Sonnet and Opus.

## A copied profile is not signed in

Copying a signed-in `CLAUDE_CONFIG_DIR` to a new path gives a profile that answers "Not logged in", because the sign-in is not stored in the folder. To run a local `--plugin-dir` build in place of an installed plugin without touching the profile, disable the installed one for that run only: `--settings '{"enabledPlugins":{"coaster@coaster":false}}'`. The `init` event then lists the `--plugin-dir` copy as `coaster@inline`.
