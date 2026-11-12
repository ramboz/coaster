---
status: DONE
skill:
use_cases: []
---

<!-- jig self-defining vocabulary (soft, forward-only): expand each acronym on first use and link the term to docs/memory/glossary.md (or jig's lexicon). See docs/workflow.md "Self-defining vocabulary". -->

# Spec 003: Conventional commits and releases

> Reserved on 2026-11-11 as a local provisional number with `workflow.py new
> --no-push`, so that pushing to the public `main` stays Julien's call.
> `origin/main` held specs 000 to 002 at the time. Serves the CI, CHANGELOG and
> tag items of scope 4 of the
> [Claude Code first release](../../releases/claude-code-first-release.md), and
> resolves the "CI/CD setup" entry in
> [refinement-todo](../../refinement-todo.md#operations), whose trigger
> is scope 4. `use_cases: []` on purpose: this is release plumbing, and no use
> case in the vision covers it.

## Overview

Julien asked for two things that bring coaster in line with its sibling packs,
jig and servo:

1. **Conventional commits, always.** Record the rule, and enforce it the way jig
   and servo do: pull requests are squash-merged, so the PR title becomes the
   commit on `main`, and a `pr-title.yml` workflow checks every title.
2. **A proper release mechanism.** jig and servo each run a CI workflow on every
   PR, and a release workflow in which release-please turns the commit subjects
   on `main` into a version, a `CHANGELOG.md`, a `vX.Y.Z` tag and a GitHub
   release, then attaches the package to that release.

This spec adapts both to coaster. It does not cut `v0.1.0`. The mechanism keeps
a release PR open, and merging that PR is the release. Julien merges it once
the release plan's release check passes.

### Current state (verified 2026-11-11)

**coaster**

- `origin/main` is at `a28e0cd` (`feat(claude): the whole loop, installed`).
  That is PR #1, squash-merged from 5 commits. The PR was titled `Spec 002: the
  whole loop, installed (scope 2)`, so the subject that landed was typed in the
  merge dialog: it matches neither the title nor a commit.
  `.github/workflows/` holds only `jig-governance.yml`,
  which fails a PR that touches a governance-protected path, among them
  `docs/conventions.md`, `.github/workflows/**` and `CODEOWNERS`. It is inert
  until branch protection is armed (`docs/governance.md`).
- The repository has no tag and no release (`gh api repos/ramboz/coaster/tags`
  and `.../releases` both return 0 items), and no `CHANGELOG.md`. `LICENSE`
  (MIT) and a `CODEOWNERS` owned by `@ramboz` are in place.
- All 17 commits on `origin/main` parse as conventional commits: 6 `feat`, 9
  `docs`, 2 `chore`. Two early ones have no scope (`chore: stop tracking Python
  bytecode`, `docs: adopt jig, ...`). 16 of the 17 were pushed directly, PR #1
  being the only PR. jig's `workflow.py new` also pushes a spec reservation
  straight to `main` unless told `--no-push` or `--pr` (its `spec-workflow`
  skill, step 2).
- `docs/conventions.md` leaves Git open: "commit message format and branch
  naming not yet decided". The file is governance-protected, and the spec-gate
  hook blocks an edit unless `JIG_CONVENTIONS_APPROVED=1` is set.
- Both `plugin.json` files say `0.1.0-pre.2` and are byte-identical. The build
  copies `.claude-plugin/plugin.json` into `hosts/claude/.claude-plugin/`
  unchanged (`scripts/build_host_packages.py`, `build()`), and `--check`
  compares every file of the rebuilt package with the committed one, so a
  release that writes the same version into both files keeps `--check` green.
  The build copies `README.md` and `LICENSE` into the package and nothing else
  from the root, so a root `CONTRIBUTING.md` or `CHANGELOG.md` does not change
  the package's bytes.
- On Claude Code 2.1.322, with an empty `CLAUDE_CONFIG_DIR` and no API key,
  `claude plugin validate --strict hosts/claude` and
  `claude plugin validate --strict .claude-plugin/marketplace.json` both exit 0.
  Each prints an `ICON_MISSING` "plugin directory" warning, which the output
  says does not change the result. `claude plugin validate --strict .` on the
  repository root exits 1, because `--strict` turns the root `CLAUDE.md`
  warning into an error. `npm view @anthropic-ai/claude-code@2.1.322 version`
  returns `2.1.322`.
- The path search from spec 001 (001-02's AC 2) finds nothing on `HEAD`. The
  publication term search reads a terms file that lives only on the local
  `pre-publication` branch, which is never pushed.
- Repository settings could not be read while drafting: under the active `gh`
  account, `ramboz_adobe`, `gh api repos/ramboz/coaster` returns `null` for
  every merge setting, and the Actions permissions endpoint returns 403. Read
  as `ramboz` after review, they allowed squash merges only, with
  `squash_merge_commit_title: PR_TITLE`, `squash_merge_commit_message:
  PR_BODY` and `can_approve_pull_request_reviews: false` (003-01's and
  003-02's DoRs record the two changes).

**jig and servo** (local checkouts of `ramboz/jig` at `35826fb0` and
`ramboz/servo` at `f0caa22`, read on 2026-11-11)

- **PR titles.** Both have `.github/workflows/pr-title.yml`:
  `amannn/action-semantic-pull-request` (`@v6` in jig, `@v5` in servo) on
  `pull_request` (`opened`, `edited`, `synchronize`, `reopened`), with
  `permissions: pull-requests: read`, the types `feat fix perf docs chore
  refactor test build ci`, `requireScope: true`, and `subjectPattern:
  ^[a-z].*[^.]$`. The rulesets are identical.
- **Where the rule is written.** Both state it in `CONTRIBUTING.md` (servo:
  "Merging: squash + conventional-commit PR titles"; jig: "Releasing"), and jig
  repeats it in its README's Contributing paragraph. Neither puts it in
  `docs/conventions.md` or `CLAUDE.md`.
- **Releases.** Both `release.yml` files run on `push` to `main` and on
  `workflow_dispatch`, with `contents: write` and `pull-requests: write`. A
  `release-please` job (`googleapis/release-please-action`, `@v5` in jig, `@v4`
  in servo) reads `.github/release-please-config.json` and
  `.github/.release-please-manifest.json`. A `package` job runs only when a
  release was created: it checks out the tag, builds one zip per host with the
  pack's own `build_release_zip.py`, smoke-tests it, uploads it with
  `gh release upload`, and appends an "Install artifacts" note to the release.
- **Config.** Both configs are `release-type: simple`,
  `include-component-in-tag: false`, `include-v-in-tag: true`, with one
  `extra-files` JSON entry (`$.version`) per `plugin.json`, root and host
  package alike. `changelog-sections` shows `feat`, `fix`, `perf` and `docs`,
  and hides `chore`, `refactor`, `test`, `ci` and `build`. jig's release PR
  #240 (`chore(main): release 2.17.0`) changed only the `plugin.json` files,
  the manifest and `CHANGELOG.md`.
- **First release.** servo seeded its manifest at `0.1.0` with no `v0.1.0`
  tag, and its first release was `v0.2.0` (its tags start at `v0.2.0`), with a
  compare link to the missing `v0.1.0`: release-please bumped from the
  manifest's version. jig pinned `release-as: "1.0.0"` for its first release
  and removed it afterwards
  (`38879bc8 chore(release): unpin release-as after v1.0.0`).
- **How release-please picks a first version** (its source on `main`, read
  2026-11-11). When no release matches, `src/manifest.ts` stands in the
  manifest's version as the previous release only if that version is not
  `0.0.0`. Otherwise `buildNewVersion` in `src/strategies/base.ts` falls back
  to `initialReleaseVersion()`, which returns the package's `initial-version`
  if set and `1.0.0` if not. A `release-as` pin wins over both. The config
  schema allows `initial-version` in a package entry, and
  `release-please-action@v5` depends on `release-please` `^17.6.0`.
- **What a `docs` merge does.** servo's `v0.2.1` holds only a Documentation
  section, so a docs-only merge produced a patch release PR. servo's
  CONTRIBUTING table says `docs` does not release, and jig's says it does not
  bump the version. The configs say otherwise, and coaster's docs follow the
  observed behaviour.
- **Checks on the release PR.** jig's release PR #240 was opened by
  `github-actions[bot]` and still ran the `conventional-commit` check and both
  `test` jobs (run `40438128461`, `triggering_actor` `ramboz`).
- **CI.** jig's `ci.yml` runs on `pull_request` and on `push` to `main`, on
  Python 3.9 and 3.12: a skill-routing eval, its tests, `spec_lint.py`, its own
  `validate_manifests.py`, ruff, and `build_host_packages.py --check`. servo
  runs its tests, `validate_manifests.py`, ruff, an install-surfaces check and
  `--check`, on the same two versions. Neither installs Claude Code in CI.

## Decisions

Julien accepted these on 2026-11-11, with the conventions text in 003-01's
AC 1.

- **Mirror the PR-title gate exactly.** coaster's `pr-title.yml` is jig's file
  (`@v6`), with a comment header. No fixed list of scopes, as in jig and servo.
- **Check what lands on `main` too.** coaster's `main` takes direct pushes,
  and nothing protects it (Non-goals). CI's run on each push to `main` checks
  every new subject against the title check's rules, so a direct push or a
  subject edited in the merge dialog turns `main` red instead of dropping out
  of the changelog unseen. jig and servo do not do this. Rejected: a rule that
  forbids direct pushes, which only branch protection could enforce.
- **Squash with an empty body.** Beyond servo's four merge settings,
  `squash_merge_commit_message: BLANK`, so a breaking change is marked only by
  the `!` that the title check sees, not by a footer copied in from a branch
  commit.
- **Record the rule in three places.** `docs/conventions.md` gets a Git rule
  (the exact text is in 003-01's AC 1 and needs Julien's approval before it is
  written). A new root `CONTRIBUTING.md` carries the long form, as in jig and
  servo. `CLAUDE.md` gets one line under Development Conventions, so every
  session sees it. The README is left alone because spec 002's slice 002-01 is
  editing it; a pointer to `CONTRIBUTING.md` can follow once 002-01 lands.
- **CI checks what coaster has.** coaster has no test suite, and the release
  plan rules out a test harness for the Markdown skills. CI runs the drift
  guard, `claude plugin validate --strict` on the package and on the
  marketplace file (in place of jig's and servo's own `validate_manifests.py`),
  a byte-compile of the Python files on 3.9 and 3.12 (the floor jig and servo
  support), and the path search. The path search is spec 001's public half of
  the pre-push check. The term search stays by hand, because its terms must not
  be published. No ruff: coaster's conventions leave code style open.
- **Pin Claude Code in CI.** CI installs `@anthropic-ai/claude-code@2.1.322`
  with npm. A pinned version keeps a CLI change from turning CI red overnight.
  Raising the pin is an ordinary `ci(...)` PR.
- **release-please, configured as in jig and servo.** Same type, tag and
  changelog settings, with `extra-files` for coaster's two `plugin.json` files.
  The marketplace manifest carries no version and is not touched.
- **Seed the manifest at `0.0.0`, with `initial-version: "0.1.0"`.** Nothing
  has been released, and `0.0.0` says so. With that seed, release-please takes
  the first version from `initial-version`, whatever the commit types (a `!`
  cannot turn it into `1.0.0`), and once `v0.1.0` exists it bumps from that
  release and the setting no longer applies. Nothing has to be removed later.
  Rejected: `0.0.0` alone, which gives `1.0.0` (release-please's source,
  above); jig's `release-as` pin, which needs a follow-up PR to remove it after
  the tag; and servo's non-zero seed (`0.0.1`, say), which records a release
  that never happened and leaves a broken compare link in the changelog.
- **No `CHANGELOG.md` stub.** release-please writes the file in the first
  release PR, with `0.1.0` as its first entry. The release plan's "CHANGELOG in
  place" is met when that PR merges, which is also the tag.
- **A zip on each release.** As in jig and servo, the `package` job attaches
  the package to the release, as `coaster-claude-vX.Y.Z.zip`. coaster has no
  `build_release_zip.py`, and none is written: the job checks the tag with
  `--check`, checks that both `plugin.json` files carry the release's version,
  zips `hosts/claude` with `git archive`, validates the unzipped copy with
  `claude plugin validate --strict`, and uploads it. This runs after the tag
  and the release exist, so it checks the shipped bytes but gates nothing. The
  release plan's "`claude plugin validate --strict` passes on the package" is
  met before the merge, by CI on `main` and on the release PR (or by hand,
  A4). The job first runs on an Ubuntu runner at `v0.1.0`, because a
  `workflow_dispatch` run creates no release. If it fails there, the tag and
  release stand without the zip, and the zip is fixed and uploaded by hand.
- **Versions.** Until `v0.1.0`, every change to the package's bytes still bumps
  the pre-release number by hand in both `plugin.json` files (spec 001), and
  the release PR then sets `0.1.0`. From `v0.1.0` on, release-please owns the
  version: nobody edits it by hand, and installed users see changes when a
  release lands, as with jig and servo (an installed plugin updates only when
  its version changes, jig ADR-0036).
- **`docs` stays visible in the changelog.** This keeps parity with jig and
  servo. Its cost: a docs-only merge, such as a spec, keeps a patch release PR
  open. Merging it stays Julien's call, so nothing ships by itself.
- **No ADR.** The choice of mechanism is the family's, recorded in servo's
  ADR-0007 and jig's spec 013. This spec records coaster's differences above.
  If Julien wants an ADR, it takes the number after 002-01's.

## Non-goals

- Cutting `v0.1.0`. Merging the release PR is the release, and it waits for
  the release plan's release check.
- The ai-pegboard catalog entry, which lives in another repository and pins a
  tag that does not exist yet.
- Branch protection, and making any check required. Arming it is Julien's
  server-side step (`docs/governance.md`).
- A test harness, ruff, or a check that the pre-release number was bumped.
- Pinning the marketplace to a tag. It keeps installing from `main`, as jig's
  and servo's do.
- Codex, Copilot or claude.ai packages.

## Assumptions

- **A1.** `claude plugin validate --strict` behaves on an Ubuntu runner with no
  sign-in as it did on macOS with an empty profile. 003-01's own PR shows it.
- **A2.** The `release-please` that `@v5` resolves to behaves as its source on
  `main` does: with the manifest at `0.0.0`, no tag and `initial-version:
  "0.1.0"`, the first release PR proposes `0.1.0`. That was read in the
  source, not run. The release PR's title shows the version before anything is
  merged, and 003-02's AC 7 checks it. With Julien's OK, release-please's own
  CLI can preview it earlier, with `release-pr --dry-run` against the pushed
  branch.
- **A3.** The repository can be set, as servo's is, to squash-merge only, with
  the PR title as the squashed subject (`allow_squash_merge: true`,
  `allow_merge_commit: false`, `allow_rebase_merge: false`,
  `squash_merge_commit_title: PR_TITLE`), and to let GitHub Actions create pull
  requests. None of these can be read under `ramboz_adobe`, and PR #1 says
  nothing about them. GitHub's defaults for a new repository allow all three
  merge methods and use `COMMIT_OR_PR_TITLE`, under which a single-commit PR
  lands its commit message, not its title. Under the defaults, a rebase merge
  lands unchecked branch commits and a merge commit lands `Merge pull request
  #N`. So 003-01 blocks until the merge settings hold, and 003-02 until
  Actions may create PRs (their DoRs). Even then, the merge dialog lets the
  merger edit the subject, as PR #1 shows, and a direct push skips the title
  check. Both are caught only after they land, by CI's subject check on
  `main`.
- **A4.** CI and the title check run on release-please's PR in coaster, as they
  did on jig's PR #240. GitHub documents that events made with `GITHUB_TOKEN`
  start no new workflow runs, and #240's runs name `ramboz` as the triggering
  actor, which points to a person's action rather than the bot's. Expect the
  fallback: if no checks run, `--check` and
  `claude plugin validate --strict hosts/claude` run by hand on the release
  PR's branch before it is merged. The release `package` job re-runs `--check` on the tag
  in any case. release-please's PR is therefore the one PR that "every PR
  checked" may not cover.
- **A5.** `git archive --format=zip HEAD:hosts/claude` writes the package's
  files at the root of the zip, which then validates like `hosts/claude`. On
  2026-11-11, on macOS, the unzipped file list matched
  `git ls-files hosts/claude` and `claude plugin validate --strict` passed on
  it. The first release shows it on the Ubuntu runner.

## Decomposition

**SPIDR axis: Rules.** SPIDR is jig's split of work by Spike, Path, Interface,
Data or Rules. The split is by when a rule is enforced: on every PR, then on
every push to `main`.

- **003-01 — every PR checked.** The convention is written down, and every PR
  gets a title check and a content check. A contributor sees both on the PR.
- **003-02 — releases from main.** Every push to `main` keeps a release PR up
  to date, and merging it tags, publishes and attaches the package. Julien sees
  the release PR.

003-02 depends on 003-01, because release-please is only as good as the
subjects on `main`: the title check guards those that come by PR, and the
subject check reports, after the fact, those that do not. Both land in one PR. The live release PR
can only appear after that PR merges, so 003-02 closes with a short follow-up
commit that records it, as spec 001 closed with `bbeda54`.

## Slices

- [003-01 — every PR checked](slice-01-every-pr-checked.md)
- [003-02 — releases from main](slice-02-releases-from-main.md)

## Deferred decisions this spec reaches

| Entry | Effect |
|---|---|
| [CI/CD setup](../../refinement-todo.md#operations) | Resolved by this spec: CI runs the drift guard, plugin validation and the path search; release-please owns releases. The term search stays by hand. |
