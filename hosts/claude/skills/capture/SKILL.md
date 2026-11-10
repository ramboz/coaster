---
name: capture
description: >
  Start a prospect dossier from a raw project idea: the hunch, who has the
  problem, what the user wants out of it, and the constraints they already
  know, in the user's own words. Use when the user says "I have an idea",
  "start a dossier", "capture this idea", "is X worth building", "let's
  explore an idea", or pastes a brainstorm or chat transcript to start from.
  Do not use for market research (use scout), for reading the evidence (use
  frame), or for writing the vision document of a project that already
  exists (the build workflow owns that).
---

# capture

Open a dossier for one idea and fill its **Intent** section with the user's
own words. This is the cheapest, friendliest step of the loop: it never
judges, never researches, and never slows the user down.

## Posture

- Encourage. The user is at the most fragile moment of an idea.
- Ask, do not interpret. Write what the user said, not what you think they
  meant.
- Every question is skippable. "Skip" or silence is a complete answer.

## Where the dossier lives

- **Chat project (preferred for new ideas):** one Claude Project per idea.
  The dossier is an artifact named `<slug> dossier`. Later steps add
  artifacts beside it.
- **Code repository:** `docs/prospects/<slug>/dossier.md`, copied from
  the `## Packaged: dossier template` section.

## Inputs

1. **A live conversation.** Ask the questions below.
2. **A pasted brainstorm or transcript.** Use it as the source. Quote the
   user's turns and attribute each quote, for example "(transcript,
   2026-10-20)". An assistant suggestion becomes Intent only where the user
   explicitly agreed to it, and then you quote the agreement.
3. **An existing note.** Same as a transcript.

A transcript usually answers how the user wants the tool or project to
behave more fully than what they want out of it. Check the goal question
explicitly, and do not borrow an example the user gave for someone else's
idea, such as "never ads", as a constraint on this one.

## Questions

Ask at most five at a time, in this order. Stop as soon as the user wants to
move on.

1. What is the idea, in a sentence or two?
2. Who has the problem? Who would use it?
3. Why do you care, and what do you want out of it: income, a portfolio
   piece, learning, impact, an open-source tool, something else? This is the
   **goal** every later reading is made against.
4. What constraints do you already know? Include money constraints, such as
   "never ads" or "must accept PayPal", and anything you refuse to do.
5. Do you already know of anything that does this, or something close?

## Writing the dossier

1. Pick a short kebab-case slug from the user's words. Set `status: hunch`,
   `decision: pending`, `created`, and `goal` if stated.
2. Write answers into `## Intent` under the matching heading. Quote; use
   bullets only where the user listed things. The answer to question 5 goes
   under `### Anything close that I know of`.
3. Anything the user states as a fact about the world goes to `## Evidence`
   under `### Reported at capture`, tagged `reported` (see
   the `## Packaged: evidence rules` section), not into Intent.
4. Under `### Unstated`, list each question that was asked and not answered,
   or that the source does not answer. A question the user answered, even
   briefly, is not unstated. **Never infer an answer.** If you
   suspect one, offer it as a question: "You did not mention X; is that
   intentional?" Add it only on an explicit yes.

## Output

End with a short summary:

- the unstated goal first, if it is unstated: every Monetizable reading and
  the shape pick depend on it;
- where the dossier is;
- what was captured and what is unstated;
- the suggested next step, usually `scout`;
- one line noting that a challenge round exists and runs only if asked.

The summary makes no comment on the market, the competition or the idea's
prospects, because `capture` never researches or judges.

Each `## Packaged:` section below runs to the next `## Packaged:` heading or the end of this file.

## Packaged: dossier template

````markdown
---
prospect: <slug>
title: <working title>
status: hunch        # hunch | scouted | framed | decided. Describes; never gates.
decision: pending    # pending | go | no-go | park | pivot. The user's call.
goal:                # the user's own goal: income, portfolio, learning, impact, open source, ...
created: YYYY-MM-DD
last_scouted:        # YYYY-MM-DD
recheck:             # when parked: the trigger or date to look again
---

# <title>

> Three voices, kept apart. **Intent** is the user's own words. **Evidence**
> carries a provenance tag on every line, and a source and date where the tag
> needs one. **Readings** are judgment and say so. Every section is optional.
> An empty section means "not looked at", never "fine".

## At a glance

_Written and refreshed by `frame`. One screen that carries the decision on
its own._

| Lens | Reading |
|---|---|
| Timely | |
| Open | |
| Wanted | |
| Monetizable | |
| Feasible | |
| Adoptable | |

**Leading shape:**

**First risks to retire:**

**Owed by the user:**

**Suggested call (a suggestion, not the decision):**

**Evidence opened:** _N of M lane entries `grounded`._

**Freshness:**

## Intent

### The hunch

### Who has the problem

### What I want out of it

### Constraints I already know

### Anything close that I know of

### Unstated

_Questions asked and not answered. Never filled by inference._

## Evidence

_Ledger rules: the evidence rules. IDs are prefixed by source and
append-only. Full entries live in the lane files under `scout/` and the round
files under `challenge/`; this section indexes the entries the readings rest
on, one line each. In a chat project, keep everything in this one artifact,
with a heading per lane._

**Link check:** _not run yet._

### Reported at capture

### Field notes

_Conversations with real people: who (by role), when, what they said._

## Readings

_Six lenses, all optional: the lenses `frame` offers._

### Timely

### Open

### Wanted

### Monetizable

### Feasible

### Adoptable

### Not looked at

## Shape options

## Risks worth retiring

| ID | Risk | Why it matters | Cheapest test | Urgency | From | Disposition |
|---|---|---|---|---|---|---|

## Decisions

_Append-only: picks, dispositions, pivots, the decision. Each entry dated._

## Hand-offs

_Links to `naming.md` and `handoff.md`, and engineering unknowns for the
project's own research._
````

## Packaged: evidence rules

# Evidence hygiene

> Shared by every skill. These are the only hard rules in the pack, and none
> of them slows the user down: they keep enthusiasm and evidence in separate
> columns, and they make sure nothing the user decides is lost.

## Three voices, kept apart

A dossier holds three kinds of text. Never blend them.

| Voice | Section | Rule |
|---|---|---|
| **Intent** | `## Intent` | The user's own words. Quote, never paraphrase. Markdown structure is the only edit allowed. |
| **Evidence** | `## Evidence` | Facts about the world, each with a provenance tag, and a source and date where the tag needs one. |
| **Readings** | `## Readings`, `## Shape options` | Judgment. Labeled as such, and it cites the evidence it rests on by ID. |

A thing the user states as fact about the world ("nobody does this", "X has
a million users") goes to Evidence tagged `reported`, not into Intent.

## Ledger entry format

```markdown
- **LND-07** [grounded] One-sentence claim in your own words. — [Source title](https://example.com/page), accessed 2026-10-21.
```

IDs carry the source's prefix so nothing is ever renumbered:

| Prefix | Source |
|---|---|
| `E` | entries written straight into the dossier, such as `reported` facts at capture |
| `LND`, `DEM`, `ENB`, `MON`, `RCH` | the five scout lanes: landscape, demand, timing & enablers, money, reach |
| `OWN` | the user's own record: their past projects, notes, repositories |
| `S`, `V`, `C` | challenge hats: skeptic, rival, customer |
| `F` | field notes from conversations with real people |

The full entries live in the lane and round files. The dossier's Evidence
section is an **index** of the entries the readings rest on, one line each,
grouped by lane, with a link to every lane file.

Provenance tags:

| Tag | Meaning | Needs |
|---|---|---|
| `grounded` | You opened the source and it says this. | link + access date |
| `field` | A real person said it in a conversation or a reply. | who (role, not name, if the dossier may be shared) + date |
| `reported` | The user says so; not yet checked. | date |
| `unverified` | Seen second-hand (a search snippet, a summary) but not opened. | link + date |
| `absence` | A claim that something does **not** exist. | what was searched, where, and the date |

Rules:

- **IDs are append-only.** Never renumber or reuse an ID. Each source takes
  the next free number under its own prefix.
- **Contradictions are struck, not deleted.** `~~E-04 …~~ contradicted by
  E-19` keeps the history readable.
- **Absence is evidence too, and the most fragile kind.** "Nothing does X"
  needs the searches behind it. Treat it as a claim to re-check, not a fact.
- **Balance.** Record evidence that cuts against the hunch with the same care
  as evidence for it, and without commentary. Commentary belongs in Readings.
- **Reports from research tools are leads until opened.** A claim imported
  from Research mode, `/deep-research`, or any other tool is `unverified`
  until its source is opened and says it.
- **Check the links before reading the evidence.** In Claude Code, run
  scout's `link_check.py` helper on the dossier folder and record the result
  in the Evidence section. A resolving link only proves the page exists; a
  quote still has to match its source, qualifiers included.
- **Quote sparingly.** Paraphrase sources. A direct quote stays under fifteen
  words, in quotation marks, with attribution.
- **Freshness.** Set `last_scouted` in the dossier's frontmatter. When a
  reading rests on evidence older than about six months in a fast-moving
  field, say so in the reading and suggest a re-scout. It is a nudge, never
  a gate.
- **Local-only material.** Private repositories, customer names, and raw
  transcripts stay out of a dossier that may be shared. Refer to them in
  general terms ("a real customer site") and keep the raw file gitignored.
