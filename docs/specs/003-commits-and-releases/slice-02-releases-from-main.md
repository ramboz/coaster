---
status: REVIEWED
dependencies: [003-01]
last_verified:
frame_review: true
claimed_by: claude/release-mechanism-cbea54
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 003-02 — releases from main

**Goal:** Let release-please turn the commit subjects on `main` into a release
PR that sets the version in both `plugin.json` files and writes
`CHANGELOG.md`, and, when Julien merges that PR, tag `vX.Y.Z`, publish a GitHub
release and attach the checked package to it.

**DoR:**
- 003-01's ACs pass on the branch.
- ✅ The repository allows GitHub Actions to create pull requests (A3):
  `gh api repos/ramboz/coaster/actions/permissions/workflow` returns
  `can_approve_pull_request_reviews: true`, the API's name for "Allow GitHub
  Actions to create and approve pull requests". Without it release-please
  cannot open its PR. Julien sets it, or lets this session set it as `ramboz`.
  On 2026-11-11 it was `false`; with Julien's OK it was set to `true` as
  `ramboz`, keeping `default_workflow_permissions: read`, and read back.
- ✅ Julien accepted the spec's decisions, including the `0.0.0` seed with
  `initial-version`, and the zip, on 2026-11-11.

**Acceptance Criteria:**

1. **The release workflow.** `.github/workflows/release.yml` runs on `push` to
   `main` and on `workflow_dispatch`, with `contents: write` and
   `pull-requests: write`. Its `release-please` job runs
   `googleapis/release-please-action@v5` with
   `config-file: .github/release-please-config.json` and
   `manifest-file: .github/.release-please-manifest.json`, and exposes
   `release_created`, `tag_name` and `version`.
2. **The package job.** A `package` job runs only when
   `release_created == 'true'`, checks out the tag, and, in order: runs
   `--check`; fails unless both `plugin.json` files say the release's version;
   writes `dist/coaster-claude-v<version>.zip` with
   `git archive --format=zip HEAD:hosts/claude`; installs
   `@anthropic-ai/claude-code@2.1.322`, unzips the file into a scratch folder
   and runs `claude plugin validate --strict` there; uploads the zip with
   `gh release upload`; and appends a short install note to the release body
   without replacing release-please's notes.
3. **The config.** `.github/release-please-config.json` has jig's settings
   (`release-type: simple`, `include-component-in-tag: false`,
   `include-v-in-tag: true`, jig's `changelog-sections`) and two `extra-files`
   entries, `.claude-plugin/plugin.json` and
   `hosts/claude/.claude-plugin/plugin.json`, each `type: json`,
   `jsonpath: $.version`, and `"initial-version": "0.1.0"` in the package
   entry. `.github/.release-please-manifest.json` is `{ ".": "0.0.0" }`. Both
   parse as JSON, and the package key `.` matches.
4. **The package steps work before any release.** The package job's steps,
   run locally on this branch with the version from `plugin.json`, produce a
   zip whose unzipped copy passes `claude plugin validate --strict`, and whose
   file list matches `git ls-files hosts/claude`. The version step fails when
   given any other version.
5. **CONTRIBUTING.md explains releases.** It gains, after servo's: how a PR
   title becomes a release, as a table that matches the config (`docs` cuts a
   patch release PR on its own); the release flow, from release PR to tag,
   release and zip; that merging the release PR is the release and waits for
   the release plan's check; and the version rule from 003-01's AC 1.
6. **The deferred entry and the release plan.** The
   [refinement-todo](../../refinement-todo.md#operations) "CI/CD setup"
   entry is marked resolved by this spec, keeping its original text. Scope 4 of
   the [release plan](../../releases/claude-code-first-release.md) says that
   CI and release-please are in place, and that merging the release PR cuts
   `v0.1.0`. The plan's status does not change.
7. **The first release PR, after merge.** After this spec's PR merges, the
   `Release` run on `main` succeeds, and release-please opens a PR titled
   `chore(main): release 0.1.0` that changes exactly both `plugin.json` files
   (to `0.1.0`), the manifest (to `0.1.0`) and a new `CHANGELOG.md`. If its
   checks run, they pass; if none run (A4, the likelier case), `--check` and
   `claude plugin validate --strict hosts/claude` pass on its branch by hand. If it proposes any version but `0.1.0`, it is
   not merged, and the config is fixed in a new PR first. The first heading in
   its `CHANGELOG.md` has no compare link: a `compare/v0.0.0...v0.1.0` link
   would mean release-please took `0.0.0` as a previous release, against A2.
   The PR is left open. A follow-up `docs(specs)` commit records the run id,
   the PR number and its diff stat, and closes the spec. It lands by PR, or by
   a direct push if Julien prefers; either way CI's subject check on `main`
   passes for it.

**DoD:**
- [ ] All ACs pass, with evidence in the deviation log. AC 7's evidence comes
      from the follow-up commit after the merge.
- [ ] The build, `--check`, the path search and the term search pass before
      each push, and `git remote -v` and `gh repo view` are checked first.
- [ ] Frame-critique, compliance and craft passes recorded with
      `review.py record-review`.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [ ] Reconciliation review passed.

**Anti-horizontal-phasing check:** After this slice, Julien sees an open
release PR that shows the next version and its changelog, and merging it
releases coaster with the package attached.

### Deviation log (after reconciliation)

The acceptance criteria above are kept as written. Implementation notes, 2026-11-11:

1. **The workflow and config.**
   - `release.yml` is as specified, except permissions, which item 5 grants
     per job. The zip smoke test also sets `CLAUDE_CONFIG_DIR` to a fresh
     folder under `$RUNNER_TEMP` and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`,
     as `ci.yml`'s `validate` job does (003-01, item 2).
   - The install note is appended with `printf '%s\n%s'`, so a blank line
     separates it from release-please's notes. A first draft had no blank
     line, which a local render through a stub `gh` showed.
   - The config's `release-type`, tag settings and `changelog-sections` equal
     jig's (compared by a script). Its two `extra-files` entries and
     `initial-version: "0.1.0"` are coaster's.
   - The manifest is `{ ".": "0.0.0" }`. Both files parse, and their package
     keys are `.`.
2. **AC 4 (local, 2026-11-11, on the then-current `0.1.0-pre.2` tree).**
   - The "Check the tagged package" script, taken from the YAML, exits 0 with
     `VERSION=0.1.0-pre.2`. With `VERSION=0.1.0` it exits 1:
     `.claude-plugin/plugin.json says 0.1.0-pre.2, but the release is 0.1.0`.
   - `git archive --format=zip HEAD:hosts/claude` gives a zip whose unzipped
     file list equals `git ls-files hosts/claude` (11 files), and
     `claude plugin validate --strict` passes on it.
3. **AC 6.**
   - The refinement-todo entry is struck and dated as RESOLVED, in the file's
     existing style, keeping its text and trigger. The spec's links point to
     the `#operations` anchor, because the heading's own anchor changed.
   - The release plan's scope 4 line now names spec 003, the open release PR
     and the catalog listing still to do. Its `candidate` status is unchanged.
4. **AC 4 again, after the rebase (2026-11-11, on `48103a6`, package at
   `0.1.0-pre.8`).**
   - The version step, taken from the YAML, exits 0 with
     `VERSION=0.1.0-pre.8` and exits 1 with `VERSION=0.1.0`.
   - The zip's file list equals `git ls-files hosts/claude` (11 files), and
     `claude plugin validate --strict` passes on it.
5. **Review findings, 2026-11-11.** Compliance and craft both passed, with
   notes. Applied:
   - **Permissions.** Granted per job: `release-please` gets `contents` and
     `pull-requests` write; `package` gets only `contents: write`. The
     workflow-level default is `{}`.
   - **Checkout.** `package` checks out with `persist-credentials: false`, so
     no token sits in `.git/config` while `npm install -g` runs.
   - **Re-runs.** The upload uses `--clobber`, and the install note is
     skipped when the release body already has `## Install`, so the job can
     be re-run. A stub `gh` showed the note added once and skipped on a second
     run. The `gh` calls name the repository with `-R "$GITHUB_REPOSITORY"`.
   - **CONTRIBUTING.md.**
     - The `!` row shows `0.1.0` → `1.0.0`.
     - The merge rule names the first release plan for `v0.1.0` only.
     - A re-run of `package` is safe, but a workflow fix needs a manual
       upload.
   - **`docs/architecture.md`.** The plugin-manifest interface points to
     release-please from `v0.1.0`.

   Differences from jig's `release.yml`:
   - **From the spec's Decisions:** one zip built with `git archive` instead
     of `build_release_zip.py` and its zips for three hosts and an alias.
   - **From AC 2:** a step that checks both `plugin.json` versions against
     the release.
   - **From this item:**
     - per-job permissions;
     - `persist-credentials: false`;
     - `--clobber` and `-R`;
     - the re-run guard.
   - **Other:**
     - the tag and version reach the scripts through `env:`, not inline
       `${{ }}`;
     - the note's heading is `## Install`, not `## Install artifacts`;
     - the note says the marketplace follows `main`, and a blank line
       separates it from release-please's notes.
6. **AC 7** waits for the merge. The follow-up commit records it.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `deferred` | Same as 003-01, and parked in `docs/inbox.md`: a pointer to `CONTRIBUTING.md` changes the package's bytes, so it goes with the next package change. |
| Spec 002's paths | `no-op` | As in 003-01's sweep: they came from `origin/main` through the rebases, and `git diff origin/main...HEAD` touches none of them. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board`. |
| `docs/product-vision.md` | `no-op` | No behaviour or scope change. |
| `docs/architecture.md` | `updated` | The plugin-manifest interface now says release-please sets the version from `v0.1.0`. |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `no-op` | 003-01's line covers both slices. |
| `docs/inbox.md` | `updated` | No earlier item was about releases. Added the README-pointer item, so that deferral outlives the spec. |
| `docs/refinement-todo.md` | `updated` | "CI/CD setup" struck and dated RESOLVED, with its original text kept. |
| `docs/releases/claude-code-first-release.md` | `updated` | Scope 4 names spec 003, the release PR as the `v0.1.0` cut, and the catalog listing still to do. Status stays `candidate`. |
| `docs/memory/**` | `updated` | See 003-01: three learnings, two of them from this slice. |
| `docs/decisions/README.md` / ADR index | `no-op` | No ADR, by the spec's decision. |
| `CHANGELOG.md` | `deferred` | release-please writes it in the first release PR (spec decision: no stub). AC 7 checks it after the merge. |
| `CONTRIBUTING.md` | `updated` | The release sections: the title-to-release table, the release flow, versions, and re-running the `package` job. |

**Leanness:**
- No `build_release_zip.py`: the `package` job is about a dozen lines of steps.
- The config is jig's, with two `extra-files` entries and `initial-version`.
- The re-run guard and per-job permissions answer craft findings.
