---
status: READY_FOR_IMPLEMENTATION
dependencies: [001-01]
last_verified:
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
- ⬜ 001-01 is DONE.
- ⬜ The scaffold, vision, release plan and this spec are committed on `main`.
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
that was installed. Raw run logs stay out of the repository, as in 001-01.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1, 2 | The review and both independent reads exist, with dispositions applied and a dated go-ahead | _not run_ | not-run | |
| 2 | 3 | Checks pass on local `main` and on the private remote: one commit, only `main`, same tree, no held-back file, no home paths or listed terms | _not run_ | not-run | |
| 3 | 4 | `LICENSE` present, no `@OWNER`, worktrees ignored | _not run_ | not-run | |
| 4 | 5 | README reads as described | _not run_ | not-run | |
| 5 | 6 | Strict validation and `--check` exit 0 | _not run_ | not-run | |
| 6 | 7 | `gh repo view` reports public and `main` | _not run_ | not-run | |
| 7 | 8 | Both commands succeed, and the dossier meets 001-01's AC 7 | _not run_ | not-run | |
| 7b | 8 | Julien's interactive run shows no prompt for a packaged file | _not run_ | not-run | |
| 8 | 9 | No `docs/` in the installed plugin folder | _not run_ | not-run | |

**DoD:**
- [ ] All ACs pass, with the table above filled in from real runs.
- [ ] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [ ] Implementation review passed.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [ ] Reconciliation review passed.
- [ ] `docs/refinement-todo.md` updated for the entries the spec lists.

### Close-out (post-DONE)

- [ ] `docs/specs/README.md` regenerated by `workflow.py status-board`.
- [ ] Primer hygiene: this slice closes the spec, so compress its Active-specs
      entry in `CLAUDE.md` if it has one.

**Anti-horizontal-phasing check:** After this slice, a stranger with Claude Code
can install coaster from GitHub and get a dossier from an idea.
