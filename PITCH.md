# coaster: triage a project idea before you build it

> A one-page description of something I am building. I would like your honest
> reaction, especially to the questions at the end. A first draft exists and
> has been tested on its own idea; nothing is released yet.

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

AI assistants are agreeable by design, and an idea discussed in chat rarely
leaves with sources you can click. Tools that ask the hard questions do exist,
such as GitHub Spec Kit's assess extension, BMAD's Deep Recon and Forge Idea,
and a fast-growing set of idea-validation skills. Most of them need a terminal
and a framework, and most lead with a kill verdict.

## The idea

> A light-weight front door for the ai-pegboard: the whole idea-to-handoff
> workflow in plain Markdown, one plugin and nothing else to install or run,
> deferring to richer skills when you have them.

A small, opinionated harness for the stretch before a project exists: from
"I have a hunch" to "this is worth building, here is its shape, here are the
risks to retire first", or "park it", or "no, and here is why". It is not a
business-plan generator and not engineering research. It is the triage you do
before spending a weekend on either.

What it adds: it starts in a chat Project before any repository exists; it is
encouraging by default, with a challenge only on request; every claim is
sourced, dated and link-checked; the dossier moves into the repository with
the build; and it uses the research and grilling tools you already have
instead of shipping its own. Its value is the breadth of the workflow, not the
depth of any one step, the same way jig provides the floor and lets you bring
your own depth.

It ships as six reusable instruction files for Claude (skills), usable in a
chat Project or in Claude Code, plus one plain-Markdown dossier per idea.
Nothing to host.

The loop:

1. **Capture.** Your hunch, in your own words, plus what you want out of it
   (money, portfolio, learning, impact). Never paraphrased.
2. **Scout.** Field research with a source and a date on every claim:
   incumbents, substitutes, demand signals, prior art, enabling technology.
   If you have a richer research skill installed, scout hands it the
   questions. Otherwise it runs a quick pass, or writes a brief you can paste
   into Claude's Research mode for a deeper run. Either way it checks the
   links and keeps what was verified apart from what was not.
3. **Frame and decide.** Read the evidence through six lenses. Every lens is
   a nudge, not a gate: skip any, come back later, or never.
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

   One screen at the top of the dossier says where the idea stands. When you
   decide (go, no-go, park with a re-check trigger, or pivot), the decision
   is recorded against the goal you stated, so the reasoning survives.
4. **Challenge (opt-in).** When, and only when, you ask for it. If you have a
   grilling skill installed, it runs the challenge, and you are asked first if
   it hands out verdicts. Otherwise three reviewers who have not seen your
   conversation read only the dossier. They are there to harden the idea with
   you, not to stonewall it. The skeptic checks that the evidence is robust.
   The rival asks how an incumbent would respond, which tells you where to
   position. The customer says what would make them switch and what would
   hold them back. Each must say what holds up first. Their output is a list
   of risks worth looking into early, each with the cheapest way to retire
   it, never a kill verdict. You decide what to do with every one.
5. **Name.** Starts by asking what you want the name to carry: a metaphor
   family, a mythology, a brand feel, a language or etymology to build on,
   and what to avoid. Then at least five candidates with their rationale,
   each checked for collisions on GitHub, npm, PyPI and products in the same
   space.
6. **Handoff.** A kickoff brief and the seeds for the project's vision
   document and first release plan, so the build starts from evidence instead
   of memory.

The posture matters. The point is to encourage ideas and explore them
honestly, not to destroy them. Every lens is a nudge you can skip, the
challenge runs only when you invite it, and enthusiasm and evidence are kept
in separate columns. A good idea leaves the loop knowing its unknowns, not
pretending it has none.

## What it is not

- Not a business plan, a pricing model, or a pitch deck.
- Not engineering research. "How would I build it" comes after, inside the
  project.
- Not a framework that owns your process, and not a research engine of its
  own.
- Not a CRM or a lead tool, and it cannot interview your users for you. It can
  draft the questions and log what you heard.
- Not an idea backlog.
- Not a gate. Nothing stops you from moving on with open questions.

## Where I am

A six-skill draft exists. It has run twice on its own idea, and those runs
changed it. The first found the space more crowded than I thought, so the
pack was slimmed to a thin layer that defers to the research and grilling
tools people already have. The second, with its opt-in challenge, sharpened
the positioning and caught a few design flaws. The next steps are to hand it
off into my build tools, test it in a real claude.ai Project, and hear whether
it resonates with anyone other than me.

## What I would like from you

1. The last time you had a project idea, what did you actually do in the
   first week? Where did you write things down?
2. Which of the six lenses would you skip, and which one is missing?
3. Would you run an adversarial pass on your own idea? What would make you
   trust it, or ignore it?
4. Would you want this in a chat project, in your editor or terminal, or both?
5. Would you pay for it, use it for free, or not bother? What is the closest
   thing you use today?
6. Where do you start a new idea, in a chat or in a repository? Do you use a
   coding agent in a terminal?
