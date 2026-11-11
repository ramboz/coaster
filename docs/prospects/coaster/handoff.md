---
prospect: coaster
date: 2026-11-09
decision: go
---

# Handoff: coaster

> Written by `handoff` from the [dossier](dossier.md), [naming](naming.md) and
> [challenge round 1](challenge/round-1.md). Facts dated 2026-11-09 come from
> a release-readiness check of this repository that day.

## Kickoff brief

_Paste this into the first session of the new project._

### What we are building

coaster is a light Claude plugin in the ai-pegboard family, for the stretch
before a project exists. It identifies new project opportunities, does initial
field research to find competitors, refines the idea, and identifies a viable
product or service to build. Six Markdown skills take one idea from hunch to
handoff: `capture` records the hunch in the user's own words, `scout` turns
research into a cited, dated evidence ledger, `frame` reads it through six
optional lenses and records the user's decision, `challenge` hardens the idea
only when asked, `name` finds a name, and `handoff` writes the starting kit
for jig and shaper. Each idea gets one plain-Markdown dossier.

The shape is a thin front door, valued for the breadth of the workflow and not
the depth of any step, deferring to richer installed skills where they exist.
The point is to be lean and complementary to the rest of the tools in the
ai-pegboard project.

The positioning, from the dossier's Open reading:

> A light-weight front door for the ai-pegboard: the whole idea-to-handoff
> workflow in plain Markdown, nothing to install or run, deferring to richer
> skills when you have them.

This repository already holds the draft pack, so the project starts here.

### Why now

_Readings, with the evidence they rest on._

- The gap is open today, in packaging, defaults and breadth rather than
  capability. BMAD has run the brief-then-ledger loop since July, and its
  standalone toolbox plugin still needs `uv` (`LND-01`, `V-04`, `S-01`, `V-01`).
- The challenge has a ready target: grilling is standalone, and its maintainer
  sends composed workflows to separate packs (`LND-12`, `LND-13`).
- The pegboard has no discovery step of its own: jig's vision-elicitation
  leaves deeper product discovery to a richer installed skill (`FR:OWN-05`).
- The window narrows if the toolbox drops `uv` or BMAD reaches claude.ai
  (`V-08`, `V-10`). R-01 watches for both.

### Who it is for

- Builders who start ideas in chat: most are expected to start in a chat
  session rather than a code session.
- People triaging an idea early, before anyone spends time on a full business
  plan to convince investors.
- Julien first (`OWN-07`).

### Settled decisions

- **Go** (Julien, 2026-10-21): with no other option running independently,
  build a light-weight version that complements jig and the other pegboard
  tools and defers to richer skills. Its value is in the breadth of the
  workflow, not the depth of any step, as with jig. Recorded in the dossier's
  Decisions.
- **Name: coaster** (Julien, 2026-10-29). See [naming.md](naming.md). Not
  trademark clearance.
- **Shape: the thin front door, six skills** (Julien, 2026-10-21). The
  three-skill variant is held until R-04's activation test.
- **The positioning leads with what does not run**, not with the lenses, which
  a BMAD user can reproduce with one config file (round 1, Rival 2; `V-06`,
  `V-13`).
- **Claude first:** Claude chat and Claude Code first, then Codex and
  Copilot later, as v1. An initial proof of concept against Claude alone is
  fine.
- **Lenses are nudges,** never enforced.
- **The challenge is opt-in only.** It defers to an installed grilling skill,
  asks first before using one that issues verdicts, and carries the hats'
  rules in the hand-off (round 1, Rival 3 and Customer 3; `V-15`, `C-07`).
- **Research by deferral:** scout uses a richer installed research skill, else
  a quick pass, with a Research-mode or `/deep-research` brief as the deeper
  option (round 1, Skeptic 3, as modified by Julien).
- **No mega pack:** not the full Spec Kit or any similar mega pack.
- **Not a business plan:** no full business plan, product tiers,
  subscriptions or operational costs.
- **Chat keeps one paste-in prompt per hat**, and changes only if R-09's
  one-chat test works (round 1, Customer 2).

### Risks to retire first

1. **R-01.** Install BMAD's toolbox with no setup, run its draft and process
   steps on this dossier's report, and note what breaks.
2. **R-02.** Run the chat path once end to end, reading the usage meter, and
   run one lane both as a Research brief and as a quick pass.
3. **R-03.** Hand off to grilling with and without the hats' rules, and check
   the dossier still gets updated.

Owed by Julien: whether income matters (R-07).

### Suggested order of work

1. Run jig's `scaffold-init` in this repository, then `vision-elicitation`,
   pointing it at this file as the pitch document. It grounds its questions in
   a pitch but does not auto-fill from one, so the vision seeds below are
   inputs to confirm.
2. Run shaper's `shape-release` for a Claude-only first release, starting from
   the release-shaping seeds below. Appetite is Julien's to set.
3. Run R-01 and R-03, which need no packaging.
4. Package the pack the way the family does: plugin and marketplace manifests
   and a generated `hosts/claude`, so dossiers and dogfood logs stay out of the
   install. The build step carries the shared references, and the templates if
   chat needs them.
5. Publish the repository, then run R-02 and R-04. R-02's install step needs a
   published marketplace. R-04 decides whether the three-skill variant comes
   back, so its result should land before the first tag.
6. Tag the first release, then add coaster to the ai-pegboard catalog and the
   community marketplace (R-06).

## Vision seeds

### Identity

**coaster** (noun): the card under your cup where an idea gets its first honest
sketch, before anyone builds anything. A workshop-register name beside jig,
servo, shaper and an unreleased sibling pack, read as `coaster@ai-pegboard`
and `/coaster:capture`.

### Target users

- **For:** builders who start in chat, where most are expected to start
  rather than in a code session; people deciding whether an idea deserves a
  business plan; Julien first (`OWN-07`).
- **Not for:** people who want a full business plan, product tiers or
  subscriptions; people who want a full framework. _Inferred from the
  constraints; confirm in vision-elicitation._

### Core problem

A tool is missing for identifying new project opportunities: initial field
research to find competitors, refining the idea, and identifying a viable
product or service to build.

The airlock record shows the cost: the brainstorm that seeded its design is
not in the repository, the 1.0 viability question was answered by a reframe
eleven days in, and real-stack field research was filed as engineering
research (`OWN-07`). The job is wanted, but
demand for another tool is weak (`OWN-02`), and research delegated to an
outside tool draws little pull (`S-10`).

### Competitive landscape

| Option | What it does | Where it falls short for this gap | Evidence |
|---|---|---|---|
| BMAD Deep Recon, in the `bmad-toolbox` plugin | Runs draft, run and process; falls back to its own defaults without BMAD setup | Still calls `uv`, and the loop is the product rather than one step in a broader workflow. BMAD users can add triage lenses and hand-offs through config, but not a pack where nothing runs | `LND-01`, `S-01`, `S-02`, `V-06`, `V-13` |
| the-researcher | The closest lean brief-and-check tool | 2 stars, unchanged since July; no ledger for later skills to read and no handoff to jig and shaper | `LND-04` |
| Three small kits that run the brief, external run, ingest loop | The same round trip, for personal or small use | 0 stars, with no triage lenses or build hand-off | `S-03` |
| vibe-check's plan-only path | The closest research-by-deferral option | coaster hands research to a richer installed skill when there is one and runs a quick pass otherwise; it does not compete on research depth | `LND-11` |
| Standalone validators | Mostly run their own research and sell a blunt stance | Verdict-first, where coaster is encouraging by default with a challenge on request | `LND-06`, `LND-08` |
| gstack Builder mode | The nearest encouraging default | Cannot install in claude.ai | `LND-10` |
| grilling and Forge Idea | Cover the challenge itself | Not a gap: coaster defers to them. grilling interviews "relentlessly" and Forge Idea stamps a verdict, so coaster carries its rules and asks first | `LND-12`, `V-15`, `C-07` |

**Where this fits:** the front door of the pegboard. Its differences are
behaviours: no step gives a verdict, the challenge runs only on request, a
skipped lens reads "not looked at", "none, by choice" answers money, and the
user decides.

### Scope

The stated jobs:

- identify new project opportunities;
- do initial field research to find competitors;
- refine the idea;
- identify a viable product or service to build;
- from the first dossier: find a project name, an internal codename, as part
  of the pack;
- from the first dossier: work in a chat Project whose artifacts can be
  exported to the code project when it starts.

**Picked shape:** `capture`, `scout`, `frame`, `challenge`, `name` and
`handoff`.

**Out:** a full business plan, product tiers, subscriptions and operational
costs.

**Later:** Codex and Copilot, as v1.

### Use cases

_Only use cases Julien stated; vision-elicitation assigns the IDs._

- A user can identify new project opportunities.
- A user can do initial field research to find competitors.
- A user can refine the idea.
- A user can identify a viable product or service to be built.
- A user can triage an idea before crafting a full business plan.
- A user can find a project name or internal codename.
- A user can start in a chat Project and export to the code project when it
  starts.

### Stack

Claude chat and Claude Code first, then Codex and Copilot later, as v1. An
initial proof of concept against Claude alone is fine.

Today: Markdown skills and templates, plus two standard-library Python helpers
for link and name-collision checks, which run only in Claude Code or a
terminal. No hooks, connectors or agents. Anything else is TBD.

### Design principles and constraints

- Nudges, not gates: no category is enforced.
- The challenge is opt-in and constructive. It finds risks to retire and never
  issues a verdict.
- The user decides; the tool suggests.
- Breadth over depth: the value is in the breadth of the workflow, not the
  depth of any step, as with jig.
- Defer to richer skills: the pack is light-weight and defers to richer
  skills.
- Three voices kept apart: Intent, Evidence and Readings. Every claim is
  tagged, and sourced and dated where its tag needs it
  (`skills/_shared/evidence.md`).
- Keep skill descriptions distinct, since overlap drives wrong selection more
  than skill count does (`S-06`, `V-02`).

### How new work enters

TBD.

### Open questions

- Whether income matters (R-07). Asked by `capture`, not answered.
- Which alternatives Julien wants to beat. Spec Kit was named as something not
  to depend on, and nothing was inferred beyond that.
- Six skills or three (R-04).
- Whether the encouraging default reads as the failure others design against
  (R-05).
- What Free-plan users get (R-10).
- Whether "nothing to install or run" holds as the lead claim while the pack
  ships two optional Python helpers. Round 1's rival names a pack with no
  scripts as the line BMAD cannot match (`V-13`). _Noted while writing this
  handoff._

## Release-shaping seeds

- **Problem and baseline:** a six-skill draft has run twice on its own idea,
  and 13 of its 36 lane entries are `grounded`. On 2026-11-09 the repository
  had no GitHub remote, tag, plugin manifest, licence, changelog or CI. A plain
  plugin copy of the skills passed `claude plugin validate --strict`, and
  `capture` wrote a correct dossier from its template in 3 of 3 Claude Code
  runs. The chat path has never been run.
- **Appetite:** TBD, the user's call.
- **Candidate no-gos:** a framework or mega pack as a dependency; a research
  engine of its own; business plans, pricing, product tiers, subscriptions,
  operating costs or pitch decks; engineering research; a CRM or lead tool; an
  idea backlog; gates on any lens; running the challenge unprompted; verdicts
  on the idea; Codex and Copilot in the first release.
- **Risks and rabbit holes:** R-01 to R-10 in the
  [dossier](dossier.md#risks-worth-retiring). The likeliest rabbit holes are
  the chat-to-repository move, since a chat Project cannot write to GitHub
  (`ENB-09`), and smoothing every hand-off (R-02). R-04 can reopen the six or
  three decision late, and R-01 can close the packaging gap.

## Engineering unknowns

_For the project's own research notes. Not researched here._

- Whether a skill in a claude.ai plugin can read `skills/_shared/` and the root
  `templates/`, or each skill must carry its own copies. In Claude Code, an
  assembled plugin found its template after a search in 3 of 3 runs on
  2026-11-09.
- Whether `git-subdir` marketplace sources, which the pegboard's generated
  manifests use, install in claude.ai. _Noted 2026-11-09._
- Whether grilling's batched questions and sub-agent work in chat.
- How to make a brief fit both a structured research brief and a one-line
  `/deep-research` question.
- How a claude.ai Research report gets into the dossier without a manual
  download and upload.
- How a chat Project's dossier reaches a repository in one step. _Carried from
  the first handoff._
- How to make `capture` fire on natural phrasing without hooks in chat.
  _Carried from the first handoff._
