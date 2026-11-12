---
name: handoff
description: >
  Turn a decided dossier into a project's starting kit: a kickoff brief,
  seeds for the project's vision document, seeds for release shaping, and a
  list of engineering unknowns to research inside the project. Use when the
  user says "hand off", "start the project", "write the kickoff brief",
  "export this to the repo", or "we're ready to build". Do not use before a
  go or pivot decision unless the user insists, and do not use to write the
  vision document, specs, or release plan themselves; the build workflow
  owns those.
---

# handoff

Write `handoff.md` from the `## Packaged: handoff template` section, next to the dossier: in a
repository, `docs/prospects/<slug>/handoff.md`. The project starts from
evidence instead of memory, and nothing in the dossier is lost on the way.

## Inputs

The dossier, `naming.md` if present, and the latest challenge round if one
ran. If the decision is still pending, say so and offer frame's "where you stand" step first. If
the user still wants the handoff, write it as a **draft**: set `decision:
pending`, open with a banner naming the suggested call it assumes, and keep
every pending choice visibly pending.

## What it writes

1. **Kickoff brief.** What we are building, in a paragraph built from Intent
   and the chosen shape. Why now, who for, the settled decisions with their
   references, the risks to retire first, and a suggested order of work.
   This is the paste-in prompt for the first session in the new project.
2. **Vision seeds.** One block per heading of the project's vision document:
   Identity, Target users, Core problem, Competitive landscape, Scope, Use
   cases, Stack, Design principles and constraints, How new work enters, Open
   questions. Rules:
   - quote Intent where it answers a heading;
   - the competitive landscape is a table built from the Open reading, with
     evidence IDs;
   - list only use cases the user stated; never infer one;
   - leave a heading `TBD` rather than invent it.
3. **Release-shaping seeds.** Problem and baseline, candidate no-gos from the
   constraints and the "what it is not" list, risks and rabbit holes from the
   register. Appetite is the user's to set: leave it `TBD`.
4. **Engineering unknowns.** Questions about how to build it, collected along
   the way. They are listed here for the project's own research notes and are
   not researched in this pack.

## Moving from chat to a repository

When the project gets a repository, copy the dossier and its sibling files
into `docs/prospects/<slug>/`. The vision-elicitation step of the build
workflow reads `handoff.md` as its pitch document.

## Boundaries

Handoff does not create the project's vision document, specs, or release
plans, and it does not run any other tool. It writes one file and stops.

## Output

- the handoff path;
- what was seeded, and what was left `TBD`;
- the first step to take in the new project.

Each `## Packaged:` section below runs to the next `## Packaged:` heading or the end of this file.

## Packaged: handoff template

````markdown
---
prospect: <slug>
date: YYYY-MM-DD
decision: <go | pivot | pending>   # pending means a draft; open with a banner naming the call it assumes
---

# Handoff: <name>

## Kickoff brief

_Paste this into the first session of the new project._

### What we are building

### Why now

### Who it is for

### Settled decisions

### Risks to retire first

### Suggested order of work

## Vision seeds

_One block per vision heading. Quote Intent where it answers; leave `TBD`
rather than invent._

### Identity

### Target users

### Core problem

### Competitive landscape

| Option | What it does | Where it falls short for this gap | Evidence |
|---|---|---|---|

### Scope

### Use cases

_Only use cases the user stated._

### Stack

### Design principles and constraints

### How new work enters

### Open questions

## Release-shaping seeds

- **Problem and baseline:**
- **Appetite:** TBD, the user's call.
- **Candidate no-gos:**
- **Risks and rabbit holes:**

## Engineering unknowns

_For the project's own research notes. Not researched here._
````
