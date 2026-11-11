---
prospect: field-research
date: 2026-10-21
---

# Naming: a field-research harness for project ideas

## Brief

Answers come from the session transcript; the `name` skill would ask the
unstated ones live.

- **What it does, in one line:** triages a project idea before anyone builds
  it: field research, six lenses, an opt-in challenge, a decision, a handoff.
- **Metaphor family or register:** a name that matches the pegboard and
  workshop terminology.
- **Brand feel:** unstated.
- **Language, root, or etymology to build on:** unstated. Two hooks surfaced
  while generating: the mining pair *prospect* (find the claim) and *assay*
  (test the ore), and Roman augury, the root of "inaugurate".
- **Constraints:**
  - fits beside jig, servo, shaper, gauge and an unreleased sibling pack.
    Observed pattern: one lowercase common noun of three to six letters, each
    README opening with a "(noun):" definition line;
  - avoids `scout`, a name Julien already uses for another tool;
  - reads well as `<name>@ai-pegboard` and as a skill prefix such as
    `/<name>:capture`.
- **Unstated:**
  - how much registry collision is acceptable. Family precedent: servo shares
    its name with the Servo browser engine, and jig is a common word;
  - where the name must be free. Pegboard's ADR-0001 checked GitHub, npm, PyPI
    and crates.io, so those were checked here.

## Candidates

| Name | The literal thing | What it carries here |
|---|---|---|
| assay | The test of an ore sample before mining | Test the idea before digging |
| bradawl | A small awl that makes the pilot hole for a screw | The smallest commitment that makes the real work go in straight |
| feeler | A feeler gauge, which measures gaps | Measures the gaps in what exists; "putting out feelers" tests interest |
| auger | A boring tool; a soil auger samples ground before building | Sample before you build; homophone *augur*, root of "inaugurate" |
| storystick | A carpenter's stick carrying every key measurement of a job | The dossier carries the idea's measurements into the build |
| centerpunch | Marks the spot so the drill bit does not wander | Decide where to drill before drilling |
| gimlet | A small tool for boring pilot holes | "Gimlet-eyed" means sharp, searching scrutiny |
| scratchawl | An awl for scribing layout lines | Lays out the work; "from scratch" |
| strop | A leather strap for honing an edge | Hardening the idea |
| froe | Splits rough timber along its grain | Finds the idea's natural shape |
| chalkline | Snaps a straight line before cutting | Lays out the path |
| whetstone | Sharpens a blade | Hardening the idea |
| plumb, plumbline | Checks true vertical; "to plumb" is to explore in depth | Depth and truth |
| trysquare | Checks a corner is true | Checks the idea is sound |
| sounding | Measures water depth before entering harbour | Look before you sail in |
| dibble | Makes a hole to plant a seedling | Plant the idea |
| prospect | Searching ground for a deposit | The working placeholder |

## Collision checks

_Checked 2026-10-21 by registry and GitHub API lookups plus web search. This
is not trademark or legal clearance._

| Name | npm | PyPI | crates.io | GitHub | Same-space products |
|---|---|---|---|---|---|
| assay | taken, test helper | taken, testing framework | taken, Rust test macro | org exists; 21 exact-name repos | an agent-native web QA CLI named assay; no idea-validation product found |
| bradawl | free | free | free | account exists, 0 repos; no repos | none found |
| feeler | taken, React UI lib, 2022 | free | free | 16 small repos | none in dev tools; consumer "feel" AI apps |
| auger | taken, readline helper | taken | taken, HTTP load tester | 18 repos, incl. an etcd tool and a unittest generator | none in idea triage |
| storystick | free | free | free | org exists, 0 repos; 3 empty repos | none found |
| centerpunch | free | free | free | free | none found |
| gimlet | taken | taken | free | 30 repos, incl. a Kubernetes deployment tool | dev-tool collision |
| scratchawl | free | free | free | free | not searched |
| strop | taken | free | taken | 3 repos | none checked |
| froe | free | taken, **a coding agent** | taken | 2 repos | **same space** |
| chalkline | taken | taken, **agent context tracking** | free | 35 repos, incl. **block/chalkline, "Snap a line before your agents build."** | **same space** |
| whetstone | taken, **Claude Code skills pack, 2026-07** | taken | taken | 35 repos, incl. an **AI agents toolkit** | **same space** |
| plumb | taken | taken | taken | **dbreunig/plumb, a spec-driven development tool** | **same space** |
| plumbline | taken | taken | taken | 46 repos, incl. **an LLM reliability analyzer** | **same space** |
| trysquare | free | free | free | **a coding-agent scenario harness** | **same space** |
| sounding | taken | free | taken | **an agent-instruction governance tool** | **same space** |
| dibble | taken, **agent guardrails and review loop** | free | free | 24 repos | **same space** |
| prospect | taken | taken | taken | 10 repos | not a workshop tool |

**Finding worth keeping:** the workshop register is crowded in AI agent tooling
as of October 2026. Eight of the seventeen candidates already name an agent,
spec-driven, or coding-agent tool. A workshop name needs a same-space check
before anything else.

## Shortlist

Ranked. Each with its strongest argument and its main risk.

1. **assay.** The best meaning fit, five letters, and it pairs with
   *Prospect* as the role word on the board: prospecting finds the claim,
   the assay tests the ore. README line: "assay (noun): the test that tells
   you whether the ore is worth mining." *Risk:* crowded registries and an
   adjacent agent QA tool with the same name; acceptable only if the servo
   precedent holds.
2. **bradawl.** Clean on every registry and on GitHub, with no product in the
   space. "The pilot hole that makes the screw go in straight" is a friendly,
   non-adversarial metaphor. *Risk:* an unfamiliar word, seven letters, and a
   metaphor about precision more than research.
3. **feeler.** Two meanings that both fit: a feeler gauge measures gaps, and
   putting out feelers tests interest. Free on PyPI and crates.io. *Risk:* it
   reads as "feelings" in search results, and it sits next to gauge on the
   board, which may confuse.
4. **auger.** Sampling the ground before building, plus the *augur* pun:
   Roman augurs read the signs before a venture began. *Risk:* taken on every
   registry, and the pun can read as a misspelling.
5. **storystick.** Clean everywhere, and the most honest description of the
   handoff: one stick carries every measurement into the build. *Risk:* ten
   letters, and it describes the handoff more than the research.
6. **centerpunch.** Clean everywhere; "decide where to drill before
   drilling". *Risk:* long, and "punch" sounds aggressive for a tool whose
   posture is encouragement.

## Pick

_Superseded._ A second naming pass, run from Julien's own brief on 2026-10-29,
ruled out the mining register (and with it "prospect" and "assay") and
picked **coaster**. See the [coaster naming file](../coaster/naming.md).
