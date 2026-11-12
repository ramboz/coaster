> Status: Draft (elicited)
>
> Decisions the initial setup explicitly deferred. Each item has a resolution trigger.
> Resolve by writing an ADR and linking it here.

# Refinement Todo: coaster

## Architecture

### ~~Decision: Tech stack~~ — RESOLVED 2026-11-09
~~**Deferred:** Markdown skills and standard-library Python helpers are recorded as locked in [architecture.md](architecture.md#tech-stack), but no ADR records them yet. Packaging is still open.~~
**Resolution trigger:** First spec that touches packaging. Record decision via an ADR.
**Resolved by:** [ADR-0001: Render a self-contained Claude package from neutral source](decisions/adr-0001-rendered-claude-package.md).

### Decision: Module boundaries
**Deferred:** Concerns are named in [architecture.md](architecture.md#module-boundaries). Spec 001 recorded the plugin manifest and the source-versus-package boundary there. Skills still couple through the dossier and relative paths, with no formal contracts between them.
**Resolution trigger:** First spec that introduces a contract between skills.

### Decision: Skill file access in claude.ai
**Deferred:** Whether a skill in a claude.ai plugin can read `skills/_shared/` and the root `templates/`, or each skill must carry its own copies. In Claude Code, [ADR-0001](decisions/adr-0001-rendered-claude-package.md) builds the text into each skill. Whether those self-contained skills also suit chat is untested.
**Resolution trigger:** R-02's chat-path run.

### Decision: Marketplace source form in claude.ai
**Deferred:** Whether `git-subdir` marketplace sources, which the pegboard's generated manifests use, install in claude.ai.
**Resolution trigger:** R-02's install step.

### Decision: grilling in chat
**Deferred:** Whether grilling's batched questions and sub-agent work in chat.
**Resolution trigger:** The first test of the grilling hand-off in a claude.ai Project.

### Decision: One brief for both research tools
**Deferred:** How to make a brief fit both a structured research brief and a one-line `/deep-research` question.
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

### Decision: The helpers' "don't ask again" exposure
**Deferred:** Answering "don't ask again" to a helper prompt saves `Bash(python3 *)`, which allows any Python command in the project. [ADR-0002](decisions/adr-0002-helpers-ask-for-bash.md) keeps jig's command form and warns users in the README and in `scout` and `name`. The in-session warning is not reliable: in 002-01's runs on `0.1.0-pre.8`, `name` ran its helper without it. The model's own inline `python3 -` edits, seen in several of 002-01's runs, would also run unprompted under that rule, so Option D removes only coaster's share of the exposure. Option D, executable helpers run by their own path, is the fallback.
**Resolution trigger:** An issue report of users accepting the broad rule, or the scope-4 release check before `v0.1.0`, whichever comes first.

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

### ~~Decision: "Nothing to install or run" as the lead claim~~ — RESOLVED 2026-11-11
~~**Deferred:** Whether the claim holds while the pack ships two optional Python helpers. Round 1's rival names a pack with no scripts as the line BMAD cannot match (`V-13`).~~
**Resolution trigger:** First packaging spec, or the next change to the positioning.
**Resolved:** spec 001 changed the line to "one plugin and nothing else to install or run", and the README calls the two helpers optional. Julien did not choose between the wordings offered, so this is the recommended default, and his go-ahead to publish covers it.

## Conventions

### Decision: Code style and linting
**Deferred:** No signal from the initial pitch.
**Resolution trigger:** First spec that produces non-trivial code, or first time inconsistency causes friction.

### Decision: Testing framework
**Deferred:** No signal from the initial pitch.
**Resolution trigger:** First spec that requires tests beyond ad-hoc verification.

## Operations

### ~~Decision: CI/CD setup~~ — RESOLVED 2026-11-11
~~**Deferred:** No CI yet. Spec 001 crosses a deploy boundary without it, and the privacy search, `--check` and the pre-release bump run by hand until then.~~
**Resolution trigger:** Scope 4 of the Claude Code first release, before the `v0.1.0` tag.
**Resolved by:** [spec 003](specs/003-commits-and-releases/spec.md). CI runs `--check`, plugin validation, the path search and a check of the subjects that land on `main`; release-please owns releases from `v0.1.0`. The publication term search, and the pre-release bump until `v0.1.0`, stay by hand.
