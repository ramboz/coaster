# Decisions

> Status: Draft (wizard-generated)
>
> Architectural Decision Records for coaster. Nygard convention: immutable
> after acceptance. New decisions supersede old ones — never edit an accepted ADR.

## Index

- [ADR-0001: Render a self-contained Claude package from neutral source](adr-0001-rendered-claude-package.md) — coaster's Claude Code package has to give each skill its templates and shared rules without relying on a runtime read of the plugin's own files. (2026-11-09, Accepted)
- [ADR-0002: Helpers ask for Bash like any other command](adr-0002-helpers-ask-for-bash.md) — ADR-0001 builds the packaged text into each skill, so reading it needs no permission. (Accepted)
- [ADR-0003: Run challenge's hats as plugin agents](adr-0003-hats-as-plugin-agents.md) — The packaged rules reached the hats intact in four runs of `challenge` out of five, so ADR-0001's kill criterion for the paste has fired. (Accepted)

## Format

Each ADR lives at `docs/decisions/adr-NNNN-<slug>.md`. Title: `# ADR-NNNN: <Title>`.

Required sections: Status, Context, Decision Options Considered, Recommended Decision, Consequences.

## When to write an ADR

- Hard-to-reverse decisions
- Decisions that affect multiple modules or the public API
- When a contract changes in a breaking way
- When the `architect` subagent produces a proposal that is accepted
