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
  `templates/dossier.md`.

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
   bullets only where the user listed things.
3. Anything the user states as a fact about the world goes to `## Evidence`
   tagged `reported` (see `../_shared/evidence.md`), not into Intent.
4. Under `### Unstated`, list each question that was asked and not answered,
   or that the source does not answer. **Never infer an answer.** If you
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
