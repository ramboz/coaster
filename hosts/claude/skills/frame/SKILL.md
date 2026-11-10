---
name: frame
description: >
  Read a dossier's evidence through six lenses (Timely, Open, Wanted,
  Monetizable, Feasible, Adoptable), sketch the product or service shapes the
  idea could take, and keep a one-screen summary of where it stands. Records
  the user's own decision when they make one: go, no-go, park with a re-check
  trigger, or pivot. Use when the user says "frame this", "what do we make of
  it", "is there an opportunity", "how could this make money", "what would
  the product be", "where do I stand", "should I build this", "go or no-go",
  "park this", or "decide". Do not use for collecting evidence (use scout),
  for pressure-testing (use challenge, only on request), or to make the
  decision for the user.
---

# frame

Turn evidence into readings, readings into two or three concrete shapes, and
keep one screen the user can decide from. The decision itself is the user's.

## Nudges, not gates

Offer the six lenses from the `## Packaged: lenses` section. The user may pick any
subset, in any order, and come back later. A skipped lens goes under
`### Not looked at`. No lens blocks another, and no missing lens blocks a
shape option or a decision.

## For each lens the user wants

1. Use the lens questions as prompts, not as a form.
2. Write a short reading in the judgment voice. Cite the evidence it rests on
   by ID. Offer a one-word summary from the lens's suggested words.
3. Name the cheapest test that would change the reading.
4. If the evidence is missing, say so and suggest the scout lane that would
   fill it. Do not guess.
5. Read against the goal in the dossier's frontmatter. If the goal is
   unstated, ask once. If it stays unstated, read the goal-dependent lenses
   in branches, one per plausible goal, and say so.
6. For a claimed difference, such as a posture or a surface, write it as
   behaviours someone could observe, not as a tone. A tone can be copied by
   editing a README; a behaviour has to be built.
7. In the Open reading, name the closest rival for each gap.

**Monetizable** asks the user's constraints first, if capture did not record
them, in one question. Then industry practice, then options, then a
recommendation. "None, by choice" is a complete answer.

## Shape options

Sketch two or three shapes the idea could take, for example an open-source
plugin, a hosted service, a template pack, a consulting offer. For each:

- who it is for and the wedge, the first thing it does better than anything
  else;
- what it is not;
- the trade-off against the other shapes;
- one sentence of positioning.

The user picks one, keeps several open, or defers. Record a pick under
`## Decisions`.

## Risks

Anything a reading leaves uncertain becomes a row in `## Risks worth
retiring`, with why it matters, the cheapest test, a suggested urgency
(*first*, *soon*, *watch*), and the lens it came from.

## Where you stand

Every time frame runs, refresh the dossier's `## At a glance` block at the
top. It should carry the decision on its own:

- one line per lens with its one-word summary, or "not looked at";
- the shape, picked or leading;
- the first three risks to retire, each with its cheapest test;
- what the user still owes: unanswered questions, pending dispositions;
- how many lane entries are `grounded` out of the total, so the reader knows
  how much was opened;
- how fresh the evidence is, and what could not be read;
- a **suggested call** with two or three reasons, labeled as a suggestion.

## Recording a decision

When the user decides, and only then, append to `## Decisions`:

- the date, the call, and the reasons in the user's words;
- every open risk carried forward, each with its path or marked accepted;
- **park:** the re-check trigger or date, also set as `recheck`;
- **no-go:** the reasons, so the idea is not researched again from scratch;
- **pivot:** what changes, then re-read the lenses it touches.

Update the frontmatter `decision` and `status: decided`. A go with open risks
is a fine decision as long as the risks are listed. A user may decide before
every lens is read: record what was and was not looked at, and move on.

## Output

- lenses read and skipped, each with its one-word summary;
- the shape options and any pick;
- risks added;
- the refreshed At a glance block;
- any decision recorded;
- set `status: framed`, or `decided` once the user has decided;
- next: for go, `name` if the idea has no name yet, then `handoff`; for park,
  the re-check trigger. A challenge round is there if the user asks for one.

Each `## Packaged:` section below runs to the next `## Packaged:` heading or the end of this file.

## Packaged: lenses

# The six lenses

> Shared by `frame` and `challenge`. Every lens is a **nudge**:
> offer it, let the user skip it, and never let one lens block another. A
> skipped lens is recorded under "Not looked at", which means exactly that.
> It is never read as "fine".

Each lens has a few questions, a suggested vocabulary for the reading, the
scout lane that feeds it, and the cheapest test that would move it. The
vocabulary is a suggestion for a one-word summary, not a scale to fill in.

Every reading is made **against the goal the user stated** at capture. The
same idea can read well as an open-source tool and poorly as a business.

## Timely — why now?

- What changed recently that makes this possible or needed: a platform
  shift, a new API, a regulation, a price collapse, a change in behaviour?
- Is the window opening, or closing because others are already in it?

Suggested words: *opening*, *open*, *closing*, *unclear*.
Fed by: the **timing & enablers** scout lane.

## Open — what exists, where are the gaps, what does not exist yet?

- What exists today: direct competitors, adjacent tools, open-source
  projects, manual methods, and "do nothing".
- Where are the gaps in the existing solutions? Complaints about incumbents
  are the best map of them.
- What does not exist yet? Every absence cites the searches behind it.
- One line: what stops the strongest incumbent from adding this tomorrow?

Suggested words: *whitespace*, *gaps in a crowded field*, *done many times*.
Fed by: the **landscape** scout lane.

## Wanted — is there demand?

- Who has the problem, how often, and how much does it hurt?
- How do they cope today, and what do they pay for that, in money or time?
- Is this a lost cause (people tried, it died, here is why) or a market
  someone would have to open?

Suggested words: *proven*, *latent*, *a market to open*, *unclear*.
Fed by: the **demand** scout lane.

## Monetizable — how could this sustain itself?

Ask in this order, and stop wherever the user wants:

1. **The user's constraints first.** What they want or refuse: never ads,
   must accept PayPal, free for individuals, open source, non-profit.
2. **What the industry does.** How comparable things make money or sustain
   themselves, with evidence.
3. **Options.** Two to four models that respect the constraints, each with
   its trade-off.
4. **A recommendation**, labeled as judgment.

"None, by choice" is a complete answer when the goal is open source, a
portfolio piece, learning, or impact. Record which goal it serves.

Not in scope: tiers, price points, unit economics, operating costs. That is
business-plan work and belongs to a different tool.

Suggested words: *clear path*, *plausible*, *none by choice*, *none yet*.
Fed by: the **money** scout lane.

## Feasible — does the enabling technology exist?

- Which pieces you would build on exist, which are emerging, which are
  missing?
- Are you allowed to build on them: terms of service, API stability,
  platform risk, licensing?
- How to build it is out of scope here. List those questions as engineering
  unknowns for the project's own research, and stop.

Suggested words: *exists*, *emerging*, *missing*, *exists but risky*.
Fed by: the **timing & enablers** scout lane.

## Adoptable — who has to say yes?

- Who uses it, who decides, and who else must cooperate for it to work?
- What do they give up to switch: money, habit, data, effort, control?
- Can you reach them: where do they gather, and what channel would carry it?

Suggested words: *easy*, *needs a champion*, *needs cooperation*, *hard*.
Fed by: the **reach** scout lane.
