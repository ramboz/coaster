---
prospect: field-research
title: A field-research harness for project ideas
status: framed       # hunch | scouted | framed | decided. Describes; never gates.
decision: pending    # pending | go | no-go | park | pivot. The user's call.
goal:                # lean and complementary to the ai-pegboard tools (2026-10-21); whether income matters is unstated
created: 2026-10-21
last_scouted: 2026-10-21
recheck:
---

# A field-research harness for project ideas

> Three voices, kept apart. **Intent** is the user's own words. **Evidence**
> carries a provenance tag on every line, and a source and date where the tag
> needs one. **Readings** are judgment and say so. Every section is optional.
> An empty section means "not looked at", never "fine".
>
> Captured from the session transcript of 2026-10-20 and 2026-10-21
> (`sources/2026-10-20-session-transcript.md`, local only). All quotes below
> are Julien's turns in that transcript. Where an element was proposed by the
> assistant, it appears here only with Julien's agreement quoted.

## At a glance

_Refreshed on 2026-10-21 after Julien's direction. **Go or no-go: pending, Julien's call.**_

| Lens | Reading |
|---|---|
| Timely | Open, and filling fast |
| Open | Gaps in a crowded field; the posture gap is real but narrower than first framed |
| Wanted | Proven for the job; round 1 proposes "wanted as a habit, served today by general grilling skills" |
| Monetizable | Depends on the unstated goal; "none, by choice" matches the sibling tools |
| Feasible | Exists, with churn risk |
| Adoptable | Easy to try, hard to be found |

**Shape:** shape 1, the pegboard's front door, slimmed to a thin layer
(Julien, 2026-10-21). Research runs in the research tools the user already
has; the challenge uses an installed grilling skill when there is one. What
stays is the dossier, the six lenses, and the handoff to jig and shaper.

**First risks to retire, an evening or less each:**

1. **R-01.** Run plain chat, Spec Kit `assess`, BMAD Forge Idea, and this pack
   on one idea, side by side.
2. **R-02.** Say whether this tool should ever earn anything. Its purpose is
   already stated.
3. **R-03.** Install the pack in claude.ai from a GitHub marketplace and run
   `capture` in a Project.

**Owed by Julien:** the go or no-go call, the income question, the round-1
dispositions, and a name.

**Suggested call (a suggestion, not the decision):** go, narrowly. Build the
thin layer as a Claude-only proof of concept for your next real idea and for
the family, and run R-01 to R-03 before investing past it.

- Continuing is cheap: the draft pack exists, and the first risks take an
  evening each.
- What incumbents cannot easily copy is the chat-first start and the family
  handoff (`V-02`, round 1).
- A generic validator would enter a crowded field (`LND-14`, `LND-15`), so a
  standalone launch should wait for R-01.

**Freshness:** scouted 2026-10-21. Reddit and most Indie Hackers pages could
not be read. Re-check when Spec Kit `assess` gains a money criterion or a chat
surface.

## Intent

### The hunch

> "we are missing a piece/tool to identify new project opportunities, do
> initial field research to find competitors, refine the idea, and identify a
> viable "product" or "service" to be built. Not the engineering research on
> how to build thing, but really more the initial market/field research for
> the viability side." (transcript, 2026-10-20)

> "Recent projects I worked on where I'd have needed this is "airlock""
> (transcript, 2026-10-20)

> "it's mostly meant to triage idea before an entrepreneur would even waste
> time on crafting a full business plan to convince investors."
> (transcript, 2026-10-20)

The questions it should answer, in Julien's words (transcript, 2026-10-20):

- "does the technology exist" that I can build on top of
- "is there an opportunity" in the market, or has this already been done over
  and over again
- "does this have an monetization possibility" for me to eventually make money
  from it or not (which could be fine for non-profit work, open source, etc.)
- "is there a demand" in the market, or am I addressing either a lost cause
  or breaching open a new market with an innovative idea
- on Open: "what exists, what are the gaps in the existing solutions, what
  doesn't exist yet."

Agreed refinements (assistant proposals, accepted with the quoted reply):

- Six lenses: Timely, Open, Wanted, Monetizable, Feasible, Adoptable. Julien
  on Timely, Fit and Adoptable: "Sounds pretty good." Then: "let's drop the
  "fit"".
- Three challenge hats, skeptic, rival, customer: "I'd do the 3 hats
  initially, I think. they make sense to me and ask the right questions
  upfront."
- Draft loosely, dogfood, then formalize with jig: "Yes. Draft the skill
  pack, templates and references into /Users/ramboz/Projects/misc/prospect in
  the final layout, export this transcript into it, and run the dogfood".

### Who has the problem

> "I feel most will start in a "chat" session, more than a "code" session."
> (transcript, 2026-10-20)

> "using a Project with artifacts that ultimately can be exported to the code
> project when it starts. It's how I started most projects actually."
> (transcript, 2026-10-20)

> "before an entrepreneur would even waste time on crafting a full business
> plan to convince investors." (transcript, 2026-10-20)

### What I want out of it

> "the point of mine is to be lean and complementary to the rest of the tools
> in the ai-pegboard project" (transcript, 2026-10-21)

> "If there are already create tools that do this out there, I could just
> leverage them." (transcript, 2026-10-21)

Julien on the posture the tool must have:

> "The intent is still to encourage ideas and exploration, and not become an
> aggressive destroyer of ideas, right." (transcript, 2026-10-20)

### Constraints I already know

- "Claude Chat/Code first, then Codex/Copilot later as v1. Initial POC is
  fine against Claude alone." (transcript, 2026-10-20)
- "The point is not to establish a full business plan, plan product tiers,
  subscriptions, operational costs, etc. That feels likely like a dedicated
  new tool instead." (transcript, 2026-10-20)
- "all those categories should be "nudges" and not forcibly enforced. some
  questions can be skipped and they should not slow down the brainstorming of
  the end user." (transcript, 2026-10-21)
- "The challenges specifically should really be opt-in only since they can
  potentially be "aggressively" destroying the idea and kill the motivation
  behind the brainstorming session" (transcript, 2026-10-21)
- "make sure the challenges are there as constructive brainstorming to harden
  the idea, and never seen and perceived as an adversary stone walling an idea
  with perceived blockers or hurdles." (transcript, 2026-10-21)
- "the skeptic should not throw away the idea of the project, but really just
  make sure the evidence we have is robust." (transcript, 2026-10-21)
- Monetizable: "the goal is make recommendations with possible alternative
  options, what's the art in the industry, and what constraints do I want (or
  don't)… like I never want ads, or I absolutely want paypal, etc."
  (transcript, 2026-10-21)
- No framework packs: "I just don't want the full spec kit or any mega pack
  like that." (transcript, 2026-10-21)
- Agreed slimming (assistant proposal, accepted with the quoted reply): "Yes.
  Slim the pack to the thin-layer shape: scout delegates research to built-in
  Research or /deep-research with a draft-then-process flow, verdict folds
  into frame, challenge defers to an installed grilling skill when present."
  (transcript, 2026-10-21)
- Naming: "a name that matches the pegboard/workshop terminology
  essentially. maybe finding a proper project name (internal codename) could
  be part of the skill pack we build." (transcript, 2026-10-20)
- Naming: "we'll need to ask things like metaphors the end user wants, or
  mythology they want, etc. ... I'd also give more than just 3… at least 5"
  (transcript, 2026-10-21)

### Unstated

- **Whether income matters for this tool.** The purpose is now stated (lean
  and complementary to the pegboard), but not whether Julien wants it to earn
  anything. _Answered in part on 2026-10-21; the money half is still open._
- **Known alternatives.** Julien did not name any existing tool that does
  this or comes close. _Asked by capture, not answered._
- **Monetization constraints for this tool.** "never want ads" and "absolutely
  want paypal" were given as examples of what a user might say, not as
  constraints on this tool. _Not inferred._

## Evidence

_Ledger rules: `skills/_shared/evidence.md`. IDs are lane-prefixed and
append-only. The full ledger, about 175 entries, lives in the lane files under
[`scout/`](scout/): [landscape](scout/landscape.md) `LND`,
[demand](scout/demand.md) `DEM`, [timing & enablers](scout/enablers.md) `ENB`,
[money](scout/money.md) `MON`, [reach](scout/reach.md) `RCH`, and
[the user's own record](scout/own-record.md) `OWN`. This index lists the
entries the readings rest on._

- **E-01** [reported] Julien is unsure whether Codex and Copilot have an
  equivalent of a chat project: "I'm not sure they have them to be fair".
  — transcript, 2026-10-20.

**Link check, 2026-10-21.** All 178 URLs cited in the lane files were
requested: 176 resolve, 2 refuse automated requests (`MON-03`'s AlternativeTo
page, 403; `DEM-19`'s BigIdeasDB page, 429, already tagged `unverified`). A
resolving link is not proof that the page says what the entry claims.
Re-run after challenge round 1 and the standalone check: 213 URLs, 212
resolve, 1 refuses automated requests (`DEM-19`).

### What exists

- **LND-15** GitHub Spec Kit shipped an opt-in `assess` extension on
  2026-07-17: intake, research, define, shape, decide; a go,
  needs-clarification or kill verdict; required counter-evidence; a hand-off
  into `/speckit-specify`.
- **LND-32** Spec Kit `assess` has no monetization criterion, and its research
  fetches without asking only from about eleven allowlisted hosts.
- **LND-16** BMAD has an optional explore-and-validate step: Forge Idea ends
  Hardened, Killed or Clearer and "does not agree or praise"; deep recon
  requires dated sources and treats absence as a finding.
- **LND-08** Anthropic's product-management plugin has `competitive-brief` and
  an assumption-testing mode in `product-brainstorming`.
- **LND-09 to LND-13** Community Claude Code skills for idea validation:
  validate-idea, startup-skill (also uploadable to claude.ai), solo-founder-skills
  (includes naming), idea-validation-agents, gstack `office-hours`.
- **LND-14** GitHub repositories with "idea validation" in name or description:
  17 created in 2024, 115 in 2025, 542 in 2026 to date.
- **LND-01 to LND-04** Web validators: ValidatorAI, DimeADozen, LEANSpark,
  Preuve (an MCP server pitched as a check coding agents run before building).
- **LND-18 to LND-24** Methods: Shape Up pitch, Lean Canvas, The Mom Test,
  opportunity solution trees, PR/FAQ, premortem, Six Thinking Hats.

- **LND-36 to LND-40** The closest pieces do not run on their own: BMAD's
  Forge Idea and Deep Recon need BMAD core installed, Anthropic's
  product-management plugin installs eight skills at once, and grill-me is a
  stub for another skill. `validate-idea` stands alone but has no research
  step. BMAD's draft-then-process research flow is reusable as a pattern.

### Gaps and absences

- **LND-29, LND-30** Deep-research citation accuracy ranges from 40% to 80%;
  3% to 13% of citation URLs probably never existed. A URL checker cut
  non-resolving links to under 1%.
- **LND-34** No independent test of AI idea validators exists; every
  comparison found was vendor-published.
- **LND-33, RCH-09** No idea-triage plugin in Anthropic's or OpenAI's official
  catalogs or awesome-copilot; Spec Kit `assess` is the one first-party
  exception.
- **DEM-18, DEM-19** ValidatorAI's visible scores cluster high; a competitor
  claims score inflation (`unverified`).

### Demand

- **DEM-01 to DEM-05** "How do I validate before building?" recurs on Hacker
  News for a decade; individual threads draw little attention. One developer,
  2026: the bottleneck moved from "can I build this" to "should I".
- **DEM-07** CB Insights 2026: poor product-market fit cited in 43% of 385
  shutdowns. (The often-quoted 42% "no market need" is from 2014, `DEM-06`.)
- **DEM-08 to DEM-11** AI raised building volume, not results: App Store
  submissions up 24% in 2025; subscription app launches up about sevenfold
  since 2022 while 4.6% reach $10K a month in two years.
- **DEM-12** No study measures abandoned AI-built projects (absence).
- **DEM-13 to DEM-15** Sycophancy is well documented across vendors.
- **DEM-16, DEM-17** Anthropic reports large reductions: Claude was
  sycophantic in 9% of personal-guidance conversations, 18% under pushback.
- **DEM-24, DEM-25** Incumbent validators claim 300K ideas analysed and 3,100
  paying customers (vendor claims).
- **DEM-27, DEM-29, DEM-31** Recent validator launches on Show HN drew 1 to 6
  points; nobody committed to paying in an Ask HN; several 2020–2025
  validators are offline or changed product.
- **DEM-32 to DEM-34** The "just ship" camp treats launching as the test.
- **RCH-12** `grill-me`, a skill that questions your plan, has 1.4M installs on
  skills.sh.

### Timing and enablers

- **ENB-01, ENB-04, ENB-06, ENB-07** Agent Skills launched 2025-10-16 and
  became an open standard 2025-12-18; Codex and Copilot adopted it in December
  2025, the Gemini app in September 2026.
- **ENB-13, RCH-19** claude.ai installs plugins from a GitHub marketplace; an
  account plugin also appears in Claude Code.
- **ENB-14** Chat loads a plugin's skills but ignores its agents and hooks.
- **ENB-11** claude.ai skill uploads accept only the six spec frontmatter
  fields and reject any other key.
- **ENB-22, ENB-23** Web search is on every claude.ai plan; Research mode is
  paid-only.
- **ENB-26** Claude Code ships a built-in `/deep-research` workflow.
- **ENB-19, ENB-21, ENB-30, ENB-32, ENB-33** Platform churn: Projects redesign
  on Pro and Max only, legacy artifacts frozen, Gems and custom GPTs retiring,
  OpenAI's deep-research API models shut down.
- **ENB-08, ENB-10** Anthropic's docs contradict each other on Free-plan skills
  and on skill sharing and sync.

### Money

- **MON-01 to MON-04** Validators sell per report or credit pack; ValidatorAI
  is free.
- **MON-06 to MON-10** Open-source packs earn around the pack: sponsorship,
  courses and membership, enterprise support, a hosted product.
- **MON-12 to MON-14** The target marketplaces have no payment mechanism.
- **MON-20, MON-27 to MON-29** Skills are plain text and easily copied;
  prompts sell for a median of $5.99.
- **MON-24, MON-25** Human validation sprints and discovery workshops sell for
  roughly $2K to $15K.
- **MON-30** No comparable product found relies on advertising.
- **MON-11** 60% of open-source maintainers are unpaid.

### Reach

- **RCH-04** Show HN posts about startup ideas or Claude plugins have a median
  of 2 points; an essay about a skills library scored 435 while repo links
  scored 3 to 5.
- **RCH-11** On skills.sh, 0.04% of skills take 62% of installs; business
  operations demand runs 1.74 times supply.
- **RCH-17, RCH-23** Skills do not always trigger; Desktop and Claude Code
  skill sync is a requested feature.
- **RCH-22** 13.4% of scanned public skills had a critical security issue.
- **RCH-26, RCH-31** Some developers reject frameworks that own the process;
  solo builders trim methods to a minimum.

### The user's own record

- **OWN-01 to OWN-04** airlock: the brainstorm was not preserved; the 1.0
  viability question was answered by a reframe eleven days after kickoff; the
  real-stack field research was filed as engineering research; server-side
  tagging was missing from the landscape.
- **OWN-05** jig's vision-elicitation defers to a richer discovery skill that
  does not exist in the family.

### From challenge round 1

_Full entries in [challenge/round-1.md](challenge/round-1.md). Hat-local IDs:
`S` skeptic, `V` rival, `C` customer._

- **S-01** Twelve of thirteen re-opened load-bearing entries match their
  sources; the thirteenth, `LND-16`, dropped a qualifier.
- **S-02** BMAD Forge Idea does not agree or praise "unless that helps you
  think", and has a "defend this" mode.
- **S-03, S-04** BMAD deep recon keeps a claims ledger with second-source
  checks, and covers pricing models.
- **S-05** `startup-idea-validator` (about 1.5K stars) makes the best case
  first, aims for "honest, not harsh", and has no kill verdict.
- **S-06** haytham, the closest front-door plugin in the community
  marketplace, stopped seeking users in July 2026.
- **S-08, S-09** On skills.sh, idea-validation skills have 26 to 3,000
  installs; grill-me has 1.4M and covers business calls.
- **S-10** Five of seven close packs load in claude.ai chat from a
  marketplace.
- **S-15** Every draft skill in this pack carries a key claude.ai uploads
  reject.
- **S-16** [absence] Nothing found that is encouraging by default with
  challenge only on request.
- **V-02, V-05** Spec Kit `assess` needs an initialized project with Python
  and uv, and its generated skills carry Claude Code-only frontmatter.
- **V-04** Of 37 Spec Kit issues run through `assess`, none got a stop
  verdict.
- **V-06** Spec Kit published 12 releases in four weeks.
- **V-08** Extensify already turns any `SKILL.md` into a Spec Kit extension.
- **V-09** GitHub Agentic Workflows run scheduled agents with Claude as an
  engine.
- **C-01 to C-03** Unprompted skill activation measured at about 40% to 55%,
  lower for natural phrasing.
- **C-04, C-08** No one-step move from a classic chat Project to a repo; the
  redesigned Projects can open a pull request but reach chat-Project users
  last.
- **C-06** Claude and Claude Code share one usage allowance on Pro and Max.

### Field notes

- 2026-10-20: `PITCH.md` prepared for sharing with a prospective user for
  validation. No answers yet.

## Readings

_Judgment. Every lens was looked at in this run. The goal is unstated, so
readings that depend on it say so._

### Timely

**Open, and filling fast.** Every enabling piece landed in the last twelve
months: the skills standard and its adoption across vendors (`ENB-01`,
`ENB-04`, `ENB-06`, `ENB-07`), and chat installs from a GitHub marketplace
(`ENB-13`). The need is sharpened by AI-driven building volume
(`DEM-08`, `DEM-09`). But others saw the same window: the repo count is up
nearly fivefold this year (`LND-14`) and GitHub shipped Spec Kit `assess` in
July (`LND-15`). _Cheapest test that would move this:_ re-scout the landscape
lane in three months.

### Open

**Gaps in a crowded field.** A skill that validates ideas is not open ground
(`LND-09` to `LND-16`). The gaps that remain:

- **Posture.** Nearly every offer markets a harsh or forcing stance: "a
  cofounder who says no" (`LND-04`), "if your idea should die, it will tell
  you" (`LND-10`), "does not agree or praise" (`LND-16`), kill verdicts
  (`LND-15`). An encouraging tool with an opt-in, constructive challenge is
  unclaimed, as far as these lanes looked. No lane searched for it
  explicitly, so treat this as a candidate absence.
- **Money.** Spec Kit `assess` has no monetization criterion (`LND-32`);
  BMAD was not checked.
- **Evidence hygiene.** Citation reliability is the documented weak spot of
  AI research (`LND-29`, `LND-30`), and no validator is independently tested
  (`LND-34`). A ledger with provenance tags and a link check is a concrete,
  demonstrable difference (this run: 176 of 178 links resolve).
- **Surface.** Most community packs are Claude Code-first, and skills.sh does
  not install into claude.ai chat (`RCH-12`). Chat-first with export to code is
  rarer, though startup-skill also uploads to claude.ai (`LND-10`).
- **Family fit.** Spec Kit and BMAD each have a front door. jig, shaper and
  servo do not (`OWN-05`).

_Round 1 proposes:_ correct the `LND-16` quote, which omits "unless that
helps you think" (`S-02`); narrow the money, hygiene and surface gaps
(`S-03`, `S-04`, `S-10`); restate posture as observable behaviours (`V-04`).

_What stops an incumbent:_ nothing much. Spec Kit could add a money criterion
and a softer mode in a release. The defensible part is fit with the pegboard
family, not novelty. _Cheapest test:_ run Spec Kit `assess` and BMAD Forge
Idea on this same idea and compare with this dossier.

### Wanted

**Proven for the job, unclear for another tool.** The job, questioning an idea
before building it, is wanted: the question recurs for a decade (`DEM-01`),
AI made building cheap without making it succeed (`DEM-09`), a plan-grilling
skill has 1.4M installs (`RCH-12`), and incumbents report real usage
(`DEM-24`, `DEM-25`). Demand for one more validation tool is weak: launches
draw almost nothing (`DEM-27`, `DEM-31`), nobody commits to pay (`DEM-29`),
and a vocal camp says launching is the test (`DEM-32`, `DEM-33`). Julien has
the problem, by their own record (`OWN-01` to `OWN-04`). The sycophancy premise needs
current numbers: Claude's rate is far lower than the 2023–2025 headlines
(`DEM-16`, `DEM-17`). _Round 1 proposes:_ "wanted as a habit, served today by general grilling
skills" (`S-08`, `S-09`).

_Cheapest test:_ the validator's answers to the pitch,
and whether Julien reaches for the pack on the next real idea.

### Monetizable

_Julien's stated purpose, "lean and complementary to the rest of the tools in
the ai-pegboard project", points to option 1. Whether income matters is still
unstated, so the other branches stay listed._

- **Industry practice.** Validators sell reports or credits (`MON-01` to
  `MON-03`). Open-source packs earn around the pack, never from it (`MON-06`
  to `MON-10`). The target marketplaces have no payment rails (`MON-12`). Skill
  files are easily copied (`MON-27` to `MON-29`). Human discovery sprints sell
  for thousands (`MON-24`, `MON-25`). Nothing comparable relies on ads
  (`MON-30`).
- **Options.**
  1. **None, by choice.** MIT like jig, servo and shaper; the return is the
     family, reputation, and Julien's own projects.
  2. **Open source plus sponsorship.** Low yield: most maintainers are unpaid
     and donations reach a quarter of them (`MON-11`).
  3. **Open source plus a service.** Run idea-triage sprints for others with
     the pack as the method (`MON-24`, `MON-25`).
  4. **Open source plus a hosted part.** What files cannot carry: scheduled
     re-scouts, link verification, shared dossiers (`MON-29`). A much larger
     build.
- **Recommendation (judgment).** If the goal matches the siblings, option 1,
  with option 4 kept as a later possibility. If income matters, option 3 is
  the shortest path, because it sells time, not files.

_Cheapest test:_ one answer from Julien on the goal.

### Feasible

**Exists, with churn risk.** Skills run in claude.ai and Claude Code from one
plugin (`ENB-13`, `ENB-15`); web search is on every plan (`ENB-22`); chat
ignores agents (`ENB-14`), which the paste-in challenge prompt already
assumes. Two constraints bite now: claude.ai rejects non-spec frontmatter
(`ENB-11`), and the shared references outside each skill folder may not
travel. The platform moves monthly (`ENB-19`, `ENB-21`) and the docs disagree
with themselves (`ENB-08`, `ENB-10`). _Cheapest test:_ install the draft pack
into claude.ai from a GitHub marketplace and run `capture` in a Project.

### Adoptable

**Easy to try, hard to be found.** A solo builder decides alone, and install
is a GitHub URL in chat or two commands in Claude Code (`RCH-19`, `RCH-21`).
The hurdles are habit, since asking the chatbot directly is the default
(`RCH-24`), trust (`RCH-22`), skills that do not fire (`RCH-17`), and
discovery in channels where a few creator packs take most installs (`RCH-11`,
`RCH-13`). Essays travel where repo links do not (`RCH-04`). The light-nudge
design fits builders who trim methods and reject process-owning frameworks
(`RCH-26`, `RCH-31`). _Cheapest test:_ publish the airlock story as an essay
with the pack linked, and list it in the pegboard and community marketplaces.

### Not looked at

_Nothing in this run._

## Shape options

_Julien picked the direction on 2026-10-21: shape 1, slimmed to a thin layer
that reuses the research and grilling tools the user already has._

1. **The pegboard's front door (picked, thin).** An open-source plugin in the ai-pegboard
   marketplace, chat-first in a Claude Project and usable in Claude Code,
   handing off to jig and shaper. _Wedge:_ the encouraging posture plus a
   handoff no generic validator has. _Not:_ a standalone validator or a
   business-plan tool. _Trade-off:_ its audience starts as the family's
   audience. _Positioning:_ "Triage an idea in an evening, with your build
   tools waiting at the other end."
2. **A standalone pack for any builder.** The same skills without the family
   dependency, published to the community marketplace and the Anthropic
   directory, with handoff targets for jig, Spec Kit and BMAD. _Wedge:_
   encouraging, evidence-checked triage in chat. _Trade-off:_ head-on with
   Spec Kit `assess` and hundreds of repos, where distribution is the problem.
   _Positioning:_ "The idea-triage pack that won't flatter you or flatten you."
3. **Contribute instead.** Bring the missing pieces, a money lens, a softer
   mode, a chat surface, to Spec Kit `assess` or BMAD, and write a jig adapter
   for their verdicts. _Wedge:_ borrowed distribution. _Trade-off:_ gives up
   the pegboard idiom and the posture to someone else's roadmap.
   _Positioning:_ n/a.

Shape 1 picked as a direction on 2026-10-21. The go or no-go call is still pending.

## Risks worth retiring

| ID | Risk | Why it matters | Cheapest test | Urgency | From | Disposition |
|---|---|---|---|---|---|---|
| R-01 | Spec Kit `assess` and BMAD already occupy the "front door of a build framework" slot | If the difference is small, building it is cost without gain | Run both on this idea; diff the outputs against this dossier | first | Open | Round 1 proposes widening the test to plain chat, BMAD defend mode and `startup-idea-validator`, naming the closest rival per gap |
| R-02 | The goal for this tool is unstated | Monetizable and the shape pick depend on it | One answer from Julien | first | Monetizable | Partly answered 2026-10-21: purpose stated, income still open |
| R-03 | The chat-first premise rests on a platform that changes monthly | Projects redesign, frozen artifacts, frontmatter limits could break the main path | Install the draft pack in claude.ai from a GitHub marketplace; run capture in a Project | first | Feasible | Round 1 proposes testing both the marketplace path and a zip upload |
| R-04 | Demand for an encouraging posture is unknown; competitors sell harshness | The posture is the main wedge | The validator's answer to the pitch's third question | soon | Open, Wanted | Round 1 proposes restating the posture as five observable behaviours |
| R-05 | Discovery: installs are concentrated and repo launches vanish | A good pack nobody finds helps only its author | Publish the airlock essay; watch installs and replies | soon | Adoptable | Round 1 proposes a shareable sample dossier first and a success bar set in advance |
| R-06 | A full scout run is expensive: about 1M subagent tokens for five lanes here | A chat user on Pro may not afford it, and the allowance is shared with Claude Code (`C-06`) | Run scout in chat mode on Pro and measure | soon | Feasible | Reshaped 2026-10-21: scout now hands research to the user's own tool, so the cost moves there; still worth measuring |
| R-07 | Skills may not trigger when expected | Nudge-style use depends on the skill firing at the right moment | Same install test as R-03, with natural prompts | watch | Adoptable | Round 1 proposes moving to soon (`C-01` to `C-03`) |
| R-08 | The habit to beat may be a general grilling skill, not a validator | Changes who the pack competes with | Ask two pack maintainers for usage or retention | soon | Wanted | Proposed by round 1 |
| R-09 | The chat-first segment is the least evidenced | If users are mostly terminal developers, the chat advantage shrinks | Two questions in the pitch conversation | soon | Wanted | Proposed by round 1 |
| R-10 | Spec Kit can wrap any skill as an extension | Someone else may own the adapter, and the reach | Run Extensify on `capture`; decide on an owned adapter | soon | Adoptable | Proposed by round 1 |
| R-11 | No one-step move from a chat Project to a repo | The handoff is where the Intent says the value lands | Count manual steps at the end of the R-03 test | soon | Feasible | Proposed by round 1 |

## Decisions

_Append-only. Each entry dated._

- 2026-10-21: dossier opened by `capture` from the session transcript.
- 2026-10-21: `scout` ran all five lanes plus the user's own record; status
  set to scouted.
- 2026-10-21: `frame` read all six lenses and sketched three shapes; status set
  to framed. No shape picked.
- 2026-10-21: `challenge` round 1 ran at Julien's request with three hats.
  Fourteen concern groups with proposed dispositions are in
  [challenge/round-1.md](challenge/round-1.md), awaiting Julien.
- 2026-10-21: `verdict` refreshed "At a glance" and suggested "go, narrowly".
  Decision pending.
- 2026-10-21: `name` produced a shortlist of six in [naming.md](naming.md).
  Pick pending.
- 2026-10-21: `handoff` drafted [handoff.md](handoff.md) ahead of the
  decision because this dogfood run asked for it; it is marked draft.
- 2026-10-21: Julien set the direction: reuse existing tools where possible,
  no framework packs, "lean and complementary to the rest of the tools in the
  ai-pegboard project". Shape 1 picked, slimmed to a thin layer. Go or no-go
  still pending.
- 2026-10-21: the pack slimmed to six skills: scout drafts research briefs for
  the user's own research tool and processes the report; verdict folded into
  frame; challenge uses an installed grilling skill when present.
- 2026-10-21: round 1 closed as superseded by the
  [prospect dossier](../prospect/dossier.md), at Julien's agreement. That
  dossier carries the live tests and the go decision.

## Hand-offs

- Naming: [naming.md](naming.md), shortlist ready, no pick.
- Challenge: [challenge/round-1.md](challenge/round-1.md), dispositions pending.
- Handoff: [handoff.md](handoff.md), draft.
- Engineering unknowns, for the project's own research:
  - whether skills in a plugin can read files outside their own folder in
    claude.ai, or each skill must carry its references;
  - which frontmatter keys survive both claude.ai and Claude Code;
  - whether Research mode can be started from a skill;
  - whether a link-check helper can run in claude.ai's code sandbox, which has
    no network on the API (`ENB-27`);
  - how a chat Project's dossier gets into a repository in one step (`C-08`).
