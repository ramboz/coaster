---
prospect: coaster
title: coaster, the lean idea-triage pack for the ai-pegboard
status: decided      # hunch | scouted | framed | decided. Describes; never gates.
decision: go         # pending | go | no-go | park | pivot. The user's call.
goal:                # lean and complementary to the ai-pegboard tools; income unstated
created: 2026-10-21
last_scouted: 2026-10-21
recheck:
---

# coaster, the lean idea-triage pack for the ai-pegboard

> Three voices, kept apart. **Intent** is the user's own words. **Evidence**
> carries a provenance tag on every line, and a source and date where the tag
> needs one. **Readings** are judgment and say so. Every section is optional.
> An empty section means "not looked at", never "fine".
>
> Opened on 2026-10-21 under the working name "prospect"; the pack was named
> coaster on 2026-10-29 and this dossier renamed with it.
>
> Second dossier on this idea. Captured by `capture` from the live
> conversation on 2026-10-21, after the pack was slimmed and committed
> (`fd473ab`). The first dossier, [field-research](../field-research/dossier.md),
> is part of Julien's own record and is cited as `OWN` evidence.

## At a glance

_Refreshed on 2026-10-29. **Decision: go (Julien, 2026-10-21). Name: coaster (Julien, 2026-10-29).**_

| Lens | Reading |
|---|---|
| Timely | Open now; BMAD has shipped the same loop since July, still needing `uv` |
| Open | A gap in packaging, defaults and breadth, not in capability |
| Wanted | Proven for the job; delegated research shows thin pull |
| Monetizable | "None, by choice" fits the stated purpose; income still unstated |
| Feasible | Exists, but every hop is a hand-off to the user |
| Adoptable | Easy to try, hard to be found; overlap with richer skills is the selection risk |

**Shape:** the thin front door, valued for the breadth of the workflow, not
the depth of any step, and deferring to richer skills where they exist, as
jig does (Julien, 2026-10-21). A three-skill variant is still open.

**First risks to retire:**

1. **R-01.** Install BMAD's toolbox with no setup and run its draft and
   process steps on this report; note what breaks.
2. **R-02.** Run the chat path once end to end, reading the usage meter, and
   run one lane both as a Research brief and as a quick pass.
3. **R-03.** Hand off to grilling with and without the hats' rules, and check
   the dossier still gets updated.

**Evidence opened:** 14 of 36 lane entries are `grounded`; the rest are
`unverified`.

**Owed by Julien:** the income question (R-07).

**Next:** `handoff`, then jig's `scaffold-init` and `vision-elicitation`
reading it, then shaper's `shape-release` for a Claude-only first release.

**Decision:** go, on Julien's own light-weight version that complements jig
and the other pegboard tools. The suggested call had been "go, narrowly, and
keep it thin".

- The loop runs standalone only in BMAD's toolbox plugin, which still calls
  `uv` (`S-01`, `S-02`, `V-01`, `V-03`); the other kits that run it have 0 to
  2 stars and no triage lenses or build hand-off (`LND-04`, `S-03`).
- The challenge has a ready target whose maintainer invites packs like this
  one (`LND-12`, `LND-13`).
- Every platform boundary goes through the user (`ENB-01`, `ENB-02`,
  `ENB-06`, `ENB-09`), so the design work is in paste-ready hand-offs.

**Freshness:** scouted 2026-10-21. Landscape, timing and reach re-scouted;
demand and money carried from the first dossier the same day. claude.ai's
screens were not observed.

## Intent

### The hunch

> "we are missing a piece/tool to identify new project opportunities, do
> initial field research to find competitors, refine the idea, and identify a
> viable "product" or "service" to be built." (conversation, 2026-10-20)

> "the point of mine is to be lean and complementary to the rest of the tools
> in the ai-pegboard project" (conversation, 2026-10-21)

> "If there are already create tools that do this out there, I could just
> leverage them." (conversation, 2026-10-21)

The shape as it stands, agreed in the conversation (assistant proposal,
accepted with the quoted reply): "Yes. Slim the pack to the thin-layer shape:
scout delegates research to built-in Research or /deep-research with a
draft-then-process flow, verdict folds into frame, challenge defers to an
installed grilling skill when present." (conversation, 2026-10-21)

### Who has the problem

> "I feel most will start in a "chat" session, more than a "code" session."
> (conversation, 2026-10-20)

> "it's mostly meant to triage idea before an entrepreneur would even waste
> time on crafting a full business plan to convince investors."
> (conversation, 2026-10-20)

### What I want out of it

> "the point of mine is to be lean and complementary to the rest of the tools
> in the ai-pegboard project" (conversation, 2026-10-21)

> "if this is really the only independently running option out there, I'm
> fine spinning my own version that complements jig, etc. it's meant to be
> light-weight and defer to richer skills anyway. I think the value is in the
> broader scope and "workflow", I cover, and not on the depth itself (like
> with jig)" (conversation, 2026-10-21)

### Constraints I already know

- "I just don't want the full spec kit or any mega pack like that."
  (conversation, 2026-10-21)
- "Claude Chat/Code first, then Codex/Copilot later as v1. Initial POC is fine
  against Claude alone." (conversation, 2026-10-20)
- "all those categories should be "nudges" and not forcibly enforced."
  (conversation, 2026-10-21)
- "The challenges specifically should really be opt-in only" (conversation,
  2026-10-21)
- "The point is not to establish a full business plan, plan product tiers,
  subscriptions, operational costs, etc." (conversation, 2026-10-20)

### Unstated

- **Whether income matters.** The purpose is stated; whether the tool should
  ever earn anything is not. _Asked by capture, not answered._
- **Known alternatives.** Julien named Spec Kit, as something not to depend
  on, but not as a competitor to beat. _Not inferred either way._

## Evidence

_Ledger rules: `skills/_shared/evidence.md`. IDs are prefixed by source and
append-only. Full entries live in the lane files under `scout/`; this section
indexes the entries the readings rest on, one line each._

**Link check, 2026-10-21:** 178 URLs across the lane files, the report and
its notes. 175 resolve; 3 refuse automated requests (two skills.sh rate
limits, one authenticated API endpoint). None broken.

**Run:** scout drafted [brief.md](scout/brief.md) and handed it to the
`anthropic-skills:deep-research` skill in Claude Code, which wrote
[the report](scout/reports/Lean%20idea%20triage%20skill%20landscape.md) and
its research notes. Scout then opened the sources behind twelve load-bearing
claims; those are `grounded`, the rest `unverified`. Round 1 grounded two
more and corrected one date, so 14 of 36 lane entries are now opened.

**Not re-scouted:** demand and money. They come from the first dossier the
same day ([own-record.md](scout/own-record.md)).

### What exists

- **LND-01** [grounded] BMAD's Deep Recon already runs draft, run and
  process, behind BMAD core and `uv`.
- **LND-04** [grounded] The closest lean tool, the-researcher, has 2 stars and
  has not changed since July.
- **LND-06, LND-08** Standalone validators mostly run their own research and
  sell a blunt stance.
- **LND-10** gstack's Builder mode is the nearest encouraging default, and it
  cannot install in claude.ai.
- **LND-11** [absence] No lean pack delegates research and hands off to build
  tools; none is encouraging by default with challenge on request.
- **LND-12, LND-13** [grounded] grilling is standalone, in the official
  marketplace, at 960,166 installs, and its maintainer sends composed
  workflows to separate packs.
- **LND-14, LND-15** grilling batches ten or more questions and uses a
  sub-agent chat cannot run.
- **LND-09** [grounded] The name `idea-triage` is taken.

### Timing and enablers

- **ENB-01, ENB-02** [grounded] The user starts Research mode and
  `/deep-research`; no skill can.
- **ENB-04** [grounded] The deep-research skill can be called by Claude, but
  only where subagents run.
- **ENB-05** No documented way to save a Research report into a Project.
- **ENB-06, ENB-07** [grounded] Nested skill calls lose the parent's flow, and
  `disable-model-invocation` blocks parent calls too; both issues open.
- **ENB-09, ENB-10** [grounded for ENB-09] Chat Projects read from GitHub but
  cannot write; only a Claude Code beta opens pull requests.

### Reach

- **RCH-01** [grounded] Pass rates fall by up to 21% as libraries grow to 202
  skills, mostly from wrong selection.
- **RCH-03, RCH-04** Descriptions of least-used skills are dropped first, and
  every enabled skill costs context each turn.
- **RCH-06 to RCH-09** Third-party packs need a manual marketplace add,
  authors get no usage data, installs concentrate, and reach follows the
  author's audience.

### From challenge round 1

_Full entries in [challenge/round-1.md](challenge/round-1.md). Hat-local IDs:
`S` skeptic, `V` rival, `C` customer._

- **S-01, S-02, V-01, V-03** BMAD's `bmad-toolbox` plugin ships Deep Recon
  and Forge Idea as standalone skills; Deep Recon falls back to its own
  defaults without BMAD setup, but still calls `uv` for its helper and log.
- **S-03** Three more 0-star skills run the brief, external run, ingest loop.
- **S-04** [absence] No public source for the `anthropic-skills:deep-research`
  skill; only this setup has it.
- **S-06** The selection study compares bundles of 11 to 77 skills against
  libraries of up to 202, and blames overlapping descriptions.
- **S-10** Deep-research prompt builders show 1 to 3 installs each; in-session
  research skills show hundreds of thousands.
- **V-02** Deep Recon's and Forge Idea's trigger phrases overlap scout's and
  challenge's.
- **V-04** Deep Recon reached BMAD's stable line on 2026-07-23.
- **V-06** In BMAD, a triage research type and hand-offs are a TOML override.
- **V-08** BMAD built chat-first bundles with Deep Research as default in May
  and removed them in October, never for claude.ai.
- **V-13** BMAD skills run Python scripts in the user's project at
  activation, an open trust issue.
- **V-15** Forge Idea stamps every session HARDENED, CLARIFIED or KILLED.
- **C-01, C-03** One Pro user got at most one finished Research run per
  session; Research runs on Opus and uses limits faster.
- **C-05, C-06** Chats in a Project share no context unless uploaded, though
  paid plans can search earlier chats in the Project.
- **C-07** grilling interviews "relentlessly" and never names strengths first.
- **C-08** Plugins in claude.ai are for paid plans.

### From the user's own record

- **OWN-01 to OWN-07** The first dossier's conclusions on the crowded field,
  demand, money, standalone pieces, chat installs, activation and airlock.

### Field notes

- 2026-10-20: `PITCH.md` prepared for a prospective user. No answers yet.

## Readings

_Judgment. All six lenses looked at; demand and money rest on the first
dossier. Round 1's dispositions, all accepted on 2026-10-21, are folded in._

### Timely

**Open now.** BMAD has run the brief-then-ledger loop since July (`LND-01`,
`LND-03` as corrected by `V-04`) and packages it in a toolbox plugin that
still needs `uv` (`S-01`, `V-01`). The grilling maintainer sends composed
workflows to other packs (`LND-13`). The window narrows if the toolbox drops
`uv` or BMAD reaches claude.ai (`V-08`, `V-10`). _Cheapest test:_ R-01, with
one watch on BMAD releases.

### Open

**A gap in packaging, defaults and breadth, not in capability.** The
positioning, combining Julien's words with round 1:

> A light-weight front door for the ai-pegboard: the whole idea-to-handoff
> workflow in plain Markdown, nothing to install or run, deferring to richer
> skills when you have them.

BMAD users can get triage lenses and hand-offs from one config file (`V-06`),
but not a pack where nothing runs (`V-13`). Each gap, with its closest rival:

- **The loop without a framework.** Closest: BMAD Deep Recon, also shipped as
  a toolbox plugin that still calls `uv` (`LND-01`, `S-01`, `S-02`).
  Difference: nothing to install or run, and the loop is one step in a broader
  workflow rather than the product.
- **A lean brief-and-check tool.** Closest: the-researcher (`LND-04`).
  Difference: a ledger later skills read, not verdicts, plus the handoff to
  jig and shaper.
- **Research by deferral.** Closest: vibe-check's plan-only path (`LND-11`).
  Difference: scout hands research to a richer installed skill when there is
  one and runs a quick pass otherwise. It does not compete on research depth.
- **Encouraging by default.** Closest: gstack Builder mode (`LND-10`).
  Difference: standalone, and it installs in chat. Written as behaviours, not
  tone: no step gives a verdict, the challenge runs only on request, a skipped
  lens reads "not looked at", "none, by choice" answers money, the user
  decides.
- **The challenge itself is not a gap.** grilling and Forge Idea cover it
  (`LND-12`, `V-15`). The pack defers to them, and asks first before using one
  that issues verdicts.

_What stops an incumbent:_ BMAD could slim its toolbox further; grilling's
maintainer will not add a triage workflow (`LND-13`). _Cheapest test:_ the
side-by-side, now against the Deep Recon toolbox and the-researcher.

### Wanted

**Proven for the job; delegated research shows thin pull.** The job is wanted
(`OWN-02`). The habit to beat is grilling, though its audience is measured in
coding agents, not chat (`LND-12`, `S-08`, `C-04`). Research delegated to an
outside tool draws little: prompt builders show 1 to 3 installs each, against
hundreds of thousands for in-session research skills (`S-10`). That is why
scout now defers to an installed research skill or runs in session first.
Julien is the first user (`OWN-07`). _Cheapest test:_ use it on the next real
idea, and in R-02 run one lane both ways.

### Monetizable

**"None, by choice" fits the stated purpose.** The purpose is lean and
complementary to the pegboard; comparable packs earn around the pack, never
from it (`OWN-03`). Whether income matters is still unstated, so options 2 to
4 from the first dossier stay open. Not re-scouted.

### Feasible

**Exists, but every hop is a hand-off to the user.** The user starts Research
mode and `/deep-research` (`ENB-01`, `ENB-02`); the report does not save into
a Project (`ENB-05`); a skill handing off to grilling loses its own flow
(`ENB-06`); a chat Project cannot write to GitHub (`ENB-09`). The one
exception, a deep-research skill Claude can call directly, is present in this
setup but listed nowhere public (`ENB-04`, `S-04`). A Research run may not fit
one Pro session (`C-01`, `C-03`), so scout warns on Pro and offers one lane
per run. The grilling hand-off is the last step and carries the hats' rules
(`C-07`). _Cheapest test:_ R-02, R-03 and R-08.

### Adoptable

**Easy to try, hard to be found.** The selection risk is overlap with Deep
Recon, Forge Idea and grilling more than skill count (`S-06`, `V-02`). The
pack answers it the jig way, with descriptions that defer to a richer
installed skill. A new, rarely used pack still loses its descriptions first
(`RCH-03`). Plugins and Research in chat are for paid plans (`C-08`), so the
README says what works on each surface. Third-party packs need a manual
marketplace add and give authors no usage data (`RCH-06`); reach follows an
audience (`RCH-09`), and there is no grilling listing to ride (`S-09`).
_Cheapest test:_ R-04's activation test; list the pack in the pegboard and
the community marketplace; write the airlock essay.

### Not looked at

_Nothing. Demand and money were carried over, not re-scouted._

## Shape options

_The thin front door is picked (Julien, 2026-10-21), deferring to richer
skills. Variant 3 is folded into it; variant 2 is held._

1. **Thin front door, six skills (picked).** capture, scout, frame,
   challenge, name, handoff, each deferring to a richer installed skill for
   its depth where one exists. _Wedge:_ the whole workflow in one small pack.
   _Trade-off:_ six descriptions to keep distinct where no richer skill exists
   (`RCH-03`).
2. **Thinner, three skills (held).** `capture` and `frame` merged, `scout`
   kept, `handoff` with naming folded in, the challenge as a paste-ready
   prompt. Held until R-04's activation test: the selection evidence is about
   overlap, not count (`S-06`).
3. **Defer to BMAD when present (folded into 1).** Scout hands research to
   Deep Recon when it is installed, as one case of the general deferral. It
   never requires BMAD.

## Risks worth retiring

| ID | Risk | Why it matters | Cheapest test | Urgency | From | Disposition |
|---|---|---|---|---|---|---|
| R-01 | Deep Recon's toolbox drops its `uv` dependency, or BMAD V7 ships | The loop's packaging gap closes completely | Install `bmad-toolbox` in a clean folder with no BMAD setup; run Draft then Process on this report; note what breaks | first | Timely | Accepted 2026-10-21. One watch on BMAD releases also covers a claude.ai bundle (`V-08`) |
| R-02 | The hand-offs feel like homework | Every boundary goes through the user | Run the chat path once end to end; count the hand-offs; read the usage meter before and after; run one lane as a Research brief and as an in-session quick pass | first | Feasible | Amended by round 1, accepted 2026-10-21 |
| R-03 | The grilling hand-off loses the challenge's flow or its posture | Nested calls return to the main session (`ENB-06`); grilling interviews relentlessly (`C-07`) | In Claude Code, hand off to grilling with and without the hats' rules; check the dossier still gets updated | first | Feasible | Amended by round 1, accepted 2026-10-21 |
| R-04 | Descriptions overlap with Deep Recon, Forge Idea and grilling | Overlap, not count, drives wrong selection (`S-06`); a new pack's descriptions drop first (`RCH-03`) | Ten natural prompts under `claude plugin eval`, with grilling and the BMAD toolbox installed; costs in `/skill-doctor` | soon | Adoptable | Restated by round 1, accepted 2026-10-21 |
| R-05 | The encouraging default reads as the failure others design against | Most validators sell harshness (`LND-08`) | Ask the pitch's validator; frame it as the stance before commitment | soon | Open | |
| R-06 | Discovery | Installs concentrate and authors get no data (`RCH-06` to `RCH-09`) | List in the pegboard and the community marketplace; write the essay | soon | Adoptable | Amended by round 1: no grilling listing to ride (`S-09`) |
| R-07 | Income unstated | Monetizable stays branched | One answer from Julien | first | Monetizable | |
| R-08 | The one hop that skips the user may exist only in this setup | No public source lists the deep-research skill (`S-04`) | Ask a CLI-only Claude Code session which skills it has | soon | Feasible | Accepted 2026-10-21 |
| R-09 | In chat, the hats cost three new chats and uploads | The opt-in moment is when the user cares most | Try one fresh chat playing all three hats; check chat search finds the dossier | soon | Adoptable | Accepted 2026-10-21, test only |
| R-10 | Free-plan users get neither plugins in chat nor Research | A friend with an uncommitted idea may not pay yet (`C-08`) | Check a single-skill ZIP upload on Free | watch | Adoptable | Accepted 2026-10-21; the README states each surface |

## Decisions

_Append-only. Each entry dated._

- 2026-10-21: dossier opened by `capture` from the live conversation.
- 2026-10-21: `scout` drafted a brief for three lanes, ran it through the
  deep-research skill, processed the report, opened twelve load-bearing
  sources, and ran the link check. Demand and money carried from the first
  dossier.
- 2026-10-21: `frame` read all six lenses, sketched three variants of the
  picked shape, and refreshed "At a glance". Go or no-go pending.
- 2026-10-21: `challenge` round 1 ran at Julien's request with the three hats.
  Fifteen concerns in twelve groups, with proposed dispositions, are in
  [challenge/round-1.md](challenge/round-1.md), awaiting Julien. Three ledger
  corrections were applied as facts.
- 2026-10-21: Julien accepted round 1's first disposition: "let's accept that
  deep recon already does something similar." R-01 rewritten as a test of
  BMAD's toolbox without setup. Eleven dispositions remain pending.
- 2026-10-21: **Decision: go.** In Julien's words: "if this is really the only
  independently running option out there, I'm fine spinning my own version
  that complements jig, etc. it's meant to be light-weight and defer to richer
  skills anyway. I think the value is in the broader scope and "workflow", I
  cover, and not on the depth itself (like with jig)". The condition holds on
  this evidence: Deep Recon's toolbox is the only maintained standalone
  option, and the other kits have 0 to 2 stars and no triage workflow
  (`S-01`, `S-03`, `LND-04`). Open risks carried, each with its test in the
  register: R-01 to R-09. Next, per the pack: `name`, then `handoff`.
- 2026-10-21: Julien accepted the remaining eleven round-1 dispositions as
  recommended, two modified: descriptions defer to a richer installed skill
  the jig way, and scout defers to an installed research skill or runs a quick
  pass, with the Research brief as the deeper option. Variant 2 held; variant
  3 folded into the picked shape. R-10 added. The first dossier's round 1 was
  closed as superseded.
- 2026-10-29: `name` ran. Brief answered by Julien: workshop, surveying and
  drafting registers, not mining; plain and crafty; test before committing,
  probe the gaps, find promising ground; only same-space collisions rule a
  name out; the napkin image added mid-brief. Shortlist of six in
  [naming.md](naming.md), led by beermat. Pick pending.
- 2026-10-29: **Name picked: coaster** (Julien), chosen over the top
  shortlist entry, beermat, after a same-space check: no AI or agent tool uses
  it; a small, active Flask library holds the PyPI name. Details in
  [naming.md](naming.md). Next, per the pack: `handoff`.
- 2026-10-29: the project folder was renamed to `~/Projects/misc/coaster`, and
  this dossier moved from `docs/prospects/prospect/` to
  `docs/prospects/coaster/`. The README and the pitch now describe the current
  state. Next, per the pack: `handoff`.

## Hand-offs

- Naming: [naming.md](naming.md); picked **coaster**.

- Challenge: [challenge/round-1.md](challenge/round-1.md), dispositions
  pending.
- Engineering unknowns, for the project's own research:
  - whether grilling's batched questions and sub-agent work in chat;
  - how to make a brief fit both the deep-research skill's four fields and a
    one-line `/deep-research` question;
  - how a claude.ai Research report gets into the dossier without a manual
    download and upload.
