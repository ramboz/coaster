# coaster

**coaster** (noun): the card under your cup where an idea gets its first
honest sketch, before anyone builds anything.

> A light-weight front door for the
> [ai-pegboard](https://github.com/ramboz/ai-pegboard): the whole
> idea-to-handoff workflow in plain Markdown, one plugin and nothing else to
> install or run, deferring to richer skills when you have them.

For the stretch before a project exists: capture a hunch, scout the field,
read the evidence through six lenses, optionally pressure-test it, decide,
name it, and hand it off to [jig](https://github.com/ramboz/jig) and
[shaper](https://github.com/ramboz/shaper). Like jig, it provides the floor
and lets you bring your own depth: scout hands research to an installed
research skill such as BMAD's Deep Recon, and the challenge to an installed
grilling skill, when you have them. See
[PITCH.md](https://github.com/ramboz/coaster/blob/main/PITCH.md) for the
one-page description.

## Install in Claude Code

```bash
claude plugin marketplace add ramboz/coaster
claude plugin install coaster@coaster
```

Then start a dossier with `/coaster:capture` followed by your idea.

**Status:** pre-release. coaster has run twice on its own idea: the
[field-research dossier](https://github.com/ramboz/coaster/blob/main/docs/prospects/field-research/dossier.md),
now superseded, then the
[coaster dossier](https://github.com/ramboz/coaster/blob/main/docs/prospects/coaster/dossier.md),
after the slimming. What each run taught is in
[docs/dogfood/](https://github.com/ramboz/coaster/tree/main/docs/dogfood). Its
[handoff](https://github.com/ramboz/coaster/blob/main/docs/prospects/coaster/handoff.md)
to jig and shaper is written, and the first release is being built from it.

## Where it works

- **Claude Code:** the supported path. Install it as above. An installed
  research or grilling skill is used when scout or challenge needs depth.
- **claude.ai:** untested. Paid plans can install plugins from a GitHub
  marketplace under Customize > Plugins, but no part of the chat path has been
  run yet. That includes the paste-in challenge prompts and moving a dossier
  from a Project into a repository.

## What's inside

Markdown skills and templates. Each installed skill carries the templates and
shared rules it needs, so it reads none of its own files at runtime. Two
optional standard-library Python helpers need network access and run only in
Claude Code or a terminal: scout's link check and name's collision check. No
hooks, no connectors, no agents, and no research engine of its own: research
goes to a richer installed skill, a quick pass, or your own research tool, and
scout checks what comes back.

## Repository layout

This is the source repository on GitHub. The installed plugin holds only the
built skills.

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
scripts/             builds the Claude Code package from the folders above
hosts/claude/        the generated Claude Code package
docs/prospects/      one dossier folder per idea (a "prospect dossier")
docs/dogfood/        what each run on its own idea taught
```

## If you try it in a Claude Project

This is untested. Skills fire on their own only part of the time, and natural
phrasing fires least, so add one line to the Project's instructions:

```text
When I describe a new project idea or ask whether something is worth building, use the capture skill, then offer scout.
```

## Not done yet

- The chat path, end to end.
- The dossier's first tests: BMAD's toolbox with no setup, and the grilling
  hand-off with and without the hats' rules.
- Codex and Copilot.
