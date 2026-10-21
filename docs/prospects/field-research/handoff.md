---
prospect: field-research
date: 2026-10-21
decision: pending   # draft; shape picked 2026-10-21, go or no-go still pending
---

# Handoff: field-research harness (name pending)

> **Draft.** Written ahead of the go or no-go call because the dogfood run
> asked for it. Julien picked the shape on 2026-10-21: the pegboard's front
> door, slimmed to a thin layer. It changes if the call goes the other way.
> Quotes are Julien's, from the session transcript.

## Kickoff brief

_Paste this into the first session of the new project._

### What we are building

A Claude plugin in the ai-pegboard family that triages a project idea before
anyone builds it. In Julien's words, the tool should "identify new project
opportunities, do initial field research to find competitors, refine the idea,
and identify a viable "product" or "service" to be built. Not the engineering
research on how to build thing". It captures the hunch in the user's own
words, drafts research briefs for the research tool the user already has and
turns the report into a cited, dated evidence ledger, reads the evidence
through six optional lenses, runs a constructive challenge only when asked,
records the user's decision, finds a name, and hands off to jig and shaper. It
starts in a claude.ai Project and moves to Claude Code with the repository.

The point, in Julien's words: "to be lean and complementary to the rest of the
tools in the ai-pegboard project". No framework packs: "I just don't want the
full spec kit or any mega pack like that."

### Why now

- Skills became a cross-vendor standard in the last year, and claude.ai now
  installs plugins straight from a GitHub marketplace (`ENB-01`, `ENB-13`).
- AI made building cheap without making it succeed (`DEM-09`).
- The pegboard has no front door: jig's vision step defers to a discovery
  skill the family does not have (`OWN-05`).

### Who it is for

- Builders who start ideas in chat: "most will start in a "chat" session, more
  than a "code" session."
- People triaging an idea "before an entrepreneur would even waste time on
  crafting a full business plan".
- Julien first: airlock is the motivating case (`OWN-01` to `OWN-04`).

### Settled decisions

- Claude first: "Claude Chat/Code first, then Codex/Copilot later as v1.
  Initial POC is fine against Claude alone."
- Six lenses, all nudges: "all those categories should be "nudges" and not
  forcibly enforced."
- The challenge is opt-in, constructive, and three hats: skeptic, rival,
  customer.
- No business plan: "not to establish a full business plan, plan product
  tiers, subscriptions, operational costs".
- Monetizable starts from the user's own constraints, then industry practice,
  then options.
- Naming asks for metaphors, mythology, brand and etymology first, and offers
  "at least 5" candidates.
- Draft loosely, dogfood, then formalize with jig.
- A thin layer: research runs in Claude's Research mode, `/deep-research`, or
  another research tool, through a draft-then-process flow; the challenge
  uses an installed grilling skill when there is one; six skills in all.
- From this run: spec-only skill frontmatter, an "At a glance" block on every
  dossier, lane-prefixed evidence IDs, a link check before readings.

### Risks to retire first

1. **R-01.** Side-by-side on one idea: plain chat, Spec Kit `assess`, BMAD
   Forge Idea, `startup-idea-validator`, and this pack.
2. **R-02.** What Julien wants out of this tool.
3. **R-03.** Install from a GitHub marketplace in claude.ai, and as a zip;
   run `capture` in a Project with natural prompts (folds in R-07 and R-11).

### Suggested order of work

1. Julien makes the go or no-go call, answers the income half of R-02,
   confirms the round-1 dispositions, and picks a name.
2. R-03: package the draft pack as a plugin and test the chat path. Needs the
   shared references copied into each skill.
3. R-01: the side-by-side, using this dossier as the reference output.
4. Run jig's `scaffold-init`, then `vision-elicitation` with this file as the
   pitch document, then shaper's `shape-release` for a Claude-only proof of
   concept.
5. Specs where ceremony pays: host packaging and the build step for shared
   references, the helper scripts, and an evaluation that replays this
   transcript against this dossier as the golden output.

## Vision seeds

### Identity

A pre-build triage tool for project ideas: field research and viability, not
engineering research. Tagline and name: pending (see `naming.md`).

### Target users

- **For:** builders who start projects in a chat session; people deciding
  whether an idea deserves a business plan; pegboard users who want a front
  door before jig and shaper.
- **Not for:** writing business plans, tiers or pricing; engineering research
  on how to build; teams that need a sprint planner or backlog. _Inferred from
  the constraints; confirm in vision-elicitation._

### Core problem

The research that should happen before a build happens later, piecemeal, and
usually because something went wrong. The airlock record shows each failure
(`OWN-01` to `OWN-04`). AI assistants can be agreeable by default, though
Claude's measured rate is now low (`DEM-16`, `DEM-17`).

### Competitive landscape

| Option | What it does | Where it falls short for this gap | Evidence |
|---|---|---|---|
| Spec Kit `assess` | Five-stage triage with go, needs-clarification or kill, handing off to Spec Kit | Needs an initialized project and a terminal; research limited to an allowlist; no money criterion; verdict-first framing | `LND-15`, `LND-32`, `V-02` |
| BMAD explore and validate | Forge Idea, deep recon with a claims ledger, product brief | Process-owning framework; challenge is the default stance, with a defend mode on request | `LND-16`, `S-02`, `S-03` |
| Community skills (validate-idea, startup-skill, solo-founder-skills, office-hours, startup-idea-validator) | Idea validation inside Claude Code, some in chat | Mostly harsh or always-on challenge; no family handoff | `LND-09` to `LND-13`, `S-05`, `S-07` |
| General grilling skills (grill-me) | Interrogates any plan | No research, no evidence ledger, no decision record | `RCH-12`, `S-09` |
| Web validators (ValidatorAI, DimeADozen, Preuve) | Scores and reports | Vendor-tested only; scores cluster high | `LND-01` to `LND-04`, `LND-34`, `DEM-18` |
| Plain chat or deep research | Free and immediate | Citation reliability; nothing persists or moves to the repo | `LND-29`, `LND-30`, `C-08` |

**Where this fits:** the front door of the pegboard family, encouraging by
default, evidence you can click, a dossier that moves to the repo.

### Scope

Julien's stated jobs, in their words:

- "identify new project opportunities"
- "do initial field research to find competitors"
- "refine the idea"
- "identify a viable "product" or "service" to be built"
- "finding a proper project name (internal codename) could be part of the
  skill pack"
- "a Project with artifacts that ultimately can be exported to the code
  project when it starts"

Out of scope: business plans, product tiers, subscriptions, operating costs,
engineering research, Codex and Copilot in the proof of concept.

### Use cases

_Only use cases Julien stated; vision-elicitation assigns the IDs._

- A user can identify new project opportunities.
- A user can do initial field research to find competitors.
- A user can refine the idea.
- A user can identify a viable product or service to be built.
- A user can find a project name or internal codename.
- A user can start in a chat Project and export to the code project when it
  starts.

### Stack

Claude chat and Claude Code first. Markdown skills and artifacts. Anything
else is TBD; the family convention is standard-library Python helpers.

### Design principles and constraints

- Nudges, not gates; nothing slows the brainstorm.
- The challenge is opt-in and constructive: risks to retire, never kill
  verdicts.
- The user decides; the tool suggests.
- Evidence hygiene: every claim tagged, sourced and dated, or marked
  unverified; nothing the user decides is lost.

### How new work enters

TBD.

### Open questions

R-02 (the goal), R-04 (demand for the posture), R-08 (the habit to beat),
R-09 (the chat-first segment), R-10 (owning a Spec Kit adapter), and the
name.

## Release-shaping seeds

- **Problem and baseline:** a draft six-skill pack exists. A seven-skill
  version ran once on its own idea before it was slimmed. Nothing is packaged
  or installed yet.
- **Appetite:** TBD, Julien's call.
- **Candidate no-gos:** framework packs as dependencies; a research engine
  of its own; business plans and pricing; engineering research;
  Codex and Copilot; running the challenge unprompted; kill verdicts; a
  hosted service; an idea backlog.
- **Risks and rabbit holes:** R-01 to R-11 in the dossier; the chat-to-repo
  move (R-11) is the likeliest rabbit hole.

## Engineering unknowns

_For the project's own research notes. Not researched here._

- Whether a skill in a plugin can read files outside its own folder in
  claude.ai, or each skill must carry its references.
- Which frontmatter keys survive both claude.ai and Claude Code.
- Whether Research mode can be started from a skill.
- Whether the link-check helper can run in claude.ai's code sandbox.
- How a chat Project's dossier reaches a repository in one step.
- How to make `capture` fire on natural phrasing without hooks in chat.
