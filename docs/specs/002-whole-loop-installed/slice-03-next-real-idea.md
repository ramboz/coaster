---
status: READY_FOR_REVIEW
dependencies: [002-02]
last_verified:
frame_review: true
claimed_by: claude/objective-diffie-02c20e
---

<!-- jig grounding (spec 064-02 / ADR-0020): ground factual claims about
     runnable surfaces by probe first (run it / read source) or a citation,
     else mark them as assumptions in the spec's `## Assumptions` section —
     never assert an unverified claim as fact. -->

## Slice 002-03 — the next real idea

**Goal:** Julien installs coaster fresh from GitHub and runs the loop on his
next real idea, from `capture` to his own decision and, for a go or a pivot, on
to `handoff`, interactively, in a profile kept to coaster, and nothing about
the idea enters this repository. The run is controlled where the floor is
concerned and is otherwise judged on what got in his way. Whatever Julien
decides about the idea, the slice can pass.

**DoR:**
- 002-02 is DONE, and its pre-release is on `origin/main`.
- Julien has a next real idea and time for one interactive loop (A5).

**Acceptance Criteria:**

1. **A fresh install from GitHub.** In a new disposable profile,
   `claude plugin marketplace add ramboz/coaster` and
   `claude plugin install coaster@coaster` succeed, and Julien signs in there.
   The installed version is the one in `origin/main`'s
   `hosts/claude/.claude-plugin/plugin.json`, and each installed `SKILL.md` is
   byte-identical to `hosts/claude` at that commit.
2. **Julien runs the loop on his real idea, as far as his decision takes
   it.** In an empty `git init` folder outside this repository, in the default
   permission mode rather than auto mode, which hides most prompts (001-02),
   Julien runs `capture`, `scout` and `frame` from the installed plugin, and
   `challenge` only if he asks for a round. The loop then follows coaster's own
   rules (`frame`'s Output, `handoff`'s description):
   - for a go or a pivot, `name` if the idea has no name yet, then `handoff`,
     and `handoff.md` exists;
   - for a no-go or a park, the recorded decision ends the loop, and the record
     says "handoff not run: the decision was <kind>";
   - if Julien has not decided by the end of the run, `frame`'s At a glance
     block and suggested call end the loop, and the record says so.

   No outcome is required. A skill Julien chose not to run is recorded with his
   reason. Where `name` or `handoff` did not run, 002-01's installed runs remain
   their evidence, and A2's helper friction is judged on the helpers that did
   run.
3. **The floor ran, whatever else the profile loaded.** Signing in can bring
   account-synced plugins and skills into the profile, including on resume
   (001-02, and the spec's Current state), and `scout` and `challenge` hand
   work to a research or grilling skill when one is present. So:
   - before the first session and before each resume, the output of
     `claude plugin list` under the profile and the contents of its
     `skills/synced/` folder are recorded, with any research or grilling skill
     named, and any plugin other than coaster is disabled, as in 002-01. If one
     joins mid-session anyway, the record names it and any files its hooks
     wrote, and friction it caused is not counted against coaster in AC 7;
   - each such skill is blocked with a `Skill(...)` deny rule in that profile's
     settings, or turned off on the account for the run, as in 002-01;
   - Julien asks `scout` for its quick pass, which 002-01's AC 12 makes it
     honour, and `challenge` for the three hats if he asks for a round;
   - the session log shows `scout`'s quick pass run by the session itself, the
     link check run or its refusal handled as 002-01's AC 2 requires, and no
     `Skill` call to a skill outside coaster.

   If `scout` or `challenge` hands off anyway, the hand-off is recorded as
   scope-3 evidence and filed as a bug against the skill. The real idea is not
   used up: once the fix ships, Julien runs `scout`'s quick pass, or the round,
   again on the same dossier, and that run is judged instead.
4. **The only prompts are for what the loop really does.** The session log
   shows no read, listing or search of the installed plugin's folder other than
   the helper commands. Julien reports each kind of permission prompt he saw,
   and each is for `WebSearch`, `WebFetch`, one of the two helper commands, or a
   change inside the run folder. None is for a packaged file. For each helper
   prompt, the record gives the rule its "don't ask again" option offers, with
   home directory paths trimmed, which settles A2. Each helper that
   ran did so from the installed path after his approval, and its result is in
   the dossier or `naming.md`.
5. **A challenge round, if one ran, passes the hat check.** If Julien asks for
   a round, every hat's prompt in that session's log passes 002-02's AC 6, and
   AC 7 there applies to a failure. The comparison was built for headless
   stream-json logs, and the interactive transcript's format has not been
   probed, so the record says how the command read it, or how it was
   adapted.
6. **Nothing about the idea enters this repository.** The dossier, its sibling
   files and the session log stay outside. The slice's record gives only the
   shape of the run: the skills run and their order, the installed version, the
   heading checks, counts and statuses, and the kinds of prompts. It gives no
   slug, title, quote or claim from the idea. Before the push that lands this
   slice, the path search, the term search, and a search for the idea's slug
   and a few distinctive words Julien names, kept outside the repository, find
   nothing, both in the tree being pushed and in `git log -p origin/main..HEAD`.
   A search of the tip alone would miss a draft that a later commit removed,
   and a push publishes every commit.
7. **What got in the way becomes follow-ups.** Each thing that broke or
   confused Julien is filed in `docs/bugs/` or `docs/inbox.md` without the
   idea's content. A fix to the package within this slice ships as a
   pre-release bump after the searches.

### Verification scenario

**Preconditions:** 002-02 is DONE and pushed. A new empty folder as
`CLAUDE_CONFIG_DIR`, and Julien signs in there by hand. No secrets.

**Invocation:** Each command runs with `CLAUDE_CONFIG_DIR` set to the new
folder.

```bash
claude plugin marketplace add ramboz/coaster
```

```bash
claude plugin install coaster@coaster
```

Then Julien starts `claude` in an empty `git init` folder outside this
repository, with no `--plugin-dir` and no permission flag, and runs the loop.
Afterwards the session log under that profile is read for ACs 3 to 5, and
nothing from it is copied into the repository.

**Preserved behavior:** `capture` still asks only its five questions and judges
nothing. `challenge` runs only when Julien asks.

**Code revision / dirty-change identity:** Record the commit on `origin/main`
that was installed and the installed version.

| Step | AC | Expected | Observed | Outcome | Evidence |
|------|----|----------|----------|---------|----------|
| 1 | 1 | Fresh install at the version on `origin/main`, byte-identical | | not-run | |
| 2 | 2 | The loop ran as far as Julien's decision takes it | | not-run | |
| 3 | 3 | Plugin lists recorded; the quick pass and link check ran, with no hand-off | | not-run | |
| 4 | 4 | Only the expected kinds of prompt, and no packaged file read | | not-run | |
| 5 | 5 | Any round's hat prompts pass 002-02's AC 6 | | not-run | |
| 6 | 6 | The record gives the shape only, and the searches find nothing in the tree or the pushed history | | not-run | |
| 7 | 7 | Follow-ups filed without the idea's content | | not-run | |

**DoD:**
- [ ] All ACs pass, with the table above filled in from the real run.
- [ ] Reviewed by `reviewer` subagent. Reviewer prompt built by `review.py`.
- [ ] Implementation review passed.
- [ ] Deviation log produced under this slice heading.
- [ ] Reconciliation sweep produced under this slice heading.
- [ ] Reconciliation review passed.
- [ ] `docs/refinement-todo.md` updated if any decisions were deferred during
      implementation.

### Close-out (post-DONE)

- [ ] `docs/specs/README.md` regenerated by `workflow.py status-board`.
- [ ] Primer hygiene: this slice closes the spec, so compress its Active-specs
      entry in `CLAUDE.md` if it has one.

**Anti-horizontal-phasing check:** After this slice, coaster has taken a real
idea from a hunch to Julien's decision or `frame`'s suggested call, and on to
a handoff if he went ahead, installed from GitHub, in a session much like a
user's.
