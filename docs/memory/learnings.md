# Learnings

> Status: Draft (wizard-generated)
>
> Dead ends, failed approaches, and "we tried X and here's why it didn't work."
> The institutional memory that ADRs don't capture — these are not decisions,
> they're anti-patterns and gotchas discovered in practice.
>
> Update via `/jig:memory-sync` during reconciliation.

<!-- Learnings below. Format: ## Title, followed by what happened and what to do instead. -->

## A refused read can degrade a skill without any error

A headless `capture` run was refused the plugin's own template, carried on, and wrote 9 of the template's 22 headings without reporting a problem. An earlier 3 of 3 result had hidden this because those runs were granted `Read`. Test a skill with no `--allowedTools` grant and check `permission_denials` in the result, not the model's summary.

## Write searches for private strings so they cannot match themselves

A check for a home path written literally in a spec matches the spec once it is pushed. Use a bracketed form in the pattern, such as `[r]amboz`. Run the search over every review sidecar too, since jig's `reviews/.candidates/` files hold absolute paths and are git-ignored for that reason.
