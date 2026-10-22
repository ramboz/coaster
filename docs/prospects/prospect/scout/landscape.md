# Scout lane: landscape

_Processed by `scout` on 2026-10-21 from [the report](reports/Lean%20idea%20triage%20skill%20landscape.md), produced by the
`anthropic-skills:deep-research` skill from [brief.md](brief.md). Entries are
`unverified` unless scout opened the source itself; those are marked
`grounded`. The report and its research notes stay untouched as the
long-form record._

## The draft-then-process loop

- **LND-01** [grounded] BMAD's Deep Recon already runs the loop: Draft writes a brief for the user's own research tool, Process turns a finished report into a cited summary, Run does the research in-session; it needs BMAD core under `_bmad/scripts` and `uv`. — [bmad-deep-recon SKILL.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-deep-recon/SKILL.md), accessed 2026-10-21 (also `FR:LND-36`, `FR:LND-37`).
- **LND-02** [unverified] Deep Recon's Process step extracts every claim as claim, source, publisher, publication date, access date, confidence and class, and spot-checks the load-bearing ones. — [process.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-deep-recon/references/process.md), via the report.
- **LND-03** [unverified] Deep Recon ~~was first committed on 2026-08-20~~ has been on BMAD's stable line since 2026-07-23; 2026-08-20 is a folder move (corrected by `V-04`, round 1). It has about 10,351 installs on skills.sh; BMAD also ships it in a `bmad-plugins` marketplace without a top-level `bin/`. — [bmad-plugins](https://github.com/bmad-code-org/bmad-plugins); [skills.sh search](https://skills.sh/api/search?q=deep-recon), via the report.
- **LND-04** [grounded] Outside BMAD, the closest lean tool is rohankgeorge/the-researcher, a brief builder plus a report checker: 2 stars, created and last pushed on 2026-07-20. — [the-researcher](https://github.com/rohankgeorge/the-researcher), accessed 2026-10-21.
- **LND-05** [unverified] No other prompt builder read has a Process step that turns a report into structured evidence for a later skill. — absence; searches listed in the report's absence table.

## Standalone idea validators

- **LND-06** [unverified] Almost every standalone validator runs its own web research rather than delegating it (ailabs-393, mathews-tom, viber, c0x12c, lorkinsey, AojiLi). — the SKILL.md files linked in the report.
- **LND-07** [unverified] The most-installed "idea" skill on skills.sh is addyosmani's `idea-refine` (55,762 installs), which refines an idea into a one-pager rather than judging it. — [idea-refine SKILL.md](https://github.com/addyosmani/agent-skills/blob/main/skills/idea-refine/SKILL.md), via the report.
- **LND-08** [unverified] Most validators advertise a blunt or anti-sycophantic stance; c0x12c says most ideas should get PASS or TEST MORE. — [c0x12c idea-validation](https://github.com/c0x12c/ai-toolkit/blob/master/.codex/skills/idea-validation/SKILL.md), via the report.
- **LND-09** [grounded] The skill name `idea-triage` is already taken, by forjd/tilezo, for auditing a project's ideas file. — [tilezo idea-triage SKILL.md](https://github.com/forjd/tilezo/blob/main/.codex/skills/idea-triage/SKILL.md), accessed 2026-10-21.
- **LND-10** [unverified] gstack's `office-hours` Builder mode acts as an enthusiastic collaborator for builders, the closest thing to an encouraging default, but it fails both claude.ai install checks (a 159-file `bin/`, non-spec fields). — [office-hours SKILL.md](https://github.com/garrytan/gstack/blob/main/office-hours/SKILL.md), via the report.
- **LND-11** [unverified] [absence] No idea-triage tool is encouraging by default with challenge only on request; no lean pack delegates research and hands off to build tools. — searches in the report's absence table.

## Grilling and challenge skills

- **LND-12** [grounded] mattpocock's `grilling` is standalone with spec-only frontmatter, ships in the `mattpocock-skills` plugin listed in Anthropic's official marketplace, and has 960,166 installs on skills.sh. — [grilling SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md); [claude-plugins-official marketplace.json](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json); [skills.sh search](https://skills.sh/api/search?q=grilling), accessed 2026-10-21.
- **LND-13** [grounded] The grilling maintainer takes no new skills and says workflows composed from grilling belong in the user's own skills, inviting people to publish their own. — [new-skills.md](https://github.com/mattpocock/skills/blob/main/.out-of-scope/new-skills.md), accessed 2026-10-21.
- **LND-14** [unverified] Users dislike grilling's batched rounds of ten or more questions, and the request to restore one-at-a-time was closed as not planned on 2026-10-06. — [mattpocock/skills#831](https://github.com/mattpocock/skills/issues/831), via the report.
- **LND-15** [unverified] grilling sends a sub-agent to look up facts, which claude.ai chat does not run. — [grilling SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), via the report.
- **LND-16** [unverified] Other standalone challengers exist: phuryn `strategy-red-team` (9,163 installs) and `pre-mortem` (10,105), addyosmani `interview-me` (53,882), jeffallan `the-fool` (4,286). — skills.sh searches linked in the report.
