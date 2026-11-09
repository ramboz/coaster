---
status: READY_FOR_IMPLEMENTATION
dependencies: []
last_verified:
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
   and no `Read` in `permission_denials` on either turn.
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

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1 | Build writes the listed contents and nothing else | _not run_ | not-run | |
| 2 | 2 | `--check` is 0, then non-zero naming the changed file | _not run_ | not-run | |
| 3 | 3 | Standard library only, Claude only, under 200 lines | _not run_ | not-run | |
| 4 | 4 | Strict validation exits 0 | _not run_ | not-run | |
| 5 | 5 | Rendered skills are self-contained, and `skills/` is unchanged in form | _not run_ | not-run | |
| 6 | 6 | The search of `_shared` and `templates` finds nothing | _not run_ | not-run | |
| 7 | 7 | Three runs meet every listed condition | _not run_ | not-run | |
| 8 | 8 | The two-turn run records the answers with no `Read` denial | _not run_ | not-run | |
| 9 | 9 | The decoy run has packaged headings and no `DECOY` | _not run_ | not-run | |
| 10 | 10 | The install succeeds and the installed file is byte-identical | _not run_ | not-run | |
| 11 | 12 | Julien's interactive run shows no prompt for a packaged file | _not run_ | not-run | |

**DoD:**
- [ ] All ACs pass, with the table above filled in from real runs.
- [ ] `--check` has been shown to fail on a changed source file (AC 2).
- [ ] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [ ] Implementation review passed.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [ ] Reconciliation review passed.
- [ ] `docs/refinement-todo.md` updated for the entries the spec lists.

### Close-out (post-DONE)

- [ ] `docs/specs/README.md` regenerated by `workflow.py status-board`.

**Anti-horizontal-phasing check:** After this slice, anyone with a checkout can
start Claude Code with `--plugin-dir hosts/claude`, run `/coaster:capture` on an
idea, and read the dossier it writes.
