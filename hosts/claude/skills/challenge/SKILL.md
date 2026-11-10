---
name: challenge
description: >
  Opt-in, constructive hardening of a framed idea from three angles: a skeptic
  who checks the evidence is robust, a rival who shows how an incumbent would
  respond, and a customer who says what would make them switch. Defers to
  any other installed skill whose description identifies it as grilling,
  interviewing, or pressure-testing a plan or idea, but asks the user first
  before using one that issues verdicts on the idea; uses its own three-hat
  review otherwise. Run only when the user
  explicitly asks: "challenge this", "pressure-test it", "harden the idea",
  "poke holes", "play devil's advocate", "run the hats". Never run it
  unprompted. Do not use for a go or no-go (use frame), for research (use
  scout), or for reviewing code, specs, or designs.
---

# challenge

Pressure-test the idea from three angles and hand back risks worth retiring
early. The aim is a stronger idea and a motivated user, never a dead one.

## Opt-in, always

- Run only on an explicit request.
- You may mention that a challenge round exists once per session, in one
  line, after `frame`. If the user says no or ignores it, do not raise it
  again.
- The user can stop a round at any time.

## Choose the engine

**1. A grilling skill the user already has.** Look at the skills available in
this session for one whose description says it grills, interviews, or
pressure-tests a plan or idea. If there is one, offer it first:

- **check its stance.** Read its instructions. If it issues a verdict on the
  idea, such as a kill, no-go, or hardened stamp (BMAD's Forge Idea does), say
  so and ask the user before using it, because this pack never gives one. If
  several qualify, prefer one that gives no verdict;
- write the hand-off as the **last** thing challenge does: a short prompt the
  user sends to start the grilling skill, carrying the dossier's At a glance
  block, its readings, the three angles from the `## Packaged: hats` section as the
  agenda, and the hats' shared rules: lead with what holds up, five concerns
  at most, no verdict, a constructive voice. A skill called from another skill
  does not return control to it, so challenge must not plan to continue after
  the hand-off;
- tell the user to say "challenge: process the grilling" when the interview
  ends. That second run reads the conversation and writes the round file, in
  the same shape as a hat round;
- a live interview runs inside the conversation, so it is not independent of
  it. Say so in the round file. In chat, a grilling skill that relies on
  sub-agents will skip that part.

**2. The three hats, otherwise, or when the user prefers them.** The hats see
only the dossier and earlier rounds, never the conversation. That
independence is what they add.

- **In Claude Code:** start three fresh read-only subagents in parallel. Paste
  into each hat's prompt the full text of the `## Packaged: hats` section,
  the `## Packaged: evidence rules` section and the `## Packaged: challenge round template` section, and name that
  hat's own section. Also give it the dossier path, earlier round files, and
  today's date. Web search is allowed. Each writes its own section file in the
  shape of the `## Packaged: challenge round template` section.
- **In a chat project:** write one paste-in prompt per hat. The user opens a
  new conversation in the same Project, where the dossier is in project
  knowledge, pastes the prompt, and brings the answer back.

## Assembling the round

1. Assemble `challenge/round-N.md` from the sections, opening with a short
   "what holds up" summary before any concern. Delete per-hat files.
2. New evidence goes into the ledger with the hat's prefix (`S`, `V`, `C`).
3. Group concerns that land on the same risk; three angles often find one
   issue from three sides.
4. For each group, **propose** a disposition and mark it proposed:
   - **retire now:** a risk with urgency *first*;
   - **retire later:** a risk with urgency *soon* or *watch*, and a trigger;
   - **accept:** a known risk the user chooses to carry;
   - **rebut:** only with a new evidence entry that answers it.
5. The user confirms or changes each disposition. Until then, readings stay
   as they are, with a one-line "Round N proposes:" note under each affected
   reading. Nothing is carried forward silently, and nothing is dropped
   silently.

## More rounds

- A next round runs only after the user has dispositioned the last one, and
  only if they ask.
- Two or three rounds is plenty. The loop is done when a round adds no new
  *first* risk and every *first* risk has a path, or whenever the user says
  so.
- No round and no angle ever ends the idea. Deciding is the user's job, in
  `frame`.
- If an accepted concern changes the wedge, record a pivot under
  `## Decisions` and suggest running `frame` again.

## Output

- the engine used and the round file path;
- what holds up, first;
- the top risks by urgency, each with its cheapest test;
- the proposed dispositions awaiting the user.

Each `## Packaged:` section below runs to the next `## Packaged:` heading or the end of this file.

## Packaged: hats

# The three hats

> Shared by `challenge`. The hats exist to **harden an idea with the user**,
> never to stonewall it. They run only when the user asks for them. When an
> installed grilling skill runs the challenge instead, the three angles below
> are its agenda.

## Rules every hat follows

1. **Read only the dossier** and any earlier challenge rounds. Never the
   conversation that produced them. That independence is the point.
2. **Lead with what holds up.** Name the strongest parts of the dossier from
   your hat's angle before any concern. Be specific.
3. **Cover every lens.** For each of the six lenses, raise a concern or say
   "nothing serious from this hat". Silence is not allowed. A lens marked
   "Not looked at" gets one line on whether looking would help.
4. **Concerns are risks to retire, never verdicts.** Each one says why it
   matters, the cheapest test that would settle it, and a suggested urgency:
   - *first*: worth looking into before anything else;
   - *soon*: worth settling before committing to a first release;
   - *watch*: keep an eye on it; a re-check trigger is enough.
5. **Five concerns at most.** Pick the ones that matter. A pile of minor
   points buries the important one and drains motivation.
6. **Constructive voice.** Write "worth checking", "we could test", "this
   would be stronger if". Never "this will fail", "fatal", or "kill".
   Avoid rhetoric and sarcasm.
7. **New evidence follows the evidence rules**: a source and
   a date, or a provenance tag that says why not. Web search is allowed and
   encouraged: finding what the scout missed is the most useful thing a hat
   can do.
8. **Do not re-raise** a risk already in the dossier's register unless you
   bring new evidence that changes it.

## Skeptic — is the evidence robust?

You check the evidence, not the idea. You never argue the idea is bad.

- Is each load-bearing reading backed by evidence that says what the reading
  claims? Which readings rest on judgment alone?
- Which sources are thin, stale, one-sided, or self-reported by a vendor?
- Which absences ("nothing does X") rest on too few searches?
- What evidence would most raise confidence, and how cheaply can it be had?

## Rival — how would an incumbent respond?

You play the most capable existing player or the most likely adjacent one.
Name who you are playing.

- If this got traction, would you ignore it, copy it, bundle it, or undercut
  it? How quickly?
- What could you **not** easily copy? That is the user's positioning.
- Where is your own offering weakest today, from the user's point of view?

## Customer — what would make you switch?

You play the target user from the dossier. Name who you are playing.

- What would make you try this, and what would make you stay?
- What holds you back: habit, cost, trust, effort, what you would give up?
- What would you need to see first? Who else would you need to convince?

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

## Packaged: challenge round template

````markdown
---
round: N
date: YYYY-MM-DD
dossier: ../dossier.md
hats: [skeptic, rival, customer]
---

# Challenge round N

> Assembled from one section file per hat, which are then deleted.
> Opt-in and constructive. The hats read only the dossier and earlier rounds.
> Their concerns are risks worth retiring, never verdicts. Dispositions are
> the user's.

## What holds up

_A short summary across the three hats, written before any concern._

## Skeptic: is the evidence robust?

### What holds up

### Worth checking

| # | Lens | Claim or reading | Concern | Why it matters | Cheapest test | Suggested urgency |
|---|---|---|---|---|---|---|

### Nothing serious from this hat

_One line per lens with no concern._

### New evidence

_Entries in the ledger format, with the hat's prefix (S-01, ...)._

## Rival: how would an incumbent respond?

_Playing: <who>._

### What holds up

### Worth checking

| # | Lens | Claim or reading | Concern | Why it matters | Cheapest test | Suggested urgency |
|---|---|---|---|---|---|---|

### Nothing serious from this hat

### New evidence

## Customer: what would make me switch?

_Playing: <who>._

### What holds up

### Worth checking

| # | Lens | Claim or reading | Concern | Why it matters | Cheapest test | Suggested urgency |
|---|---|---|---|---|---|---|

### Nothing serious from this hat

### New evidence

## Dispositions

| Concern | Proposed | Becomes | Confirmed by user |
|---|---|---|---|
````
