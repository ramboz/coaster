# Lightweight Decisions

> Status: Draft (wizard-generated)

Small shipped decisions that fall outside spec slices but carry durable rationale:
brand/icon swaps, cosmetic CSS polish, UI string or translation choices, scoped
visual decisions, and "future sessions should/should not override this" notes.

## Routing rubric — where does this decision land?

Triage each settled decision to exactly **one** home:

| Route | Criterion |
|---|---|
| **ADR** | A load-bearing design choice with rejected alternatives — one a future agent would need to know about to avoid undoing it — warrants an ADR even when it changes no module boundary or public contract. Also: any change to a module boundary, public contract, or cross-cutting policy. |
| **Lightweight record (here)** | Settled, local, bounded (one screen / component / string / asset), with no real rejected alternatives — and a future agent would need to know it to avoid undoing it. |
| **`refinement-todo.md`** | Still *open* — has a resolution trigger; not shipped yet. |
| **Drop (write nothing)** | Ephemeral / trivial / already obvious from the code or a commit message. |

The **ADR** row's trigger sentence is single-sourced — the *same* wording appears
in both reconcile checklists and the memory-sync session-end prompt, so the "when
is an ADR required?" policy can't drift across surfaces.

Record a lightweight entry with the helper (idempotent append):

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/memory-sync/decisions.py" add-lightweight \
  --title "<short title>" --decision "<what>" --context "<why>" --scope "<where>"
```

## Template

```markdown
### [Date] — [Short title]

**Decision:** _what was decided_

**Context:** _why — constraint, user feedback, design call_

**Scope:** _which screen / component / string / asset — not product-wide_

**Commit:** _optional — git SHA or PR; may be added retroactively_
```

This matches what `decisions.py add-lightweight` emits (one blank line between
fields), so the documented shape and the helper output agree.

---

## Entries

### 2026-11-12 — A hat prompt may say where the dossier's own files are

**Decision:** Under ADR-0003's list of what a hat's Agent prompt may hold, a note that only says where the dossier's own files are, such as its lane files, counts as part of the dossier path. A note that states a rule, limit, lens instruction or reply shape still breaks the list. ADR-0003 stands.

**Context:** In slice 002-02's installed Sonnet run, the parent added a lane-file note to every hat prompt after challenge was told to add nothing else, the second Sonnet run of three to do so. ADR-0003's remedy line would reopen Option F1 on such a recurrence. Julien ruled on 2026-11-12 that the note adds nothing the list guards against, so it is allowed and recorded.

**Scope:** The release check on challenge's hat prompts (ADR-0003; slice 002-02's AC 6)

### 2026-11-12 — A self-describing off-list evidence tag is a recorded slip

**Decision:** A hat's evidence entry whose tag is not one of the five, but whose own text names its provenance and carries the fields that provenance needs, is a format slip that is recorded, not a failure of the hats' rules. An untagged entry, or one that claims more than its source supports, still fails.

**Context:** In slice 002-02's installed Sonnet run, the Skeptic tagged S-01 [grounded-lead, unverified until opened], and the entry said it stays unverified, with links and a date. Julien ruled on 2026-11-12 to allow and record it.

**Scope:** Judging hat replies against the evidence rules (slice 002-02's AC 4)
