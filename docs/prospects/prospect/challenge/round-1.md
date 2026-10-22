---
round: 1
date: 2026-10-21
dossier: ../dossier.md
hats: [skeptic, rival, customer]
engine: three hats (no grilling skill installed in this session)
---

# Challenge round 1

> Opt-in, run at Julien's request. The hats read only the dossier, its scout
> folder, and the first dossier as the user's own record, never the
> conversation. Their concerns are risks worth retiring, never verdicts.
> Dispositions below are **proposed** and wait for Julien.

## What holds up

- **The evidence holds where it carries weight.** The skeptic re-opened eight
  grounded entries and all match; two unverified entries are now grounded
  (`S-07`, `S-08`).
- **The Feasible reading is well supported**, and putting the grilling
  hand-off last is the right answer to the nested-call bug whether or not it
  gets fixed (skeptic).
- **What BMAD cannot easily copy:** a pack that is Markdown only, where
  nothing runs; a dossier that lives in the chat; no step that gives a
  verdict; a hand-off outside its own family; money read from the builder's
  own constraints (rival).
- **What would make a chat-first builder switch:** one paste of the brief and
  one Research run within a Pro allowance, giving a one-screen dossier worth
  reopening instead of the report (customer).
- **At a glance works**, and saying what was not checked builds trust (all
  three).

## Skeptic: is the evidence robust?

_Read: the dossier, its lane files, the brief, the report, own-record.md, and
round 1 on the first dossier. Sources re-opened and new searches run on
2026-10-21. Concerns are risks worth retiring, not verdicts._

### What holds up

- **The grounded entries hold.** I re-opened eight of them, and all match.
  `LND-04`: 2 stars, created and last pushed on 2026-07-20. `LND-12`: 963,620
  installs later the same day, in line with 960,166. `LND-13` matches the
  note's wording. `LND-14`: #831 was closed as not planned on 2026-10-06.
  `ENB-06` and `ENB-07`: both issues are still open. `RCH-01`: the abstract
  says "up to 21%", and the paper's table shows these are absolute points.
  `RCH-08`: the prompt builders' install counts.
- **Two unverified entries are now grounded.** `RCH-03` matches the current
  skills docs: a budget of 1% of the context window, the least-invoked
  descriptions dropped first, and a 1,536-character cap (S-07). `RCH-07`'s
  1,745 installs for the plugin that carries grilling match its claude.com
  page (S-08).
- **The dossier says what it did not check.** It keeps the twelve opened
  claims apart from the rest, says demand and money were carried over, and
  says claude.ai's screens were not seen. The report's "could not be read or
  verified" section is thorough, and most of this hat's leads came from it.
- **The core of the Feasible reading is well supported.** The Commands page
  confirms that `/deep-research` runs only when the user starts it. No doc
  defines a way for one skill to call another. Putting the grilling hand-off
  last is a sound answer to `ENB-06` whether or not the bug gets fixed.
- **The Open reading names the closest rival for each gap.** That makes each
  gap testable, and row 1 relies on it.

### Worth checking

| # | Lens | Claim or reading | Concern | Why it matters | Cheapest test | Suggested urgency |
|---|---|---|---|---|---|---|
| 1 | Open, Timely | "Nothing standalone does this: the loop exists only inside BMAD" (At a glance, `LND-01`). The Open gap "the loop without a framework". R-01 watches for BMAD to package Deep Recon on its own. | BMAD already ships Deep Recon outside the framework, in a form a Claude user can install. Since 2026-08-21, a Claude Code marketplace has carried the `bmad-toolbox` plugin, which BMAD describes as standalone skills (S-01). The toolbox copy of Deep Recon falls back to its own defaults when BMAD's scripts are missing. Only the main-branch copy, the one `LND-01` read, offers BMAD setup instead (S-02). The toolbox copy still logs through `uv` and a `_bmad/scripts` path, so whether it runs cleanly is untested. One extra code search also found three small skills that run the same loop: a brief, a run outside the session, then ingestion. All three have 0 stars (S-03). The report's absence searches inspected only the top 12 hits per query. | Three things rest on this claim: the first reason under the suggested call, the Timely reading, and R-01's trigger. If the toolbox's Draft and Process work without BMAD core, R-01 has partly happened. The gap that remains is then the lenses, the posture and the family hand-off, not the loop itself. | Install `bmad-toolbox` from `bmad-code-org/bmad-plugins` in a clean Claude Code session with no `_bmad` folder. Ask Deep Recon to draft a brief for this idea, then to process this run's report, and note what breaks. In the side-by-side, use the toolbox, not full BMAD. About 30 minutes. | first |
| 2 | Feasible | "The one exception: in Claude Code, scout can call the deep-research skill directly (`ENB-04`)." The brief is shaped to that skill's four fields. | `ENB-04` is grounded in a local file in Julien's own setup, under the desktop app's agent-mode plugin folder. The skill is not in Anthropic's public skills repo. Claude Code's Commands page lists only the `/deep-research` workflow, which only the user can start (S-04). For a CLI-only user, the Claude Code path may be one more hand-off. Separately, the latest report reproducing `ENB-06` dates from 2026-05-20, five months of releases ago (S-05). | The exception is the only hop that does not go through the user, and the brief's format is fitted to it. If most Claude Code users don't have the skill, the brief should first fit `/deep-research`'s single free-text question. | On a machine or account without the desktop app, start `claude`, ask "What skills are available?", and look for `deep-research`. About 10 minutes. R-03 already re-tests `ENB-06` on the current version. | soon |
| 3 | Wanted | "Proven for the job; the lean variant is unproven beyond Julien." Demand is carried from the first dossier (`OWN-02`). At a glance reads the-researcher's 2 stars as a gap (`LND-04`). | The demand lane was gathered before delegation became the design. Delegation is now this shape's distinctive choice, and it has the thinnest pull in the evidence. Published research-prompt builders show 1 to 3 installs each, against hundreds of thousands for in-session research skills (S-10, `RCH-08`). The three further loops found are 0-star personal or small kits (S-03). The report notes that low uptake may also mean most authors find in-session research good enough. The readings record only the gap side. The personal kits point the other way: builders make this round trip for themselves. | The balance rule applies: the same numbers back "nobody does this" and "few want research delegated". If in-session research is good enough for most builders, the Research-mode hand-off is the step most likely to feel like homework (R-02). | In R-02, run one lane both ways in the same chat: once from a Research-mode brief, once with plain in-session web search. Compare the minutes, the hand-offs, and how many claims each lets you ground. Ask the pitch's prospective user which they would keep. Either way, record the other reading next to `LND-04`. | soon |
| 4 | Adoptable | "Fewer skills help selection (`RCH-01`)". Shape 2's wedge, "the smallest footprint, which the selection evidence favours". R-04. | `RCH-01` compares each task's helpful bundle, 11 to 77 skills with a median of 22, against libraries of 52 to 202 skills. It does not test a pack of 3 or 6. Its mechanism is shadowing: other skills whose descriptions overlap the right one. The paper names clearer, more distinct descriptions as a fix (S-06). In round 1 on the first dossier, activation was 62% with one skill installed and 58% with ten (`FR:C-03`). So the evidence points at overlap with grilling, deep-research, Deep Recon and brainstorming more than at skill count. | Shape 2 gives up trigger points and naming's own entry, on evidence that may not bear on a choice between 3 and 6 skills. The overlap risk would remain in either variant. | Write ten natural idea prompts. Run them with `claude plugin eval` and a `tool_used: Skill` grader (S-07) against both variants, with grilling and `bmad-toolbox` installed alongside. Then check each skill's cost in `/skill-doctor`. An afternoon. | soon |
| 5 | Adoptable, Wanted | "The habit to beat is grilling (`OWN-02`, `LND-12`)." "A ready target whose maintainer invites packs like this one (`LND-12`, `LND-13`)." R-06: list it next to grilling. | The 960,166 figure comes from skills.sh, which installs into coding agents. The plugin that carries grilling shows 1,745 installs on claude.com, with only an "Install in Claude Code" button. That is twelve weeks after it joined the official marketplace on 2026-07-27 (S-08). grilling's sub-agent does not run in chat (`LND-15`, unverified). The maintainer welcomes people publishing their own skills, but says the repo need not know about them, so there is no listing to ride (S-09). No figure measures grilling in claude.ai, where the Intent expects most users to start. | Riding grilling's audience is the reach path the report recommends. In chat it rests on no number yet, and in the plugin channel the audience runs to four figures. | Add one step to R-03. Add `mattpocock/skills` as a marketplace in a claude.ai Project, run grilling on this dossier's At a glance block, and note whether its sub-agent step degrades cleanly. Where the readings cite `LND-12`, say the habit is measured in coding agents. About 20 minutes. | soon |

### Nothing serious from this hat

- **Monetizable:** nothing serious from this hat. The reading says it was not
  re-scouted, rests on `OWN-03`, and keeps the options open while income is
  unstated. R-07 is the right test.

### New evidence

- **S-01** [grounded] The `bmad-code-org/bmad-plugins` repository is a Claude
  Code marketplace, created 2026-08-21, with its last commit on 2026-09-05.
  Its `bmad-toolbox` plugin is described as generally useful standalone
  skills from the BMAD Method. It holds eight skills, among them Deep Recon,
  Forge Idea and brainstorming. It has no top-level `bin/`, its entry is
  `strict: false`, and its version is 6.13.0-next. The README installs it with
  `/plugin marketplace add bmad-code-org/bmad-plugins`. The repo's one-line
  description says Claude ships from a separate `bmad-skills` repo. A
  2026-09-05 commit calls that repo a rehearsal mirror being deleted, and it
  now returns 404. — [bmad-plugins README](https://github.com/bmad-code-org/bmad-plugins); [marketplace.json](https://github.com/bmad-code-org/bmad-plugins/blob/main/.claude-plugin/marketplace.json); [commit history](https://github.com/bmad-code-org/bmad-plugins/commits/main), accessed 2026-10-21.
- **S-02** [grounded] The two copies of Deep Recon differ on activation. The
  toolbox copy reads its own `customize.toml` and uses defaults when BMAD's
  customization script fails, and missing config keys take neutral defaults
  without blocking. The main-branch copy, last changed 2026-10-17, instead
  offers to run BMAD setup when the script is not found. Both still send every
  memlog line through `uv run {project-root}/_bmad/scripts/memlog.py`. I read
  both files but did not run either. — [toolbox bmad-deep-recon SKILL.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/SKILL.md); [BMAD-METHOD bmad-deep-recon SKILL.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-deep-recon/SKILL.md), accessed 2026-10-21.
- **S-03** [grounded] Three more small skills run the loop of a brief, a
  deep-research run by the user, then ingestion:
  - lritter's `opportunity-research` round-trips between Claude Code and
    claude.ai Deep Research. It ends in an opportunity matrix that is not a
    recommendation, and it leaves the ranking to the user. It lives in
    personal dotfiles (0 stars, last pushed 2026-09-15) and is grounded in an
    existing codebase.
  - DiologIR's `research-to-roadmap` is a Claude Code plugin. Its general
    track takes any idea, pauses while the user runs Gemini Deep Research, and
    synthesizes the reports into a decision-ready document (0 stars, last
    pushed 2026-08-29).
  - pi-shelf's `market-research`, for the pi agent, drafts a brief for Gemini
    or ChatGPT Deep Research and checks every claim against a fresh source (0
    stars, last pushed 2026-10-13).

  None is an idea-triage pack with lenses and a build hand-off. All three came
  from one GitHub code search, `"deep research" "paste" "report back"
  filename:SKILL.md` (77 hits, the top 30 listed). — [opportunity-research SKILL.md](https://github.com/lritter/dotfiles/blob/master/claude/skills/opportunity-research/SKILL.md); [research-to-roadmap SKILL.md](https://github.com/DiologIR/diolog-plugins/blob/main/plugins/research-to-roadmap/skills/research-to-roadmap/SKILL.md); [pi-shelf market-research SKILL.md](https://github.com/justEstif/pi-shelf/blob/main/skills/market-research/SKILL.md), accessed 2026-10-21.
- **S-04** [absence] No public source was found for the
  `anthropic-skills:deep-research` skill. Searched on 2026-10-21:
  - the `anthropics/skills` repository tree, which has 20 `SKILL.md` files
    and none for deep research;
  - Claude Code's Commands page, which lists `/deep-research` only as a
    bundled workflow that runs when the user invokes it, and no bundled
    deep-research skill;
  - two web searches, for an "anthropic-skills" deep-research skill in Claude
    Code, the desktop app or Cowork, and for a built-in desktop deep-research
    skill that writes research notes.

  The report cites a local copy under
  `~/.claude/local-agent-mode-sessions/skills-plugin/`. — [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills); [Commands](https://code.claude.com/docs/en/commands), searched 2026-10-21.
- **S-05** [grounded] anthropics/claude-code#17351 is open, labelled
  `has repro` and `area:core`, with 30 reactions. The latest comment reporting
  the bug is dated 2026-05-20, from a team running the Agent SDK in CI. Their
  workaround, reading the child skill inline, failed again in production.
  There is no later report and no staff reply. — [anthropics/claude-code#17351](https://github.com/anthropics/claude-code/issues/17351), accessed 2026-10-21.
- **S-06** [grounded] In arXiv 2605.24050, the baseline is each task's helpful
  ("oracle") skill bundle, 11 to 77 skills with a median of 22. The expanded
  libraries hold 52, 102 and 202 skills. The drops of 0.08, 0.14 and 0.21 are
  absolute differences in pass rate. Shadowing means other skills displacing
  the helpful ones at selection, through overlapping descriptions. The
  mitigations named include making descriptions distinct. The paper says
  nothing about plugin size, and the corresponding author's affiliation is
  Databricks. — [More Skills, Worse Agents? (HTML)](https://arxiv.org/html/2605.24050), accessed 2026-10-21.
- **S-07** [grounded] Claude Code's skills docs set the description-listing
  budget at 1% of the model's context window. When the listing overflows,
  the least-invoked skills lose their descriptions first. Each entry is capped
  at 1,536 characters, and `skillListingBudgetFraction` changes the budget.
  `/skill-doctor` shows each skill's context cost and how often it is used.
  For plugin skills, `claude plugin eval` with a `tool_used: Skill` grader
  measures how often a skill triggers across realistic prompts. — [Extend Claude with skills](https://code.claude.com/docs/en/skills), accessed 2026-10-21.
- **S-08** [grounded] The claude.com page for `mattpocock-skills` shows
  1,745 installs and 21 skills, with a single "Install in Claude Code"
  button. The plugin was added to `claude-plugins-official` on 2026-07-27, in
  PR #4479. Later the same day, skills.sh showed 963,620 installs for
  `grilling`. — [mattpocock-skills on claude.com](https://claude.com/plugins/mattpocock-skills); [claude-plugins-official PR #4479](https://github.com/anthropics/claude-plugins-official/pull/4479); [skills.sh API q=grilling](https://skills.sh/api/search?q=grilling), accessed 2026-10-21.
- **S-09** [grounded] The grilling maintainer's note on new skills says that
  compositions built from grilling and its siblings belong in the user's own
  prompts or skills. It welcomes people publishing their own skills, and says
  the repo need not know about them. Among its prior requests is #414, for a
  skill that writes one-shot prompts for external chat models. #414 was
  closed on 2026-07-02 with no reactions. — [new-skills.md](https://github.com/mattpocock/skills/blob/main/.out-of-scope/new-skills.md); [mattpocock/skills#414](https://github.com/mattpocock/skills/issues/414), accessed 2026-10-21.
- **S-10** [grounded] skills.sh install counts on 2026-10-21. The published
  deep-research prompt builders show 1 to 3 installs each: kj-aiml 3,
  the-researcher 3, raymond-hear 2, gamaroff 2, build000r 1.
  davidondrej's `research-prompt` shows 207. In-session research skills show
  far more: mattpocock `research` 698,262, and `firecrawl-deep-research`
  35,288. Deep Recon shows 10,351, and that count does not split Draft and
  Process from Run. — [skills.sh API q=deep-research-prompt](https://skills.sh/api/search?q=deep-research-prompt); [q=research](https://skills.sh/api/search?q=research); [q=deep-recon](https://skills.sh/api/search?q=deep-recon), accessed 2026-10-21.

## Rival: how would an incumbent respond?

_Playing: BMad Code (`bmad-code-org`), maintainers of BMAD-METHOD and of the
`bmad-toolbox` plugin that carries Deep Recon and Forge Idea (`LND-01`,
`V-01`). Matt Pocock's pack is larger, but its maintainer takes no new skills
(`LND-13`), so they would not respond. I would._

_Read: the dossier, its lane files, the brief, the report and its landscape
notes, the own-record file, and the first dossier's round 1. New searches and
sources opened on 2026-10-21. Concerns are risks worth retiring, not
verdicts._

_How I would respond if this got traction (judgment):_ At first I would ignore
it. My toolbox already carries the loop to a 54,000-star audience (`V-01`,
`V-07`), and a new pack starts at the back of the queue (`RCH-08`). If it
caught on with claude.ai users, I would not copy the pack. I would bundle: let
my toolbox run without setup, which it nearly does (`V-03`), and point it at
claude.ai. If chat demand looked real, I would run my skill-to-bundle
converter for Claude Projects. In May I built a chat-first planning shelf,
with Deep Research as its default research path, in one day (`V-08`). So the
timescale is days to weeks. I would not undercut on price: I am free and say
I always will be (`V-07`).

### What holds up

- **The dossier reads me accurately.** "A gap in packaging and defaults, not
  in capability" is the honest frame. My Deep Recon has run Draft, Process and
  Run on my stable line since 2026-07-23, with a claims schema and a research
  firewall (`LND-01`, `LND-02`, `V-04`). Putting me first in R-01 is right. One
  small correction: the loop is three months old, not two. The 2026-08-20 date
  in `LND-03` is when the skill moved folders (`V-04`).
- **What I could not easily copy:**
  - **Nothing runs.** My design puts deterministic work in Python. Every
    toolbox skill ships scripts. In July an issue counted 101 calls to
    scripts in the user's project at activation, across 33 skill files, and
    it is still open (`V-13`). A pack of Markdown with no scripts is the opposite design. To
    match it I would give up my memlog, my config resolver and my citation
    checker (`V-03`). This is the line to lead with.
  - **The chat as the store.** Deep Recon treats the conversation as "a
    control channel, never the store" and writes everything to a run folder
    in the project (`V-03`). A dossier that lives in a chat Project and moves
    to a repo later runs against that. I can ship a chat bundle quickly (row
    4), but a bundle is not my method.
  - **No verdict.** Forge Idea starts by scrutinizing and stamps an outcome,
    `KILLED` among them, on an "Idea Death Certificate" (`V-15`). The posture
    point was covered in the first dossier's round (`FR:S-02`). What is new is
    that my verdict is a rendered artifact. I would have to retire it to match
    "no step gives a verdict".
  - **Handing off outside my family.** Deep Recon ends by calling `bmad-help`
    for the next step. Forge Idea offers its brief to my own planning skills
    (`V-03`, `V-15`). I can route elsewhere through configuration (row 2), but
    I would never default users to jig or shaper.
  - **Money from the builder's own constraints.** My market pack is built to
    price an offer (`FR:S-04`). "None, by choice" is not a shape my research
    types take.
- **Good, though copyable:** delegating research by default. My Deep Recon
  already puts Draft or Run up front and calls Draft often cheaper (`V-03`),
  and my chat bundle made Deep Research the default path (`V-08`). Making
  delegation my default would be a one-line change.
- **Where I am weakest today, from your side:**
  - two install lines; the one I recommend for small teams is a preview alpha
    whose release date has passed (`V-05`);
  - `uv` on both lines for setup and scripts (`V-05`), with a Windows setup
    issue still open (`V-05`);
  - my README tells plugin users to install `bmad-core-tools`, a name my
    manifest does not use (`V-01`, `V-05`);
  - I am not listed in either of Anthropic's marketplaces (`V-12`);
  - I have no claude.ai story (`V-10`, `V-11`).

### Worth checking

| # | Lens | Claim or reading | Concern | Why it matters | Cheapest test | Suggested urgency |
|---|---|---|---|---|---|---|
| 1 | Open | Open reading: "The loop without a framework. Closest: BMAD Deep Recon. Difference: no BMAD core or `uv`". R-01: "BMAD packages Deep Recon on its own", watched on `bmad-plugins`. | Half of R-01 has already happened. Since late August I publish Deep Recon and Forge Idea in `bmad-toolbox`, which my manifest calls standalone skills, with spec-only frontmatter and no top-level `bin/` (`V-01`, `V-02`). My Deep Recon falls back to its own defaults when the BMAD resolver is missing (`V-03`). What still ties it to me is `uv` for a helper script and the memlog, and a subagent for Process (`V-03`). V7, which should take my plugin route out of preview, was due 2026-10-16 and has not shipped (`V-05`). `bmad-plugins` only moves on release builds, so a monthly look there sees the change late (`V-01`, `V-04`). | The first gap in the Open reading rests on a dependency I am loosening. If my toolbox runs Draft and Process well enough with no setup, "no BMAD core" stops being a difference you can show. | In a fresh Claude Code folder, without `bmad setup`, add `bmad-code-org/bmad-plugins`, install the toolbox, and run Deep Recon Draft, then Process on this dossier's report. Note where it stops: `uv`, the memlog or the subagent. Repeat in a claude.ai Project if the marketplace adds there. About an hour, and it fits R-02's end-to-end run. Then restate R-01's trigger as "Deep Recon runs with no `uv`" or "V7 ships", watched on `BMAD-METHOD/skills/bmad-deep-recon` and its releases. | first |
| 2 | Open | Open reading: "lenses written for triage" (against Deep Recon) and "the handoff to jig and shaper" (against the-researcher). Shape 3, "Defer to BMAD when present". | For my users, both differences are configuration. Deep Recon's research types are an override registry: one TOML file adds a "triage" type with its own pack, so your six lenses could load into my skill (`V-06`). `external_handoffs` and `on_complete` route a finished report to named tools (`V-06`), and my README invites users to carry my output into their existing delivery workflow (`V-07`). Overrides live under `_bmad/custom/`, so this needs `bmad setup` (`V-06`). The difference that survives is no setup and no runtime, not the lenses. The same evidence makes Shape 3 cheaper than the dossier suggests: my forwarded activation honours a caller's intent and type (`V-03`), though a nested call still loses the parent's flow (`ENB-06`). | A README that leads with the lenses or the handoff can be matched by a BMAD user in an afternoon. A line about what does not run (`V-13`) I cannot match without dropping my own design. | Write the positioning sentence two ways: "lenses for triage" and "Markdown only: nothing to install, nothing runs, works in chat". For each, ask whether a BMAD user could reproduce it with one TOML file (`V-06`). About 20 minutes. Optional: draft the lenses as a Deep Recon pack file to see whether Shape 3 is nearly free. | soon |
| 3 | Adoptable | R-04: "Six descriptions compete with installed skills". challenge's engine 1: a grilling skill the user already has, chosen by its description. | The skills most likely to sit next to yours are mine, and our triggers overlap. Deep Recon answers "research this", "market research", "competitor research" and "process this research report"; scout answers "find competitors", "research the market for" and a report brought back (`V-02`). Forge Idea answers "pressure-test this idea" and "harden this idea"; challenge answers "pressure-test it" and "harden the idea" (`V-02`). Skills shadowing one another cause most of the selection loss (`RCH-02`). challenge's own rule would also pick Forge Idea as the grilling skill, because its description says it pressure-tests an idea. Forge Idea opens by scrutinizing and ends every session with an outcome stamp, one of which drops the idea (`V-15`). That hands an opt-in, no-verdict challenge to a verdict-first tool. | For people who already have BMAD, the first prompt may route to me, and the challenge hand-off may carry a verdict that prospect's design rules out. R-04 counts descriptions; this is about which incumbent's phrases yours collide with. | In Claude Code with both the BMAD toolbox and prospect installed, try ten natural prompts ("research competitors for my idea", "pressure-test this") and count which skill fires. Then decide whether challenge prefers grilling, asks the user, or names Forge Idea with a note on its stance. About an hour, next to R-04's always-on check. | soon |
| 4 | Timely | Timely: "Open now … The window could close if BMAD packages Deep Recon on its own." Intent: "I feel most will start in a "chat" session, more than a "code" session." | I have built chat-first once already. On 2026-05-25 I shipped six chat bundles for Gemini Gems and ChatGPT Custom GPTs in one day, including a market research bundle with Deep Research as its default path. The pitch was yours: plan in a flat-rate subscription before opening the IDE (`V-08`). I keep a converter that turns any skill into such a bundle (`V-08`). I removed the bundles on 2026-10-02 because those platforms moved to skills (`V-08`). No user issue about them turned up in four months, a weak proxy for use (`V-09`). I never pointed them at claude.ai, which my docs mention only as an AI that cannot read local files (`V-10`, `V-11`). So claude.ai chat is open because I left it, not because I cannot reach it. | The chat surface is the main thing I do not do today. If idea triage in claude.ai gets traction, my cheapest move is to point my converter, or my toolbox, at it. | Watch for three triggers: a BMAD bundle or doc for Claude Projects, the toolbox documented for claude.ai, or V7 shipping with the plugin route as stable. A release watch on BMAD-METHOD and a monthly look at its CHANGELOG cover all three. Separately, ask once in BMAD's Discord how much the web bundles were used. The answer says as much about chat-first demand as about me. | watch |

### Nothing serious from this hat

- **Wanted:** nothing serious from this hat. The reading rests on grilling and
  on Julien's own use, which I do not contest. One caution for the Timely
  reading, which says my shipping the loop "proves it is wanted": seven of my
  eight toolbox skills sit between 10,290 and 11,010 installs on skills.sh, the
  shape a bundle install leaves (`V-14`). Read Deep Recon's 10,351 (`LND-03`)
  as my reach, not as people choosing the loop.
- **Monetizable:** nothing serious from this hat. I am free, funded by
  donations and corporate sponsorship (`V-07`), so I cannot undercut you, and
  "none, by choice" matches how I sustain myself. Earning around the pack
  (`OWN-03`) is my model too.
- **Feasible:** nothing serious from this hat. The hand-offs the reading
  worries about are ones I ship too. My chat bundle told users to switch on
  Deep Research before every session (`V-08`), and my Draft ends by telling
  the user to run the prompt and bring the report back (`V-03`). Users accept
  that hand-off from me; R-02 tests whether it feels like homework in yours.

### New evidence

- **V-01** [grounded] The `bmad-code-org/bmad-plugins` marketplace lists two plugins at 6.13.0-next, both `strict: false`: `bmad-method` and `bmad-toolbox`, described as "generally useful standalone skills from the BMAD Method". The toolbox folder holds eight skills (advanced-elicitation, brainstorming, customize, deep-recon, forge-idea, party-mode, review, and the `bmad` hub with its setup, config and memlog scripts) and a Codex manifest, but no `.claude-plugin/plugin.json`. The repo was created 2026-08-21; its last commit, 2026-09-05, rebuilt both plugins from BMAD-METHOD, and it changes only on release builds. — [bmad-plugins marketplace.json](https://github.com/bmad-code-org/bmad-plugins/blob/main/.claude-plugin/marketplace.json); [toolbox tree](https://github.com/bmad-code-org/bmad-plugins/tree/main/plugins/toolbox); [commits](https://github.com/bmad-code-org/bmad-plugins/commits/main), accessed 2026-10-21.
- **V-02** [grounded] All eight toolbox `SKILL.md` files use only `name` and `description`. Deep Recon's description lists, among others, "research this", "draft a research prompt", "process this research report", "market research" and "competitor research". Forge Idea's lists "forge an idea", "pressure-test this idea", "stress-test my thinking" and "harden this idea". By comparison, this pack's scout description lists "find competitors" and "research the market for", and challenge lists "pressure-test it" and "harden the idea". — [toolbox Deep Recon SKILL.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/SKILL.md); [toolbox Forge Idea SKILL.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-forge-idea/SKILL.md), accessed 2026-10-21; `skills/scout/SKILL.md` and `skills/challenge/SKILL.md` in this repository, read 2026-10-21.
- **V-03** [grounded] The toolbox Deep Recon first runs `uv run {project-root}/_bmad/scripts/resolve_customization.py`. On failure it reads its own `customize.toml` defaults, and missing config keys never block. Draft and Process still call a skill-local `uv run scripts/recon_kit.py` to name the run folder and start the memlog, whose documented path is `{project-root}/_bmad/scripts/memlog.py`. Process extracts claims with a fresh-context subagent. The skill says nothing exists until it is a file and treats the conversation as a control channel. A bare research ask gets Draft or Run up front, with Draft called often cheaper. A forwarded activation honours a caller's stated intent and type. Finalize runs any configured `external_handoffs`, then invokes `bmad-help` for the next step. — [SKILL.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/SKILL.md); [draft.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/references/draft.md); [process.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/references/process.md); [finalize.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/references/finalize.md), accessed 2026-10-21.
- **V-04** [grounded] Deep Recon reached BMAD's stable line through PR #2611, merged 2026-07-23. The PR replaced the market, domain and technical research skills and shipped Draft, Process and Run from the start. Forge Idea arrived through PR #2492, merged 2026-06-22. The `skills/bmad-deep-recon` path history begins on 2026-08-20 because PR #2768 moved all skills into a flat `skills/` tree. That path has 22 commits from 2026-08-20 to 2026-10-17; the latest feature added research from code and git history (PR #3085, merged 2026-10-15). — [PR #2611](https://github.com/bmad-code-org/BMAD-METHOD/pull/2611); [PR #2492](https://github.com/bmad-code-org/BMAD-METHOD/pull/2492); [PR #2768](https://github.com/bmad-code-org/BMAD-METHOD/pull/2768); [skills/bmad-deep-recon commits](https://github.com/bmad-code-org/BMAD-METHOD/commits/main/skills/bmad-deep-recon); [PR #3085](https://github.com/bmad-code-org/BMAD-METHOD/pull/3085), accessed 2026-10-21.
- **V-05** [grounded] BMAD's README offers stable v6.12 through the npm installer and a V7 "preview alpha" through the Skills CLI and the Claude Code and Codex plugin marketplaces. It gives V7's release ETA as 2026-10-16 and says both lines need `uv`. It tells plugin users to install `bmad-core-tools` for standalone skills, a name the manifest does not use (`V-01`). On 2026-10-21 the latest release is v6.12.4 (2026-10-14) and no v7 tag exists. A Windows setup issue opened 2026-10-19 is still open. — [BMAD-METHOD README](https://github.com/bmad-code-org/BMAD-METHOD); [releases](https://github.com/bmad-code-org/BMAD-METHOD/releases); [tags](https://github.com/bmad-code-org/BMAD-METHOD/tags); [issue #3124](https://github.com/bmad-code-org/BMAD-METHOD/issues/3124), accessed 2026-10-21.
- **V-06** [grounded] Deep Recon's `customize.toml` treats research types as an override registry. A team or personal TOML file under `{project-root}/_bmad/custom/` can add a type with its own pack file, or replace a shipped one. The same file offers `external_handoffs`, which route the finished report to named tools and skip unavailable ones, `on_complete`, and a `subagents = none` setting for environments without subagents. — [toolbox Deep Recon customize.toml](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-deep-recon/customize.toml), accessed 2026-10-21.
- **V-07** [grounded] BMAD's README invites users to carry its briefs, specifications and architecture into their existing delivery workflow. It says BMAD is "free for everyone and always will be", and asks for coffee donations or corporate sponsorship. BMAD-METHOD had 54,422 stars and 6,096 forks on 2026-10-21. — [BMAD-METHOD README](https://github.com/bmad-code-org/BMAD-METHOD); GitHub repository API, accessed 2026-10-21.
- **V-08** [grounded] PR #2421, opened and merged on 2026-05-25 within eight hours, brought back six BMAD "web bundles" for Gemini Gems and ChatGPT Custom GPTs. Their README pitches running planning in a flat-rate web subscription before opening the IDE. One bundle, Market & Industry Research, has Deep Research as its default research path, and its install steps tell users to enable Deep Research before each session. The bundles are generated by `bmad-os-skill-to-bundle` in `bmad-utility-skills`, added 2026-05-25; that repo was last pushed 2026-09-24. PR #3011 removed all web bundles on 2026-10-02, saying Gems and Custom GPTs are deprecated and being replaced by skills on both platforms. The bundles targeted Gemini and ChatGPT only. — [PR #2421](https://github.com/bmad-code-org/BMAD-METHOD/pull/2421); [web-bundles README at tag web-bundles-v1.0.0](https://github.com/bmad-code-org/BMAD-METHOD/blob/web-bundles-v1.0.0/web-bundles/README.md); [market bundle INSTRUCTIONS.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/web-bundles-v1.0.0/web-bundles/market-and-industry-research/INSTRUCTIONS.md); [bmad-os-skill-to-bundle](https://github.com/bmad-code-org/bmad-utility-skills/tree/main/skills/bmad-os-skill-to-bundle); [PR #3011](https://github.com/bmad-code-org/BMAD-METHOD/pull/3011), accessed 2026-10-21.
- **V-09** [absence] No GitHub issue about using a web bundle was found in their four-month life. Searched on 2026-10-21 with the GitHub search API: `repo:bmad-code-org/BMAD-METHOD "web bundle" is:issue` and `"web-bundles" is:issue`, both for 2026-05-25 to 2026-10-21. Each returned two issues, #2504 and #3003, neither about using a bundle. This is a weak proxy: people using a chat bundle may not file GitHub issues.
- **V-10** [grounded] BMAD's docs mention claude.ai once: a reader whose AI cannot read local files, such as ChatGPT or Claude.ai, is sent to the docs site. A community PR adding Claude Cowork support through the plugin marketplace (#2369) was closed without merging on 2026-05-08; I did not find a stated reason. — [get-answers-about-bmad.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/start/get-answers-about-bmad.md); [PR #2369](https://github.com/bmad-code-org/BMAD-METHOD/pull/2369), accessed 2026-10-21.
- **V-11** [absence] BMAD-METHOD has no other mention of claude.ai, Claude Projects or Cowork on its default branch. Searched on 2026-10-21 with GitHub code search on `repo:bmad-code-org/BMAD-METHOD`: `"claude.ai"` (one hit, the page in `V-10`), `"Claude Projects"` (none), `Cowork` (none). Code search covers the default branch only.
- **V-12** [absence] Neither of Anthropic's plugin marketplaces lists BMAD. On 2026-10-21 I scanned every entry in the official manifest (315) and the community manifest (2,283) for "bmad", "deep-recon" and "forge-idea" in any field, and found none. — [claude-plugins-official marketplace.json](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json); [claude-plugins-community marketplace.json](https://github.com/anthropics/claude-plugins-community/blob/main/.claude-plugin/marketplace.json), accessed 2026-10-21.
- **V-13** [grounded] Issue #2624, opened 2026-07-24 and still open, reports that BMAD skills run Python scripts from `{project-root}/_bmad/scripts/` at activation, 101 times in 33 `SKILL.md` files, with no check on where the scripts came from. It notes that plugin installs do not ship those scripts. PR #2768 says BMAD's deterministic work runs through Python. — [issue #2624](https://github.com/bmad-code-org/BMAD-METHOD/issues/2624); [PR #2768](https://github.com/bmad-code-org/BMAD-METHOD/pull/2768), accessed 2026-10-21.
- **V-14** [grounded] skills.sh install counts for seven of the eight toolbox skills under `bmad-code-org/bmad-method`, 2026-10-21 (the `bmad` hub was not looked up): brainstorming 11,010; advanced-elicitation 10,603; review 10,567; party-mode 10,545; deep-recon 10,351; forge-idea 10,322; customize 10,290. The copies under `bmad-code-org/bmad-plugins` show 1 or 2 each. — [skills.sh API q=deep-recon](https://skills.sh/api/search?q=deep-recon); [q=forge-idea](https://skills.sh/api/search?q=forge-idea); [q=bmad-brainstorming](https://skills.sh/api/search?q=bmad-brainstorming); [q=advanced-elicitation](https://skills.sh/api/search?q=advanced-elicitation); [q=party-mode](https://skills.sh/api/search?q=party-mode); [q=bmad-review](https://skills.sh/api/search?q=bmad-review); [q=bmad-customize](https://skills.sh/api/search?q=bmad-customize), accessed 2026-10-21.
- **V-15** [grounded] The toolbox Forge Idea tells Claude to start by scrutinizing the idea, not endorsing it. Every session renders an HTML report with an outcome stamp: `HARDENED`, `CLARIFIED`, or `KILLED` on an "Idea Death Certificate". A hardened idea becomes `forged-idea.md`, offered to BMAD's own planning skills when they are installed. Its memlog and config calls go to `{project-root}/_bmad/scripts/`, and it runs without saving state when the memlog cannot start. — [toolbox Forge Idea SKILL.md](https://github.com/bmad-code-org/bmad-plugins/blob/main/plugins/toolbox/skills/bmad-forge-idea/SKILL.md), accessed 2026-10-21.

## Customer: what would make me switch?

_Playing: a solo builder on Claude Pro. I start side projects in a claude.ai chat Project and use Research mode now and then. I have grill-me in Claude Code from skills.sh, but nothing extra in claude.ai. I move to Claude Code once an idea looks worth building._

### What holds up

- **The research hop uses a tool I already pay for.** There's no new subscription, no `uv`, and no framework core to install (`LND-01`). In Claude Code there's no hop at all: Claude can call the deep-research skill itself (`ENB-04`), which is how this dossier was made.
- **I can read the brief before I spend a run on it.** `brief.md` is short and tool-neutral. It asks for evidence against the idea and for the searches behind every absence. Seeing the questions first makes me trust the run more.
- **I can decide from one screen.** At a glance gives six one-word readings, three first risks with their tests, what I owe, and a call that says it's only a suggestion. Round 1 asked for this, and it's there.
- **It says what it didn't check.** Every line is tagged grounded or unverified. It says "claude.ai's screens were not observed", and that demand and money were carried over, not re-scouted.
- **It leaves my process alone.** It defers to grilling instead of shipping its own interrogator. It puts that hand-off last, so a broken nested call doesn't cost me the session (Feasible reading, `ENB-06`). A smaller pack also keeps my other skills working (`RCH-01`).
- **I'd remember the three-skill variant.** Shape option 2 leaves three names to keep in my head: a dossier skill, scout and handoff. That matters for something I'd reach for every few weeks.
- **What would make me stay is the register.** Each risk has a test I could run this week, and the dossier tells me when to check again.
- **What would make me switch:** one paste of the brief and one Research run, within my Pro allowance, giving me a one-screen dossier that I'd reopen instead of the report.

### Worth checking

| # | Lens | Claim or reading | Concern | Why it matters | Cheapest test | Suggested urgency |
|---|---|---|---|---|---|---|
| 1 | Feasible | The Feasible reading: "The user starts Research mode … so the design work is in paste-ready artifacts". R-02's test: run the chat path once and count the hand-offs. | Counting hand-offs misses the one that costs the most. The brief puts nine questions across three lanes into one Research run. On Pro, one writer got at most one finished Research question per session: one run stopped at the limit, and a later one used 56% of the allowance (`C-01`). A commenter says one Research chat can use up to 30% of a Pro session (`C-02`, unverified). Research always runs on Opus, whatever model I picked, and uses limits faster than a normal chat (`C-03`). Scout's processing and frame then draw on the same allowance, which Claude Code shares too (first dossier, `C-06`). | If the Research run stops at the limit, there's nothing to process and the evening is gone. That's the hop where I'd give up, and being organised doesn't help. | In R-02's run on a Pro account, read the usage meter before Research, after it, and after processing, and note whether the run finishes. Try Research both in the same chat as scout and in a fresh one. Using the same chat would also save the download and re-upload (`ENB-05`). If it doesn't fit, try one lane per run. | first (it rides on R-02) |
| 2 | Adoptable | Hand-offs: "No grilling skill is installed in this session, so it would use the three hats." R-03 tests the grilling hand-off in Claude Code only. | In chat, I probably won't have grilling either. The plugin that carries it shows 1,745 installs on claude.com, against 960,166 for the skill on skills.sh (`C-04`, `LND-12`). Skills sync from claude.ai into Claude Code, not the other way (`ENB-11`), so my grill-me in the terminal doesn't help in chat. In chat, the hats path means three new conversations, three pastes, and three answers carried back. Each new chat sees the dossier only if I've uploaded it to project knowledge. Chats in a Project don't share context (`C-05`), and Claude can't write Project files (`ENB-05`). One hopeful sign: on paid plans, Claude can search earlier chats in the same Project (`C-06`). The page doesn't say whether that brings back a whole artifact. | I opt into a challenge when I care most about the idea. Six or seven chores at that moment is where I'd skip it. The hats' independence does nothing for me if I never run them. | In a claude.ai Project, ask for a round and count the steps. Then open a fresh chat without uploading anything, and see whether chat search finds the full dossier. Also try one fresh chat that plays all three hats in turn. It still can't see the original conversation, and it takes one paste instead of three. | soon |
| 3 | Open | The Open reading says the pack is "encouraging by default" and "the challenge runs only on request", and that "the challenge itself is not a gap. grilling covers it." In `challenge`, the hand-off carries At a glance, the readings and the three angles as the agenda. | The angles travel with the hand-off. The rules that make the challenge feel safe do not: lead with what holds up, raise five concerns at most, give no verdict, use a constructive voice (`hats.md` rules 2, 5 and 6). grilling tells the agent to interview the user "relentlessly". Each round asks every open question whose prerequisites are settled, and nothing says to start with strengths (`C-07`). Users have already pushed back on rounds of ten or more questions (`LND-14`). | The challenge is where the encouraging default gets tested. If the round I opt into feels like an interrogation, I'll blame this pack, not grilling. | Add the hats' shared rules to the hand-off prompt in a few lines. In Claude Code, run grilling on this dossier with and without them. Count the questions in round one, and note whether it opens with what holds up. | soon |
| 4 | Wanted | The Wanted reading: "Julien is the first user", with the test "use it on the next real idea". Evidence: scout "opened the sources behind twelve load-bearing claims; those are `grounded`, the rest `unverified`." | In this version the research comes from my own tool, and its report already carries citations. What the pack adds is the brief, the ledger, the readings and the register. In this run, 24 of the 36 lane entries are still `unverified`, including 8 of the 9 reach entries. That's honest, and `evidence.md` requires it. But round 1 said I'd switch for evidence I can click and trust. A ledger that's mostly unverified reads to me like the report with tags added. What I'd actually reuse is At a glance and the register. | If the dossier mostly restates the report, I'll open the report next week, and the dossier stops being the record. | On the next real idea, note which file gets opened first a week later. It would also help if At a glance said how many load-bearing claims were opened, for example "12 of 36 opened". | soon |
| 5 | Adoptable | Intent: triage "before an entrepreneur would even waste time on crafting a full business plan". The Adoptable reading: "Easy to try". | It's easy for me because I pay. Plugins in chat are listed for paid plans only (`C-08`), and so is Research (`C-03`), while Projects are open to Free users (`C-05`). The friend I'd send this to has an idea and hasn't committed to it, which makes them the person least likely to pay for Claude yet. The dossier doesn't say what scout does when Research isn't available. | Reach follows an audience (`RCH-09`). For a pack like this, the first audience is the friends its users pass it on to (judgment). A recommendation that starts with "upgrade first" doesn't travel far. | Add one README line per surface: what works on Free, on Pro, and in Claude Code. Check whether a single-skill ZIP upload works on Free. | watch: check again when the first outside user is on Free |

### Nothing serious from this hat

- **Timely:** nothing serious from this hat. My moment is now. I already have Research, and on paid plans Claude can now search earlier chats in the same Project (`C-06`), which may cut a hop. BMAD's two-month head start matters more to the Rival than to me, because I won't install BMAD core for a side project (`LND-01`).
- **Monetizable:** nothing serious from this hat. I'd expect it to be free and MIT-licensed like its siblings, and "none, by choice" fits that. The cost I'd feel is my plan's allowance, which row 1 covers.

### New evidence

- **C-01** [grounded] A blogger on the $20 Pro plan got at most one finished Research question per session. One run stopped at the usage limit before finishing. A later run of the same prompt finished with 236 sources and used 56% of the session allowance. This is one person's report from before Research moved to Opus 5.5 (post dated 2026-05-20). — [Claude.AI Pro Plan quotas too small for deep research (William Angel)](https://www.williamangel.net/blog/2026/05/20/ClaudeAI-Pro-Plan-Gives-Single-Deep-Research.html), accessed 2026-10-21.
- **C-02** [unverified] In an r/ClaudeAI thread captured on 2026-07-20, a commenter calls Research the most limit-consuming feature on Claude. The same commenter says one Research chat can use up to 30% of a Pro session. Read through a third-party snapshot, not on Reddit itself. — [r/ClaudeAI thread snapshot](https://reddit.sentinel-team.org/posts/1v014kx/snapshots/2026-07-20T20%3A24%3A21.6759Z), accessed 2026-10-21.
- **C-03** [grounded] Research is for paid plans only (Pro, Max, Team, Enterprise). It runs on Claude Opus 5.5, falling back to Opus 4.8, whatever model the chat has selected. It counts against the same limits as a normal chat but can use them up faster. The page says nothing about Projects, report format, saving or run time ("Updated over a week ago" on 2026-10-21). — [Use research on Claude (Claude Help Center)](https://support.claude.com/en/articles/11088861), accessed 2026-10-21.
- **C-04** [grounded] The claude.com page for the `mattpocock-skills` plugin shows 1,745 installs and describes 21 skills, with `/grill-me` among those it names. The page gives no date. This confirms the claude.com figure in `RCH-07`. — [mattpocock-skills (claude.com)](https://claude.com/plugins/mattpocock-skills), accessed 2026-10-21.
- **C-05** [grounded] Chats in the same Project don't share context unless the information is added to project knowledge. The page describes adding knowledge by upload only. Projects are open to all users, Free included, with a cap of five projects on Free ("Updated over a week ago" on 2026-10-21). — [How can I create and manage projects? (Claude Help Center)](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), accessed 2026-10-21.
- **C-06** [grounded] On paid plans, Claude can search past chats. Inside a Project, the search stays within that Project's conversations. The feature is on by default once it reaches an account, and each Project keeps its own memory. The page doesn't say whether a search returns a whole artifact or report ("Updated today" on 2026-10-21). — [Chat search and memory (Claude Help Center)](https://support.claude.com/en/articles/11817273), accessed 2026-10-21.
- **C-07** [grounded] `grilling` tells the agent to interview the user "relentlessly" until both share an understanding. Each round asks every open question whose prerequisites are settled, numbered, with a recommended answer for each. It has no step that names the plan's strengths first, and it gives no verdict. The session ends when no open questions remain. It writes no file, and it sends a sub-agent to look up facts in the environment. — [grilling SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), accessed 2026-10-21.
- **C-08** [grounded] Plugins in claude.ai are "available to all paid plans"; the page doesn't list Free. In chat, a plugin's skills and commands work, while its sub-agents and hooks are grayed out ("Updated over 2 weeks ago" on 2026-10-21). — [Use plugins in Claude (Claude Help Center)](https://support.claude.com/en/articles/13837440-use-plugins-in-claude), accessed 2026-10-21.

## Dispositions

_All dispositions confirmed by Julien on 2026-10-21: the first as proposed,
the rest as recommended, two of them modified. Readings and the register now
reflect them. Fifteen
concerns land on eleven risks or changes, so they are grouped._

### Ledger corrections already applied

These are corrections of fact, not readings, so they are in the lane files
now, each pointing at the hat entry that made it:

- `LND-03`: Deep Recon has been on BMAD's stable line since 2026-07-23; the
  2026-08-20 date is a folder move (`V-04`).
- `RCH-03` and `RCH-07`: now `grounded` (`S-07`, `S-08`).

### Proposed

| Concern | Proposed | Becomes | Confirmed by user |
|---|---|---|---|
| Skeptic 1, Rival 1: BMAD already ships Deep Recon as a standalone plugin that falls back to its own defaults | **retire now** | R-01 rewritten: install `bmad-toolbox` in a clean folder with no BMAD setup, run Draft then Process, note what breaks; trigger becomes "Deep Recon runs without `uv`, or V7 ships". "Nothing standalone does this" in At a glance becomes "the loop runs standalone only inside a BMAD plugin that still needs `uv`". | **accepted** 2026-10-21: "let's accept that deep recon already does something similar." |
| Rival 2: for BMAD users, triage lenses and the hand-off are one config file away | **accept** | The Open reading leads with "Markdown only: nothing to install, nothing runs, works in chat", not with the lenses (`V-06`, `V-13`). | **accepted** 2026-10-21, paired with breadth in one positioning line |
| Rival 3, Skeptic 4: trigger phrases collide with Deep Recon and Forge Idea; the selection study is about overlapping descriptions, not pack size | **retire later** | R-04 restated as description overlap with installed skills; test with `claude plugin eval` against both variants with grilling and the BMAD toolbox installed (`S-06`, `S-07`, `V-02`). Shape 2's rationale weakens. Pack change: challenge checks a candidate grilling skill's stance and asks the user before handing to one that gives verdicts, such as Forge Idea (`V-15`). | **accepted, modified** 2026-10-21: solved the jig way; descriptions defer to a richer installed skill, and challenge asks before using one that issues verdicts |
| Skeptic 2: the only hop that skips the user rests on a skill seen only in Julien's desktop setup | **retire later** | New R-08 (soon): check whether a CLI-only Claude Code user has a deep-research skill; the brief's one-line question becomes the default for `/deep-research` (`S-04`). `ENB-04` reworded to "present in this setup". | **accepted** 2026-10-21 |
| Skeptic 3: demand for delegated research itself is thin | **accept** | Wanted reading records the other side: prompt builders show 1 to 3 installs, in-session research skills hundreds of thousands (`S-10`). R-02 runs one lane both ways, Research brief and in-session quick pass. | **accepted, modified** 2026-10-21: scout defers to a richer installed research skill, else runs a quick pass; the Research brief becomes the deeper option |
| Skeptic 5, Customer 2: grilling's audience is measured in coding agents, not chat | **accept** | Readings citing `LND-12` say "measured in coding agents"; R-06 drops "ride grilling's listing", since the maintainer keeps none (`S-08`, `S-09`, `C-04`). | **accepted** 2026-10-21 |
| Customer 1: one Research run may exhaust a Pro session | **retire now** | R-02 amended: read the usage meter before and after Research and processing; fall back to one lane per run (`C-01`, `C-03`). Pack change: scout warns on Pro and offers one lane per run. | **accepted** 2026-10-21 |
| Customer 2: in chat, the hats mean three new chats and uploads | **retire later** | New R-09 (soon): try one fresh chat that plays all three hats in turn, and check whether chat search finds the dossier (`C-05`, `C-06`). Pack change if it works: one paste, three hats. | **accepted, test only** 2026-10-21: the pack changes only if one chat playing all three hats works |
| Customer 3: the grilling hand-off carries the angles but not the hats' rules | **retire now** | Pack change: the hand-off prompt carries the shared rules (what holds up first, five concerns at most, no verdict, constructive voice); test with and without (`C-07`). | **accepted** 2026-10-21 |
| Customer 4: a ledger that is mostly unverified reads like the report with tags | **accept** | At a glance states how many load-bearing claims were opened, now "14 of 36" (`S-07`, `S-08`). Pack change: frame always shows that count. | **accepted** 2026-10-21 |
| Customer 5: plugins in chat and Research are paid-only | **retire later** | Watch item: one README line per surface for Free, Pro and Claude Code; check a single-skill ZIP on Free (`C-08`). | **accepted** 2026-10-21 |
| Rival 4: BMAD built and retired chat-first bundles; claude.ai is open because BMAD left it | **retire later** | `recheck` triggers: a BMAD bundle or doc for Claude Projects, the toolbox documented for claude.ai, or V7 shipping (`V-08`, `V-10`). | **accepted, folded** 2026-10-21 into R-01's watch on BMAD releases |
