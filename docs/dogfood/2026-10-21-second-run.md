# Dogfood: the slimmed pack's run on itself

_2026-10-21. The six-skill pack ran on its own project, then named prospect and
now coaster, as it stood after
the slimming commit, in a second dossier,
[docs/prospects/coaster/](../prospects/coaster/dossier.md). The first dossier
counted as Julien's own record, so only the lanes the slimming changed were
re-scouted._

## What ran

| Step | How | Output |
|---|---|---|
| capture | Live conversation | Intent; income still unstated |
| scout: draft | `templates/research-brief.md` | [brief.md](../prospects/coaster/scout/brief.md), nine questions over three lanes |
| scout: run | The `anthropic-skills:deep-research` skill, called by Claude | three research notes and [a cited report](../prospects/coaster/scout/reports/Lean%20idea%20triage%20skill%20landscape.md) |
| scout: process | Extract, open twelve load-bearing sources, link check, file | 36 entries in three lane files; 178 links, none broken |
| frame | Six lenses, three variants of the picked shape, At a glance | Suggested call: go, narrowly, keep it thin |
| challenge | Offered, not run | Opt-in respected |
| name, handoff | Not run | The go or no-go call is still pending |

| Cost | First run | This run |
|---|---|---|
| Research | about 1.03M subagent tokens, five lanes | about 0.79M: three researchers and a report writer, three lanes |
| Wall time for research | 10 to 19 minutes per lane, in parallel | about 23 minutes end to end |

**Delegation saved maintenance, not tokens.** In Claude Code the research
tool fans out its own subagents, so the bill drops only because fewer lanes
ran. What the pack no longer carries is a research engine of its own. In chat,
the cost moves to the user's Research mode allowance.

## What this run found that the first did not

- **The loop is not new.** BMAD's Deep Recon has run draft, run and process
  since August, inside BMAD. The opening is packaging and defaults.
- **The challenge has a ready target.** grilling is standalone, in the
  official marketplace, at about 960K installs, and its maintainer sends
  composed workflows to separate packs.
- **Every boundary is a hand-off to the user.** The user starts Research mode
  and `/deep-research`; a skill calling another loses its own flow; chat
  Projects cannot write to GitHub.
- **Selection, not context, is what bloat costs.** That favours few skills
  with distinctive descriptions, and makes a three-skill variant worth trying.
- **The name `idea-triage` is taken.**

## What the pack got right

- Briefing only the changed lanes and citing the first dossier as the user's
  own record kept the run focused. It was not in the skill; it is now.
- The `unverified` until opened rule worked: twelve checks turned the
  load-bearing claims `grounded`, and one figure that appeared only in the
  report body stayed `unverified`.
- The challenge was offered once and not run, as designed.

## What the pack got wrong, and the change made

| Problem | Change |
|---|---|
| The link checker cut a URL at a `>` in its query and kept a trailing backtick | Fixed in `skills/scout/scripts/link_check.py` |
| Scout said Claude Code runs `/deep-research`; only the user can | The run step now says who presses the button on each surface, and that Claude may call a deep-research skill directly |
| The narrative report dropped qualifiers that the notes kept | Process prefers structured notes when the tool leaves them |
| The brief's fields did not match the research tool's | The template now has a one-line question, an objective, and suggested sources, matching the deep-research skill's fields |
| Challenge planned to continue after handing off to grilling, which cannot return control | The hand-off is the last step; a second challenge run processes the interview |
| Re-scouting after a pivot was not covered | Scout cites an earlier dossier as the user's own record and briefs only what changed |

## Still untested

The chat path end to end, Research mode, the grilling hand-off, and the
three-skill variant. Those are the dossier's first risks.

## Follow-up: the opt-in challenge on this dossier

Run at Julien's request with the three hats, since no grilling skill is
installed in this session. About 0.66M subagent tokens, 7 to 14 minutes per
hat in parallel. Round file:
[challenge/round-1.md](../prospects/coaster/challenge/round-1.md).

What the challenge caught that scout and frame missed:

- **BMAD already ships the loop as a standalone plugin.** `bmad-toolbox`
  carries Deep Recon, which falls back to its own defaults without BMAD setup
  but still calls `uv`. The scout report had read only BMAD's main repository.
  The lead difference becomes "nothing runs", not "no framework".
- **The challenge skill's own rule would pick the wrong engine.** It looks
  for a skill whose description says it pressure-tests an idea, which BMAD's
  Forge Idea matches. Forge Idea stamps a verdict, which this pack rules out.
- **The one hop that skips the user may be local.** The deep-research skill
  scout called has no public source; a CLI-only user may not have it.
- **The grilling hand-off drops the rules that make the challenge feel
  safe**, and a Research run may not fit one Pro session.

How the challenge behaved: each hat stayed within five concerns, covered all
six lenses, led with what holds up, and kept a constructive voice. The rival
chose BMAD over Matt Pocock and said why. The hats read the first dossier's
round and did not re-raise its concerns without new evidence. Fifteen concerns
grouped into twelve dispositions. The pack changes they imply are proposed,
not applied, until Julien confirms them.

## Dispositions accepted, and what changed in the pack

Julien accepted the first disposition and decided go, then accepted the other
eleven as recommended. Two were modified to fit the positioning, "the value is
in the broader scope and workflow, not the depth" (Julien), which is jig's
"bring your own depth; jig provides the floor".

| Change | Where |
|---|---|
| Scout's description defers research to any installed deep, market, or competitor research skill, the jig way; its triggers are tied to the dossier | `skills/scout/SKILL.md` |
| Scout's run order: a richer installed research skill, else a quick pass by default, with the Research-mode or `/deep-research` brief as the deeper option | `skills/scout/SKILL.md` |
| Scout warns that one Research run can take most of a Pro session and offers one lane per run | `skills/scout/SKILL.md` |
| Scout maps a richer skill's own claims ledger into entries | `skills/scout/SKILL.md` |
| Challenge's description defers to an installed grilling skill, and asks first before using one that issues verdicts | `skills/challenge/SKILL.md` |
| Challenge checks a candidate's stance and carries the hats' rules in the hand-off | `skills/challenge/SKILL.md` |
| The summary says how many lane entries were opened | `skills/frame/SKILL.md`, `templates/dossier.md` |
| One line per surface on what works, and the positioning line | `README.md` |

Not changed: chat still uses one paste-in prompt per hat. The one-chat,
three-hats idea is a test (R-09), and the pack changes only if it works. The
three-skill variant is held until the activation test (R-04). The first
dossier's round was closed as superseded.

## Since then

- **2026-10-29, naming.** The name skill ran from Julien's own brief. It
  excluded the mining register, found "napkin" taken by AI and agent tools,
  and shortlisted six names. Julien picked **coaster**.
- **2026-10-29, renames.** The project folder became `~/Projects/misc/coaster`
  and this run's dossier moved to `docs/prospects/coaster/`. The brief and the
  challenge round keep their original wording, with a dated note.
- **2026-10-29, docs.** The README and the pitch were brought up to date, and
  the first dossier and its drafts were marked as superseded.
