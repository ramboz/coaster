---
name: scout
description: >
  Gather field evidence for a captured idea using research tools the user
  already has. Draft a research brief per lane, hand it to Claude's Research
  mode, Claude Code's /deep-research or any deep-research tool, then process
  the report into a cited, dated evidence ledger: what exists, the gaps, what
  does not exist yet, demand, enabling technology, how comparable things make
  money, and how people adopt them. Use when the user says "scout this",
  "what's out there", "who else does this", "has this been done", "find
  competitors", "research the market for", or brings back a research report
  to process. Do not use for engineering research on how to build it, for
  name collisions (use name), or for business plans and pricing.
---

# scout

Scout does not run its own research engine. It decides what to ask, hands the
asking to a research tool the user already has, and turns what comes back
into evidence the dossier can trust. Readings come later, in `frame`.

## Lanes

Five lanes, each optional. Offer them and let the user pick.

| Prefix | Lane | Looks for | Feeds |
|---|---|---|---|
| `LND` | **Landscape** | Direct competitors, adjacent tools, open-source projects, substitutes including manual methods and "do nothing". End with the gaps in what exists and what does not exist yet. | Open |
| `DEM` | **Demand** | Who asks for this, complains, pays, or hires for it: forum threads, issue trackers, reviews of incumbents, job posts, search interest. Also lost causes: who tried, what happened, and why. | Wanted |
| `ENB` | **Timing & enablers** | What changed recently: platforms, APIs, regulation, prices, behaviour. Which enabling pieces exist, are emerging, or are missing, and their terms and platform risk. | Timely, Feasible |
| `MON` | **Money** | How comparable products and projects make money or sustain themselves: model types, not price planning. Note where the user's stated constraints rule a model out. | Monetizable |
| `RCH` | **Reach** | Who adopts and who decides, where they gather, which channels and marketplaces carry tools like this, and the switching costs people describe. | Adoptable |

Three rules shape every brief:

- **Search for the claimed difference.** If the hunch claims something is
  new, such as a posture, a surface, or a combination, the landscape brief
  asks for it explicitly, and for the searches behind any "nothing does this".
- **Name the closest rival per gap**, not only the best-known incumbent.
- **The user's own record is a sixth source.** Past projects, notes, and
  repositories the user points to. Scout reads those directly, tags them
  `OWN`, and cites them in general terms if the dossier may be shared.

## 1. Draft

For each lane the user wants, write a brief from `templates/research-brief.md`:
the idea in a paragraph taken from Intent, the lane's questions, the claimed
difference to search for, what counts as evidence, and the exact output
format. One brief can cover several lanes when the tool takes long prompts.
Give the user the brief as a block they can copy.

## 2. Run

The user runs the brief in the tool that fits:

- **claude.ai:** Research mode on paid plans, in a new chat in the same
  Project. On a free plan, a regular chat with web search, one lane at a time.
- **Claude Code:** `/deep-research` with the brief.
- **Any other deep-research tool** the user prefers.

Say what it costs before they start: a deep-research run takes minutes and a
real share of a plan's usage allowance, which Claude and Claude Code share.

If the user would rather not run a separate tool, offer a **quick pass**: a
few web searches per lane, at most ten entries, labeled as a quick pass in the
ledger.

## 3. Process

When the report comes back, pasted, attached, or as a file:

1. **Extract** one entry per claim, with the lane's prefix and the next free
   number. A claim is `grounded` only once its source has been opened and says
   it, qualifiers included. Until then it is `unverified`. An absence without
   its searches is `unverified` too.
2. **Check the links.** In Claude Code, run `scripts/link_check.py
   <dossier-folder>`. In chat, open the sources behind the load-bearing claims.
   Research tools invent or misattribute part of their citations, so this step
   is never skipped. Record the result in the Evidence section.
3. **File the entries.** In chat, under a heading per lane inside the one
   dossier artifact. In a repository, in `scout/<lane>.md`, plus one index line
   per load-bearing entry in the dossier's Evidence section. Never copy or
   renumber entries.
4. **Note the gaps in the report**: lanes it skipped, sources it could not
   read, questions it did not answer. Frame needs to know what was not looked
   at.

Every entry follows `../_shared/evidence.md`. Record evidence against the
hunch with the same care as evidence for it, and keep readings out of the
ledger.

## Output

- lanes drafted, run and processed, and the tool that ran them;
- entries added, and the three that surprised you most;
- notable absences with their searches;
- the link-check result;
- set `status: scouted` and `last_scouted`;
- suggest `frame` next.
