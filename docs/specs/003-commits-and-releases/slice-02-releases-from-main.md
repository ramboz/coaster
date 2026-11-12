---
status: IN_PROGRESS
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
