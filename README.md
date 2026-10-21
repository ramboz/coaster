# prospect (placeholder name)

A lean skill pack for the stretch before a project exists: capture a hunch,
scout the field, read the evidence through six lenses, optionally
pressure-test it, decide, name it, and hand it off to jig and shaper. It
reuses what the user already has: research runs in Claude's Research mode or
`/deep-research`, and the challenge uses an installed grilling skill when
there is one. See
[PITCH.md](PITCH.md) for the one-page description.

**Status:** draft pack. The first dogfood run, on the pack's own idea, is in
[docs/prospects/field-research/](docs/prospects/field-research/); what it
taught is in [docs/dogfood/2026-10-21-first-run.md](docs/dogfood/2026-10-21-first-run.md).

## Layout

```text
skills/
  _shared/           evidence rules, the six lenses, the three hats
  capture/           start a dossier from a hunch, in the user's words
  scout/             research briefs for the user's own research tool; turns reports into cited evidence
  frame/             six lenses, shape options, where it stands, the user's decision
  challenge/         opt-in; an installed grilling skill, or three independent hats
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
research runs in the user's own tool, and scout checks what comes back.

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
