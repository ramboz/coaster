---
status: DONE
dependencies: []
last_verified: 2026-11-09
frame_review: true
arch_review: true
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 001-01 — capture from the built package

**Goal:** Build coaster into a Claude Code plugin package of self-contained
skills, and show that `capture`, loaded from that package with no extra
permission, writes a correct dossier in an empty repository.

**DoR:**
- ✅ Probes on 2026-11-09 showed the read failure, and that a skill with its
  packaged text built in avoids it.
- ✅ shaper's build script is available as the pattern to follow.

**Acceptance Criteria:**

1. **The package builds from source.** `python3 scripts/build_host_packages.py`
   writes `hosts/claude/` from the repository root, holding
   `.claude-plugin/plugin.json`, one rendered `SKILL.md` per skill, both helpers
   and `README.md`. It holds no `templates/` or `skills/_shared/`, nothing from
   `docs/`, and no `__pycache__`.
2. **Drift is caught.** `--check` exits 0 on an in-sync tree. After a one-byte
   change to `skills/capture/SKILL.md` it exits non-zero and names the file.
   The change is then restored.
3. **The build stays small.** The script imports only the standard library,
   builds only the Claude package, and is under 200 lines. Its only changes to
   skill text are the AC 5 map and the two helper paths.
4. **The package validates.** `claude plugin validate --strict hosts/claude`
   exits 0. The manifest has name `coaster`, version `0.1.0-pre.1`, a
   description that makes no claim about chat, and author `ramboz`.
5. **Source stays neutral and each rendered skill is self-contained.** The build
   holds an explicit map of what goes into each skill. Each
   `hosts/claude/skills/<skill>/SKILL.md` carries the full text of its files
   under `## Packaged:` headings, and points to those sections instead of a path.

   | Skill | Built-in text |
   |---|---|
   | `capture` | `templates/dossier.md`, `_shared/evidence.md` |
   | `scout` | `templates/research-brief.md`, `_shared/evidence.md` |
   | `frame` | `_shared/lenses.md` |
   | `challenge` | `_shared/hats.md`, `_shared/evidence.md`, `templates/challenge-round.md` |
   | `name` | `templates/naming.md` |
   | `handoff` | `templates/handoff.md` |

   The 2 helper references use
   `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>`. A search of the rendered
   files for `` `templates/ ``, `` `../_shared/ `` and `` `evidence.md` `` finds
   nothing, and none has an `allowed-tools` grant for reading packaged text. In
   the rendered `challenge`, the step
   that starts the hats says to paste the packaged sections into each hat's
   prompt. `skills/` itself holds neither `${CLAUDE_PLUGIN_ROOT}` nor
   `## Packaged:`.
6. **No path that an installed user lacks is left in packaged text.**
   `skills/_shared/evidence.md` names scout's helper without a path,
   `skills/_shared/hats.md` says "the evidence rules" without naming a file, and
   `templates/dossier.md` no longer points at `skills/_shared/`. A search of
   `skills/_shared/*.md` and `templates/*.md` for `skills/` and `` `evidence.md` ``
   finds nothing.
7. **`capture` writes a correct dossier.** Loaded with the first invocation
   below, in an empty `git init` folder, in 3 of 3 Sonnet runs:
   - `permission_denials` in the run's result has no `Read`;
   - the run log shows no read of, or search for, a packaged file;
   - the only new file under `docs/` is `docs/prospects/<slug>/dossier.md`;
   - the frontmatter has `prospect: <slug>`, `status: hunch`,
     `decision: pending` and today's date in `created`;
   - every heading in `templates/dossier.md` appears, in the same order;
   - `### The hunch` quotes the idea word for word, and the questions not
     answered are listed under `### Unstated`;
   - the six lens sections under `## Readings` are empty, and no `<slug>` or
     `<title>` placeholder is left.
8. **`capture` holds up across a second turn.** With the two-turn invocation
   below, one Sonnet run ends with the user's answers quoted under `## Intent`,
   the answered questions absent from `### Unstated`, every heading in place,
   and no `Read` in `permission_denials` on either turn. **Amended by Julien,
   2026-11-09:** `### Unstated` may hold a narrower follow-up on a partly answered
   question, such as other constraints beyond the one given.
9. **The packaged template wins.** In a repository that holds its own
   `templates/dossier.md` with a `# DECOY` heading, one run of `capture` writes
   the packaged headings and no `DECOY`.
10. **A marketplace install delivers the rendered package before anything is
    public.** With `CLAUDE_CONFIG_DIR` set to a new empty folder,
    `claude plugin marketplace add` on a scratch marketplace that points at a
    copy of `hosts/claude`, and `claude plugin install`, both succeed. The
    installed `skills/capture/SKILL.md` is byte-identical to the built one. The
    scratch marketplace is not committed.
11. **The packaging decision is recorded.** An ADR written with
    `/jig:adr-workflow new` records Julien's choice of a generated and committed
    `hosts/claude`, rendered from neutral source, and that it relaxes the release
    plan's build-system no-go. It records the alternatives set aside: a hand-kept
    plugin folder with the text built in, which would duplicate only
    `evidence.md` and hand-edit two helper paths; a family-style copy build with
    a read grant; a plain copy with no grant, which accepts a permission prompt
    and can write a partial dossier silently when no one can answer it; and the
    repository root as the plugin, which would put the dossiers and dogfood logs
    in the plugin cache.
12. **`capture` works in a real interactive session.** In an empty `git init`
    folder, Julien starts `claude --plugin-dir hosts/claude`, runs
    `/coaster:capture` by hand and answers its questions. No permission prompt
    appears for a packaged file, and the dossier holds every template heading
    and the answers.

### Verification scenario

**Preconditions:** Claude Code 2.1.300 or later, signed in. An empty folder made
with `git init`. No secrets.

**Invocation:** Run from the empty folder, with no `--allowedTools` and no bypass
flag. `acceptEdits` allows the write and does not grant a read outside the
folder, which is what makes this a fair test. The idea matches the 2026-11-09
runs.

```bash
claude -p '/coaster:capture A small app that reminds me when my houseplants need water. Skip the other questions.' --plugin-dir "$REPO/hosts/claude" --model sonnet --permission-mode acceptEdits --output-format stream-json --verbose
```

For AC 8, start without the skip, then resume the session with the answers:

```bash
claude -p '/coaster:capture A small app that reminds me when my houseplants need water.' --plugin-dir "$REPO/hosts/claude" --model sonnet --permission-mode acceptEdits --output-format json
```

```bash
claude -p --resume "$SESSION_ID" 'It is for me and other forgetful plant owners. I want to learn. No ads. I do not know of anything close.' --plugin-dir "$REPO/hosts/claude" --model sonnet --permission-mode acceptEdits --output-format json
```

**Preserved behavior:** `capture` still asks only its five questions, never
researches and never judges.

**Code revision / dirty-change identity:** Record the tree hash from
`git rev-parse HEAD:hosts/claude`, because 001-02 replaces the commit history at
publication and a tree hash survives that. If the tree is dirty, also record a
digest of the saved diff. Raw run logs stay out of the repository because they
hold home directory paths. The evidence is this table and a list of each run's
tool calls with those paths trimmed.

**Recorded revision:** the `hosts/claude` tree, computed with a scratch index before the commit, is `92a70a34c4baa24b5e22511d11ed8f0d000d172e`. `git rev-parse HEAD:hosts/claude` at commit `2caadb2` gives the same hash. Tool calls:
[evidence/slice-01-tool-calls.md](evidence/slice-01-tool-calls.md).

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1 | Build writes the listed contents and nothing else | Build wrote 10 files: `.claude-plugin/plugin.json`, `README.md`, 6 `SKILL.md`, `name_check.py`, `link_check.py`. No `templates/`, `_shared/`, `docs/`, `__pycache__` or `.DS_Store` (find). No root `LICENSE` exists, so none was copied. The build renders into a scratch folder and swaps it in only on success; guard tests (a skill missing from the map, a missing helper reference) failed with `hosts/claude` untouched. | pass | `python3 scripts/build_host_packages.py`; `find hosts -type f` |
| 2 | 2 | `--check` is 0, then non-zero naming the changed file | `--check` exit 0 on a fresh build. After appending one byte to `skills/capture/SKILL.md` it exited 1 and printed `hosts/claude/skills/capture/SKILL.md`. File restored, `--check` exit 0 again. | pass | `--check` output |
| 3 | 3 | Standard library only, Claude only, under 200 lines | Script is 158 lines. Imports: argparse, shutil, sys, tempfile, pathlib, `__future__`. Builds only `hosts/claude`. Text changes are the per-skill map (references derived from the map) and the two helper paths; the challenge-specific rewrite is gone. AC 3 passes only with one exception: the script also adds a line to each rendered skill saying where a `## Packaged:` section ends (see deviation 3). | pass | `wc -l scripts/build_host_packages.py` |
| 4 | 4 | Strict validation exits 0 | `claude plugin validate --strict hosts/claude` exit 0, "Validation passed". Advice only: README has no marketplace install line. The directory-profile subset of checks also reports `LICENSE_MISSING` (no root `LICENSE` yet) and `ICON_MISSING` as non-verdict findings. | pass | validate output |
| 5 | 5 | Rendered skills are self-contained, and `skills/` is unchanged in form | Search of `hosts/` for `` `templates/ ``, `` `../_shared/ ``, `` `evidence.md` ``, `` `scripts/ `` and `allowed-tools` found nothing. `${CLAUDE_PLUGIN_ROOT}` appears only in the 2 helper references. The rendered `challenge` hats step, rendered from the source wording, tells the parent to paste the `hats`, `evidence rules` and `challenge round template` sections into each hat's prompt. Each rendered skill has a line saying each `## Packaged:` section runs to the next one or the end of the file. `skills/` holds neither `${CLAUDE_PLUGIN_ROOT}` nor `## Packaged:`. Rendered lengths: capture 285, challenge 319, frame 196, handoff 135, name 116, scout 258. | pass | greps over `hosts/` and `skills/` |
| 6 | 6 | The search of `_shared` and `templates` finds nothing | `grep -nE 'skills/|`evidence.md`' skills/_shared/*.md templates/*.md` printed nothing. | pass | grep |
| 7 | 7 | Three runs meet every listed condition | All 3 Sonnet runs (r1d, r2d, r3d), fresh `git init` folders: `permission_denials` empty in each result. Tool calls: each run made one `Write` of the dossier. None read or searched for a packaged file. The dossier is the only new file under `docs/`. Frontmatter in each: `prospect: <slug>`, `status: hunch`, `decision: pending`, today's date in `created`. All 24 headings of `templates/dossier.md` (including `### Anything close that I know of` and `### Reported at capture`) appear in the template's order. `### The hunch` quotes the idea word for word. `### Unstated` lists the 4 unanswered questions. The six lens sections hold no text, and no `<slug>` or `<title>` is left. Slug `houseplant-watering-reminder` in all three. Cost $0.13 per run. | pass | `impl-01/r1d`..`r3d` logs and dossiers; `evidence/slice-01-tool-calls.md` |
| 8 | 8 | The two-turn run records the answers with no `Read` denial | Both turns run with `stream-json --verbose`; session id taken from turn 1's `result` event. Neither turn had a permission denial. Turn 1: one `Write`. Turn 2 (all four answers in one message): three `Edit` calls. `## Intent` quotes all four answers under their headings ("It is for me and other forgetful plant owners.", "I want to learn.", "No ads.", "I do not know of anything close."), and `goal: learning` is set. All 24 template headings are present in order. Met as amended by Julien on 2026-11-09, and not as first written: `### Unstated` still lists two entries, "Why you care, beyond wanting to learn (only the goal was given)" and "Constraints other than \"no ads\": other money constraints, platforms, or anything else you refuse to do". Those are follow-ups on the goal and constraints questions, which the user did answer, so the answered questions are not fully absent from `### Unstated`. The closing message also asks an extra question (what the user wants to learn). Cost $0.13 for turn 1 and $0.17 for turn 2. (The previous round, twoc, did meet this clause.) | pass | `impl-01/twod/turn1.jsonl`, `turn2.jsonl` and dossier; `evidence/slice-01-tool-calls.md` |
| 9 | 9 | The decoy run has packaged headings and no `DECOY` | One run (decoyd) in a folder holding `templates/dossier.md` with `# DECOY`. `permission_denials` empty; one `Write` to `docs/prospects/houseplant-watering-reminder/dossier.md`. The new dossier has all 24 packaged headings in order and no `DECOY`. The decoy file is untouched. | pass | `impl-01/decoyd` log and dossier |
| 10 | 10 | The install succeeds and the installed file is byte-identical | With a new empty `CLAUDE_CONFIG_DIR` and a scratch marketplace holding a copy of `hosts/claude`: `marketplace add` and `install coaster@coaster-scratch` both exited 0. `cmp` of the installed `skills/capture/SKILL.md` against the built one: identical. The scratch marketplace is outside the repository. | pass | `impl-01/mktd` (outside the repository) |
| 11 | 12 | Julien's interactive run shows no prompt for a packaged file | Julien ran `/coaster:capture` by hand in an interactive session on 2026-11-09 and reported no prompt for a packaged file. The dossier held every heading of the template as it stood then, in order, and the answers under `## Intent`. The model added one heading under `## Evidence`. This run used the package before the last text changes. The `d` runs read no packaged file either, and 001-02's AC 8 repeats an interactive run on the final package. | pass | Julien's report. The dossier was inspected in a scratch folder and not committed, because it describes a real idea. |
| 12 | Preserved | `capture` asks only its questions, does no research and offers no judgment, including in its closing message | Across the 6 `d` runs (r1d, r2d, r3d, decoyd, twod turns 1 and 2) `capture` asked no new kind of question, made no search or web call (tool calls were `Write` and `Edit` only), and no closing message comments on the market, the competition or the idea's prospects. Each suggests `scout` and mentions the challenge round once. The remark from the previous round ("Plant-care reminder apps are common") did not recur; a search of all 6 logs for "crowded", "saturated", "competitive" and "common" found nothing. All closing messages say what `scout` will look for. Three of them mention gaps in neutral terms (r3d, twod turn 1 and decoyd), which names scout's job and is not a judgment. Narrow follow-ups on questions 2 and 3 appear in twod's two turns and decoyd. | pass | `impl-01/r1d`..`r3d`, `decoyd`, `twod` logs |

**DoD:**
- [x] All ACs pass, with the table above filled in from real runs.
- [x] `--check` has been shown to fail on a changed source file (AC 2).
- [x] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [x] Implementation review passed.
- [x] Deviation log produced under this slice heading.
- [x] Reconciliation sweep produced under this slice heading.
- [x] Reconciliation review passed.
- [x] `docs/refinement-todo.md` updated for the entries the spec lists.

### Close-out (post-DONE)

- [x] `docs/specs/README.md` regenerated by `workflow.py status-board`.
- [x] `git rev-parse HEAD:hosts/claude` matches the Recorded revision.

**Anti-horizontal-phasing check:** After this slice, anyone with a checkout can
start Claude Code with `--plugin-dir hosts/claude`, run `/coaster:capture` on an
idea, and read the dossier it writes.

### Deviation log (after reconciliation)

The original spec is preserved above. Implementation notes:

1. **AC 8 was amended.** Julien ruled on 2026-11-09, in the session that ran this slice, that `### Unstated` may hold a narrower follow-up on a partly answered question. Follow-ups appeared in two of the three two-turn runs. The original wording stays in the AC, and row 8 records that it passes only as amended. The sentence added to `capture`'s step 4 is stricter than the amended AC.
2. **Source changed beyond the ACs, from review.** `templates/dossier.md` gained `### Anything close that I know of` and `### Reported at capture`, because question 5's answer and reported facts had no slot and the dossier shape varied between runs. No other skill names those headings. `capture` gained three edits and a rule that its closing summary makes no comment on the market. `challenge`'s hats step now says to paste the full text of the packaged files.
3. **One build text change beyond the map.** Each rendered skill also gets a line saying where a `## Packaged:` section ends, because the packaged files keep their own headings. AC 3 and ADR-0001 name only the map and the two helper paths, so AC 3 holds only with this exception. The script also copies a root `LICENSE` when one exists, ahead of 001-02's AC 4.
4. **Verification ran in stages.** The first attempts at ACs 7 to 9 failed on an expired CLI sign-in and are kept as such. Rounds `b` and `c` were real runs that later source changes superseded, and round `c` met AC 8's original wording where the final round did not. The final evidence is the `d` runs, on the package as built for commit. A tree hash identifies those package bytes in place of the diff digest the slice asks for on a dirty tree. AC 8 used `stream-json --verbose` on both turns so its tool calls could be traced, where the slice's two-turn commands say `json`. AC 11 has no table row, because the accepted ADR is its evidence.
5. **AC 12 predates the final package.** Julien's hand-run came before the last text changes. No packaged file is read in any final run, and 001-02's AC 8 repeats the interactive run.
6. **Reviews.** Craft and arch passed first time. Compliance returned needs-changes, then passed on a re-check by the same reviewer, which was not a fresh review.
7. **Left for later.** The packaged README's layout section and links are now part of 001-02's AC 5. The root `.claude-plugin/plugin.json` is the build's source and is not a supported `--plugin-dir` target, which `docs/architecture.md` now says. Three smaller points are parked in `docs/inbox.md`.

### Reconciliation sweep

| Artifact | Disposition | Rationale |
|----------|-------------|-----------|
| `README.md` | `updated` | Removed the stale bullet that listed packaging as not done. The layout and links in the packaged copy, and the lines saying the handoff is still to come, are 001-02's AC 5. |
| `docs/specs/README.md` | `updated` | Regenerated by `workflow.py status-board`. |
| `docs/product-vision.md` | `no-op` | Scope and use cases are unchanged. The lead claim is decided in 001-02. |
| `docs/architecture.md` | `updated` | Added the package, the build script, ADR-0001, the rebuild rule and the plugin manifest contract. |
| Primer surfaces: `CLAUDE.md` / `AGENTS.md` / scaffold templates | `no-op` | `CLAUDE.md` has no entry for this spec to compress, and there is no `AGENTS.md`. |
| `docs/inbox.md` | `updated` | Parked three follow-ups from review. |
| `docs/refinement-todo.md` | `updated` | Tech stack resolved by ADR-0001. Module boundaries, claude.ai file access and CI/CD updated as the spec lists. |
| `docs/memory/**` | `updated` | Two learnings added: refused reads, and searches that match themselves. |
| `docs/decisions/README.md` / ADR index | `updated` | ADR-0001 accepted and the index regenerated. |
| `docs/releases/claude-code-first-release.md` | `updated` | The no-go names the script as its exception, and the release check covers the hat prompts. |
| `.gitignore` | `updated` | jig's review sidecars hold absolute paths and stay out of the repository. |
