---
status: DONE
dependencies: [001-01]
last_verified: 2026-11-11
frame_review: true
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 001-02 — install from GitHub

**Goal:** Publish a reviewed coaster to GitHub so that someone with only Claude
Code can add its marketplace, install it, and get a correct dossier from
`capture`.

**DoR:**
- ✅ 001-01 is DONE.
- ✅ The scaffold, vision, release plan and this spec are committed on `main`.
- ✅ What goes public and how the history goes public are decided (see the
  spec's Decisions).
- ✅ `ramboz/coaster` was free on GitHub on 2026-11-09. Check again at publish.

**Acceptance Criteria:**

1. **The publication review covers everything to be pushed.** ACs 4 to 6 land
   first, so the review sees the final tree. `publication-review.md` records the
   review of the whole tree that will be pushed, hidden files included. It lives
   on the local `pre-publication` branch and is never pushed, because it indexes
   each private passage. A finding is anything whose source is not public or not Julien's
   to publish: content drawn from private repositories or local notes, quotes or
   paraphrases of non-public skills, personal details, local paths, and any
   public claim whose only citation is withheld. Each finding is listed by file
   and line with a keep, redact or remove disposition, and private content is
   not quoted. Julien sets or confirms every `keep`. The review covers at least the airlock material throughout
   `docs/prospects/`, the transcript-derived quotes in
   `field-research/dossier.md`, the paraphrases of the non-public skill wherever
   they appear (`ENB-04`, the seven lines in the `research_notes` copy of
   `enablers.md`, and line 74 of the landscape report), and the `local` citation
   in the first dogfood note.
2. **Nothing leaves the machine before two independent reads and Julien's
   go-ahead.** A reviewer subagent that did not write `publication-review.md`
   reads the whole tree to be pushed against AC 1's finding definition, without
   being given that file's list. Its findings are added to the file, and every
   disposition is applied and committed as the candidate first commit. A second
   independent reader then checks that commit's diff against `pre-publication`,
   with the final `publication-review.md`, and confirms each redact and remove
   finding is gone. Julien's go-ahead comes after that. It covers the final diff
   and the full list of `keep` findings, and is recorded with its date and the
   candidate's tree id before the repository is created. Any later change to the
   candidate repeats the second read and the go-ahead.
3. **The public tree is the reviewed tree, on one commit, checked before it is
   public.** `docs/prospects/field-research/scout/own-record.md` is absent, and
   no relative link in the tree points to it. Every evidence entry that rests
   only on that file is re-tagged `reported` and says its source is unpublished.
   The five earlier commits and the held-back file stay on a local
   `pre-publication` branch, cut from `main` after ACs 4 to 6 so that the second
   reader's diff shows only the redactions.
   `git grep -E '/Users/[r]amboz|~/[P]rojects|-Users-[r]amboz|/private/tmp/[c]laude-' main`
   finds nothing before the repository is created, and neither does a search for
   the distinctive terms of each redact or remove finding. Those terms are listed
   in a file on `pre-publication` and are narrow enough not to match the spec
   itself. The repository is created private and pushed. Then
   `git rev-list --count origin/main` prints 1, `git ls-remote --heads origin`
   lists only `main`, `origin/main^{tree}` is the tree id in Julien's go-ahead,
   and the same searches on `origin/main` find nothing. A later fix ships as an ordinary new commit with
   a pre-release bump, after the same search by hand. That cannot remove a leak
   found after the repository is public. The remedy for a leak is to delete the
   repository and recreate it from a cleaned tree, and even that cannot reach
   clones already on installers' disks, which is why these checks come first.
   **Amended by Julien, 2026-11-11:**
   `docs/prospects/field-research/scout/own-record.md` is published, with each
   citation linked to its public source, instead of being held back. The
   clauses on the held-back file (its absence, the ban on relative links to
   it, the `reported` re-tags of entries that rest only on it, and keeping it
   on `pre-publication`) no longer apply.
   **Amended by Julien, 2026-11-11:** the private stage and the one-commit
   checks did not happen, because another session had already published the full
   history. The reviewed tree was pushed as ordinary commits on top, and its
   tree id, the path search and the term search were checked on `origin/main`.
4. **The repository has a licence and a real owner.** `LICENSE` is MIT with
   "Copyright (c) 2026 Julien Ramboz", as in jig and servo. `CODEOWNERS` names
   `@ramboz` and holds no `@OWNER`. `git check-ignore .claude/worktrees` exits 0.
5. **The README says where coaster runs.** "Where it works" leads with Claude
   Code and marks claude.ai as untested, and the README gives the two install
   commands. Its layout section and links read correctly in the packaged copy,
   which holds no `docs/`, `templates/` or `PITCH.md`, and it no longer says the
   handoff is still to come. Julien's call on "nothing to install or run" is applied to
   `README.md`, `PITCH.md` and `docs/product-vision.md`, and recorded against
   that entry in `docs/refinement-todo.md`.
6. **The marketplace manifest validates.** `.claude-plugin/marketplace.json` has
   name `coaster` and one plugin, whose source is `git-subdir` at
   `https://github.com/ramboz/coaster.git`, path `hosts/claude`, the same shape
   as shaper's. `claude plugin validate --strict .claude-plugin/marketplace.json`
   exits 0, and `build_host_packages.py --check` exits 0.
7. **The repository goes public last.** Once AC 3's checks have passed on the
   private repository, its visibility changes to public. `gh repo view
   ramboz/coaster` reports public visibility and default branch `main`.
   **Amended by Julien, 2026-11-11:** the repository was already public before
   these checks, as AC 3's amendment explains.
8. **A fresh install works in an isolated profile.** With `CLAUDE_CONFIG_DIR`
   set to a new empty folder and no reference to a local checkout,
   `claude plugin marketplace add ramboz/coaster` and
   `claude plugin install coaster@coaster` succeed. One headless run of
   `/coaster:capture` in a new empty `git init` folder, with the flags 001-01
   pins and without `--plugin-dir`, meets every condition in 001-01's AC 7.
   Julien then runs it once by hand in an interactive session in that profile
   and answers its questions. No permission prompt appears for a packaged file,
   and the dossier holds every template heading and the answers.
9. **The plugin folder carries only the package.** The installed plugin's folder
   holds no `docs/` directory. `marketplace add` still clones the whole repository
   to the installer's disk, so the AC 1 review applies to everything pushed.

### Verification scenario

**Preconditions:** The repository is public. A new empty folder as
`CLAUDE_CONFIG_DIR`. A disposable profile does not inherit the sign-in, so Julien
signs in there once by hand. No secrets.

**Invocation:** Each command runs with `CLAUDE_CONFIG_DIR` set to the new folder.

```bash
claude plugin marketplace add ramboz/coaster
```

```bash
claude plugin install coaster@coaster
```

Then run the 001-01 `capture` command from an empty folder, without
`--plugin-dir`, and start one interactive session in a second empty folder for
Julien's run.

**Preserved behavior:** `claude --plugin-dir hosts/claude` still loads the
package from a checkout.

**Code revision / dirty-change identity:** Record the commit on `origin/main`
that was installed. Installed: `5e52e52`, tree `8457508c`, version `0.1.0-pre.1`. Rows 7, 7b and 8 are for that install. `0.1.0-pre.2` differs only in the README and the version, and lands with this slice. Raw run logs stay out of the repository, as in 001-01.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1, 2 | The review and both independent reads exist, with dispositions applied and a dated go-ahead | Done on 2026-11-11. The first review recorded 29 findings and the independent read 10 more. Julien decided four questions, the dispositions were applied on a candidate, and the second independent read passed after two rounds of fixes. Julien's go-ahead is recorded with tree id `8457508c`. The review stays on `pre-publication`. | pass | `pre-publication:docs/specs/001-install-and-capture/publication-review.md` |
| 2 | 3 | Checks pass on local `main` and on the private remote: one commit, only `main`, same tree, no home paths or listed terms | The approved tree passed the path search, all 27 terms and the excluded-file check locally. The private stage did not happen: another session had published the full history at 11:03 PST. The reviewed tree went out as three ordinary commits. `origin/main^{tree}` is the approved `8457508c`, only `main` exists, and the path and term searches on `origin/main` find nothing. The commit count is 14, not 1. Met as amended by Julien on 2026-11-11, and not as first written. | pass | `git ls-remote origin`, `git rev-parse origin/main^{tree}`, the searches |
| 3 | 4 | `LICENSE` present, no `@OWNER`, worktrees ignored | `LICENSE` is MIT, "Copyright (c) 2026 Julien Ramboz", copied from jig. `CODEOWNERS` names `@ramboz` on all six rules and has no `@OWNER`. `git check-ignore .claude/worktrees` exits 0 in the main checkout. | pass | the files; `git check-ignore -v` |
| 4 | 5 | README reads as described | "Where it works" leads with Claude Code and marks claude.ai untested. The README gives the two install commands, links by absolute GitHub URLs, labels its layout as the repository's, and no longer says the handoff is to come. The lead line now reads "one plugin and nothing else to install or run" in the README, the pitch and the vision. Julien did not choose between the wordings offered, so the recommended one was applied and his go-ahead covered it. | pass | `README.md`, `hosts/claude/README.md`, `docs/refinement-todo.md` |
| 5 | 6 | Strict validation and `--check` exit 0 | The manifest names `coaster`, one plugin, a `git-subdir` source at `https://github.com/ramboz/coaster.git`, path `hosts/claude`. Strict validation passed once a top-level description was added. `--check` reports the package in sync. | pass | `claude plugin validate --strict .claude-plugin/marketplace.json` |
| 6 | 7 | `gh repo view` reports public and `main` | `gh repo view ramboz/coaster` reports PUBLIC and default branch `main`. The repository was public before AC 3's checks, as its amendment explains. | pass | `gh repo view` |
| 7 | 8 | Both commands succeed, and the dossier meets 001-01's AC 7 | In a new `CLAUDE_CONFIG_DIR`, `marketplace add ramboz/coaster` and `install coaster@coaster` succeeded and installed `0.1.0-pre.1`. After Julien signed in there, one headless run with 001-01's flags and no `--plugin-dir` loaded the installed plugin, made one `Write`, had no permission denials, and wrote a dossier with every template heading in order, the frontmatter right, the idea quoted word for word, four unanswered questions under `### Unstated`, empty lens sections and no placeholder. | pass | scratch run `gh-run1`; the installed `capture` is byte-identical to `hosts/claude` |
| 7b | 8 | Julien's interactive run shows no prompt for a packaged file | Julien ran `/coaster:capture` by hand in that profile. He gave the idea and left the other four questions unanswered, which `capture` listed under `### Unstated`. The session ran in auto permission mode across an exit and resume, and plugins synced from his account joined it on resume, so it was not fully isolated. Its tool log shows one tool call, a Bash write of the dossier in that folder, and no read of a packaged file. The dossier has every template heading in order. | pass | Julien's report; the session log. The dossier is not committed. |
| 8 | 9 | No `docs/` in the installed plugin folder | The installed plugin folder holds `.claude-plugin`, `LICENSE`, `README.md` and `skills`, and no `docs/`. The marketplace's own clone holds the whole repository, as AC 9 expects. | pass | the install folder |
| 9 | Preserved | `claude --plugin-dir hosts/claude` still loads the package | After the README change and the bump to `0.1.0-pre.2`, a Haiku session started with `--plugin-dir hosts/claude` listed all six `coaster:` skills. | pass | the `pd-check` session log, kept outside the repository |

**DoD:**
- [x] All ACs pass, with the table above filled in from real runs.
- [x] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [x] Implementation review passed.
- [x] Deviation log produced under this slice heading.
- [x] Reconciliation sweep produced under this slice heading.
- [x] Reconciliation review passed.
- [x] `docs/refinement-todo.md` updated for the entries the spec lists.

### Close-out (post-DONE)

- [x] `docs/specs/README.md` regenerated by `workflow.py status-board`.
- [x] Primer hygiene: this slice closes the spec, so compress its Active-specs
      entry in `CLAUDE.md` if it has one.

**Anti-horizontal-phasing check:** After this slice, a stranger with Claude Code
can install coaster from GitHub and get a dossier from an idea.

### Deviation log (after reconciliation)

The original spec is preserved above. Implementation notes:

1. **Another session published first.** At 11:03 PST on 2026-11-11 a different Claude session on this machine created a public `ramboz/coaster` and pushed the full local history, while the publication review was still running. No agent of this session ran that command, which a scan of their logs confirmed. Julien kept the repository public and asked for what could be cleaned up. The reviewed tree went out as three ordinary commits ending at `5e52e52`, whose tree is the approved one. The earlier commits stay public with the material the review removed from the current files. Only rewriting or recreating the repository could remove them, and Julien chose not to. ACs 3 and 7 are amended accordingly.
2. **Julien's decisions changed the review's outcome.** Every source the airlock record cites turned out to be public, so `own-record.md` was published with links instead of held back. Quoted session turns and first-person anecdotes were reworded as plain statements or removed. The unreleased sibling name, a private tool's name and the work-email sentence were redacted. The low-risk keeps were confirmed.
3. **Two items resolved outside the findings table.** Python bytecode committed in 001-01 embedded an absolute source path. It was untracked, and `__pycache__/` and `*.pyc` are now ignored. A link to `own-record.md` was both a redact finding and a kept item, and was resolved as kept.
4. **The lead line is a default.** Julien did not choose between the wordings offered. The recommended "one plugin and nothing else to install or run" was applied, and his go-ahead on the final diff covered it.
5. **Smaller fixes.** Strict validation of the marketplace manifest needed a top-level description. The worktree ignore rule has no trailing slash, so `git check-ignore` works on the path itself.
6. **Julien's hand-run.** He gave the idea and left the other four questions unanswered, which `capture` recorded under `### Unstated`. The session ran in auto permission mode, which suppresses most prompts, and was exited and resumed. On resume the profile had picked up plugins synced from Julien's account, whose hooks wrote files into the run folder, so it was not fully isolated. The dossier was written through Bash. The result that no packaged file was read rests on the session's tool log, not on the absence of a prompt. The headless run, whose profile loaded only coaster, ran between the hand-run's first turn and its resume.
7. **The craft fixes.** The lead-claim note moved into its entry in `docs/refinement-todo.md`, the pitch's status caught up with the README, and the README links the ai-pegboard, jig and shaper. The README change altered the package, so it was rebuilt and bumped to `0.1.0-pre.2`. Separately, the compliance review noted a sentence in `CODEOWNERS` left over from the scaffold's placeholder, and it was reworded. That file is governance-protected: the change is to a comment only, the ownership rules are unchanged, and it was not separately put to Julien.
8. **How the reconciliation edits ship.** Every file changed since `5e52e52`, whose tree is the go-ahead's `8457508c`, ships this way: the README links, the pitch's status, the `CODEOWNERS` comment, the refinement-todo move, `CLAUDE.md`'s description, the version bump, the architecture, inbox and learnings updates, the status board, spec 001 and this slice's record, and the slice's review files. The repository is already public, so they ship under AC 3's clause for later fixes: an ordinary commit, a `0.1.0-pre.2` bump, and the path and term searches run by hand before the push, not a repeated second read.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `updated` | Rewritten for AC 5 and checked inside the package. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board`. |
| `docs/product-vision.md` | `updated` | The lead line changed, and quoted turns became plain statements. The elicitation hashes no longer match those sections. |
| `docs/architecture.md` | `updated` | One quoted platform commitment became a plain statement, and the marketplace manifest joined the contract surfaces. |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `updated` | `CLAUDE.md`'s placeholder description of the project now says what coaster is. It has no entry for this spec, and there is no `AGENTS.md`. |
| `docs/inbox.md` | `updated` | Parked the refresh of the stale elicitation hashes. |
| `docs/refinement-todo.md` | `updated` | The lead-claim entry is resolved, and CI stays with scope 4. |
| `docs/memory/**` | `updated` | Learnings on publishing and bytecode. |
| `docs/decisions/README.md` / ADR index | `no-op` | No ADR for this slice: the publication choices are recorded as Julien's decisions in spec 001. |
| `docs/releases/claude-code-first-release.md` | `updated` | Quoted turns reworded, the grounded count corrected, and the risk-first row updated. |
| `docs/prospects/**`, `docs/dogfood/**`, `PITCH.md` | `updated` | The publication edits in public commits `beab254` to `5e52e52`, plus the pitch's status paragraph in reconciliation. |
| `CODEOWNERS` | `updated` | Owner set to `@ramboz` for AC 4, and a leftover placeholder sentence reworded. A governance-protected file, with a comment-only change in reconciliation. |
| `.gitignore` | `updated` | Ignores linked worktrees, Python bytecode and jig's review sidecars. |
| `LICENSE` | `updated` | Added for AC 4. |
| `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json` | `updated` | The marketplace manifest for AC 6, and the version bump to `0.1.0-pre.2`. |
| `hosts/claude/**` | `updated` | Rebuilt for the README and the version, and in sync by `--check`. |
