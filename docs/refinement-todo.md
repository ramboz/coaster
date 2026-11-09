> Status: Draft (elicited)
>
> Decisions the initial setup explicitly deferred. Each item has a resolution trigger.
> Resolve by writing an ADR and linking it here.

# Refinement Todo: coaster

## Architecture

### Decision: Tech stack
**Deferred:** Markdown skills and standard-library Python helpers are recorded as locked in [architecture.md](architecture.md#tech-stack), but no ADR records them yet. Packaging is still open.
**Resolution trigger:** First spec that touches packaging. Record decision via an ADR.

### Decision: Module boundaries
**Deferred:** Concerns are named in [architecture.md](architecture.md#module-boundaries); skills couple through the dossier and relative paths, with no formal contracts yet.
**Resolution trigger:** First spec that introduces a contract or interface.

### Decision: Skill file access in claude.ai
**Deferred:** Whether a skill in a claude.ai plugin can read `skills/_shared/` and the root `templates/`, or each skill must carry its own copies. In Claude Code, an assembled plugin found its template after a search in 3 of 3 runs on 2026-11-09.
**Resolution trigger:** R-02's chat-path run, or the first packaging spec.

### Decision: Marketplace source form in claude.ai
**Deferred:** Whether `git-subdir` marketplace sources, which the pegboard's generated manifests use, install in claude.ai.
**Resolution trigger:** R-02's install step.

### Decision: grilling in chat
**Deferred:** Whether grilling's batched questions and sub-agent work in chat.
**Resolution trigger:** The first test of the grilling hand-off in a claude.ai Project.

### Decision: One brief for both research tools
**Deferred:** How to make a brief fit both the deep-research skill's four fields and a one-line `/deep-research` question.
**Resolution trigger:** R-08's check of which skills a CLI-only session has.

### Decision: Research report into the dossier
**Deferred:** How a claude.ai Research report gets into the dossier without a manual download and upload.
**Resolution trigger:** R-02's chat-path run.

### Decision: Chat Project to repository
**Deferred:** How a chat Project's dossier reaches a repository in one step.
**Resolution trigger:** R-02's chat-path run.

### Decision: Activation on natural phrasing in chat
**Deferred:** How to make `capture` fire on natural phrasing without hooks in chat.
**Resolution trigger:** R-04's activation test, then R-02's chat-path run.

## Product

### Decision: Whether income matters
**Deferred:** Asked by `capture`, not answered. The Monetizable reading stays branched until it is.
**Resolution trigger:** One answer from Julien (R-07).

### Decision: Which alternatives to beat
**Deferred:** Spec Kit was named as something not to depend on, and nothing more was inferred.
**Resolution trigger:** Julien names one, or the side-by-side against the Deep Recon toolbox and the-researcher runs.

### Decision: Six skills or three
**Deferred:** The picked shape is six skills. The three-skill variant is held.
**Resolution trigger:** R-04's activation test.

### Decision: How the encouraging default reads
**Deferred:** Whether the encouraging default reads as the failure others design against.
**Resolution trigger:** R-05, asking the pitch's validator.

### Decision: What Free-plan users get
**Deferred:** What Free-plan users get, given that plugins in chat and Research are for paid plans.
**Resolution trigger:** R-10's check of a single-skill ZIP upload on Free.

### Decision: "Nothing to install or run" as the lead claim
**Deferred:** Whether the claim holds while the pack ships two optional Python helpers. Round 1's rival names a pack with no scripts as the line BMAD cannot match (`V-13`).
**Resolution trigger:** First packaging spec, or the next change to the positioning.

## Conventions

### Decision: Code style and linting
**Deferred:** No signal from the initial pitch.
**Resolution trigger:** First spec that produces non-trivial code, or first time inconsistency causes friction.

### Decision: Testing framework
**Deferred:** No signal from the initial pitch.
**Resolution trigger:** First spec that requires tests beyond ad-hoc verification.

## Operations

### Decision: CI/CD setup
**Deferred:** No signal that CI is set up.
**Resolution trigger:** First spec that crosses a deploy boundary.
