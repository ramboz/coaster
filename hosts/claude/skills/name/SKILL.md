---
name: name
description: >
  Find a project name or internal codename. First ask what the name should
  carry: a metaphor family, a mythology, a brand feel, a language or
  etymology to build on, names to fit with or avoid. Then generate
  candidates, check each for collisions, and shortlist at least five with
  trade-offs. Use when the user says "name this", "find a codename", "what
  should we call it", "brainstorm names", or "is this name taken". Do not
  use for naming code identifiers or files, and do not present the result
  as trademark clearance.
---

# name

A name carries a story. Start from the story the user wants to tell.

## 1. The naming brief

Ask, all skippable, at most five at a time:

1. What does it do, in one line? Take this from the dossier if it exists.
2. What metaphor family or register: workshop tools, nautical, botany,
   astronomy, a mythology (which one), something else?
3. What brand feel: playful, serious, technical, warm, strange?
4. Any language, word root, or etymology to build on?
5. Constraints: length, sound, lowercase, how it reads as a command, a
   prefix, or a plugin id; names it must fit beside; names or meanings to
   avoid; where it must be free (package registries, GitHub, a domain); and
   how much collision is acceptable. A family may already tolerate some: a
   sibling may share its name with a famous project.

Write the answers into `naming.md` from the `## Packaged: naming template` section. Record
unanswered questions as unstated rather than guessing.

## 2. Candidates

Generate ten to fifteen candidates across the registers the user chose. For
each, note the literal thing, the meaning it carries for this project, and a
one-line rationale.

## 3. Collision checks

For each candidate, record with the date:

- package registries: npm, PyPI, crates.io;
- GitHub: repositories and organizations with that exact name, especially in
  the same space;
- products in the same or adjacent space, by web search;
- notable unrelated uses and connotation risks, including other languages
  where known;
- how it reads as a command, a prefix, and a plugin id.

Check **products in the same space first**. A popular register can be
crowded where it matters: in the first run, eight of seventeen workshop-tool
candidates already named an AI agent or spec-driven tool. Drop or flag those
before spending time on registries.

In Claude Code, `python3 "${CLAUDE_PLUGIN_ROOT}/skills/name/scripts/name_check.py" <name> ...` does the registry
and GitHub lookups. In chat, use web search. If the helper is refused or fails,
try no other command to the same end, such as `curl` or an inline script: the
user declined running code. If web tools are allowed, do the lookups by web
search instead and say so in `naming.md`. Otherwise mark those columns "not
checked", with the reason and the command to run by hand. Never record a
result that no tool returned.

## 4. Shortlist

Present **at least five** candidates, ranked, each with its strongest
argument and its main collision or risk. State plainly that this is not
trademark or legal clearance.

## 5. The pick

The user picks one, asks for another round with an adjusted brief, or
defers. Record the pick and its reasons under `## Decisions` in the dossier.

Each `## Packaged:` section below runs to the next `## Packaged:` heading or the end of this file.

## Packaged: naming template

````markdown
---
prospect: <slug>
date: YYYY-MM-DD
---

# Naming: <working title>

## Brief

- **What it does, in one line:**
- **Metaphor family or register:**
- **Brand feel:**
- **Language, root, or etymology to build on:**
- **Constraints:** length, sound, command / prefix / plugin id, names to fit
  beside, names or meanings to avoid, where it must be free.
- **Unstated:**

## Candidates

| Name | The literal thing | What it carries here | Rationale |
|---|---|---|---|

## Collision checks

_Checked YYYY-MM-DD. Not trademark or legal clearance._

| Name | npm | PyPI | crates.io | GitHub | Same-space products | Connotation and reading risks |
|---|---|---|---|---|---|---|

## Shortlist

_At least five, ranked, each with its strongest argument and its main risk._

1.

## Pick

_The user's pick and reasons, also recorded in the dossier's Decisions._
````
