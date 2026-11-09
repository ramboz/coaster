---
slice: 001-02 — install from GitHub
pass: frame-critique
verdict: pass
reviewer: jig:reviewer
reviewed_at: 2026-11-09T23:54:55Z
prompt_source: review.py frame-critique, then two re-checks by the same reviewer
---

Sixth frame-critique round: pass, reached in three steps by one reviewer. A fresh reviewer first returned needs-changes: nothing established that the tree cleared by the review is the tree that goes public. After an amendment, the same reviewer found that finding substantially resolved but returned needs-changes because no one with authority had to approve `keep` findings. After a second amendment, the same reviewer returned pass. The two re-checks were not fresh reviews.

Non-blocking notes: private prose nobody flags stays an accepted residual (A3); terms narrowed to avoid matching the spec give no search backstop for findings whose only distinctive word the spec also uses; `keep` line numbers should cite `pre-publication`; and AC 8 is the first `git-subdir` install of this package, after the repository is public, which is recoverable with a pre-release bump.
