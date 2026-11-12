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
