> Status: Draft (wizard-generated)
>
> **Changes to this file require explicit human approval.**
> Set `JIG_CONVENTIONS_APPROVED=1` in your shell session before editing, or the
> spec-gate hook will block the edit.

# Conventions: coaster

> Each rule below uses the format: **Rule** → **Why:** → **How to apply:**.
> Add rules as the project encounters real decisions worth recording.

## Documentation

**Rule:** Every wizard-generated doc carries a `Status: Draft (wizard-generated)` marker at the top.
**Why:** Distinguishes generated stubs from deliberate content, so reviewers and agents know what is authoritative.
**How to apply:** scaffold-init adds this marker. Flip it to `Status: Stable` after 3–5 reconciled specs have validated the doc structure (via a `scaffold-stable` ADR).

**Rule:** Deferred decisions are explicit, not silent.
**Why:** Silent gaps get forgotten. Explicit `Deferred` markers turn unknowns into trackable items.
**How to apply:** Use a `> **Deferred — <reason>.**` blockquote in the section. Add a corresponding entry to `docs/refinement-todo.md` with a resolution trigger.

## Decisions

**Rule:** Accepted decision records are append-only — never erased. Once a record
in `docs/decisions/` is `Accepted`, correct it by striking the stale wording
(`~~old~~`) with a date and reason, or by superseding it with a new record
(`Supersedes: ADR-NNNN`) — never by deleting or overwriting the original. A
`Proposed` / draft record is still a working draft: edit its body inline.
**Why:** `docs/decisions/` is the audit trail of *why* the project is shaped the
way it is. When superseded reasoning is silently swapped for its replacement, a
later reader cannot tell carefully established reasoning from a quiet edit, and
the record stops being trustworthy — especially when an option was rejected *on*
the reasoning that got erased. A draft record carries no such trail yet, so
locking it down only invites churn.
**How to apply:** While a record is `Proposed` / draft, edit freely. Once it is
`Accepted`, treat its body as immutable: strike-and-date, or open a superseding
record. Git history is the deep audit trail; the struck-through prose is the
one a reader sees without digging.

## Specs

**Rule:** Every non-trivial change starts with a spec, SPIDR-split into vertical slices.
**Why:** Specs as contracts at the right granularity let humans and agents work in parallel without constant re-alignment.
**How to apply:** Run `/jig:spec-workflow` (when implemented), or write `docs/specs/NNN-<slug>/spec.md` by hand using the SPIDR template. Each slice must touch the user-facing layer (no horizontal phasing).

## Code style

> **Deferred — no signal from initial pitch.** Will be filled in as the project
> encounters style decisions worth recording. Each addition follows the
> Rule/Why/How format above.

## Testing

> **Deferred — no test framework decided yet.** Will be filled in once the first
> spec requires tests beyond ad-hoc verification.

## Git

**Rule:** Every commit that lands on `main`, by pull request or by a direct
push, is a Conventional Commit, `<type>(<scope>): <subject>`. The type is
one of `feat`, `fix`, `perf`, `docs`, `chore`, `refactor`, `test`, `build`
or `ci`; the scope is required; the subject starts lowercase and does not
end with a period. Pull requests are squash-merged, the only merge the
repository allows, with the PR title as the subject and an empty body, so
the PR title is the commit that lands. `.github/workflows/pr-title.yml`
checks the title on every PR, and `.github/workflows/ci.yml` checks every
subject pushed to `main`, after the fact. Do not edit the subject in the
merge dialog. Commits on a branch use the same form.
**Why:** release-please reads the subjects on `main` to choose the next
version and to write `CHANGELOG.md`, as in jig and servo. A subject it cannot
parse is left out of both.
**How to apply:** Write the PR title in this form; it is the subject that
lands. `feat` bumps the minor version; `fix`, `perf` and `docs` bump the
patch; `chore`, `refactor`, `test`, `build` and `ci` release nothing on their
own. A `!` after the scope or a `BREAKING CHANGE:` footer bumps the major
version. Until `v0.1.0`, every change to the package's bytes still bumps the
pre-release number in both `plugin.json` files by hand; from `v0.1.0` on,
release-please owns the version and nobody edits it by hand. Branch names
stay open. `CONTRIBUTING.md` has the long form.
