# coaster

**coaster** (noun): the card under your cup where an idea gets its first
honest sketch, before anyone builds anything.

> A light-weight front door for the ai-pegboard: the whole idea-to-handoff
> workflow in plain Markdown, nothing to install or run, deferring to richer
> skills when you have them.

For the stretch before a project exists: capture a hunch, scout the field,
read the evidence through six lenses, optionally pressure-test it, decide,
name it, and hand it off to jig and shaper. Like jig, it provides the floor
and lets you bring your own depth: scout hands research to an installed
research skill such as BMAD's Deep Recon, and the challenge to an installed
grilling skill, when you have them. See
[PITCH.md](PITCH.md) for the one-page description.

**Status:** draft pack, decided go on 2026-10-21. Two dogfood runs on its own
idea: [field-research](docs/prospects/field-research/dossier.md), then
[prospect](docs/prospects/prospect/dossier.md), the working name, after the slimming. What each
taught is in [docs/dogfood/](docs/dogfood/).

## Layout

```text
skills/
  _shared/           evidence rules, the six lenses, the three hats
  capture/           start a dossier from a hunch, in the user's words
  scout/             defers research to a richer skill, or runs a quick pass; turns results into cited evidence
  frame/             six lenses, shape options, where it stands, the user's decision
  challenge/         opt-in; defers to an installed grilling skill, or runs three independent hats
  name/              naming brief, candidates, collisions, a shortlist of five or more
  handoff/           kickoff brief and vision seeds for jig and shaper
templates/           dossier, research brief, challenge round, naming, handoff
docs/prospects/      one folder per idea
```

## What's inside

Markdown skills and templates, plus two standard-library Python helpers that
need network access and run only in Claude Code or a terminal:
`skills/scout/scripts/link_check.py` and `skills/name/scripts/name_check.py`.
No hooks, no connectors, no agents, and no research engine of its own:
research goes to a richer installed skill, a quick pass, or the user's own
research tool, and scout checks what comes back.

## Where it works

- **claude.ai, Free:** Projects and web search work, so scout's quick pass
  does too. Installing plugins in chat is for paid plans, and whether a
  single-skill upload works on Free is unconfirmed.
- **claude.ai, Pro and above:** install from a GitHub marketplace under
  Customize > Plugins. Research mode is there for deeper scouting, and one run
  can take most of a Pro session.
- **Claude Code:** install as a plugin. An installed research or grilling
  skill is used when scout or challenge needs depth.

## Using it in a Claude Project

Skills fire on their own only part of the time, and natural phrasing fires
least. Add one line to the Project's instructions:

```text
When I describe a new project idea or ask whether something is worth building, use the capture skill, then offer scout.
```

## Not done yet

- Packaging as a plugin. The skills point at `skills/_shared/`, which a
  claude.ai skill may not be able to read from outside its own folder; a build
  step will copy the shared references into each skill.
- The chat path is untested: install from a GitHub marketplace, the paste-in
  challenge prompts, and moving a dossier from a Project into a repository.
- Codex and Copilot.
