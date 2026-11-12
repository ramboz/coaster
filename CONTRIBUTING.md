# Contributing to coaster

coaster is built with [jig](https://github.com/ramboz/jig)'s spec workflow.
Read [docs/workflow.md](docs/workflow.md) first: every non-trivial change
starts with a spec under [docs/specs/](docs/specs/README.md). The rules below
are the long form of the Git rule in
[docs/conventions.md](docs/conventions.md#git).

## Merging: squash, with a conventional PR title

Pull requests are squash-merged. It is the only merge the repository allows,
and the squashed commit takes the **PR title** as its subject and an empty
body. release-please reads those subjects on `main` to choose the next version
and to write `CHANGELOG.md`, so the PR title is what lands, and
[`pr-title.yml`](.github/workflows/pr-title.yml) checks it on every PR.

A PR title is a [Conventional Commit](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>
```

- **type**: one of `feat`, `fix`, `perf`, `docs`, `chore`, `refactor`, `test`,
  `build`, `ci`.
- **scope**: required, for example `capture`, `challenge`, `release`, `specs`.
- **subject**: starts lowercase and does not end with a period.

`feat(scope): add a deferral to research skills` passes. `Update stuff.` fails:
it has no type or scope, it starts with a capital, and it ends with a period.

Leave the subject as it is in the merge dialog. GitHub appends ` (#N)`, which
is fine. Commits on a branch use the same form, though only the title lands.

## Direct pushes to `main`

Some commits reach `main` without a PR, such as a spec number reserved with
jig's `workflow.py new`. They follow the same form. CI checks every subject
pushed to `main` after it lands, and a bad one turns `main` red. Nothing is
rewritten: fix it forward with an empty commit whose subject states the missed
change in the right form, so release-please counts it:

```bash
git commit --allow-empty -m "feat(scope): what the earlier commit added"
```

Before a direct push, check the subjects you are about to push:

```bash
git log --format=%s origin/main..HEAD \
  | grep -v -E '^(feat|fix|perf|docs|chore|refactor|test|build|ci)\([^)]+\)!?: [a-z].*[^.]$'
```

It should print nothing.

## What CI checks

[`ci.yml`](.github/workflows/ci.yml) runs on every PR and every push to `main`.
To run the same checks locally:

```bash
python3 scripts/build_host_packages.py --check
git ls-files -z '*.py' | xargs -0 python3 -m py_compile
claude plugin validate --strict hosts/claude
claude plugin validate --strict .claude-plugin/marketplace.json
```

- `--check` rebuilds `hosts/claude` and fails if the committed package is
  stale. `hosts/` is generated: edit the source, run
  `python3 scripts/build_host_packages.py`, and commit the result. Never edit
  `hosts/` by hand.
- The byte-compile runs on Python 3.9 and 3.12 in CI, because the helpers run
  on users' `python3`.
- `claude plugin validate` runs on the package folder and the marketplace
  file, not the repository root, where `--strict` fails on the root
  `CLAUDE.md`.
- The home-path search is spec 001's pre-push path search; its pattern is in
  `ci.yml`.

Maintainers also run the publication term search by hand before any push. Its
terms are not published, so CI cannot run it.

The `jig-governance` check fails on any PR that touches a protected path, such
as `docs/conventions.md` or `.github/workflows/`. That is by design: it asks
for the owner's review. See [docs/governance.md](docs/governance.md).

## How a PR title becomes a release

coaster is pre-1.0. These are the effects in release-please's terms:

| Title type | Example | Effect |
|---|---|---|
| `feat` | `feat(scout): …` | minor bump (`0.1.0` → `0.2.0`) |
| `fix`, `perf` | `fix(name): …` | patch bump (`0.1.0` → `0.1.1`) |
| `docs` | `docs(specs): …` | patch bump, and listed under Documentation. A docs-only merge opens a release PR too. |
| `feat!`, or any type with `!` | `feat(capture)!: …` | major bump |
| `chore`, `refactor`, `test`, `build`, `ci` | `ci(release): …` | no release on its own, and hidden from the changelog |

## The release flow

Releases are run by release-please, in
[`release.yml`](.github/workflows/release.yml):

1. Merge PRs to `main` as usual.
2. On each push to `main`, release-please opens or updates a **release PR**,
   `chore(main): release X.Y.Z`. It sets the version in both `plugin.json`
   files, writes `CHANGELOG.md`, and updates
   [`.github/.release-please-manifest.json`](.github/.release-please-manifest.json).
3. **Merging the release PR is the release.** It tags `vX.Y.Z` and publishes a
   GitHub release. Merge it only when the
   [release plan](docs/releases/claude-code-first-release.md)'s release check
   passes. Before merging, if its CI did not run, run `--check` and
   `claude plugin validate --strict hosts/claude` on its branch by hand.
4. Once the release exists, the `package` job checks the tagged package,
   zips `hosts/claude` as `coaster-claude-vX.Y.Z.zip`, validates the unzipped
   copy, and attaches it to the release.

The first release is `0.1.0`: the manifest starts at `0.0.0`, which means
nothing has been released, and the config's `initial-version` sets the first
version.

## Versions

Until `v0.1.0`, every change to the package's bytes bumps the pre-release
number (`0.1.0-pre.N`) in both `plugin.json` files by hand, because an
installed plugin updates only when its version changes. From `v0.1.0` on,
release-please owns the version: nobody edits it by hand, and installed users
see changes when a release lands.
