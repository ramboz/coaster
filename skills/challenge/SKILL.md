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
  block, its readings, the three angles from `../_shared/hats.md` as the
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

- **In Claude Code:** start the three hats in parallel, in one message, as the
  subagents `coaster:skeptic`, `coaster:rival` and `coaster:customer`. Each one
  already carries the hats' rules, its own section, the evidence rules and the
  round template, and has no tool that writes or runs commands. Its prompt
  holds its hat's name, the dossier path, the paths of earlier round files,
  and today's date, and nothing else: no notes, rules, limits, lens
  instructions or reply shape of your own.
- `challenge` does not run the link check. That belongs to `scout`'s next
  pass, and every change to the dossier belongs to you.
- **In a chat project:** write one paste-in prompt per hat, holding the full
  text of `../_shared/hats.md`, `../_shared/evidence.md` and
  `templates/challenge-round.md`, the name of that hat's own section, and
  today's date. The user opens a new conversation in the same Project, where
  the dossier is in project knowledge, pastes the prompt, and brings the
  answer back.

## Assembling the round

1. Write `challenge/round-N.md` yourself from the hats' replies. Copy each
   hat's section as the hat replied it, from its own `## ` heading on, without
   shortening it. Open with a short "what holds up" summary before any
   concern.
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
