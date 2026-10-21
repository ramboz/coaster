# Scout lane: reach

Scouted 2026-10-21 by a scout subagent.

## Where solo builders and AI-native developers discover tools

- **RCH-01** [grounded] In Stack Overflow's 2025 survey (49,000+ responses), the community platforms respondents used were GitHub 66.9%, YouTube 60.5%, Reddit 53.7%, Discord 38.9%, LinkedIn 37.2%, Hacker News 19.6%, X 17.1%, Bluesky 10.8% and Substack 7.1%, with Stack Overflow itself at 84.2%. In the same survey about 31% said they use AI agents at work at some frequency, and 37.9% said they do not plan to adopt them. — [Stack Overflow Developer Survey 2025: Technology](https://survey.stackoverflow.co/2025/technology), accessed 2026-10-21.
- **RCH-02** [grounded] A cross-referenced analysis of 3,869 Product Hunt launches in the first half of 2026 found 49% were AI products. Average upvotes fell from 190 to 144 as monthly launches rose to a peak of 900. Solo-maker launches averaged 123 upvotes against 288 for teams of four or more. The author presents these as correlations. — [Who actually launched on Product Hunt in 2026 (Anysite, Product Hunt forum)](https://www.producthunt.com/p/anysite/who-actually-launched-on-product-hunt-in-2026), accessed 2026-10-21.
- **RCH-03** [grounded] A study of 138 AI and LLM tool repositories launched on Hacker News in 2024–2025 found average gains of about 121 GitHub stars in 24 hours, 189 in 48 hours and 289 in a week. Posting time mattered, and the "Show HN" tag showed no statistical advantage once other factors were controlled. — [Launch-Day Diffusion: Tracking Hacker News Impact on GitHub Stars for AI Tools (arXiv 2511.04453)](https://arxiv.org/abs/2511.04453v1), accessed 2026-10-21.
- **RCH-04** [grounded] Hacker News search data for Show HN posts since 2025-01-01, matched on title words:
  - "startup idea" matched 56 posts. None reached 100 points, the best scored 15, and 79% scored 3 or less.
  - "validate idea" matched 42 posts, with a best score of 8.
  - "claude code plugin" matched 66 posts. None reached 100 points, and the best scored 61.
  - "claude skill" matched 163 posts. 1.8% reached 100 points.

  Every set had a median of 2 points. Separately, an essay about the Superpowers skills library scored 435 points (Oct 2025), while four direct links to its repository scored 3 to 5 each. The skills.sh leaderboard's Show HN scored 135 points (Jan 2026). — [HN Search API, Show HN title query](https://hn.algolia.com/api/v1/search?query=startup%20idea&tags=show_hn&restrictSearchableAttributes=title&numericFilters=created_at_i%3E1735689600), [Superpowers essay on HN](https://news.ycombinator.com/item?id=45547344), accessed 2026-10-21.
- **RCH-05** [absence] No primary dataset found on how well newsletters, YouTube, X or Bluesky work as discovery or conversion channels for developer tools or skill packs. Searched on 2026-10-21:
  - the web, for Show HN and Product Hunt conversion data, developer-tool discovery channels, and "how developers discover new tools" in the Stack Overflow 2025 survey;
  - Indie Hackers launch postmortems, which returned HTTP 403.

  Results were vendor launch guides and single-founder anecdotes.

## Distribution channels for skills and plugins

- **RCH-06** [grounded] Anthropic runs three general plugin marketplaces for Claude Code: official, community and demo.
  - **Official** (`claude-plugins-official`): added automatically on first interactive launch and browsable in the `/plugin` Discover tab. Most entries come from partners and other authors.
  - **Community** (`claude-community`): holds author-submitted third-party plugins, and users must add it by hand.
  - **Third-party marketplaces**: Anthropic does not review them.

  The web catalog at claude.com shows install counts and an "Anthropic verified" badge. — [Anthropic's marketplaces (Claude Code docs)](https://code.claude.com/docs/en/plugins/anthropic-marketplaces), accessed 2026-10-21.
- **RCH-07** [grounded] The Claude Marketplace web catalog listed 342 plugins, and the visible listings were weighted toward software development. Two plugin pages showed install counts: Frontend Design (Anthropic) at 1,134,112 and Superpowers (third party, Claude Code only) at 1,009,371. — [Claude Marketplace: plugins](https://claude.com/marketplace/plugins), [Superpowers listing](https://claude.com/plugins/superpowers), accessed 2026-10-21.
- **RCH-08** [grounded] The marketplace manifests held the following entry counts on 2026-10-21:

  | Marketplace | Entries |
  |---|---|
  | `claude-plugins-official` | 315 |
  | `claude-plugins-community` | 2,283 |
  | `knowledge-work-plugins` | 123 |

  A keyword scan of the community manifest returned 13 hits. Six to eight of them sit in idea-to-product or product-discovery territory, such as haytham, arn-spark, subconscious, closedloop-skills and guided-ai-product-management. The knowledge-work marketplace includes an Anthropic product-management plugin for specs, roadmaps, research synthesis and competitive analysis. — [claude-plugins-community marketplace.json](https://github.com/anthropics/claude-plugins-community/blob/main/.claude-plugin/marketplace.json), [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins), accessed 2026-10-21.
- **RCH-09** [absence] The keyword scan found no idea-validation, startup-idea, lean-canvas or market-research entry in two places: the official Claude Code marketplace manifest (315 entries) and the awesome-copilot manifest (182 entries). Among the 273 skills visible on the skills.sh all-time leaderboard, none was about startup ideas or idea validation. Searched 2026-10-21 with a regex over plugin names and descriptions, plus a read of the skills.sh front page. — [claude-plugins-official marketplace.json](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json), [skills.sh](https://skills.sh/), accessed 2026-10-21.
- **RCH-10** [grounded] Anyone on a paid Claude plan can submit to Anthropic's directory; Free accounts cannot.
  - Skills are not a submission type on their own and must be bundled in a plugin from a public GitHub repository.
  - Every version gets automated validation and a security scan, and a person reviews each new listing.
  - Review time is not fixed.
  - The first organization to submit a given repository folder holds the listing.
  - Listed plugins get usage figures: installs, runs and error rates.

  — [Publish to the directory (Claude docs)](https://claude.com/docs/directory/publish), accessed 2026-10-21.
- **RCH-11** [grounded] Vercel's report on skills.sh says the registry reached 1 million skill listings and nearly 280 million installs in seven months. Installs are highly concentrated:
  - nearly half of all skills were installed exactly once;
  - 375 skills (0.04%) account for 62% of installs.

  Business operations draws about 1.74 times the average installs per listing, against 0.7 times for software engineering. Cross-industry skills get about 3.6 times the installs per listing of industry-specific ones. Install counts are aggregate counters, not unique people. — [State of agent skills (Vercel, 2026-09-25)](https://vercel.com/blog/state-of-agent-skills), accessed 2026-10-21.
- **RCH-12** [grounded] The skills.sh leaderboard installs skills with `npx skills add` into 20 listed agents, among them Claude Code, Codex and GitHub Copilot. The claude.ai chat app is not among them. All-time leaders:

  | Skill | Installs |
  |---|---|
  | find-skills | 4.0M |
  | grill-me (mattpocock) | 1.4M |
  | brainstorming (obra/superpowers) | 400.7K |
  | to-prd (mattpocock) | 351.6K |

  grill-me stress-tests a plan through systematic questioning and was first seen 2026-03-13. — [skills.sh](https://skills.sh/), [grill-me](https://skills.sh/mattpocock/skills/grill-me), accessed 2026-10-21.
- **RCH-13** [grounded] GitHub stars on 2026-10-21:

  | Repository | Stars |
  |---|---|
  | obra/superpowers | 303,122 |
  | mattpocock/skills (created Feb 2026) | 299,771 |
  | anthropics/skills | 182,738 |
  | ComposioHQ/awesome-claude-skills | 77,614 |
  | hesreallyhim/awesome-claude-code | 56,191 |
  | anthropics/claude-plugins-official | 43,607 |
  | github/awesome-copilot | 40,279 |
  | travisvn/awesome-claude-skills | 15,494 |
  | anthropics/claude-plugins-community | 4,720 |

  — [anthropics/skills](https://github.com/anthropics/skills), [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills), accessed 2026-10-21.
- **RCH-14** [grounded] ChatGPT and Codex share one public plugin catalog. Codex CLI users browse and install with `/plugins`, and the Codex IDE extension does not support plugins. Plugins can bundle skills, MCP servers, browser extensions and hooks. They can also be shared through repo or team marketplaces, and workspace admins can import a GitHub marketplace. — [Plugins (OpenAI docs, redirected from developers.openai.com/codex/plugins)](https://learn.chatgpt.com/docs/plugins), accessed 2026-10-21.
- **RCH-15** [grounded] GitHub Copilot CLI plugins can carry custom agents, `SKILL.md` skills, hooks, MCP and LSP configurations. Two marketplaces are registered by default, copilot-plugins and awesome-copilot, and install is `copilot plugin install` or `/plugin install`. GitHub's docs list Anthropic's `claude-code-plugins` repository as an example marketplace. The awesome-copilot manifest held 182 entries on 2026-10-21. — [About plugins for GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins), accessed 2026-10-21.
- **RCH-16** [grounded] JetBrains' early 2026 results surveyed more than 15,000 developers in April–May 2026. 39% of professional developers used Claude Code at work (47% in the US), against 21% for GitHub Copilot and 16% for Codex. 90% used coding agents at least weekly. — [JetBrains Reveals Widespread Adoption of AI Coding Agents (I Programmer)](https://www.i-programmer.info/news/99-professional/19118-jetbrains-reveals-widespread-adoption-of-ai-coding-agents-.html), accessed 2026-10-21.

## Install friction: claude.ai chat versus Claude Code

- **RCH-17** [grounded] Anthropic's help center lists skills on the Free, Pro, Max, Team and Enterprise plans.
  - **Setup:** "Code execution and file creation" must be on under Settings > Capabilities.
  - **Upload:** zip the skill folder, then use Customize > Skills > + > Create skill > Upload a skill.
  - **Common failures:** an oversized zip, a folder name that doesn't match the skill name, or a missing SKILL.md.
  - **Sharing:** custom skills are personal by default. Sharing (view-only) exists only on Team and Enterprise.
  - **Triggering:** Claude may not use a skill unless its description clearly says when to apply it.

  — [Use skills in Claude (Claude Help Center)](https://support.claude.com/en/articles/12512180-use-skills-in-claude), accessed 2026-10-21.
- **RCH-18** [grounded] The claude.com skills overview lists skills on Pro, Max, Team and Enterprise only. It says skills run in Claude's code sandbox, which needs code execution turned on. It adds that a skill's description is the only part Claude sees before deciding to load it. Skills that users upload or that others share are not reviewed by Anthropic. — [Skills overview (Claude docs)](https://claude.com/docs/skills/overview), accessed 2026-10-21.
- **RCH-19** [grounded] In claude.ai and the desktop app, users add plugins from Customize > Plugins in three ways:
  - **Discover:** directory plugins, shown on Pro and above.
  - **Add marketplace:** a GitHub URL or owner/repo shorthand.
  - **Upload plugin:** a .zip of the folder.

  Plugins added from a marketplace URL or by upload get no Anthropic review. An installed plugin is saved to the account and works in chat, in Cowork, and in Claude Code as a synced plugin. — [Plugins (Claude docs)](https://claude.com/docs/plugins/overview), accessed 2026-10-21.
- **RCH-20** [grounded] Chat loads only part of a plugin:
  - It loads skills, and loads commands as skills.
  - It ignores agents, hooks and local MCP servers.
  - It refuses any plugin with a top-level `bin/` folder.

  An account can add up to 25 marketplaces per organization, and each plugin can hold up to 5,000 files and 200 MB. On Team and Enterprise plans, an Owner sets each plugin to Not available, Available to install, Installed by default, or Required. Claude Code admins can allowlist or block marketplaces through managed settings. — [Plugin feature support across platforms (Claude docs)](https://claude.com/docs/plugins/platform-support), accessed 2026-10-21.
- **RCH-21** [grounded] In Claude Code, a third-party plugin takes `/plugin marketplace add owner/repo` and then `/plugin install name@marketplace`, and the user picks user, project or local scope. A one-step `--marketplace` flag exists in recent versions.
  - Auto-update is off by default for third-party and community marketplaces.
  - Cloud sessions, including claude.ai/code, do not load plugins installed on the user's own machine.
  - Plugins installed from the command line stay on that machine and do not reach the claude.ai account.

  — [Install and manage plugins (Claude Code docs)](https://code.claude.com/docs/en/discover-plugins), accessed 2026-10-21.
- **RCH-22** [grounded] Snyk's February 2026 scan covered 3,984 agent skills from ClawHub and skills.sh. 13.4% (534) had at least one critical issue, such as malware, prompt injection or exposed secrets, and 36.82% had some security flaw. Human review confirmed 76 malicious payloads. — [ToxicSkills (Snyk, 2026-02-05)](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), accessed 2026-10-21.
- **RCH-23** [grounded] Two open Claude Code issues concern skill discovery and sync:
  - Opened 2025-10-17: Claude Code does not recognise skills in `.claude/skills/`. 70 comments.
  - Opened 2026-01-25: a request to sync skills between Claude Desktop and Claude Code. 171 reactions.

  — [Issue #9716](https://github.com/anthropics/claude-code/issues/9716), [Issue #20697](https://github.com/anthropics/claude-code/issues/20697), accessed 2026-10-21.

## Switching costs and habits: asking the chatbot versus a structured tool

- **RCH-24** [grounded] OpenAI's large-sample study of ChatGPT use found that "Practical Guidance", "Seeking Information" and "Writing" together make up nearly 80% of conversations. Non-work messages rose from 53% to over 70% of use. The authors see the product's economic value mainly in decision support, especially in knowledge-intensive jobs. — [How People Use ChatGPT (NBER Working Paper 34255, Sept 2025)](https://www.nber.org/papers/w34255), accessed 2026-10-21.
- **RCH-25** [grounded] Five state-of-the-art AI assistants consistently gave sycophantic responses across four free-form tasks, tailoring feedback to the user's stated views. In human preference data, responses that matched a user's views were more likely to be preferred. — [Towards Understanding Sycophancy in Language Models (arXiv 2310.13548)](https://arxiv.org/abs/2310.13548), accessed 2026-10-21.
- **RCH-26** [grounded] The mattpocock/skills README makes three points:
  - It offers a newsletter to "~60,000 other devs".
  - It lists the pack both in the official Claude Code marketplace, where it updates itself, and on skills.sh, which copies editable files that users update by hand.
  - It argues that frameworks such as GSD, BMAD and Spec-Kit "own the process" and take control away from the user, and presents its own skills as small and composable.

  — [mattpocock/skills README](https://github.com/mattpocock/skills), accessed 2026-10-21.
- **RCH-27** [grounded] Process-heavy spec-driven workflow repositories had large GitHub followings on 2026-10-21:

  | Repository | Stars | Created |
  |---|---|---|
  | github/spec-kit | 142,298 | Aug 2025 |
  | gsd-build/get-shit-done | 64,254 | Dec 2025 |
  | bmad-code-org/BMAD-METHOD | 54,418 | Apr 2025 |

  — [github/spec-kit](https://github.com/github/spec-kit), [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD), accessed 2026-10-21.
- **RCH-28** [absence] No survey found that measures how many founders or solo builders ask ChatGPT or Claude for feedback on ideas, or why they move to a structured tool. Searched the web on 2026-10-21 for surveys of founders using ChatGPT for idea validation and of entrepreneurs using AI for business ideas. Results were vendor blogs citing reports that could not be checked. The Indie Hackers threads on validation habits returned HTTP 403, and an Inc. article on founders and AI confirmation bias could not be opened.

## Adoption of structured methods by solo builders

- **RCH-29** [grounded] LEANSTACK says Lean Canvas is used by over a million entrepreneurs. This is the vendor's own figure. — [LEANSTACK](https://www.leanstack.com/), accessed 2026-10-21.
- **RCH-30** [grounded] Randomized trials by Camuffo, Gambardella and colleagues tested training entrepreneurs in a scientific approach: forming hypotheses and testing them.
  - In one trial with 250 nascent entrepreneurs, trained founders were more likely to close their business and earned higher revenue on average.
  - A replication across 759 firms in four trials reports that the approach can be taught, that it produces fewer pivots, and that fewer pivots go with higher performance.

  — [Innovation Growth Lab summary of the RCT](https://www.innovationgrowthlab.org/blog/confused-or-unimaginative-how-adoption-scientific-approach-improves-entrepreneurial), [CEPR DP15972 summary](https://causalclaims.trfetzer.com/paper/DP15972.html), accessed 2026-10-21.
- **RCH-31** [grounded] On Hacker News, a solo developer described cutting Shape Up down to its bare minimum. When asked for estimates, they offer a fixed time box of usually one or two weeks instead. — [HN comment, 2023-05-03](https://news.ycombinator.com/item?id=35806403), accessed 2026-10-21.
- **RCH-32** [absence] No survey or dataset found on how many solo builders adopt, or drop, Lean Canvas or Shape Up. Searched the web on 2026-10-21 for Shape Up adoption surveys and solo use, for Lean Canvas user counts, and for Lean Canvas critiques among indie hackers. Searched HN comments for "shape up" and "solo". What turned up was team case studies, opinion pieces, vendor user claims, and a self-selected Basecamp testimonial questionnaire (seen only as a search snippet).

## Notes for frame

_Judgment, not evidence._

- The chat path no longer needs a zip upload. A GitHub marketplace URL works in Customize > Plugins (RCH-19). But chat drops agents and hooks (RCH-20), so a pack meant for chat projects has to work as plain skills.
- The default channels are crowded with developer tooling and dominated by a few creator-led packs (RCH-07, RCH-11, RCH-13). Repo-link launches on HN mostly vanish, while essays and creator newsletters spread (RCH-04, RCH-26). Reach probably depends on a written argument more than a listing.
- The registry under-supplies business-operations skills relative to demand (RCH-11), and nobody holds an idea-triage slot in the main marketplaces (RCH-09). Some community entries come close, though (RCH-08).
- The habit to beat is asking the chatbot directly (RCH-24). Sycophancy (RCH-25) is a reason to switch that needs no persuasion. grill-me's installs suggest developers will adopt a skill that questions their plan (RCH-12).
- Trial evidence favours structured testing of ideas (RCH-30), but solo builders trim methods hard (RCH-31) and some reject process-owning frameworks (RCH-26). This supports keeping the lenses as light nudges.
- Trust and triggering are real adoption risks: security findings (RCH-22), unreviewed self-added marketplaces (RCH-19), and skills that don't fire (RCH-17, RCH-23). The plan conflict between RCH-17 and RCH-18 is worth re-checking before stating which plans the pack requires.
