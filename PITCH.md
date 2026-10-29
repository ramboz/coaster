# coaster: triage a project idea before you build it

> A one-page description of something I am exploring. I would like your honest
> reaction, especially to the questions at the end. Nothing is built yet.

## The itch

Most of my projects start as a conversation with an AI assistant. The idea
takes shape in the chat, the chat is abandoned, and a few days later I am
scaffolding a repository around a vision that was never checked against the
outside world. The research that should have happened first happens later,
piecemeal, and usually because something went wrong:

- I find the competitor category I missed weeks in, not on day one.
- I discover who actually has to say yes to adoption, and that it is not my
  user, after the architecture is settled.
- I learn from the first prototype that my "performance win" was really an
  "isolation win", and reposition.
- I re-research an idea I quietly dropped six months earlier, because nothing
  recorded why.

AI assistants make this worse in one specific way: they are enthusiastic. Ask
one whether your idea is good and it will help you build it. Nothing in the
loop asks the cheap, early questions: has this been done, what is missing from
what exists, does anyone want it, who has to change their behaviour, why now.

## The idea

A small, opinionated harness for the stretch before a project exists: from
"I have a hunch" to "this is worth building, here is its shape, here are the
risks to retire first", or "park it", or "no, and here is why". It is not a
business-plan generator and not engineering research. It is the triage you do
before spending a weekend on either.

It ships as a set of reusable instruction files for Claude (skills), usable in
a chat project or in Claude Code, plus one plain-Markdown dossier per idea.
Nothing to install beyond the skills, nothing to host.

The loop:

1. **Capture.** Your hunch, in your own words, plus what you want out of it
   (money, portfolio, learning, impact). Never paraphrased.
2. **Scout.** AI-driven research with a source and a date on every claim:
   incumbents, substitutes, demand signals, prior art, enabling technology,
   name collisions.
3. **Frame.** Read the evidence through six lenses. Every lens is a nudge,
   not a gate: skip any, come back later, or never. Nothing here is allowed
   to slow the brainstorm down.
   - **Timely.** Why now? What changed?
   - **Open.** What exists, where the gaps in the existing solutions are,
     and what does not exist yet.
   - **Wanted.** Is there demand? Proven, latent, or a market you would have
     to open?
   - **Monetizable.** Your constraints first (never ads, must take PayPal,
     free for individuals, and so on), then what the industry does today,
     then options with a recommendation. "None, by choice" is a fine answer
     for open source or non-profit work.
   - **Feasible.** Does the enabling technology exist, and are you allowed to
     build on it?
   - **Adoptable.** Who has to say yes, what do they give up, can you reach
     them?
4. **Challenge (opt-in).** When, and only when, you ask for it: three
   reviewers who have not seen your conversation and read only the dossier.
   They are there to harden the idea with you, not to stonewall it. The
   skeptic checks that the evidence is robust and marks what is thin. The
   rival asks how an incumbent would respond, which tells you where to
   position. The customer says what would make them switch and what would
   hold them back. Each must also say what holds up. Their output is a list
   of risks worth looking into early, each with the cheapest way to retire
   it, never a kill verdict. You decide what to do with every one.
5. **Verdict.** Yours to make, when you ask "where do I stand?". The dossier
   summarises what was looked at, what was skipped, what the evidence
   supports, and which risks are open. Go, no-go, park with a re-check
   trigger, or pivot is recorded against the goal you stated, so the
   reasoning survives.
6. **Name.** Starts by asking what you want the name to carry: a metaphor
   family, a mythology, a brand feel, a language or etymology to build on,
   and what to avoid. Then at least five candidates with their rationale,
   each checked for collisions on GitHub, npm, PyPI and products in the same
   space.
7. **Handoff.** A kickoff brief and the seeds for the project's vision
   document, so the build starts from evidence instead of memory.

The posture matters. The point is to encourage ideas and explore them
honestly, not to destroy them. Every lens is a nudge you can skip, the
challenge runs only when you invite it, and enthusiasm and evidence are kept
in separate columns. The challenge finds risks worth retiring, not reasons to
stop. A good idea leaves the loop knowing its unknowns, not pretending it has
none.

## What it is not

- Not a business plan, a pricing model, or a pitch deck.
- Not engineering research. "How would I build it" comes after, inside the
  project.
- Not a CRM or a lead tool, and it cannot interview your users for you. It can
  draft the questions and log what you heard.
- Not an idea backlog.
- Not a gate. Nothing stops you from moving on with open questions.

## Where I am

Nothing is built. The design is done and the next step is to draft the skills
and run them on this very idea as the first test. Before that, I would like to
know whether this resonates with anyone other than me.

## What I would like from you

1. The last time you had a project idea, what did you actually do in the
   first week? Where did you write things down?
2. Which of the six lenses would you skip, and which one is missing?
3. Would you run an adversarial pass on your own idea? What would make you
   trust it, or ignore it?
4. Would you want this in a chat project, in your editor or terminal, or both?
5. Would you pay for it, use it for free, or not bother? What is the closest
   thing you use today?
