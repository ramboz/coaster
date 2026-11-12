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

For each lane the user wants, write a brief from `templates/research-brief.md`:
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
   most ten entries per lane, labeled as a quick pass in the ledger. It runs
   in the session and needs no other tool.
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
   its searches is `unverified` too.
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
   command in the project. Then run `python3 scripts/link_check.py <dossier-folder>`
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
