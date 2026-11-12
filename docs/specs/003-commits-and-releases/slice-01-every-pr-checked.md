---
status: DRAFT
dependencies: [001-02]
last_verified:
frame_review: true
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 003-01 — every PR checked

**Goal:** Write down the conventional-commit rule, and check every pull request
on GitHub twice: its title against the rule, and its contents with the drift
guard, plugin validation, a Python byte-compile and the path search. Every
push to `main` gets the content checks too, and a check of the subjects that
landed.

**DoR:**
- ✅ Spec 001 is DONE, and `origin/main` is at `a28e0cd` or later.
- ✅ jig's and servo's `pr-title.yml`, `ci.yml`, `release.yml`, release-please
  files and `CONTRIBUTING.md` were read on 2026-11-11 (the spec's Current
  state).
- Julien has approved the exact conventions text in AC 1.
- The repository's merge settings are the ones servo recorded in its slice
  010-01 (A3): `gh api repos/ramboz/coaster` returns
  `allow_squash_merge: true`, `allow_merge_commit: false`,
  `allow_rebase_merge: false` and `squash_merge_commit_title: PR_TITLE`, plus,
  beyond servo, `squash_merge_commit_message: BLANK`. Julien sets them, or lets
  this session set them with `gh api -X PATCH` after switching `gh` to
  `ramboz`, and switch back. The slice does not start while any of the five
  differs: under GitHub's defaults the title check would not check what lands,
  and the default body (`COMMIT_MESSAGES`) would carry branch commits' footers,
  such as `BREAKING CHANGE:`, which release-please reads and no check sees.
- Julien accepted the spec's decisions.

**Acceptance Criteria:**

1. **The rule is written.** The `## Git` section of `docs/conventions.md` holds
   this text in place of its Deferred note, written with
   `JIG_CONVENTIONS_APPROVED=1` set for that edit only, after Julien approved it:

   ```markdown
   **Rule:** Every commit that lands on `main`, by pull request or by a direct
   push, is a Conventional Commit, `<type>(<scope>): <subject>`. The type is
   one of `feat`, `fix`, `perf`, `docs`, `chore`, `refactor`, `test`, `build`
   or `ci`; the scope is required; the subject starts lowercase and does not
   end with a period. Pull requests are squash-merged, the only merge the
   repository allows, with the PR title as the subject and an empty body, so
   the PR title is the commit that lands. `.github/workflows/pr-title.yml`
   checks the title on every PR, and `.github/workflows/ci.yml` checks every
   subject pushed to `main`, after the fact. Do not edit the subject in the
   merge dialog. Commits on a branch use the same form.
   **Why:** release-please reads the subjects on `main` to choose the next
   version and to write `CHANGELOG.md`, as in jig and servo. A subject it cannot
   parse is left out of both.
   **How to apply:** Write the PR title in this form; it is the subject that
   lands. `feat` bumps the minor version; `fix`, `perf` and `docs` bump the
   patch; `chore`, `refactor`, `test`, `build` and `ci` release nothing on their
   own. A `!` after the scope or a `BREAKING CHANGE:` footer bumps the major
   version. Until `v0.1.0`, every change to the package's bytes still bumps the
   pre-release number in both `plugin.json` files by hand; from `v0.1.0` on,
   release-please owns the version and nobody edits it by hand. Branch names
   stay open. `CONTRIBUTING.md` has the long form.
   ```

   `CLAUDE.md`'s Development Conventions gain one line: every commit on `main`,
   and so every PR title, is a conventional commit, because PRs are
   squash-merged and release-please reads `main`, with links to the Git rule
   and `CONTRIBUTING.md`.
2. **The title check mirrors jig's.** `.github/workflows/pr-title.yml` runs
   `amannn/action-semantic-pull-request@v6` on `pull_request` (`opened`,
   `edited`, `synchronize`, `reopened`) with `permissions: pull-requests: read`,
   the nine types above, `requireScope: true`, `subjectPattern: ^[a-z].*[^.]$`
   and jig's error message. A `diff` with jig's file shows only the comment
   header.
3. **CI runs on every PR and on `main`.** `.github/workflows/ci.yml` runs on
   `pull_request` and on `push` to `main`, with `permissions: contents: read`:
   - a job on Python 3.9 and 3.12 (`fail-fast: false`) that runs
     `python3 scripts/build_host_packages.py --check`, byte-compiles every
     tracked `.py` file, and runs spec 001's path search,
     `git grep -n -E '/Users/[r]amboz|~/[P]rojects|-Users-[r]amboz|/private/tmp/[c]laude-'`,
     failing when the search finds anything;
   - a job that installs `@anthropic-ai/claude-code@2.1.322` with npm and runs
     `claude plugin validate --strict hosts/claude` and
     `claude plugin validate --strict .claude-plugin/marketplace.json`;
   - on `push` to `main` only, a step in a checkout with full history
     (`fetch-depth: 0`) that lists the subjects in
     `github.event.before..github.event.after` and fails, naming them, when
     any does not match
     `^(feat|fix|perf|docs|chore|refactor|test|build|ci)\([^)]+\)!?: [a-z].*[^.]$`,
     the title check's rules as one pattern. This is what covers direct pushes,
     including `workflow.py new` reservations, and subjects edited in the merge
     dialog. A red `main` is the signal, and only for that run; nothing is
     rewritten. The fix is forward: an empty commit whose subject states the
     missed change in the right form, so release-please counts it.
4. **Each check can fail.** Run locally with the same commands, each check
   exits non-zero on a planted fault and zero once it is removed: a line added
   to a rendered `hosts/claude/skills/*/SKILL.md` (`--check`); a tracked
   scratch file holding a home path (the path search); a scratch copy of the
   package whose `plugin.json` has no `name` (validate); a scratch `.py` file
   with a `match` statement, compiled with the macOS `/usr/bin/python3` 3.9
   (the byte-compile). No fault is committed. The subject check needs no
   planted fault: on all of `origin/main` it fails and names the two unscoped
   early commits, and on `bbeda54..a28e0cd` it passes (run on 2026-11-11 while
   drafting, to be re-run with the committed step).
5. **Both workflows pass on this spec's PR, and the title check fails a bad
   title.** On the PR that lands this spec, `PR Title` and both CI jobs pass
   with the PR's conventional title. With Julien's OK, the title is changed to
   `Update stuff.`, the `PR Title` check fails, and the title is restored; the
   run ids are recorded. That this is the first PR the workflows run on is
   expected: GitHub runs a PR's own new workflows. `jig-governance` fails on
   this PR, as designed, because it touches `docs/conventions.md` and
   `.github/workflows/**`. It will fail on any later PR that touches them too,
   such as one raising the Claude Code pin, and asks for Julien's review there.
6. **CONTRIBUTING.md.** A new root `CONTRIBUTING.md` explains, after servo's:
   squash-merge as the only merge, with the title as the subject that lands
   and left unedited at merge, and the title form, with a passing and a
   failing example; that a direct push to `main` follows the same form, is
   checked after the fact, and is fixed forward with a correctly worded empty
   commit; the checks CI runs, with the commands to run them locally,
   including the subject check over `origin/main..HEAD` before a direct push;
   and, for maintainers, that the publication term search runs by hand before
   a push, because its terms are not published.
7. **The merge settings are recorded.** The deviation log quotes the five
   fields from `gh api repos/ramboz/coaster` as they stand when the PR is
   opened, and the squash commit that lands this spec carries the PR's title
   followed by GitHub's ` (#N)`, with an empty body. The `CI` run on `main` for
   that commit passes the subject check.

**DoD:**
- [ ] All ACs pass, with evidence in the deviation log (commands, exit codes,
      run ids).
- [ ] The build, `--check`, the path search, the term search and the subject
      check over `origin/main..HEAD` pass before the push, and `git remote -v`
      and `gh repo view` are checked first.
- [ ] Frame-critique, compliance and craft passes recorded with
      `review.py record-review`.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [ ] Reconciliation review passed.

**Anti-horizontal-phasing check:** After this slice, anyone who opens a PR on
coaster sees whether its title follows the rule and whether the package is
current, valid and free of home paths, before anything merges.
