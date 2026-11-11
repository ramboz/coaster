# Release Plan: coaster, Claude Code first release

## Status

`candidate`

Allowed statuses: `candidate`, `committed`, `shipping`, `shipped`, `dropped`.
Do not move a plan from `candidate` to `committed` without an explicit user
decision.

## Problem / Baseline

- Current baseline: A six-skill draft has run twice on its own idea, and 13 of its 36 lane entries are `grounded`. jig is scaffolded, and the vision and architecture are elicited. On 2026-11-09 the repository had no GitHub remote, tag, plugin manifest, licence, changelog or CI. A plain plugin copy of the skills passed `claude plugin validate --strict`, and `capture` wrote a correct dossier from its template in 3 of 3 Claude Code runs. The chat path has never been run.
- Problem this release addresses: coaster exists only as a local draft, so nobody can install it. The goal is to release coaster alongside jig, servo, shaper and the rest of the family.
- Why now: The gap is open today, in packaging, defaults and breadth rather than capability. BMAD's standalone toolbox plugin still needs `uv` (`S-01`, `V-01`), and the window narrows if that changes or BMAD reaches claude.ai (`V-08`, `V-10`).

## Appetite

- Time or attention this release is worth: One or two sessions.
- Fixed constraints: Claude Code only; an initial proof of concept against Claude alone is fine. Time is fixed, and scope gets cut to fit it.
- Variable scope: Scope 3, deferral to richer skills, is the first to cut if time runs out.

## Solution Outline

- Proposed shape: The six existing skills, packaged as a Claude Code plugin from a public GitHub repository and listed in the ai-pegboard catalog.
- Main user-facing path: Add the marketplace, install coaster, and run the loop from `capture` to `handoff` on a new idea.
- Important non-goals: The claude.ai chat path, Codex and Copilot wait for later releases.

### Vertical Scopes (delivery order)

Ordered thinnest-demoable-path-first. Each scope must deliver end-to-end,
demoable value on its own (not "just the data model" / "just the parser").

1. Install and capture. Add coaster's marketplace from GitHub in Claude Code, install it, run capture in an empty repo, and get a correct dossier.
2. The whole loop, installed. Run capture through handoff on the next real idea, with the helpers working from the plugin.
3. Deferral to richer skills. Hand off to grilling and to an installed research skill, and the dossier still gets updated (R-03).
4. Public release. Tag v0.1.0 and install it through the ai-pegboard catalog.

## Risks / Rabbit Holes

- Risk: Descriptions overlap with Deep Recon, Forge Idea and grilling (R-04).
  - Why it matters: Overlap, not count, drives wrong selection (`S-06`), and a new pack's descriptions drop first (`RCH-03`). The result could reopen six skills or three.
  - Retirement path: Ten natural prompts under `claude plugin eval`, with grilling and the BMAD toolbox installed; costs in `/skill-doctor`.
- Risk: The grilling hand-off loses the challenge's flow or its posture (R-03).
  - Why it matters: Nested calls return to the main session (`ENB-06`), and grilling interviews relentlessly (`C-07`).
  - Retirement path: In Claude Code, hand off to grilling with and without the hats' rules, and check the dossier still gets updated.
- Risk: Deep Recon's toolbox drops its `uv` dependency, or BMAD V7 ships (R-01).
  - Why it matters: The loop's packaging gap closes completely.
  - Retirement path: Install `bmad-toolbox` in a clean folder with no BMAD setup, run Draft then Process on the coaster dossier's report, and note what breaks.
- Risk: The one hop that skips the user may exist only in this setup (R-08).
  - Why it matters: No public source lists the deep-research skill (`S-04`).
  - Retirement path: Ask a CLI-only Claude Code session which skills it has.
- Risk: Discovery (R-06).
  - Why it matters: Installs concentrate and authors get no data (`RCH-06` to `RCH-09`).
  - Retirement path: List in the pegboard and the community marketplace; write the essay.

The full register, R-01 to R-10, is in the [dossier](../prospects/coaster/dossier.md#risks-worth-retiring). The chat-only risks, R-02, R-09 and R-10, move with the chat path.

## No-Gos

- This release will not:
  - run in the claude.ai chat path;
  - ship for Codex or Copilot;
  - depend on a framework or mega pack;
  - add a research engine of its own;
  - cover business plans, pricing, product tiers, subscriptions, operating costs or pitch decks;
  - do engineering research;
  - become a CRM or lead tool, or an idea backlog;
  - gate any lens;
  - run the challenge unprompted;
  - issue verdicts on the idea.

## Cutline

### Include

| Item | Evidence | Rationale |
|---|---|---|
| Install and capture (scope 1) | An assembled plugin passed strict validation and `capture` worked in 3 of 3 runs, 2026-11-09 | The thinnest demoable path |
| The whole loop, installed (scope 2) | UC-1 to UC-6 and UC-9 to UC-11 | The value is the breadth of the workflow |
| Public release (scope 4) | The ai-pegboard catalog pins a tag and SHA | The point of this release |
| LICENSE, CHANGELOG, CI and a real CODEOWNERS owner | Absent on 2026-11-09 | Needed once the repository is public |
| The README says the chat path is untested | Julien's decision, 2026-11-09 | Keeps the claims to what has been run |

### Defer

| Item | Evidence | Rationale |
|---|---|---|
| claude.ai chat path (R-02), UC-7 and UC-8 | Julien's decision, 2026-11-09; never run | It becomes the next release |
| R-09 and R-10 | Both depend on the chat path | They move with it |
| Codex and Copilot | Planned for later, as v1 | Claude first |
| Three-skill variant | Held until R-04 | Returns only if the activation test calls for it |
| R-01, the BMAD toolbox test | Not a ship criterion | It does not block an install; run it if time allows |
| Community marketplace listing and the essay (R-06) | Not in the delivery order | The pegboard listing comes first |

### Split

| Item | Evidence | Rationale |
|---|---|---|
| Packaging | Whether chat needs shared files inside each skill is unknown (refinement-todo) | Package for Claude Code now; chat bundling goes with the chat release |

### Risk-First

| Item | Evidence | Rationale |
|---|---|---|
| Review `docs/prospects/` before the repository goes public | Research notes held local paths and paraphrases of a non-public skill; `own-record.md` turned out to cite only public sources | Scope 1 publishes the repository, so this comes first |
| R-04 activation test | `S-06`, `V-02`, `RCH-03` | Its result can change the shape, so it lands before the tag |

## JIG Handoff

- Candidate JIG specs or slices: None yet. Only the seeded `000-adopt-jig` exists.
- New JIG work to draft: Spec `001` for scope 1, install and capture. At this appetite the later scopes may not need specs of their own.
- Patch-ready instructions, if any: None.
- Non-mutating notes: This plan changes no jig status. The scopes serve UC-1 to UC-6 and UC-9 to UC-11.

### Architecture appetite

A leanness ceiling jig reads before drafting specs. Appetite / no-gos /
spike pointer only — shaper never names an ADR, module boundary, mechanism,
or design; jig decides those. This is the prospective half; jig's
leanness/YAGNI review lens is the retrospective complement, enforced at jig
review — not here.

- Investment posture (upper bound — "at most", never "at least"): At most what the sibling packs spent on packaging, with no new dependencies.
- Over-investment no-gos (over-builds to refuse): No bespoke plugin framework or build system, apart from the one rendering script Julien accepted on 2026-11-09 (spec 001); No runtime dependencies for users of the pack; No test harness for the Markdown skills beyond plugin validation and the activation test.
- Spike (architectural risk to retire early): Whether a claude.ai skill can read files outside its own folder.

## Release-Check Criteria

- Before this release can ship:
  - `claude plugin validate --strict` passes on the package.
  - A fresh install from GitHub runs the whole loop.
  - R-04's activation test has a result, and the six or three call is made.
  - A `challenge` run's log shows each hat received the packaged rules intact.
  - LICENSE, CHANGELOG and CI are in place, and CODEOWNERS has no placeholder.
  - `docs/prospects/` has been reviewed before going public.
  - The README says the chat path is untested.
- Evidence to inspect: The plugin validation output, a dossier from the installed run, the `claude plugin eval` result, and a trimmed comparison of the hat prompts with the packaged rules.
- Known missing signals: No servo signals were found; release-check criteria remain advisory.

_Last shaped: 2026-11-09_
