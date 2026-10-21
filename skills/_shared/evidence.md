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
  `skills/scout/scripts/link_check.py <dossier-folder>` and record the result
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
