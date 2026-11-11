---
prospect: coaster
date: 2026-10-29
---

# Naming: the lean idea-triage pack for the ai-pegboard

## Brief

Asked by `name` on 2026-10-29; answers are Julien's.

- **What it does, in one line:** a light-weight front door for the
  ai-pegboard, taking an idea from hunch to handoff in plain Markdown and
  deferring to richer skills for depth.
- **Metaphor family or register:** workshop tools, surveying and navigation,
  and drafting, the register an unreleased sibling pack's name comes from.
  The name should fit the workshop overall; mining and prospecting feel
  disjoint from it. So the working name "prospect" and its mining cousins are
  out.
- **Image added mid-brief:** the napkin drafting idea, a sketch made over a
  coffee chat.
- **Brand feel:** plain and crafty: a common noun with a one-line "(noun):"
  definition, like the siblings.
- **Meaning to carry:** test before committing; probe the gaps; find
  promising ground.
- **Collision tolerance:** only a use in the same space rules a name out:
  AI, agent, or developer tooling. Registry collisions elsewhere are fine, as
  with servo.
- **Fixed constraints:** fits beside jig, servo, shaper, gauge and an
  unreleased sibling pack; avoids `scout`; reads as `<name>@ai-pegboard` and
  `/<name>:capture`.

## Candidates

| Name | The literal thing | What it carries here |
|---|---|---|
| beermat | The card coaster a first plan gets sketched on | The napkin idiom in its plain British form: the first sketch of an idea over a drink |
| bradawl | A small awl that makes the pilot hole for a screw | Test before committing: the smallest step that makes the real work go in straight |
| pilothole | The starter hole drilled before the screw | The same idea said plainly |
| offing | The stretch of sea visible from shore; "in the offing" means coming soon | Find promising ground on the horizon |
| scratchawl | An awl for scribing layout lines before cutting | Mark the lines before committing the saw |
| testpiece | The scrap cut to check a setup before the real board | Test before committing |
| corer | A tool that pulls a core sample | Sample the ground before building |
| underlay | Tracing paper slid under a drawing to work over it | Draft over what exists |
| napkin | The back-of-the-napkin sketch | Julien's image; see collisions |
| coaster | The card under a cup, the napkin's sturdier cousin | The idea sketched over coffee, before anyone builds |
| serviette, jotter, napery | Napkin cousins | The coffee-table sketch |
| feeler | A feeler gauge measures gaps | Probe the gaps |
| alidade, theodolite, sextant, transect, leadline, groma | Surveying and navigation instruments | Probe and sight the ground |
| esquisse, croquis, parti, charrette, blueline, sightline | Drafting and architecture terms | The first sketch and the big idea |
| dryfit | Assembling parts without glue to check the fit | Test before committing |
| fieldbook, landfall, waymark, cairn, lodestar, recce | Surveying and navigation terms | Field notes, first sight of land, markers |

## Collision checks

_Checked 2026-10-29 with `skills/name/scripts/name_check.py`, a GitHub search
of names and descriptions filtered for AI, agent and idea-tool terms, npm
search, and web search. Not trademark or legal clearance._

| Name | npm | PyPI | crates.io | GitHub | Same-space use |
|---|---|---|---|---|---|
| beermat | free | free | free | 8 tiny repos | **none**; a hobby beer-mat collector app; the book *The Beermat Entrepreneur* |
| bradawl | free | free | free | none | **none** |
| pilothole | free | free | free | 1 repo | **none**; Pilot Protocol, an agent network, shares only the word "pilot" |
| offing | free | free | free | 2 tiny repos | **none** |
| scratchawl | free | free | free | none | **none** |
| testpiece | free | free | free | 4 empty repos | **none** |
| corer | free | free | free | no exact-name repos | **none** found |
| underlay | taken, unclear | free | free | UI backdrop libraries | none in AI; minor UI-library overlap |
| napkin | taken | taken | free | 19 repos | **Napkin AI**, a funded AI visuals startup; a Claude Code skill named napkin (642 stars); an agent knowledge system; `napkin-to-blueprint`, an idea-to-blueprint engine for Claude Code and Codex; Napkin MCP servers |
| serviette | taken | taken, a RAG server | free | pathwaycom/serviette | **AI**: a no-code RAG server |
| jotter | taken | taken | taken | 34 repos | **agent**: a log for Claude Code sessions and a Jotter MCP server |
| feeler | taken | free | free | 16 small repos | **AI**: `feeler-e2e`, test automation powered by Claude |
| alidade | taken | taken | taken | 19 repos | **agent**: a code-graph MCP server for AI agents |
| theodolite | taken | free | taken, an LSP MCP server | — | **agent** |
| transect | free | free | free | AI-Safety-Institute/transect | **AI** |
| groma | free | taken | free | FoundationVision/Groma | **AI**: a vision-language model |
| esquisse | free | taken | free | 36 repos | **agent**: a Claude Code plugin and an agentic coding framework |
| charrette | taken | taken | free | 6 repos | **agent**: a CLI that turns a PRD into reviewed pull requests; a multi-agent framework |
| parti | taken | free | taken | google-research/parti | **AI**: an image model |
| pounce | taken | taken | taken | 27 repos | **agent**: coding-agent control and MCP servers |
| dryfit | free | free | free | getbeton/dryfit | **AI**: a test bed for agentic product-signal discovery |
| fieldbook | taken, a readiness-evidence tool | taken, ML experiments | free | 12 repos | **dev tooling** |
| coaster | taken, a Node routing framework, last changed 2022 | taken, Hasgeek's Flask utilities | taken, an HPC compute library, last changed 2021 | 4 repos; hasgeek/coaster, 74 stars, active | **none in AI or agents**; the nearest are Coast, a desktop AI assistant, and Coasty. **Dev tooling:** the Flask library, small and active; far smaller than servo's collision with Mozilla's browser engine |
| sextant, sightline, blueline, recce, lodestar, landfall, croquis, cairn, waymark, setsquare, leadline | mostly taken | mostly taken | mostly taken | many | **dev tooling** in each case |

**Note:** as in the first naming pass, agent tooling has taken most of the
workshop, drafting and surveying vocabulary. The free names are the humbler
or more obscure nouns.

## Shortlist

Ranked against the brief. Each with its strongest argument and its main risk.

1. **beermat.** The napkin image, kept: "the back of a beermat" is the
   everyday British phrase for a first rough plan. It reads as plain and
   crafty, works as `beermat@ai-pegboard` and `/beermat:scout`, and is free in
   every place checked. *The Beermat Entrepreneur* (Southon and West, 2002;
   third edition 2018) is a startup book about turning the first notes on a
   beermat into a business, which is a strong echo of the job. *Risk:* a pub
   rather than a coffee shop, and the book title is worth a trademark check
   before launch. README line: "beermat (noun): where a good idea gets its
   first honest sketch."
2. **bradawl.** The workshop's own word for testing before committing: the
   small awl that starts the pilot hole so the screw goes in straight. Free
   everywhere, nothing in the same space. *Risk:* an unfamiliar word to many,
   and it says "precision" more than "exploration".
3. **pilothole.** The same metaphor in plain words. Free everywhere. *Risk:*
   a compound word, and "pilot" echoes Copilot.
4. **offing.** "In the offing": what is coming into view on the horizon,
   which carries finding promising ground. Free everywhere. *Risk:* an obscure
   noun that reads as a verb form ("off-ing").
5. **scratchawl.** The awl that scribes the layout lines before the saw,
   crossing the workshop and drafting registers, with a "from scratch" echo.
   Free everywhere. *Risk:* awkward to say and to type.
6. **testpiece.** The scrap you cut to check the setup before the real board.
   Free everywhere. *Risk:* the plainest of the six, close to bland.

Napkin itself is out under the brief: an AI startup, a Claude Code skill and
an idea-to-blueprint engine for coding agents already use it.

## Pick

**coaster**, picked by Julien on 2026-10-29, after weighing it against
beermat. It keeps the napkin image Julien asked for, a sketch made over a
coffee chat, in a word that reads naturally outside the UK. Accepted
trade-offs: it has no idiom of its own, unlike "the back of a beermat"; it
shares its PyPI name with a small, active Flask library, which the family's
servo precedent tolerates; and "coasting" and "roller coaster" are side
meanings. Not trademark clearance.

README line: "coaster (noun): the card under your cup where an idea gets its
first honest sketch, before anyone builds anything."
