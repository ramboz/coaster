> Status: Draft (elicited)
>
> Captures *why* this project exists, *for whom*, and *with what
> principles*. Architectural mechanics live in [architecture.md](architecture.md).
> Update via reconciliation, or via `/jig:vision-elicitation`.

# Vision: coaster

## Identity

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:393e2cf92ca4 -->

- **Vision statement:** A light-weight front door for the ai-pegboard: the
  whole idea-to-handoff workflow in plain Markdown, one plugin and nothing else
  to install or run, deferring to richer skills when you have them.
- **Tagline:** coaster (noun): the card under your cup where an idea gets its
  first honest sketch, before anyone builds anything.

## Target users

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:090f80c855ca -->

- **For:**
  - Builders who start in chat: "I feel most will start in a "chat" session,
    more than a "code" session."
  - People triaging early: "it's mostly meant to triage idea before an
    entrepreneur would even waste time on crafting a full business plan to
    convince investors."
  - Julien first.
- **Not for:**
  - People who want a full business plan, product tiers or subscriptions.
  - People who want a full framework or mega pack.

## Core problem

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:9041d7718efa -->

- **Problem:** Most of my projects start as a conversation with an AI
  assistant. The idea takes shape in the chat, the chat is abandoned, and a few
  days later I am scaffolding a repository around a vision that was never
  checked against the outside world. The research that should have happened
  first happens later, piecemeal, and usually because something went wrong.
- **Today's paths and where they fall short:**
  - Plain chat: agreeable by design, and an idea discussed in chat rarely
    leaves with sources you can click.
  - Spec Kit's assess, BMAD's Deep Recon and Forge Idea: most need a terminal
    and a framework.
  - Idea-validation skills: most lead with a kill verdict.

## Competitive landscape

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:d95e66d38f6b -->

| Option | What it does | Where it falls short for this gap |
|---|---|---|
| BMAD Deep Recon, in the `bmad-toolbox` plugin | Draft, run and process; falls back to its own defaults without BMAD setup | Still calls `uv`; the loop is the product, not one step in a broader workflow |
| the-researcher | The closest lean brief-and-check tool | 2 stars, unchanged since July; no ledger or handoff |
| Three small loop kits | The same round trip, for personal use | 0 stars; no triage lenses or build hand-off |
| vibe-check's plan-only path | The closest research-by-deferral option | coaster hands research to a richer installed skill, else runs a quick pass |
| Standalone validators | Their own research, with a blunt stance | Verdict-first; coaster is encouraging by default |
| gstack Builder mode | The nearest encouraging default | Cannot install in claude.ai |
| grilling, Forge Idea | Cover the challenge itself | Not a gap: coaster defers and carries its rules |

**Where this project fits:** the front door of the pegboard: no step gives a
verdict, the challenge runs only on request, a skipped lens reads "not looked
at", "none, by choice" answers money, and the user decides.

The evidence for each row is in the
[handoff](prospects/coaster/handoff.md#competitive-landscape).

## Scope

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:050d5decb14e -->

### Core features (prioritized)

1. `capture`: the hunch, in the user's own words
2. `scout`: research turned into a cited, dated evidence ledger
3. `frame`: six optional lenses and the user's decision
4. `challenge`: constructive hardening, only when asked
5. `name`: a name, checked for collisions
6. `handoff`: the starting kit for jig and shaper

### Tiers / phases

- First release: Claude. "Initial POC is fine against Claude alone."
- Later: "then Codex/Copilot later as v1"

### MVP scope

- All six skills, for Claude only. The three-skill variant is held until R-04's
  activation test.

### Out of scope (deliberately)

- "The point is not to establish a full business plan, plan product tiers,
  subscriptions, operational costs, etc."
- "I just don't want the full spec kit or any mega pack like that."
- Engineering research. "How would I build it" comes after, inside the project.
- A research engine of its own.
- A CRM or lead tool, an idea backlog, or a gate.

## Use cases

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:94bcc46b143c -->

- UC-1: A user can identify new project opportunities
- UC-2: A user can do initial field research to find competitors
- UC-3: A user can refine the idea
- UC-4: A user can identify a viable product or service to be built
- UC-5: A user can triage an idea before crafting a full business plan
- UC-6: A user can find a project name or internal codename
- UC-7: A user can start in a chat Project
- UC-8: A user can export a chat Project to the code project when it starts
- UC-9: A user can ask for a constructive challenge on their idea
- UC-10: A user can record a go, no-go, park or pivot decision
- UC-11: A user can hand a decided idea off to jig and shaper

## Stack

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:bfba736864d0 -->

- **Runtime / language:** Markdown skills and templates, plus two
  standard-library Python helpers that run only in Claude Code or a terminal.
- **Platform commitments:** "Claude Chat/Code first, then Codex/Copilot later
  as v1."
  - Deployment shape: open; the family convention is a generated
    `hosts/claude`.
  - Package manager: none.
  - Database: none.
  - Key external services: GitHub for marketplace install; claude.ai Projects
    and Research; npm, PyPI, crates.io and GitHub for name checks.
- **Locked-in vs. still open:** runtime and platform are locked in; packaging
  is open.

## Design principles & constraints

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:fa8aa66ee627 -->

1. Nudges, not gates: "all those categories should be "nudges" and not forcibly
   enforced."
2. "The challenges specifically should really be opt-in only". It finds risks
   to retire and never issues a verdict.
3. The user decides; the tool suggests.
4. Breadth over depth: "the value is in the broader scope and "workflow", I
   cover, and not on the depth itself (like with jig)".
5. Defer to richer skills: "it's meant to be light-weight and defer to richer
   skills anyway."
6. Three voices kept apart: Intent, Evidence and Readings. Every claim is
   tagged, and sourced and dated where its tag needs it.
7. Keep skill descriptions distinct, since overlap drives wrong selection more
   than skill count does.

**Non-obvious constraints:**

- In chat, a plugin's sub-agents and hooks do not run (`C-08`).
- Plugins in chat and Research are for paid plans (`C-08`, `C-03`).
- One Research run may not fit a Pro session (`C-01`, `C-03`).
- Every enabled skill costs context each turn, and the least-used descriptions
  drop first (`RCH-03`, `RCH-04`).
- A chat Project cannot write to GitHub (`ENB-09`).

## How new work enters

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:581271e4fba1 -->

- **Prioritization model:** Mixed. shaper shapes each release; dogfood runs and
  the dossier's risk tests decide what goes in.
- **Spec-triggering rules:**
  - A dogfood run shows the pack got something wrong.
  - A risk test changes the shape or the positioning.
  - A release plan needs specs.
  - The same pain is hit twice.

## Open questions

<!-- elicited: 2026-11-09 / status: filled / hash: sha256:8f8e5d607455 -->

> Deferred items live in [refinement-todo.md](refinement-todo.md).
