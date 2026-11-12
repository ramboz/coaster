---
name: scout
description: >
  Gather field evidence for an idea in a prospect dossier, light-weight by
  design. Defers the research itself to any other installed skill whose
  description identifies it as handling deep, market, or competitor research,
  such as BMAD's Deep Recon; otherwise runs a quick pass with web search, or
  drafts a brief for Claude's Research mode or /deep-research. Then turns what
  comes back into the dossier's cited, dated evidence ledger: what exists, the
  gaps, what does not exist yet, demand, enabling technology, how comparable
  things make money, and how people adopt them. Use when the user says "scout
  this idea", "scout the field", "what's out there for this idea", "has this
  been done", or brings back a research report for the dossier. Do not use for
  engineering research on how to build it, for name collisions (use name), or
  for business plans and pricing.
---

# scout

Scout does not compete on research depth. It decides what to ask, lets a
richer research skill or tool do the asking when one is available, runs a
quick pass when none is, and turns what comes back into evidence the dossier
can trust. Readings come later, in `frame`.

## Lanes

Five lanes, each optional. Offer them and let the user pick.

| Prefix | Lane | Looks for | Feeds |
|---|---|---|---|
| `LND` | **Landscape** | Direct competitors, adjacent tools, open-source projects, substitutes including manual methods and "do nothing". End with the gaps in what exists and what does not exist yet. | Open |
| `DEM` | **Demand** | Who asks for this, complains, pays, or hires for it: forum threads, issue trackers, reviews of incumbents, job posts, search interest. Also lost causes: who tried, what happened, and why. | Wanted |
| `ENB` | **Timing & enablers** | What changed recently: platforms, APIs, regulation, prices, behaviour. Which enabling pieces exist, are emerging, or are missing, and their terms and platform risk. | Timely, Feasible |
| `MON` | **Money** | How comparable products and projects make money or sustain themselves: model types, not price planning. Note where the user's stated constraints rule a model out. | Monetizable |
| `RCH` | **Reach** | Who adopts and who decides, where they gather, which channels and marketplaces carry tools like this, and the switching costs people describe. | Adoptable |

Four rules shape every brief:

- **Search for the claimed difference.** If the hunch claims something is
  new, such as a posture, a surface, or a combination, the landscape brief
  asks for it explicitly, and for the searches behind any "nothing does this".
- **Name the closest rival per gap**, not only the best-known incumbent.
- **The user's own record is a sixth source.** Past projects, notes, and
  repositories the user points to. Scout reads those directly, tags them
  `OWN`, and cites them in general terms if the dossier may be shared.
- **An earlier dossier on the same idea is part of that record.** After a
  pivot, cite it as `OWN` and brief only the lanes the pivot changes. Say
  which lanes were carried over rather than re-scouted.

## 1. Draft

For each lane the user wants, write a brief from the `## Packaged: research brief template` section:
the idea in a paragraph taken from Intent, the lane's questions, the claimed
difference to search for, what counts as evidence, and the exact output
format. One brief can cover several lanes when the tool takes long prompts.
A quick pass uses the same questions to guide its searches. When the brief
goes to the user, give it as a block they can copy. In a repository, every file
scout writes, briefs included, goes in the dossier's own folder: a brief as
`scout/brief-<lanes>.md` next to the dossier.

## 2. Run

If the user asks for a particular option, such as the quick pass, take it.
Otherwise take the first option that applies.

1. **A richer research skill is installed.** If a skill in this session says
   it handles deep, market, or competitor research, such as BMAD's Deep Recon,
   a deep-research skill, or a research skill, hand it the brief. If Claude
   can call it, call it. If only the user can start it, give them the line to
   send. Then process what it returns.
2. **Otherwise, a quick pass, by default.** A few web searches per lane, at
   most ten entries per lane, counting every entry, absences included,
   labeled as a quick pass in the ledger. It runs in the session and needs no
   other tool.
3. **The deeper option, on request.** Offer the brief for the user's own
   research tool:
   - **claude.ai:** only the user can turn Research mode on, per chat, on paid
     plans. Give them the brief to paste into a new chat in the same Project.
   - **Claude Code's `/deep-research`:** only the user can start it. Give them
     the brief's one-line question, plus the brief's path.
   - **Any other deep-research tool** the user prefers.

**Say what it costs first.** Research mode runs on Opus and uses limits faster
than a normal chat; on a Pro plan one run can take most of a session, so offer
one lane per run. A deep-research run in Claude Code fans out its own agents.
Claude and Claude Code share one usage allowance.

## 3. Process

When the report comes back, pasted, attached, or as a file. If the tool also
left structured notes, such as per-question findings with their sources,
extract from those: a narrative report loses qualifiers. If a richer skill
returns its own claims ledger, such as Deep Recon's, map each claim into an
entry with the lane's prefix. Leave the report, notes, and ledger untouched
as the long-form record.

1. **Extract** one entry per claim, with the lane's prefix and the next free
   number. A claim is `grounded` only once its source has been opened and says
   it, qualifiers included. Until then it is `unverified`. An absence without
   its searches is `unverified` too, and something not searched at all is a
   gap to note in step 4, not an entry.
2. **File the entries.** In chat, under a heading per lane inside the one
   dossier artifact. In a repository, in `scout/<lane>.md`, plus one index line
   per load-bearing entry in the dossier's Evidence section. Create and edit
   files, the dossier included, with the file tools, which make the `scout/`
   folder as needed, not with a shell command or an inline script. Never copy
   or renumber entries.
3. **Check the links**, once the entries are filed, so the check sees them.
   Research tools invent or misattribute part of their citations, so this step
   is never skipped. In chat, open the sources behind the load-bearing claims.

   In Claude Code, first tell the user that if Claude Code asks, they should
   answer Yes rather than "don't ask again", which would allow any Python
   command in the project. Then run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scout/scripts/link_check.py" <dossier-folder>`
   exactly as written, without listing or reading the plugin's own folder, and
   record the result in the Evidence section.

   If the helper is refused, try no other command to the same end, such as
   `curl` or an inline script, because the user declined running code. If it is
   refused or fails and web tools are allowed, open the sources behind the
   load-bearing claims instead, as in chat, and say in the Evidence section that
   the links were checked on the web. Otherwise record the link check as "not
   run", with the reason and the command to run by hand. Never record a result
   that no tool returned.
4. **Note the gaps in the report**: lanes it skipped, sources it could not
   read, questions it did not answer. Frame needs to know what was not looked
   at.

Every entry follows the `## Packaged: evidence rules` section. Record evidence against the
hunch with the same care as evidence for it, and keep readings out of the
ledger.

## Output

- lanes drafted, run and processed, and the tool that ran them;
- entries added, and the three that surprised you most;
- notable absences with their searches;
- the link-check result;
- set `status: scouted` and `last_scouted`;
- suggest `frame` next.

Each `## Packaged:` section below runs to the next `## Packaged:` heading or the end of this file.

## Packaged: research brief template

````markdown
# Research brief: <idea>, <lane or lanes>

_Paste this into Claude's Research mode, Claude Code's `/deep-research`, or
another deep-research tool. Bring the full report back to `scout`._

## One line

<A single question built from the objective, for tools that take only one
line, such as Claude Code's `/deep-research`.>

## Objective

<What the dossier needs from this research, and which lenses it feeds.>

## The idea

<One paragraph from the dossier's Intent, in the user's words where
possible.>

## What to find out

1. <The lane's questions, one per line.>

## Suggested sources

- <Types of source to prioritize: product pages, repositories, docs, threads,
  registries.>

## Search specifically for

- <The claimed difference, for example: "an idea-triage tool that is
  encouraging by default, with challenge only on request".>
- The closest existing tool for each gap you find.

## Constraints and what counts as evidence

- <Any bounds: dates, regions, surfaces.>

- Primary sources first: the product's own pages, the repository, the thread
  itself, the filing.
- Evidence against the idea, with the same care as evidence for it.
- Nothing from memory alone. Every claim needs a source retrieved in this run.

## Output format

One claim per line, each with:

- the claim, in one sentence;
- the source title and link;
- the publication date, if known.

For every "nothing does X", list the searches you ran and where. End with what
you could not read or verify.
````

## Packaged: evidence rules

# Evidence hygiene

> Shared by every skill. These are the only hard rules in the pack, and none
> of them slows the user down: they keep enthusiasm and evidence in separate
> columns, and they make sure nothing the user decides is lost.

## Three voices, kept apart

A dossier holds three kinds of text. Never blend them.

| Voice | Section | Rule |
|---|---|---|
| **Intent** | `## Intent` | The user's own words. Quote, never paraphrase. Markdown structure is the only edit allowed. |
| **Evidence** | `## Evidence` | Facts about the world, each with a provenance tag, and a source and date where the tag needs one. |
| **Readings** | `## Readings`, `## Shape options` | Judgment. Labeled as such, and it cites the evidence it rests on by ID. |

A thing the user states as fact about the world ("nobody does this", "X has
a million users") goes to Evidence tagged `reported`, not into Intent.

## Ledger entry format

```markdown
- **LND-07** [grounded] One-sentence claim in your own words. — [Source title](https://example.com/page), accessed 2026-10-21.
```

IDs carry the source's prefix so nothing is ever renumbered:

| Prefix | Source |
|---|---|
| `E` | entries written straight into the dossier, such as `reported` facts at capture |
| `LND`, `DEM`, `ENB`, `MON`, `RCH` | the five scout lanes: landscape, demand, timing & enablers, money, reach |
| `OWN` | the user's own record: their past projects, notes, repositories |
| `S`, `V`, `C` | challenge hats: skeptic, rival, customer |
| `F` | field notes from conversations with real people |

The full entries live in the lane and round files. The dossier's Evidence
section is an **index** of the entries the readings rest on, one line each,
grouped by lane, with a link to every lane file.

Provenance tags:

| Tag | Meaning | Needs |
|---|---|---|
| `grounded` | You opened the source and it says this. | link + access date |
| `field` | A real person said it in a conversation or a reply. | who (role, not name, if the dossier may be shared) + date |
| `reported` | The user says so; not yet checked. | date |
| `unverified` | Seen second-hand (a search snippet, a summary) but not opened. | link + date |
| `absence` | A claim that something does **not** exist. | what was searched, where, and the date |

Rules:

- **IDs are append-only.** Never renumber or reuse an ID. Each source takes
  the next free number under its own prefix.
- **Contradictions are struck, not deleted.** `~~E-04 …~~ contradicted by
  E-19` keeps the history readable.
- **Absence is evidence too, and the most fragile kind.** "Nothing does X"
  needs the searches behind it. Treat it as a claim to re-check, not a fact.
- **Balance.** Record evidence that cuts against the hunch with the same care
  as evidence for it, and without commentary. Commentary belongs in Readings.
- **Reports from research tools are leads until opened.** A claim imported
  from Research mode, `/deep-research`, or any other tool is `unverified`
  until its source is opened and says it.
- **Check the links before reading the evidence.** In Claude Code, run
  scout's `link_check.py` helper on the dossier folder and record the result
  in the Evidence section. A resolving link only proves the page exists; a
  quote still has to match its source, qualifiers included.
- **Quote sparingly.** Paraphrase sources. A direct quote stays under fifteen
  words, in quotation marks, with attribution.
- **Freshness.** Set `last_scouted` in the dossier's frontmatter. When a
  reading rests on evidence older than about six months in a fast-moving
  field, say so in the reading and suggest a re-scout. It is a nudge, never
  a gate.
- **Local-only material.** Private repositories, customer names, and raw
  transcripts stay out of a dossier that may be shared. Refer to them in
  general terms ("a real customer site") and keep the raw file gitignored.
