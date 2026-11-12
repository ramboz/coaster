---
slice: 002-04 — the hats as plugin agents
pass: compliance
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-12T18:01:24Z
prompt_source: review.py implementation, then a re-check by the same reviewer
---

Compliance pass on a re-check by the same reviewer, not a fresh review. The first pass, on `b6052c4`, returned needs-changes:
- each `f1s` hat prompt added "(lane files are under scout/ beside it)", outside AC 5's list, and the record had judged it allowed;
- the evidence did not name the commit the local build was made from;
- AC 4 waits on the push;
- `_part`'s bare `StopIteration`, and no ADR-0003 entry in `docs/architecture.md`.

Fixed: `challenge` now says each prompt holds the four items "and nothing else" (`cbe06fc`), and both runs were repeated from a `git archive` of `hosts/claude` at `cbe06fc`. All six prompts hold only the four items. The evidence names `b6052c4` and `cbe06fc`. `_part` exits with a named error. The architecture doc has an ADR-0003 section and the agents as a contract surface.

On re-check, ACs 1, 2, 3 and 5 are met, and AC 4 is met except for the push, which waits on Julien's go-ahead by design. One medium item: the evidence said "Five of the six made one `Glob` call inside the dossier's folder", and the trimmed listing showed only the patterns. The logs show each of those calls passed the dossier's folder as its `path`, or named it in its pattern, so the sentence stands. The listing now shows the folder. Reconciliation notes: log the tighten-and-rerun as a deviation; the brief's clearer split of link check and dossier changes; the `INTRO` line and `## Packaged: hats` heading in the agent layout; the brief's lane files; the `f2s` round's "not yet added" slip; and the `f2s` parent's compound Bash read, which ran.
