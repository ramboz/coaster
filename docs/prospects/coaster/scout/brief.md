# Research brief: prospect, landscape, timing & enablers, and reach

_The brief as it was sent on 2026-10-21, under the pack's working name. The
pack is now named coaster._

_Drafted by `scout` on 2026-10-21 from `templates/research-brief.md`. Paste
this into Claude's Research mode, Claude Code's `/deep-research`, or another
deep-research tool. Bring the full report back to `scout`._

## The idea

A lean skill pack for Claude that helps a builder triage a project idea before
building it or writing a business plan. The point is to be lean and
complementary to the rest of the tools in the ai-pegboard project, a family of small open-source plugins for spec-driven building,
evaluation, and release shaping. It reuses what the user already has instead
of bundling its own machinery: it writes research briefs for the user's own
deep-research tool and turns the report into a cited evidence ledger, and its
optional challenge step hands off to an installed grilling skill when there is
one. It starts in a claude.ai chat Project and moves to Claude Code with the
repository. Claude only for the first version.

## What to find out

**Landscape**

1. Which tools turn an idea or question into a brief for a deep-research tool,
   and then turn the finished report back into structured, cited evidence?
   Include BMAD Deep Recon's draft and process modes, deep-research prompt
   generators packaged as skills, GPTs or prompts, and any idea-validation
   tool that delegates its research instead of running it.
2. Which small, standalone skills or plugins for idea triage or idea
   validation exist as of October 2026, outside a framework such as Spec Kit,
   BMAD, or gstack? Which of them install into claude.ai chat?
3. Which grilling, interviewing, or pressure-testing skills exist that another
   skill could hand a plan or dossier to? Which of them run standalone, and
   which depend on a parent pack?

**Timing & enablers**

4. Can a Claude skill start Claude's Research mode in claude.ai, or must the
   user start it? What does a Research report contain, and can it be saved
   into a Project as an artifact or as project knowledge?
5. How does Claude Code's `/deep-research`, or a deep-research skill, accept a
   brief, and what does it output and where?
6. Can one skill invoke or defer to another installed skill, in claude.ai and
   in Claude Code? How reliable is it, and what does the documentation say?
7. What changed in 2026 about moving files from a claude.ai chat Project into
   a GitHub repository?

**Reach**

8. What evidence is there that developers prefer small, composable skills over
   framework packs, or complain about skill or plugin bloat, such as context
   cost or skills triggering less as more are installed?
9. How are plugins from third-party GitHub marketplaces discovered and
   installed in claude.ai and Claude Code today, and what install numbers exist
   for small skill packs?

## Search specifically for

- A lean idea-triage skill pack that delegates research to built-in research
  tools and hands off to build tools.
- An idea-triage tool that is encouraging by default, with challenge only on
  request.
- The closest existing tool for each gap you find.

## What counts as evidence

- Primary sources first: the product's own pages, the repository, the
  documentation, the thread itself.
- Evidence against the idea, with the same care as evidence for it.
- Nothing from memory alone. Every claim needs a source retrieved in this run.

## Output format

One claim per line, each with:

- the claim, in one sentence;
- the source title and link;
- the publication date, if known.

For every "nothing does X", list the searches you ran and where. End with what
you could not read or verify.
