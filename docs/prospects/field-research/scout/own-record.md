# Scout source: the user's own record

Scouted 2026-10-20 and 2026-10-21 from Julien's sibling repositories during the
design session. Not one of the five lanes: the user's own past projects are a
source the pack did not plan for (see the dogfood note). Every repository cited
here is public: airlockjs, ai-pegboard, jig and shaper. Each entry links to the
files it rests on. On 2026-11-11 each entry was checked against those public
files: `OWN-01`, `OWN-03` and `OWN-07` were narrowed to what the files show,
and `OWN-02`'s quoted definition now matches ADR-0018's wording.

- **OWN-01** [grounded] airlock's vision and architecture were pre-seeded from a
  2026-08-25 brainstorm. The start prompt, committed with the seeded vision and
  architecture in the repository's first commit, is the earliest durable
  record; the brainstorm itself is not in the repository. — airlock
  [`START_PROMPT.md`](https://github.com/ramboz/airlockjs/blob/main/START_PROMPT.md)
  and its [first commit](https://github.com/ramboz/airlockjs/commit/d35fecf2acf4032a885d94a3dc7196e2de95a7f5),
  read 2026-10-20, rechecked 2026-11-11.
- **OWN-02** [grounded] airlock's definition of 1.0 changed on 2026-09-05 from
  "the public API is frozen" to "a developer can rewire a real site's
  TBT-dominant tags onto airlock with confirmed parity", recorded as a reframe
  decision with a corpus-wide re-baselining manifest, eleven days after
  kickoff. — airlock
  [ADR-0018](https://github.com/ramboz/airlockjs/blob/main/docs/decisions/adr-0018-reframe-onto-adoptable-one-point-oh.md),
  read 2026-10-20, rechecked 2026-11-11.
- **OWN-03** [grounded] airlock's classification of a real production stack,
  created 2026-08-31, was filed as research note R-007, in a series of
  engineering investigations such as worker egress and Alloy in a worker
  chamber, and described as deliberately beyond current scope until it became
  the 1.0 benchmark on 2026-09-07. — airlock
  [R-007](https://github.com/ramboz/airlockjs/blob/main/docs/research/R-007-real-prod-stack-breadth.md)
  and the [research-note index](https://github.com/ramboz/airlockjs/blob/main/docs/research/README.md),
  read 2026-10-20, rechecked 2026-11-11.
- **OWN-04** [grounded] Server-side tagging, an incumbent way to move tag work
  off the page, appears in airlock's corpus only in ADR-0019 and its critique;
  the vision's competitive landscape does not list it. — airlock
  [ADR-0019](https://github.com/ramboz/airlockjs/blob/main/docs/decisions/adr-0019-ga4-gtag-protocol-connector.md)
  (Option D), its
  [frame critique](https://github.com/ramboz/airlockjs/blob/main/docs/decisions/reviews/adr-0019-frame-critique.md)
  and the [product vision](https://github.com/ramboz/airlockjs/blob/main/docs/product-vision.md#competitive-landscape);
  search of airlock's `docs/`, 2026-10-20, repeated on the public repository
  2026-11-11.
- **OWN-05** [grounded] jig's vision-elicitation skill describes itself as a
  slim baseline and leaves deeper product-discovery facilitation to a richer
  user-installed skill, to which it defers by category. — jig
  [`skills/vision-elicitation/SKILL.md`](https://github.com/ramboz/jig/blob/main/skills/vision-elicitation/SKILL.md),
  read 2026-10-20, rechecked 2026-11-11.
- **OWN-06** [grounded] Name collision checks were done by hand in pegboard's
  ADR-0001 (2026-10-12) and in airlock's product vision (2026-08-25). —
  ai-pegboard
  [ADR-0001](https://github.com/ramboz/ai-pegboard/blob/main/docs/decisions/adr-0001-hub-marketplace-shape.md)
  and airlock's [product vision](https://github.com/ramboz/airlockjs/blob/main/docs/product-vision.md),
  read 2026-10-20, rechecked 2026-11-11.
- **OWN-07** [grounded] jig's research-notes convention (ADR-0054, 2026-08-11)
  covers open investigation before a decision is named. The notes live in a
  project's `docs/research/` and promote into that project's refinement-todo
  entries, ADRs or specs. — jig
  [ADR-0054](https://github.com/ramboz/jig/blob/main/docs/decisions/adr-0054-research-notes-artifact-convention.md),
  read 2026-10-20, rechecked 2026-11-11.
- **OWN-08** [grounded] shaper's release plans already record risks with a
  retirement path, and its release-check gives an advisory ship, cut scope,
  stop and re-shape, or extend call. — shaper
  [`templates/release-plan.md`](https://github.com/ramboz/shaper/blob/main/templates/release-plan.md)
  and
  [`skills/release-check/SKILL.md`](https://github.com/ramboz/shaper/blob/main/skills/release-check/SKILL.md),
  read 2026-10-20, rechecked 2026-11-11.
