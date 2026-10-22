# Reach: how small composable skill packs are adopted and discovered vs. large framework packs (as of 2026-10-21)

Research run date: 2026-10-21. All live counts (GitHub stars, skills.sh installs, claude.com installs, npm downloads) are snapshots taken that day unless another date is given. Direct quotes are kept to one; everything else is paraphrase.

## Q1. Do developers prefer small, composable skills over framework packs, and is there evidence of skill/plugin bloat (context cost, weaker triggering as more are installed, conflicts between packs)?

### Takeaway
The cost side is well documented and partly quantified. Anthropic's own docs say every enabled skill's description is charged to context on every turn. Claude Code drops descriptions once the listing passes 1% of the context window. A June 2026 study measured pass rates falling 8–21 points as skill libraries grew from about 50 to 202 skills, mostly from choosing the wrong skill rather than from context length. There are also many developer complaints about bloat, including some aimed at Superpowers by name. On preference, the evidence is mixed. Small single-purpose skills (Matt Pocock's) lead skills.sh installs. A framework (Superpowers) leads GitHub stars and has about 1M installs on Anthropic's marketplace. Spec Kit and gstack each have more than 130k stars.

### Cited Findings

**Developer stance and positioning (for small/composable)**
- Matt Pocock's skills README sets their pack against GSD, BMAD and Spec-Kit, saying those take over the process, take away the user's control, and make bugs in the process hard to fix. They call their own skills "small, easy to adapt, and composable" (undated README, read 2026-10-21). — [mattpocock/skills README](https://github.com/mattpocock/skills)
- The same README warns that installing both the plugin and the skills.sh copy gives you every skill twice (undated, read 2026-10-21). — [mattpocock/skills README](https://github.com/mattpocock/skills)
- Thoughtworks' Birgitta Böckeler (2025-10-15) found that Spec Kit produced many repetitive, verbose markdown files (one spec ran to about eight files). The workflow felt like overkill for a 3–5 point feature, and they would rather review code than those documents. — [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl (martinfowler.com)](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- In the same article, Kiro turned a small bug into 4 user stories with 16 acceptance criteria, which they judged far too heavy (2025-10-15). — [martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- That article drew 128 points and 32 comments on HN (2025-10-16), far more than any Spec Kit repo submission (7 points at most). — [HN Algolia story search "spec-kit"](https://hn.algolia.com/api/v1/search?query=spec-kit&tags=story)
- Addy Osmani (2026-05-03) argues for small, phase-loaded workflow skills with exit criteria over long handbooks. He says a 20-skill library can fit a roughly 5K-token slot only through progressive disclosure: a complex feature may use about 11 skills and a small bug fix about 3. — [Agent Skills (addyosmani.com)](https://addyosmani.com/blog/agent-skills/)
- An HN commenter (2026-10-05) said they hid their team's bloated shared skills directory and used a stripped-down personal one. — [HN comment 49969899 (bunderbunder)](https://news.ycombinator.com/item?id=49969899) (via [Algolia comment search "skills bloat"](https://hn.algolia.com/api/v1/search?query=skills%20bloat&tags=comment&hitsPerPage=40&numericFilters=created_at_i>1735689600))
- An HN commenter (2026-10-14) said bloated frameworks make AI steering worse, and that they use skills on top of a lean framework. — [HN comment 50084096 (theplumber)](https://news.ycombinator.com/item?id=50084096)
- An HN commenter (2026-01-25) said a composable skill of about 500 tokens versus a 10K-token one is a meaningful difference. — [HN comment 46753788 (kxbnb)](https://news.ycombinator.com/item?id=46753788)

**Complaints about framework packs specifically**
- An HN commenter (2026-08-13) called the skills Superpowers adds bloated, saying they slow capable models down and lower output quality. — [HN comment 49283567 (MuteXR)](https://news.ycombinator.com/item?id=49283567)
- Superpowers issue #2454 (opened 2026-10-03): `using-superpowers` is injected into every session through a SessionStart hook. Its emphatic, all-caps "must invoke" wording makes current models invoke skills before trivial questions, so the issue proposes cutting it to one sentence and a 2–3 row table. — [obra/superpowers #2454](https://github.com/obra/superpowers/issues/2454)
- The Superpowers repo has open issues titled "brainstorming/writing-plans SKILL efficiency" (#512, 2026-02-20, 17 comments), "reduce reviewer subagent verbosity to conserve tokens" (#1930, 2026-07-05), and "Codex: … simple plan with subagent-driven development consumes full 5h token budget in a single run (PLUS plan)" (#1152, 2026-04-13, 15 comments). I read titles only, from a GitHub search listing. — [GitHub issue search repo:obra/superpowers](https://github.com/obra/superpowers/issues?q=conflict+OR+tokens+OR+bloat)
- gstack HN launch thread (2026-03-12, 15 points): one commenter liked splitting roles into planning, review, QA and ship, but doubted the clone-and-copy install would hold up across repos with different review and QA gates. Another raised its usage telemetry, and a reply said it can be opted out of. — [HN item 47355173 via Algolia](https://hn.algolia.com/api/v1/items/47355173)
- A tweet submitted to HN was titled "Gstack to Be Renamed as Gslop" (2026-04-01, 3 points). I did not open the tweet. — [HN Algolia story search "gstack"](https://hn.algolia.com/api/v1/search?query=gstack&tags=story)

**Complaints about skill bloat in general**
- In HN comments from Aug–Oct 2026, users said that adding skills or plugins bloats the context window (2026-08-07), that too many skills need a search layer (2026-08-10), that they removed skills because they mostly inflated tokens (2026-08-04), and that people should be wary of context bloat from skills and tool definitions (2026-10-20). — [HN 49211081](https://news.ycombinator.com/item?id=49211081); [HN 49238759](https://news.ycombinator.com/item?id=49238759); [HN 49170484](https://news.ycombinator.com/item?id=49170484); [HN 50162436](https://news.ycombinator.com/item?id=50162436)
- An HN commenter (2026-05-14) found skills far less reliable than clear instructions in AGENTS.md. — [HN 48137164 (gbro3n)](https://news.ycombinator.com/item?id=48137164)
- An HN commenter (2026-02-09, on a dead story) said the agent starts picking the wrong tools once there are more than about 30. — [HN 46942341](https://news.ycombinator.com/item?id=46942341)
- Counterpoint: other HN commenters (2026-08-05, 2026-02-26) said progressive disclosure already makes skills cheaper than MCP tool definitions. — [HN 49179362](https://news.ycombinator.com/item?id=49179362); [HN 47160341](https://news.ycombinator.com/item?id=47160341)

**Context-window cost (official docs)**
- Claude Code docs: every session with a plugin enabled carries the names and descriptions of its skills, agents and commands, and those tokens count against usage whether or not the plugin is used (undated docs, read 2026-10-21). — [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure)
- `claude plugin details` reports an "Always-on" token figure per plugin. To lower it, the docs say to shorten descriptions or to split a large plugin so users install only the parts they need. They also warn that a shorter description can stop a skill from triggering. — [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure)
- For official-marketplace plugins, `/plugin` shows a "Context cost" estimate before install (Every turn / When invoked), and highlights the Every-turn line at 2,000 tokens or more. Plugins from custom or third-party marketplaces show no cost estimate. — [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure); [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- The `/plugin` Installed tab moves a plugin under "Not used recently" after 14 days and 10 sessions without use. `/skill-doctor` (v2.1.252+) flags listed skills that have never been invoked, and `/doctor` recommends disabling unused plugins. — [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure); [Skills docs](https://code.claude.com/docs/en/skills)

**Skill listing budget and truncation (why triggering gets worse as more skills are installed)**
- Claude Code docs: the skill listing budget is 1% of the model's context window. On overflow, descriptions are dropped starting with the least-invoked skills, but names always stay. Each entry is capped at 1,536 characters. Users can raise `skillListingBudgetFraction` or `SLASH_COMMAND_TOOL_CHAR_BUDGET`, or set skills to "name-only" in `skillOverrides` (undated, read 2026-10-21). — [Skills docs, "Skill descriptions are cut short"](https://code.claude.com/docs/en/skills)
- Claude Code issue #64606 (2026-06-02, closed as not planned three minutes after opening) estimated the budget at about 8,000 characters for a 200K context. A 25-skill project at about 490 characters per description went over it, and Claude then wrote its own scripts instead of using the skills. — [anthropics/claude-code #64606](https://github.com/anthropics/claude-code/issues/64606)
- Issue #68134 (2026-06-13, v2.1.153): the startup warning said 81 descriptions were dropped, and that opting in to all of them would cost about 6k tokens every session. — [anthropics/claude-code #68134](https://github.com/anthropics/claude-code/issues/68134)
- Issue #81081 (2026-07-25, open, 14 comments): with 36 project skills and about 30 personal skills, only 9 of the 36 project skills kept their descriptions. The listing appeared to fill greedily in alphabetical order, with no indicator. It cites an earlier issue (#31505) where skills beyond about 28 were dropped entirely. — [anthropics/claude-code #81081](https://github.com/anthropics/claude-code/issues/81081)
- Conflict: the current docs say the least-invoked descriptions are dropped first, while #81081 (July 2026) observed alphabetical greedy filling. The behavior may have changed after July; I could not verify which version changed it. — [Skills docs](https://code.claude.com/docs/en/skills); [#81081](https://github.com/anthropics/claude-code/issues/81081)
- Issue #47627 (2026-04-13): the changelog for v2.1.105 raised the per-skill listing cap from 250 to 1,536 characters and added a truncation warning at startup. — [anthropics/claude-code #47627](https://github.com/anthropics/claude-code/issues/47627)
- A third-party plugin fleet (melodic-software, 2026-08-31) measured 163 skills with 120,723 characters of descriptions, 34% over a 90,000-character budget even after raising the fraction to 0.03. The mean description was 740 characters, against about 176 in Anthropic's own examples. — [melodic-software/claude-code-plugins #3505](https://github.com/melodic-software/claude-code-plugins/issues/3505)

**Measured activation and selection effects**
- Databricks researchers ("More Skills, Worse Agents?", arXiv 2605.24050 v2, 2026-06-23) tested Haiku 4.5 and Sonnet 4.6 on SkillsBench, across 2,545 trajectories. Pass rate fell by 0.08, 0.14 and 0.21 as the library grew to 52, 102 and 202 skills, compared with a library holding only the helpful skills. — [arXiv 2605.24050](https://arxiv.org/html/2605.24050)
- In the same paper, trajectories that invoked only the correct skills fell from 88.0% to 52.6%. Those invoking no skill at all rose from 12.0% to 38.5%, and about 9% invoked a distractor at 202 skills. — [arXiv 2605.24050](https://arxiv.org/html/2605.24050)
- Same paper: about two-thirds of the drop at 202 skills came from skill shadowing (0.14, significant). Pure context overhead (0.07) was not statistically distinguishable from zero. Haiku tended to abandon skills, while Sonnet tended to pick wrong ones. Caveat: two models from one provider. — [arXiv 2605.24050](https://arxiv.org/html/2605.24050)
- SkillsBench (arXiv 2602.12670; v1 2026-02-13, v4 2026-06-14): across 87 tasks and 18 model-harness setups, curated skills raised average pass rate from 33.9% to 50.5%. The abstract says focused skills with at most three modules beat larger or exhaustive bundles. Note that "modules" refers to how a skill is built internally, not to how many skills are installed. — [SkillsBench abstract](https://arxiv.org/abs/2602.12670)
- Scott Spence (2026-02-08) tested 4 Svelte skills on Sonnet 4.5 with 22 prompts. Baseline activation was 55% and 50% across two runs, and a "forced-eval" hook reached 100%. He did not vary the number of installed skills. — [Measuring Claude Code Skill Activation With Sandboxed Evals](https://scottspence.com/posts/measuring-claude-code-skill-activation-with-sandboxed-evals)

**Conflicts between packs**
- Claude Code docs: plugin skills are namespaced as `plugin:skill`, so a plugin skill and a personal skill with the same name both load. Among non-plugin skills, enterprise beats personal and personal beats project. — [Skills docs](https://code.claude.com/docs/en/skills)
- Anthropic's docs tell users to install demo-marketplace plugins from the official marketplace instead, to avoid ending up with two copies of the same plugins. — [Anthropic's marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)
- capa issue #330 (2026-10-15): mattpocock/skills and ovid/paad both ship a `/handoff` skill. The user couldn't tell which one runs, and the installer reported an unresolved conflict without naming the winner. — [infragate/capa #330](https://github.com/infragate/capa/issues/330)
- oh-my-pi issue #14127 (2026-10-02): a user found two Superpowers installs running side by side without noticing (a 6.4.2 fork and a 6.3.0 marketplace copy), with bare and namespaced variants of the same skills. — [can1357/oh-my-pi #14127](https://github.com/can1357/oh-my-pi/issues/14127)
- Claude Code issue #93318 (2026-09-10): the skill listing doesn't label where a skill came from. Bundled Anthropic skills look exactly like user skills, so the model credited a bundled `code-review` skill with user authority over `superpowers:requesting-code-review`. — [anthropics/claude-code #93318](https://github.com/anthropics/claude-code/issues/93318)

### Inferences
- The documented mechanism (a fixed listing budget, with the oldest-used or alphabetically-late descriptions dropped first) plus the shadowing result means each extra installed pack lowers the odds that any given skill triggers. That penalizes large packs more than small ones, and it penalizes newly installed, rarely used skills most.
- "Small vs. framework" is not about how many skills a pack has. Matt Pocock's pack has more skills (55 on skills.sh, 21 in the plugin) than Superpowers (15). The real difference is whether a pack injects an always-on bootstrap or process (Superpowers' SessionStart hook; gstack's required CLAUDE.md section) or leaves the user to call standalone skills.
- Complaints about bloat are many but anecdotal. The one controlled study (2605.24050) supports them on selection quality, not on raw context size.

### Gaps
- I found no controlled measurement that compares installing one framework pack with installing an equivalent set of small skills. I searched HN Algolia comments for "skills bloat" (2025-01 onward), ran web searches for "Claude skills bloat too many skills context window activation" and "skill selection accuracy degrades number of skills library size agent arxiv 2026", and searched GitHub issues in obra/superpowers for conflict, tokens, context window and bloat.
- Three more arXiv papers surfaced in search but I did not open them: 2601.04748 (a "phase transition" in selection accuracy as libraries grow), 2605.16508 (scaling laws of skills) and 2609.22218 (Toollery). Their claims are unverified here.
- I found no survey of developer preference (for example a poll asking whether people prefer small skills or frameworks). The evidence is positioning statements, HN comments and adoption counts. Searches: as above, plus HN story searches for gstack, spec-kit, BMAD, superpowers, "claude skills" and "agent skills".

## Q2. How are third-party GitHub-marketplace plugins discovered and installed in claude.ai and Claude Code, and what friction is documented?

### Takeaway
Both surfaces support third-party GitHub marketplaces. In Claude Code you add one with `/plugin marketplace add owner/repo` (or one command using `--marketplace`). In claude.ai it is Customize > Plugins > Add marketplace. Third-party marketplaces get no Anthropic review, no pre-install context-cost estimate, and no auto-update by default, and the official marketplace is the only one pre-registered. On Team and Enterprise plans, Owners can hide sources, disable member-added marketplaces, and allowlist sources. Telemetry redacts third-party plugin names by default, so neither authors nor admins see usage for third-party packs unless they configure it.

### Cited Findings

**Claude Code discovery and install path**
- Claude Code registers Anthropic's official marketplace (`claude-plugins-official`) on the first interactive terminal session. Every other marketplace must be added first with `/plugin marketplace add`, which accepts a GitHub owner/repo, any git URL, a local path or a hosted marketplace.json. — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- One-step install from a marketplace you haven't added: `/plugin install <name> --marketplace owner/repo` in a session (v2.1.275+, asks for confirmation), or `claude plugin install … --marketplace` in a shell (v2.1.292+, no confirmation). — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- `/plugin` with no arguments opens a Discover tab listing plugins from your registered marketplaces, so a third-party plugin is invisible there until its marketplace is added. — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- Auto-update is on by default for official marketplaces and off by default for the community marketplace and every third-party marketplace. — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- Cloud sessions, including claude.ai/code in the browser, have no plugin browser and don't load locally installed plugins or ones enabled in the repo's `.claude/settings.json`. — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- A project-scope `enabledPlugins` entry turns a plugin on for collaborators but doesn't download it. Each collaborator still has to run `claude plugin install … --scope project`, and repo-declared marketplaces apply only after the workspace trust dialog is accepted. — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins); [Manage plugins for your organization (Claude Code)](https://code.claude.com/docs/en/plugins/org)
- Anthropic runs three general marketplaces: official (Anthropic, partner and other-author plugins), community (`claude-community`, third-party plugins their authors submitted, which you must add manually) and demo. The docs note that many popular plugins sit in authors' own marketplaces and that Anthropic doesn't review third-party marketplaces. — [Anthropic's marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)
- Catalog sizes on 2026-10-21: the official marketplace.json lists 315 plugins and the community marketplace.json lists 2,283. Superpowers, mattpocock-skills and frontend-design are all in the official catalog. — [claude-plugins-official marketplace.json](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json); [claude-plugins-community marketplace.json](https://github.com/anthropics/claude-plugins-community/blob/main/.claude-plugin/marketplace.json)
- Some packs install outside the plugin system entirely. gstack tells users to paste a prompt that git-clones it into `~/.claude/skills/gstack`, runs `./setup` (which needs Bun, among other things), and adds a gstack section to CLAUDE.md. A team mode commits a "required" bootstrap. — [garrytan/gstack README](https://github.com/garrytan/gstack)
- Spec Kit installs through `uv tool install specify-cli`, then `specify init`. — [github/spec-kit README](https://github.com/github/spec-kit)

**claude.ai / Cowork discovery and install path**
- In claude.ai and the desktop app you add plugins at Customize > Plugins: Discover (Anthropic's default marketplaces, the directory, and your org's catalog), Add marketplace (a GitHub/GHE URL or owner/repo, or a public GitLab or Bitbucket repo), or Upload plugin (zip). — [Plugins (claude.com docs)](https://claude.com/docs/plugins/overview)
- Private GitHub marketplaces require connecting GitHub and installing the Claude GitHub App on the repo. — [Plugins (claude.com docs)](https://claude.com/docs/plugins/overview)
- Plan requirement: directory plugins appear on Pro, Max, Team and Enterprise, and Free isn't listed. On Team and Enterprise an Owner decides whether the directory is included at all. — [Plugins (claude.com docs)](https://claude.com/docs/plugins/overview)
- Review: Anthropic runs automated validation and a security scan on every directory version, and a person reviews each new listing. That review doesn't cover plugins added from a marketplace URL or uploaded, and the docs advise adding only from trusted sources. — [Plugins (claude.com docs)](https://claude.com/docs/plugins/overview)
- Plugins installed on claude.ai sync into Claude Code as `<name>@synced`, but plugins installed from the Claude Code CLI don't sync back to the claude.ai account. — [Plugins (claude.com docs)](https://claude.com/docs/plugins/overview); [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)

**Admin controls (Team/Enterprise)**
- claude.ai Owners set each plugin to Not available, Available to install, Installed by default, or Required. For Anthropic's directory, the only choices are Not available and Available to install. — [Manage plugins for your organization (claude.com)](https://claude.com/docs/plugins/admin)
- When the "User-created skills" policy is off, the add-marketplace and upload options disappear from members' Add menu. Turning "Skills" off disables plugins for everyone. — [Manage plugins for your organization (claude.com)](https://claude.com/docs/plugins/admin)
- Default publishing policy for members' plugins: Team is Open. Enterprise was Off and became "Requires review" on 2026-10-02. — [Manage plugins for your organization (claude.com)](https://claude.com/docs/plugins/admin)
- Owners can remove Anthropic's directory or a partner catalog as a source for the whole organization. — [Manage plugins for your organization (claude.com)](https://claude.com/docs/plugins/admin)
- Claude Code managed settings offer a `strictKnownMarketplaces` allowlist (`[]` blocks every source, including the official one), `blockedMarketplaces`, `disableSideloadFlags`, force-enable or block through `enabledPlugins`, and `pluginTrustMessage` to append text to the install trust warning. — [Manage Claude Code plugins for your organization](https://code.claude.com/docs/en/plugins/org)
- claude.ai also enforces an allowlist or blocklist set in the admin console when a member adds a git marketplace there, but it doesn't re-check marketplaces added before the lists were set, and it doesn't check uploads. — [Manage Claude Code plugins for your organization](https://code.claude.com/docs/en/plugins/org)

**Visibility and measurement friction for third-party authors**
- Claude Code doesn't report a plugin's usage back to its author. Usage is recorded only on each user's machine. — [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure)
- In OpenTelemetry, third-party plugin and marketplace names are redacted to "third-party" or omitted by default, even for an organization's own marketplace, unless `OTEL_LOG_TOOL_DETAILS=1` is set. The Enterprise-only Analytics API lumps unnamed plugin activity into one "third-party" row. — [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure)
- On Team and Enterprise, a plugin's page shows organization Adoption (distinct users in the last 30 days) and Activity (runs). — [Plugins (claude.com docs)](https://claude.com/docs/plugins/overview)

### Inferences
- Getting into `claude-plugins-official` is the main distribution advantage inside Claude Code. It brings pre-registration, auto-update, a context-cost display and a public install counter. A pack in its own GitHub marketplace starts with none of these, and in managed organizations it can be blocked outright.
- Third-party usage data is redacted by default, so admins can't easily see whether small third-party packs earn their context cost. Anthropic-listed plugins can be judged that way.

### Gaps
- I found no published numbers on how many users add third-party marketplaces, or on drop-off during the `marketplace add` step. Searched: HN Algolia story search "claude code plugins marketplace", and the Claude Code plugin docs (install, org and measure pages).
- I did not open the Plugin security and trust page (code.claude.com/docs/en/plugins/security) or the directory "Prepare for review" page directly, so details of the trust tiers and the review timeline are unverified beyond what the overview and admin pages say.
- I did not confirm Free-plan availability of Add marketplace or Upload directly. The docs name the plans for directory plugins only.

## Q3. What install or usage numbers exist for small skill packs vs. large ones?

### Takeaway
Which pack wins depends on the channel. On skills.sh, small single-purpose skills from Matt Pocock take 13 of the top 30 slots, at 0.8–1.4M installs each. Superpowers' top skill has about 0.4M, and gstack has only 44K installs across all 67 of its skills, mostly because gstack installs by git clone. On Anthropic's marketplace the picture flips. Superpowers has about 1.0M installs, next to Anthropic's own Frontend Design at about 1.13M, while Matt Pocock's plugin has 1,745. On GitHub stars, Superpowers (303K) and mattpocock/skills (300K) are roughly tied, ahead of Spec Kit (142K), gstack (137K) and BMAD (54K). Vercel's report shows extreme concentration: 0.04% of skills take 62% of installs, and about half were installed only once.

### Cited Findings

**Vercel "State of agent skills" (2026-09-25; Amelia Charles, Andrew Qu, Jonathan Hefner)**
- skills.sh reached 1 million skills in 7 months, with nearly 280 million installs. Vercel compares this with 27 months for GitHub repos, 63 months for App Store apps and 117 months for npm packages to reach a million. — [State of agent skills (Vercel)](https://vercel.com/blog/state-of-agent-skills)
- Nearly half of all skills were installed exactly once. The top 375 skills (0.04%) account for 62% of installs and the top 1.2% for 94%, while the single most-installed skill has under 1%. — [Vercel](https://vercel.com/blog/state-of-agent-skills)
- Software engineering skills are about a quarter of listings but 18% of installs, about 30% below the average installs per listing. Business operations is 74% above average, and writing is 50% above. — [Vercel](https://vercel.com/blog/state-of-agent-skills)
- Agent workflow and automation skills are 14.8% of installs and the largest category among skills with at least 100K installs. — [Vercel](https://vercel.com/blog/state-of-agent-skills)
- Caveat stated by Vercel: installs are aggregate counters, not unique people or independent choices, and category figures come from a classified sample. — [Vercel](https://vercel.com/blog/state-of-agent-skills)
- The report does not compare packs or frameworks with single skills, and it doesn't name top skills. — [Vercel](https://vercel.com/blog/state-of-agent-skills)
- A critique (apis.io, 2026-10-08) points out that Vercel runs the registry it is measuring. — [apis.io commentary](https://apis.io/2026/10/08/vercel-counts-a-million-skills-and-publishes-none-for-its-own-api/)

**skills.sh leaderboard and repo pages (snapshot 2026-10-21)**
- Top of the all-time list: find-skills (vercel-labs) 4.0M, grill-me 1.4M, grill-with-docs 1.2M, agent-browser 1.2M, hyperframes-cli (HeyGen) 1.2M, improve-codebase-architecture 1.2M, tdd 1.1M. Anthropic's frontend-design is 13th at 1.0M. — [skills.sh](https://skills.sh)
- 13 of the top 30 come from mattpocock/skills, and HeyGen's hyperframes bundle holds 7 of the top 30. — [skills.sh](https://skills.sh)
- mattpocock/skills: 55 skills and 29.4M total installs. The top skill (grill-me) has 1.4M and the 10th (domain-modeling) 863K. — [skills.sh/mattpocock/skills](https://skills.sh/mattpocock/skills)
- obra/superpowers: 15 skills and 3.6M total installs. The top skill (brainstorming) has 400.8K, most others have 212K–303K, and diagnosing-superpowers has 18.4K. — [skills.sh/obra/superpowers](https://skills.sh/obra/superpowers)
- garrytan/gstack: 67 skills and 44.3K total installs. The umbrella `gstack` skill has 24.0K and most others have only about 250–575. — [skills.sh/garrytan/gstack](https://skills.sh/garrytan/gstack)
- A separate repo, "101-skills/superpowers" (not obra), appears in the top 30 with a 3.3M group total. Don't confuse it with obra/superpowers. — [skills.sh](https://skills.sh)
- The leaderboard's "All Time" tab shows 1,434,971. The page doesn't say what that counts, possibly the number of listed skills. — [skills.sh](https://skills.sh)
- Skillselion's snapshot of 2026-07-29 put the top 10 Claude Code skills at: find-skills 2.72M, frontend-design 716K, grill-me 691K. Matt Pocock held 5 of the 10 slots, Vercel 4 and Anthropic 1. — [Skillselion on DEV](https://dev.to/skillselion/the-entire-claude-code-skills-top-10-belongs-to-three-authors-anthropic-holds-one-slot-27jc)
- Bundling inflates counts. Skillselion found 15 Lark skills inside an 863-install band, meaning one install of the bundle counts once for every skill in it (2026-07-29). — [Skillselion on DEV](https://dev.to/skillselion/the-entire-claude-code-skills-top-10-belongs-to-three-authors-anthropic-holds-one-slot-27jc)

**Anthropic Claude Marketplace (claude.com, snapshot 2026-10-21)**
- Superpowers: 1,009,371 installs, no "Anthropic verified" badge. — [claude.com/plugins/superpowers](https://claude.com/plugins/superpowers)
- Frontend Design (Anthropic, verified): 1,134,112 installs. — [claude.com/plugins/frontend-design](https://claude.com/plugins/frontend-design)
- Matt Pocock's Skills, described there as 21 composable skills, has 1,745 installs. — [claude.com/plugins/mattpocock-skills](https://claude.com/plugins/mattpocock-skills)
- The marketplace lists 342 plugins. Superpowers is second in the default listing, behind Frontend Design. Spec Kit, BMAD and gstack don't appear among the visible entries. — [claude.com/plugins](https://claude.com/plugins)
- Anthropic's docs confirm the web marketplace shows install counts and "Anthropic verified" badges. — [Anthropic's marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)

**GitHub stars (GitHub API, 2026-10-21)**
- obra/superpowers: 303,136 stars (created 2025-10-09). mattpocock/skills: 299,802 (created 2026-02-03). anthropics/skills: 182,748. github/spec-kit: 142,303 (created 2025-08-21). garrytan/gstack: 137,199 (created 2026-03-11). addyosmani/agent-skills: 109,319 (created 2026-02-15). bmad-code-org/BMAD-METHOD: 54,419 (created 2025-04-13). anthropics/claude-plugins-official: 43,620. vercel-labs/skills: 35,973. anthropics/claude-plugins-community: 4,720. — [GitHub REST API repos endpoint](https://api.github.com/repos/obra/superpowers) (queried for each repo named)

**npm downloads (npm API, 2026-09-19 to 2026-10-18)**
- `skills` (Vercel's `npx skills` CLI): 22,913,466 downloads. `bmad-method`: 74,435 downloads. — [npm downloads API: skills](https://api.npmjs.org/downloads/point/last-month/skills); [npm downloads API: bmad-method](https://api.npmjs.org/downloads/point/last-month/bmad-method)

### Inferences
- Counts can't be compared across channels. gstack's 137K stars against 44K skills.sh installs mostly reflects its git-clone install path. Matt Pocock's 1,745 marketplace installs against tens of millions on skills.sh probably reflects their README moving from skills.sh to the official plugin, which I could not date. Spec Kit (`uv`) and BMAD (`npx bmad-method`) don't show up on skills.sh at all.
- Repo totals on skills.sh count every skill in a pack, so a per-skill figure is a better proxy for people. On that basis Matt Pocock's top skills (about 1.0–1.4M) beat Superpowers' (about 0.2–0.4M) on skills.sh by roughly 3–5x.
- Evidence against small packs: on Anthropic's own marketplace, a framework pack (Superpowers, about 1.0M) is effectively tied with Anthropic's own plugin and far ahead of the leading small-skills pack. Frameworks also hold three of the top six skill repos by GitHub stars. Where installation is a single unit, through the plugin marketplace, frameworks do at least as well.
- Vercel's concentration data suggests a new small pack from an unknown author most likely ends up in the "installed once" half unless an author with an audience or an official listing carries it.

### Gaps
- I could not find a claude.com install count for Spec Kit, BMAD or gstack. None was visible in the listing, and I didn't find plugin pages for them. Checked: the claude.com/plugins and claude.com/marketplace/plugins listings.
- I found no unique-user or retention figures for any pack. Vercel says outright that its counters aren't unique users, and Anthropic doesn't share usage with authors.
- I found no download or install stats for Spec Kit, because it installs from git via uv and I found no PyPI or package counter. I didn't run a separate search for one.
- I couldn't load the skills.sh Trending and Hot tabs.

## Q4. How do small packs reach users (essays, newsletters, marketplace listings, awesome lists)?

### Takeaway
The packs with the most reach have a well-known author with their own audience: Matt Pocock's roughly 60K-person newsletter, Garry Tan, Jesse Vincent's essay that hit 435 points on HN, and Addy Osmani. They also use an aggregator channel: skills.sh, where the #1 skill is itself a skill for finding skills, or Anthropic's official marketplace. Curated "awesome" lists have large star counts but no measured effect on installs. HN rewards single-purpose skills with a clear demo (several Show HNs scored 76–363 points), while framework launches drew little HN attention.

### Cited Findings

**Author audience and newsletters**
- The mattpocock/skills README invites readers to join about 60,000 developers on their newsletter for updates and carries a skills.sh badge (read 2026-10-21). — [mattpocock/skills README](https://github.com/mattpocock/skills)
- Jesse Vincent's essay "Superpowers: How I'm using coding agents in October 2025" (blog.fsck.com, 2025-10-09) scored 435 points and 231 comments on HN (2025-10-11). Direct HN submissions of the Superpowers repo scored 1–4 points. — [HN Algolia story search "superpowers"](https://hn.algolia.com/api/v1/search?query=superpowers&tags=story); [HN Algolia "claude skills superpowers"](https://hn.algolia.com/api/v1/search?query=claude%20skills%20superpowers&tags=story&hitsPerPage=30)
- The gstack repo submission scored 15 points on HN (2026-03-12), even though the repo has 137K stars. — [HN Algolia story search "gstack"](https://hn.algolia.com/api/v1/search?query=gstack&tags=story); [GitHub API](https://api.github.com/repos/garrytan/gstack)
- BMAD's HN submissions peaked at 4 points (2025-08-12). — [HN Algolia story search "BMAD"](https://hn.algolia.com/api/v1/search?query=BMAD&tags=story)

**Essays and launch moments**
- Anthropic's "Claude Skills" announcement drew 816 points and 427 comments (2025-10-16). Simon Willison's essay "Claude Skills are awesome, maybe a bigger deal than MCP" drew 738 points and 370 comments (2025-10-17). — [HN Algolia story search "claude skills"](https://hn.algolia.com/api/v1/search?query=claude%20skills&tags=story)
- agentskills.io drew 544 points (2026-02-03), Addy Osmani's "Agent Skills" essay 376 points (2026-05-04), SkillsBench 364 points (2026-02-16), and the skills.sh "Show HN: Agent Skills Leaderboard" 135 points (2026-01-20). — [HN Algolia story search "agent skills"](https://hn.algolia.com/api/v1/search?query=agent%20skills&tags=story)
- Single-purpose skill Show HNs that did well: Godot game-building skills, 337 points (2026-03-16). An ASD-STE100 simplified-English skill, 363 (2026-07-30). A TDD skill, 251 (2026-06-04). Geosql, 139 (2026-07-08). A chess-analysis skill, 76 (2026-09-26). — [HN Algolia "claude skills"](https://hn.algolia.com/api/v1/search?query=claude%20skills&tags=story); [HN Algolia "agent skills"](https://hn.algolia.com/api/v1/search?query=agent%20skills&tags=story)
- Addy Osmani's own pack (20 skills plus 7 commands) is distributed through the Claude Code plugin marketplace commands, with plain-markdown copies for Cursor, Gemini CLI, Codex and others (2026-05-03). It had about 27K stars at the time of writing and 109K on 2026-10-21. — [Agent Skills (addyosmani.com)](https://addyosmani.com/blog/agent-skills/); [GitHub API](https://api.github.com/repos/addyosmani/agent-skills)

**Aggregators and in-agent discovery**
- The most-installed skill on skills.sh is `find-skills` (vercel-labs, 4.0M), a skill whose job is to find and install other skills. — [skills.sh](https://skills.sh)
- Vercel's `skills` CLI had about 22.9M npm downloads in the 30 days to 2026-10-18. — [npm downloads API](https://api.npmjs.org/downloads/point/last-month/skills)
- Claude Code's `/plugin` Discover tab and the claude.com marketplace are the in-product discovery surfaces. Third-party marketplaces surface only after the user adds them. — [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins); [Anthropic's marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)
- Superpowers is listed in Anthropic's official Claude marketplace, OpenAI's Codex plugin marketplace and its own marketplace, and its README gives install steps for 16 harnesses. — [obra/superpowers README](https://github.com/obra/superpowers)

**Curated "awesome" lists**
- Star counts on 2026-10-21: ComposioHQ/awesome-claude-skills 77,618, hesreallyhim/awesome-claude-code 56,195, travisvn/awesome-claude-skills 15,494. — [GitHub API](https://api.github.com/repos/ComposioHQ/awesome-claude-skills); [GitHub API](https://api.github.com/repos/hesreallyhim/awesome-claude-code); [GitHub API](https://api.github.com/repos/travisvn/awesome-claude-skills)
- Authors still submit to awesome lists. For example, an issue proposing "diffback" for jqueryscript/awesome-claude-code was opened 2026-10-16, and one asking to add json-claude-plugin to an awesome-ai-plugins list was opened 2026-10-21. I saw titles only, in a GitHub search listing. — [GitHub issue search results](https://github.com/search?q=%22conflicting+skills%22+OR+%22skill+conflict%22+claude+plugin&type=issues)

### Inferences
- The strongest predictor of reach in this evidence is the author's existing audience plus a one-command install channel, not a pack's size or design. Small packs from authors with no audience face Vercel's long tail, where about half of skills are installed once.
- HN attention and installs don't line up. gstack and BMAD got little HN traction but large GitHub followings. Single-skill Show HNs score well, but I have no install data linked to those launches.

### Gaps
- I found no data linking an awesome-list inclusion, a newsletter mention or an HN launch to a change in installs. Searched: HN Algolia story searches (above), the skills.sh repo pages, and GitHub repo stats. I didn't search newsletter archives.
- I didn't verify where gstack's reach came from (for example Garry Tan's X following or YC channels). Only the HN data was checked.

#### Could not read or verify (applies to the whole run)
- I read HN comments through the Algolia search API (comment excerpts summarized by the fetch tool), not as full threads. The comment-level paraphrases are faithful to those excerpts, but I didn't read surrounding context. Item links are given for checking.
- skills.sh and claude.com figures are rendered page snapshots from 2026-10-21, read through a summarizing fetch tool. Rounded values (M/K) are as displayed.
- I saw these only as search-result titles or snippets and did not open them: Socket's "supply chain security to skills.sh" post (HN, 2026-02-19), "The Claude Code plugin marketplace has no price field" (promptreceipts, 2026-08-02), arXiv 2601.04748, 2605.16508 and 2609.22218, the Medium "650 trials" activation post, the Superpowers issues #512, #1152 and #1930 (titles only), the awesome-list submission issues (titles only), and the X/Twitter "Gslop" post.
- I didn't open the Claude Code plugin security and trust page or the claude.com directory publish and review page directly.
- I couldn't date when mattpocock-skills joined `claude-plugins-official`, which matters for reading its 1,745-install figure.
- I couldn't reconcile the skills.sh "All Time" figure (1,434,971) with Vercel's 1M-skill and 280M-install totals.
