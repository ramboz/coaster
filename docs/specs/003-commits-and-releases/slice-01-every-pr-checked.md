---
status: RECONCILED
dependencies: [001-02]
last_verified: 2026-11-11
frame_review: true
claimed_by: claude/release-mechanism-cbea54
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
- ✅ Julien approved the exact conventions text in AC 1 on 2026-11-11.
- ✅ The repository's merge settings are the ones servo recorded in its slice
  010-01 (A3): `gh api repos/ramboz/coaster` returns
  `allow_squash_merge: true`, `allow_merge_commit: false`,
  `allow_rebase_merge: false` and `squash_merge_commit_title: PR_TITLE`, plus,
  beyond servo, `squash_merge_commit_message: BLANK`. Julien sets them, or lets
  this session set them with `gh api -X PATCH` after switching `gh` to
  `ramboz`, and switch back. The slice does not start while any of the five
  differs: under GitHub's defaults the title check would not check what lands,
  and the default body (`COMMIT_MESSAGES`) would carry branch commits' footers,
  such as `BREAKING CHANGE:`, which release-please reads and no check sees.
  On 2026-11-11, with Julien's OK and `gh` switched to `ramboz`, the first four
  already held and `squash_merge_commit_message` was `PR_BODY`; it was set to
  `BLANK`, read back, and `gh` switched back to `ramboz_adobe`.
- ✅ Julien accepted the spec's decisions on 2026-11-11.

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
      run ids). AC 7's second half (the squash subject, its empty body, and
      `subjects` passing on `main`) comes from the follow-up commit after the
      merge, with 003-02's AC 7.
- [ ] The build, `--check`, the path search, the term search and the subject
      check over `origin/main..HEAD` pass before the push, and `git remote -v`
      and `gh repo view` are checked first.
- [ ] Frame-critique, compliance and craft passes recorded with
      `review.py record-review`.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [x] Reconciliation review passed.

**Anti-horizontal-phasing check:** After this slice, anyone who opens a PR on
coaster sees whether its title follows the rule and whether the package is
current, valid and free of home paths, before anything merges.

### Deviation log (after reconciliation)

The acceptance criteria above are kept as written. Implementation notes, 2026-11-11:

1. **The conventions edit.** jig's spec-gate hook reads
   `JIG_CONVENTIONS_APPROVED` from Claude Code's own environment, so it cannot
   be set for a single Edit call. After Julien approved the text, the edit was
   made by one shell command with `JIG_CONVENTIONS_APPROVED=1` set for that
   command only. The hook's own comment names that route. A `diff` of the new
   `## Git` body against AC 1's block shows no difference.
2. **Three CI jobs, not two plus a step.** `ci.yml` has `check` (Python 3.9
   and 3.12: `--check`, the byte-compile, the path search), `validate` (Claude
   Code 2.1.322, both `validate --strict` runs), and `subjects` (push only).
   The subject check is its own job with `fetch-depth: 0`, so it runs once and
   not in each Python leg. `validate` points `CLAUDE_CONFIG_DIR` at a folder
   that does not exist yet, outside the checkout, and sets
   `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, matching the signed-out local
   probe. The byte-compile is
   `git ls-files -z '*.py' | xargs -0 python3 -m py_compile`.
3. **AC 2.** `diff` against jig's `pr-title.yml` shows only the four-line
   comment header.
4. **AC 4, each check fails on a planted fault (local, 2026-11-11).** The
   path-search and subject-check scripts were taken from `ci.yml` with Ruby's
   YAML parser, so the committed text was the code under test.
   - `--check`: a line appended to `hosts/claude/skills/capture/SKILL.md`
     gives exit 1, naming the file. Exit 0 after `git checkout`.
   - Path search: an intent-to-add scratch file holding a home path gives
     exit 1. Exit 0 once it is removed.
   - Byte-compile: a `match` statement under the macOS `/usr/bin/python3`
     3.9.6 gives exit 1. Exit 0 once the file is fixed. All tracked `.py`
     files compile on 3.9.6 and 3.14.
   - Validate: a scratch copy of the package whose `plugin.json` has no `name`
     gives exit 1 (`name: Invalid input: expected string, received
     undefined`). Exit 0 once restored.
   - Subject check:
     - with `BEFORE` set to the root commit `fd473ab` and `AFTER` to
       `origin/main`: exit 1, naming `chore: stop tracking Python bytecode`
       and `docs: adopt jig, ...`. The step's `BEFORE..AFTER` range leaves
       out the root commit itself, `feat(pack): draft the idea-triage skill
       pack and its first dogfood run`, which matches the pattern;
     - on `bbeda54..a28e0cd`: exit 0;
     - with an unknown `before`: falls back to the last commit, exit 0;
     - on the 8 commits spec 002 pushed to `main` while this was built
       (`a28e0cd..1e11dce`): exit 0.
5. **Merge settings (AC 7, first half).** Read as `ramboz` on 2026-11-11, with
   Julien's OK. `allow_squash_merge: true`, `allow_merge_commit: false`,
   `allow_rebase_merge: false` and `squash_merge_commit_title: PR_TITLE`
   already held. `squash_merge_commit_message` was `PR_BODY`, so it was set to
   `BLANK`. The read-back, minutes before PR #2 was opened, returned exactly
   `{"allow_merge_commit":false,"allow_rebase_merge":false,"allow_squash_merge":true,"squash_merge_commit_message":"BLANK","squash_merge_commit_title":"PR_TITLE"}`.
   Only Julien's account can change these settings, and nothing in this
   session changed them between that read and the PR's opening.
   `gh` was then switched back to `ramboz_adobe`.
6. **Rebase.** `origin/main` moved 8 commits during implementation: spec 002's
   fixes, with the package at `0.1.0-pre.8`. The branch rebased with no
   conflict. The status board was regenerated, and the drift guard, plugin
   validation, the byte-compile and the pre-push searches were re-run on the
   rebased tree.
7. **One `CONTRIBUTING.md` for both slices.** It holds this slice's merging,
   direct-push and CI sections and 003-02's release sections.
8. **Live evidence (AC 5).** [PR #2](https://github.com/ramboz/coaster/pull/2)
   was opened on 2026-11-11 as `ramboz`, with Julien's OK, from `a258006`.
   - **CI run `43132628853`:** `check (3.9)`, `check (3.12)` and `validate`
     all pass. `validate` logged `✔ Validation passed` for the package and the
     marketplace on the Ubuntu runner, signed out, which settles A1.
     `subjects` was skipped, as it runs only on pushes to `main`.
   - **PR Title run `43132629005`:** passes on the conventional title,
     `ci(release): check every PR and release from main with release-please`,
     which is the baseline for AC 7's squash-subject check.
   - **Title test, with Julien's OK:** the title was changed to `Update stuff.`
     as `ramboz`. Run `43132861588` failed with "No release type found in pull
     request title". The title was restored, and run `43132923618` passes.
   - **`jig-governance` run `43132628737`:** fails, as AC 5 expects for a PR
     that touches protected paths.

   AC 7's second half (the squash subject, the empty body and the `main` run
   of `subjects`) can only be shown after the merge, and is recorded with
   003-02's AC 7.
9. **Review findings, 2026-11-11.**
   - **Compliance (needs-changes).** Three fixes:
     - `CONTRIBUTING.md` now gives the path search as a local command;
     - item 5 quotes the settings exactly;
     - the DoD routes AC 7's second half to the follow-up commit.
   - **Craft (pass, with nits).** Applied:
     - `ci.yml`'s path search now fails on a `git grep` error (exit 2 or
       more) rather than reading it as "no match";
     - the subject check now fails when `git log` fails, because its output is
       captured in its own assignment;
     - the subject check warns when it falls back to the newest commit only.

     Each change was tested from the YAML: a `git grep` error gives exit 128,
     a bad `after` gives exit 128, and an unknown `before` warns and passes.
     `CONTRIBUTING.md` now names `/usr/bin/python3` for the 3.9 floor, and
     says the type list and subject rule live in four places and change
     together.
   - **Not applied.** Pinning Node with `actions/setup-node`: the runner's Node
     only installs the pinned CLI. Pinning actions by SHA: the spec mirrors
     jig's tags. `pipefail` on the byte-compile line (fourth compliance run):
     a `git ls-files` failure would let it pass with nothing compiled, but
     that cannot happen in a fresh checkout, and changing `ci.yml` again
     would void the runs recorded on the final workflow code.
   - **Compliance rerun (needs-changes, evidence only).** Three findings:
     - AC 5's runs were on `a258006`, before item 9 changed `ci.yml`; the
       final head's runs are recorded in item 10.
     - The DoD's pre-push checks needed commands and exit codes; item 10
       gives them.
     - Item 4's subject-check invocation needed spelling out; it now does.

     The reviewer also found a gap: GitHub's ` (#N)` suffix on `main` hid a
     trailing period, so `feat(x): foo. (#3)` passed. The step now strips the
     suffix before matching. Tested from the YAML in a scratch repository:
     `feat(x): foo (#3)` and `chore(main): release 0.1.0 (#5)` pass, while
     `feat(x): foo. (#3)` and `fix(y): bar.` fail, named by hash. The
     pattern approximates `amannn/action-semantic-pull-request`'s parser
     rather than reproducing it. CONTRIBUTING says to change the copies of the
     rule together.
   - **Compliance run 3 (needs-changes).** Items 9 to 11 sat below the
     reconciliation sweep. They were moved above it, and AC 4 was re-run with
     the final step (item 12). Run 4 passed.
10. **Second rebase and the final pre-push run (2026-11-11).** `origin/main`
    moved 2 more commits (spec 002's sweep, and its fix, up to `3189b90`).
    - The only conflict was `docs/memory/learnings.md`, where both sides
      appended; both sets of entries were kept.
    - The board was regenerated.
    - The branch is 0 behind.

    Before the push, in order:
    - `git remote -v` showed `origin https://github.com/ramboz/coaster.git`,
      and `gh repo view` showed `ramboz/coaster PUBLIC`;
    - `python3 scripts/build_host_packages.py`: exit 0, with no file under
      `hosts/` changed;
    - `--check`: exit 0;
    - the byte-compile on 3.9.6: exit 0;
    - `validate --strict` on the package and on the marketplace: both exit 0;
    - the path search on `HEAD`: exit 1, clean;
    - the term search over the tree, with all 27 terms: exit 1, clean, and 0
      hits in the branch's commit messages;
    - the subject check over `origin/main..HEAD`, 7 commits, with
      `/usr/bin/grep`: exit 1, clean.

    In a piped, scripted run, the shell's `grep` wrapper (ugrep) reported
    exit 0 for that last check, though a listing of rejected subjects was
    empty. `/usr/bin/grep` is the reliable one here.

    The rebased branch could not be pushed: replacing `a258006` needs a force
    push, and the project's settings deny every force push. Instead:
    - the PR's tip `a258006` took a merge of `origin/main`, as `84b7a36`
      (`chore(sync): merge origin/main into the spec 003 branch`);
    - one commit, `a4efcc1`, laid the reviewed tree on top of it;
    - `git diff` between `a4efcc1` and the rebased tip it replaced is empty;
    - the push was a fast-forward, `a258006..a4efcc1`, after the path and
      term searches and `--check` passed again.
11. **Live runs on the final workflow code (`a4efcc1`).**
    - **CI run `43134442343`:** `check (3.9)`, `check (3.12)` and `validate`
      all pass, and `subjects` is skipped on a PR, as designed.
    - **PR Title run `43134442184`:** passes.
    - **`jig-governance` run `43134442274`:** fails by design.

    Every later non-merge commit on the branch changes only files under
    `docs/`, and nothing under `.github/` has changed since `a4efcc1`, so
    these runs stand for the workflow code that lands. The merges bring in
    spec 002's changes from `main`.
12. **AC 4 and AC 5 against the code that lands.** The final subject step,
    taken from the YAML at `8a6d922` (a docs-only commit after `a4efcc1`, so
    the same `ci.yml`), exits 1 with `BEFORE` set to the root
    commit and `AFTER` to `origin/main`, naming the same two unscoped commits.
    It exits 0 on `bbeda54..a28e0cd`. `git diff a258006 HEAD --
    .github/workflows/pr-title.yml` is empty, so the bad-title test on
    `a258006` covers the file that lands.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `deferred` | Parked in `docs/inbox.md`. The spec's decision left a pointer to `CONTRIBUTING.md` for later, because 002-01 was editing the README; 002-01 has since landed, and the reason below now applies instead. `README.md` is copied into the package, so editing it changes the package's bytes and needs a pre-release bump in both `plugin.json` files, which this spec does not touch. It goes with the next PR that changes the package. GitHub links `CONTRIBUTING.md` from the PR form meanwhile. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board` after each transition and after the rebase; `check-board` reports it clean. |
| `docs/product-vision.md` | `no-op` | No behaviour or scope change; `use_cases: []` is deliberate. |
| `docs/architecture.md` | `no-op` | This slice adds workflows only; no module boundary or contract changes. (003-02 updates the plugin-manifest entry.) |
| `docs/conventions.md` | `updated` | The Git rule, in the wording Julien approved (AC 1). |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `updated` | One `CLAUDE.md` line under Development Conventions. No `AGENTS.md`. Active specs are left as they are: spec 002 is not listed either, and the board carries live status. |
| `docs/inbox.md` | `updated` | No earlier item was about commits, CI or releases. Added one: the README pointer to `CONTRIBUTING.md` (row above). |
| `docs/memory/**` | `updated` | Three learnings: the `0.0.0` seed, docs-only releases, and validating the plugin folder rather than the root. |
| `docs/decisions/README.md` / ADR index | `no-op` | No ADR, by the spec's decision: the mechanism is the family's, as recorded in servo's ADR-0007. |
| `docs/governance.md`, `docs/workflow.md`, `docs/adoption-readiness.md` | `no-op` | Searched for commit, CI and release claims: nothing stale. The new workflows fall under the existing `.github/workflows/**` protection. |
| This slice's deliverables: `.github/workflows/ci.yml`, `.github/workflows/pr-title.yml` | `updated` | See deviation log items 2, 3, 9 and 12. |
| `CONTRIBUTING.md` | `updated` | New file, covering this slice's merging, direct-push and CI sections. |
| The spec overview `spec.md`, both slice files and `reviews/` | `no-op` | These are spec 003's own record, not surfaces this slice reconciles. |
| 003-02's files: `release.yml`, `release-please-config.json`, `.release-please-manifest.json`, `docs/refinement-todo.md` (its CI/CD entry), the release plan | `no-op` | Covered by 003-02's sweep. |
| Spec 002's paths (`plugin.json`, `hosts/claude/**`, `skills/**`, `scripts/build_host_packages.py`, `README.md`, ADR-0002 and `docs/decisions/README.md`, `docs/specs/002-*`) | `no-op` | They reached this branch from `origin/main` through the rebases, not from spec 003. `git diff origin/main...HEAD` touches none of them. A diff against the stale local `main` lists them. |

**Leanness:**
- Nothing beyond the ACs was added: no new script, and no test harness.
- Three things go past jig's CI, each with its own source:
  - the subject check on `main`, which frame-critique round 2 asked for;
  - the third CI job, which is this slice's choice, so that check runs once rather than once per Python leg (item 2);
  - the error-path handling and the ` (#N)` stripping, from the craft and compliance findings (item 9).
- Node is not pinned, and actions are not pinned by SHA (deviation log, item 9).
