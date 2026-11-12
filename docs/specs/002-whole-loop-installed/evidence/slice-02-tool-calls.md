# Slice 002-02: tool calls per run

Trimmed from each run's stream-json log by short scripts kept outside the repository. `./` is the run's own empty `git init` folder, `<root>` the plugin folder the run loaded, and `<scratch>` the rest of the session's scratch folder. A multi-line command is shown on one line, with ⏎ for each line break, and cut at 170 characters. A `Glob` or `Grep` call shows the folder it searched in brackets when it names one. Raw logs and hat prompts stay outside the repository. Claude Code's built-in plugins (`cc-plugin-*`) are listed once per run. Each run ends with the files under `docs/` in its folder afterwards, including the framed dossier copied in.

## How the runs were made

- **Profile.** 002-01's disposable profile, signed in, with coaster `0.1.0-pre.11` installed from GitHub (`ac1f86f`), the account-synced plugins disabled, and `deep-research` and `anthropic-skills:deep-research` blocked by `Skill(...)` deny rules in its settings. Claude Code 2.1.322.
- **The framed dossier.** 002-01's `frame` run kept both turns in one folder, so that folder holds the dossier after "Go.". The framed state was recovered from the `r4` logs: the first `Edit` of turn 2 records the file it started from (`originalFile`), and replaying turn 1's last `Edit` gives the same bytes. With `r4`'s two lane files, which neither turn changed, that is the copy every run starts from: `status: framed`, `decision: pending`, 196 lines.
- **AC 1's builds.** The working tree's draft of AC 2 says `HAT_TYPE` where the type goes. Two copies of the source were rendered with `scripts/build_host_packages.py` in the scratch folder, one with `Explore` and one with `general-purpose`, and `diff` shows that line is the only difference between the two rendered packages. The draft did not bump `plugin.json`, so both say `0.1.0-pre.11`.
- **AC 1's profile.** The slice asks for a copy of the profile with the installed coaster disabled. A copied profile is not signed in: a probe in a copy returned "Not logged in". So each AC 1 run used the profile itself and disabled the installed plugin for that run alone, with `--settings '{"enabledPlugins":{"coaster@coaster":false}}'`. The profile's own settings were not changed. Each `init` event lists `coaster@inline` from the `--plugin-dir` build and the built-in plugins, and nothing else.
- **Invocation.** In a new `git init` folder holding the framed dossier, with `CLAUDE_CONFIG_DIR` set to the profile: `claude -p '/coaster:challenge challenge this' --model <sonnet|opus> --permission-mode acceptEdits --allowedTools "WebSearch,WebFetch" --output-format stream-json --verbose --plugin-dir <build> --settings '<as above>'`.

## How the checks were made

- **Hats.** A hat is an `Agent` call by the parent. Its own tool calls carry that call's id as `parent_tool_use_id`, and its model is the `model` of its own assistant events.
- **Replies.** In 2.1.322 the hats run in the background. The `Agent` call's `tool_result` is only a launch notice ("Async agent launched successfully"). The hat's reply comes later, in a `system` event of subtype `task_notification` that names the same `tool_use_id`, with the reply as its `summary` and the hat's tokens, tool uses and time as its `usage`. For one hat (`a1g`, Skeptic), the `summary` was checked against the last message of the subagent's own transcript in the profile, and the two are identical. Every check of a reply below reads the `summary`.
- **A run's results.** A run with background hats ends with several `result` events, one per turn of the parent. Denials are collected from all of them, and from the `permission_denied` events.
- **Reading the whole dossier.** A hat covers `dossier.md` with `Read` calls, by their offset and limit, or with a Bash `cat` of the whole file.
- **AC 4.** Each reply: "What holds up" before "Worth checking"; at most five rows in the concerns table, each with why it matters, a cheapest test and an urgency of first, soon or watch; every one of the six lenses either in a concern or on a "nothing serious" line; and each new entry with the hat's prefix, a known tag and the fields that tag needs. A search for "fatal", "kill" and "will fail" lists every hit, with its context. Every entry tagged `grounded` was also checked against the URLs that hat's `WebFetch` calls opened.
- **AC 6.** The four parts are cut from the `SKILL.md` the run loaded, by its headings, as AC 6 defines them. Each part is looked for in the hat's `prompt` at four levels, and the first that matches is reported: the exact text; the same text with whitespace collapsed; the same with heading, list and quote markers removed and fence lines dropped; and the same with `N`, `YYYY-MM-DD` and `<who>` matching any value. When none matches, the part is grown line by line from its start to find the first line that no longer matches.
- **AC 5, for information.** A second script checks each `round-1.md` for the template's headings in order, its opening "What holds up", and whether each concern cell and lens line under a hat's heading appears in that hat's reply. It also diffs the dossier against the framed copy.

## AC 1: the two types, hat by hat (2026-11-12)

AC 1 asks for one Sonnet and one Opus run with `Explore` hats and one Sonnet run with `general-purpose` hats. One more Sonnet run of each type was added, `a2e` and `a2g`, to see how often each result recurs. Each row is one hat. "Bash" counts that hat's Bash calls, all of which only read, and how many were denied. "Pages opened" counts its `WebFetch` calls. "New entries" counts the evidence entries in its reply, with the `grounded` ones in brackets.

| Run | Hat | Type, model | AC 6: rules, own section, evidence, template | Whole dossier | Writes | Bash (all reads) | Searches | Pages opened | New entries (grounded) | AC 4 | Tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `a1e-explore-sonnet` | Skeptic | Explore, sonnet-5-5 | whitespace, whitespace, FAIL, FAIL | yes | 0 | 1 | 1 | 1 | 3 (1) | pass | 32k | 46s |
| `a1e-explore-sonnet` | Rival | Explore, sonnet-5-5 | whitespace, whitespace, FAIL, FAIL | yes | 0 | 1, 1 denied | 2 | 0 | 3 (0) | pass | 33k | 46s |
| `a1e-explore-sonnet` | Customer | Explore, sonnet-5-5 | whitespace, exact, FAIL, FAIL | yes | 0 | 1 | 1 | 1 | 3 (1) | pass ('kill' literal) | 32k | 47s |
| `a2e-explore-sonnet` | Skeptic | Explore, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1 | 1 | 1 | 3 (1) | pass | 32k | 42s |
| `a2e-explore-sonnet` | Rival | Explore, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 2 | 0 | 3 (0) | pass | 34k | 44s |
| `a2e-explore-sonnet` | Customer | Explore, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1 | 2 | 0 | 3 (0) | pass | 33k | 39s |
| `a1o-explore-opus` | Skeptic | Explore, opus-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 3 | 9 | 9 (7) | pass | 42k | 93s |
| `a1o-explore-opus` | Rival | Explore, opus-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 4 | 4 | 7 (4) | pass | 42k | 96s |
| `a1o-explore-opus` | Customer | Explore, opus-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 4 | 7 | 7 (5) | pass | 44k | 93s |
| `a1g-gp-sonnet` | Skeptic | general-purpose, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 2 | 1 | 1 | 3 (1) | pass | 47k | 39s |
| `a1g-gp-sonnet` | Rival | general-purpose, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 2 | 0 | 3 (0) | pass | 50k | 43s |
| `a1g-gp-sonnet` | Customer | general-purpose, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1 | 2 | 0 | 3 (0) | pass | 50k | 49s |
| `a2g-gp-sonnet` | Skeptic | general-purpose, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 1 | 2 | 3 (2) | pass | 50k | 48s |
| `a2g-gp-sonnet` | Rival | general-purpose, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 2 | 0 | 3 (0) | pass | 50k | 49s |
| `a2g-gp-sonnet` | Customer | general-purpose, sonnet-5-5 | exact, exact, exact, exact | yes | 0 | 1, 1 denied | 2 | 0 | 3 (0) | pass | 50k | 37s |

Per hat, on average:

| Type, model | Hats | Searches | Pages opened | New entries (grounded) | Tokens | Time |
|---|---|---|---|---|---|---|
| `Explore`, Sonnet | 6 | 1.5 | 0.5 | 3 (0.5) | 33k | 44s |
| `general-purpose`, Sonnet | 6 | 1.7 | 0.5 | 3 (0.5) | 49k | 44s |
| `Explore`, Opus | 3 | 3.7 | 6.7 | 7.7 (5.3) | 43k | 94s |

Every entry tagged `grounded`, in every reply, cites a URL that the same hat's `WebFetch` opened.

## What the runs found

1. **AC 6 fails in one run of five.** In `a1e` (`Explore`, Sonnet), the parent pasted the hats' rules and each hat's own section intact, with only the line breaks changed. It condensed the other two parts, in all three prompts, although the draft says to paste them "unchanged, placeholders included" and not to "shorten, summarize or reword them":
   - the evidence rules lost their opening note, two of their tables became sentences, and their list of rules became one paragraph without "Check the links before reading the evidence" or "Local-only material". The first failing line is line 3, the opening note;
   - the round template kept only that hat's part. The first failing line is line 3, `round: N`;
   - outside AC 6's four parts, the other two hats' sections were replaced by "(not your hat)".

   In the other four runs every part of every hat's prompt is the packaged text byte for byte. Under AC 7, ADR-0001's kill criterion applies, and the `a1e` log stays the evidence.
2. **AC 8 fails in every run, for both types.** In each run, at least one hat first tried to read the dossier and both lane files with a single compound Bash command inside the run folder: `ls -R`, `cat`, a `for` loop over `scout/*`, or a shell variable. The hats run in the background, where Claude Code cannot ask ("Permission prompts are not available in this context"), and `acceptEdits` does not allow such a command by itself, so it was denied. Nine of the fifteen hats had one such denial, and each then read the same files with `Read`. Plain `cat`, `ls` and `wc` commands ran.
3. **The Opus parent searched for the link-check helper.** In `a1o`, after the hats replied, the parent ran `find . -name link_check.py` from the scratch folder, then `find <scratch>/build-Explore -name link_check.py`, which searches the folder holding the plugin it loaded. Both were denied, and it recorded that the link check was not run. The pasted evidence rules tell the reader to run the link check, and the draft told the parent that the link check "belongs to you and to `scout`", while `challenge` carries no helper. AC 8 fails on a search of `<root>` even when it is denied.
4. **A hat's reply is a task notification.** AC 4 reads a hat's reply from its `Agent` call's `tool_result`. In 2.1.322 that result is only a launch notice, and the reply arrives in the `task_notification` described above. In every run, the three `Agent` calls still share one `message.id`.
5. **AC 1's comparison on its own terms.** Every `Explore` hat, on Sonnet and on Opus, wrote nothing, ran only reading Bash commands, ran on the session's model and read the whole dossier, which are AC 3's checks. Every reply, of either type, meets AC 4. The one word from AC 4's list is in `a1e`'s Customer reply, "A missed reminder kills a plant", which is about a plant, not a verdict on the idea. At Sonnet the two types research the same amount, and `Explore` uses about two thirds of the tokens. On Opus, `Explore` hats ran on Opus, which settles A4, and researched much more. By AC 1's rule `Explore` would be kept. But AC 1 also applies AC 8 to every run, and the `general-purpose` hats fail it too, so AC 2 waits for Julien's decision.
6. **The parent also condenses the round (AC 5, for information).** Every `round-1.md` has the template's headings in order and opens with "What holds up". In the four Sonnet runs, the parent wrote each hat's concerns in fewer words than the hat's reply. In `a1o` it copied them. Every parent added "Round 1 proposes:" notes under the readings it touched, and the Opus parent also added an index of the hats' new entries to the dossier's Evidence section.

## Runs

### `a1e-explore-sonnet`: Explore hats, Sonnet (AC 1)

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 13 | result events: 4 | cost: 0.82
- plugin: coaster coaster@inline 0.1.0-pre.11; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: ['Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && cat dossier.md && for f in scout/*; do echo "=== $f"; cat "$f"; done']
- parent:
  - `Bash: find . -path ./.git -prune -o -type f -print | head -50`
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder && cat dossier.md; wc -c scout/*`
  - `Bash: cd . && pwd && ls docs/prospects/houseplant-watering-reminder`
  - `Agent: Skeptic hat review` (Explore)
  - `Agent: Rival hat review` (Explore)
  - `Agent: Customer hat review` (Explore)
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md (offset 96, limit 40)`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && wc -c dossier.md scout/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app no account no subscription iPhone unlimited plants`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
- Rival hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && cat dossier.md && for f in scout/*; do echo "=== $f"; cat "$f"; done`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app iOS no account no subscription`
  - `WebSearch: Planta app free plan plant limit reminders 2026`
- Customer hat:
  - `Bash: cd "./docs/prospects/houseplant-watering-reminder"; ls -R .; wc -c dossier.md scout/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
  - `WebFetch: https://github.com/ruuda/sempervivum`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `a1o-explore-opus`: Explore hats, Opus (AC 1)

- model: claude-opus-5-5 | cc: 2.1.322 | turns: 15 | result events: 4 | cost: 2.49
- plugin: coaster coaster@inline 0.1.0-pre.11; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: ['Bash: D=./docs/prospects/houseplant-watering-reminder; ls -R $D; cat $D/dossier.md $D/scout/landscape.md $D/scout/demand.md', 'Bash: D=./docs/prospects/houseplant-watering-reminder; ls -R $D; cat $D/dossier.md $D/scout/landscape.md $D/scout/demand.md', 'Bash: D=./docs/prospects/houseplant-watering-reminder; ls -R $D; cat $D/dossier.md $D/scout/landscape.md $D/scout/demand.md', 'Bash: cd <scratch> && find . -name link_check.py 2>/dev/null | head', 'Bash: find <scratch>/build-Explore -name link_check.py']
- parent:
  - `Bash: find docs -type f | head -50`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Agent: Skeptic hat challenge` (Explore)
  - `Agent: Rival hat challenge` (Explore)
  - `Agent: Customer hat challenge` (Explore)
  - `Bash: cd <scratch> && find . -name link_check.py 2>/dev/null | head`
  - `Bash: find <scratch>/build-Explore -name link_check.py`
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Bash: D=./docs/prospects/houseplant-watering-reminder; ls -R $D; cat $D/dossier.md $D/scout/landscape.md $D/scout/demand.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
  - `WebSearch: reddit houseplants how do you remember to water your plants app`
  - `WebSearch: free plant watering reminder iPhone no account no subscription app`
  - `WebFetch: https://apps.apple.com/us/app/remindew/id1546126954`
  - `WebFetch: https://apps.apple.com/app/id6769872312`
  - `WebSearch: Greg plant app notification time setting reminders daily digest`
  - `WebFetch: https://ruuda.github.io/sempervivum/`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
  - `WebFetch: https://github.com/ruuda/sempervivum/commits/master`
  - `WebFetch: https://raw.githubusercontent.com/ruuda/sempervivum/master/README.md`
  - `WebFetch: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/`
- Rival hat:
  - `Bash: D=./docs/prospects/houseplant-watering-reminder; ls -R $D; cat $D/dossier.md $D/scout/landscape.md $D/scout/demand.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: Planta app free version watering reminders plant limit notification time setting`
  - `WebSearch: Greg plant app free watering reminders pricing subscription`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebFetch: https://apps.apple.com/us/app/id1512912236?l=en-us`
  - `WebFetch: https://apple.co/3241Dmb`
  - `WebFetch: https://apps.apple.com/us/app/planta-keep-your-plants-alive/id1410126781`
  - `WebSearch: iOS 26 Reminders app plant watering recurring reminder Apple Intelligence suggestions`
  - `WebSearch: getplanta.com help what is included in Planta free vs premium watering reminders`
- Customer hat:
  - `Bash: D=./docs/prospects/houseplant-watering-reminder; ls -R $D; cat $D/dossier.md $D/scout/landscape.md $D/scout/demand.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: reddit how do you remember to water houseplants app or spreadsheet`
  - `WebSearch: iOS Safari web push notifications home screen web app requirements`
  - `WebSearch: Planta free version watering reminders limit what's free`
  - `WebFetch: https://support.getplanta.com/do-planta-offer-a-free-trial-of-premium`
  - `WebFetch: https://www.mumsnet.com/talk/gardening/5484261-looking-for-an-app-to-remind-me-to-water`
  - `WebFetch: https://apps.apple.com/us/app/plant-watering-care-ploi/id1491443538`
  - `WebFetch: https://apple.co/3L8Mzd7`
  - `WebFetch: https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers`
  - `WebSearch: Greg plant app free vs Greg Plus watering reminders free plant limit`
  - `WebFetch: https://apps.apple.com/app/id1474539700`
  - `WebFetch: https://apps.apple.com/us/app/ploi-plant-care/id1624280409`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `a1g-gp-sonnet`: general-purpose hats, Sonnet (AC 1)

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 15 | result events: 4 | cost: 0.98
- plugin: coaster coaster@inline 0.1.0-pre.11; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: ['Bash: cd ./docs/prospects/houseplant-watering-reminder; ls -R; cat dossier.md; for f in scout/*; do echo "=== $f"; cat "$f"; done']
- parent:
  - `Bash: find . -path ./.git -prune -o -type f -print | head -50`
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder && cat dossier.md; echo ======; cat scout/landscape.md; echo =====; cat scout/demand.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md (offset 75, limit 50)`
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder && ls; ls challenge 2>&1 | head`
  - `Agent: Skeptic hat review` (general-purpose)
  - `Agent: Rival hat review` (general-purpose)
  - `Agent: Customer hat review` (general-purpose)
  - `Bash: mkdir -p ./docs/prospects/houseplant-watering-reminder/challenge`
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder; ls -R .; cat dossier.md`
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder/scout; cat landscape.md demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription unlimited plants`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
- Rival hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder; ls -R; cat dossier.md; for f in scout/*; do echo "=== $f"; cat "$f"; done`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: Planta app free plan watering reminders unlimited plants 2026`
  - `WebSearch: free plant watering reminder iPhone no account no subscription app`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Bash: ls -R ./docs/prospects/houseplant-watering-reminder`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
  - `WebSearch: reddit how do you remember to water houseplants app or calendar reminder`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `a2e-explore-sonnet`: Explore hats, Sonnet, a second run

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 15 | result events: 4 | cost: 0.87
- plugin: coaster coaster@inline 0.1.0-pre.11; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: ['Bash: D=./docs/prospects/houseplant-watering-reminder; cat $D/dossier.md; echo ======; cat $D/scout/landscape.md; echo ======; cat $D/scout/demand.md; ls -R $D']
- parent:
  - `Bash: find . -path ./.git -prune -o -type f -print | head -50`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `Agent: Skeptic hat review` (Explore)
  - `Agent: Rival hat review` (Explore)
  - `Agent: Customer hat review` (Explore)
  - `Bash: mkdir -p ./docs/prospects/houseplant-watering-reminder/challenge`
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && cat dossier.md scout/*.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app no account no subscription iPhone`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
- Rival hat:
  - `Bash: D=./docs/prospects/houseplant-watering-reminder; cat $D/dossier.md; echo ======; cat $D/scout/landscape.md; echo ======; cat $D/scout/demand.md; ls -R $D`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: Planta app free plan watering reminders unlimited plants notification settings quiet hours`
  - `WebSearch: free plant watering reminder iOS app no account no subscription unlimited plants`
- Customer hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && cat dossier.md scout/landscape.md scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
  - `WebSearch: reddit how do you remember to water your houseplants reminder calendar app`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `a2g-gp-sonnet`: general-purpose hats, Sonnet, a second run

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 14 | result events: 4 | cost: 0.98
- plugin: coaster coaster@inline 0.1.0-pre.11; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: ['Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && cat dossier.md && for f in scout/*; do echo "=== $f"; cat "$f"; done', 'Bash: cd "./docs/prospects/houseplant-watering-reminder/" && ls -R . && cat dossier.md && for f in scout/*; do echo "=== $f"; cat "$f"; done', 'Bash: cd "./docs/prospects/houseplant-watering-reminder"; ls -R .; cat dossier.md; for f in scout/*; do echo "=== $f"; cat "$f"; done']
- parent:
  - `Bash: find . -path ./.git -prune -o -type f -print | head -50`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `Agent: Skeptic hat review` (general-purpose)
  - `Agent: Rival hat review` (general-purpose)
  - `Agent: Customer hat review` (general-purpose)
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder/ && ls -R . && cat dossier.md && for f in scout/*; do echo "=== $f"; cat "$f"; done`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
  - `WebFetch: https://github.com/MDeLuise/plant-it`
- Rival hat:
  - `Bash: cd "./docs/prospects/houseplant-watering-reminder/" && ls -R . && cat dossier.md && for f in scout/*; do echo "=== $f"; cat "$f"; done`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free plant watering reminder iPhone no account no subscription unlimited plants app`
  - `WebSearch: Planta app free plan notification time quiet hours batch reminders settings`
- Customer hat:
  - `Bash: cd "./docs/prospects/houseplant-watering-reminder"; ls -R .; cat dossier.md; for f in scout/*; do echo "=== $f"; cat "$f"; done`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `ToolSearch: select:WebSearch,WebFetch`
  - `WebSearch: free houseplant watering reminder app no account no subscription iPhone reddit`
  - `WebSearch: iOS Reminders app or calendar recurring reminder water plants how to`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

## Slice 002-04: the hat agents, local runs (2026-11-12)

Runs of `/coaster:challenge challenge this` from a `--plugin-dir` copy of this branch's `hosts/claude` at `0.1.0-pre.12`, set up as AC 1's runs were. Each `init` event lists `coaster@inline` `0.1.0-pre.12`, the built-in plugins, and the agents `coaster:skeptic`, `coaster:rival` and `coaster:customer`.

**How the system prompts were checked.** Each hat's `Agent` call is matched to its task by the `task_started` event, and the task to its transcript in the profile, at `projects/<run>/<session>/subagents/agent-<task id>.jsonl`. The transcript's `prompt_snapshot` attachment holds the system prompt. A script kept outside the repository compares it with the body of `agents/<hat>.md` in the loaded build, and cuts the four parts from that file for the same four-level comparison as AC 6 above.

### First runs, at `b6052c4`: `f1s` (Sonnet) and `f1o` (Opus)

The build was the working tree that became `b6052c4`, byte for byte (`diff -rq`). Every system prompt matched its agent file, nothing was denied, and no hat wrote or ran Bash. But each `f1s` prompt added "(lane files are under scout/ beside it)", which is not on AC 5's list of what a prompt may hold. Slice 002-04's compliance review held it to that list, so, as ADR-0003 says, `challenge`'s wording was tightened to "and nothing else" and both runs were repeated. The same change asks the parent to copy each hat's section without shortening it, because the `f1s` parent had shortened them. These runs are not judged. Their hats are in the table below for comparison.

### Judged runs, at `cbe06fc`: `f2s` (Sonnet) and `f2o` (Opus)

The build was a `git archive` of `hosts/claude` at commit `cbe06fc`, identical to the committed tree (`diff -rq`). In both runs:

- **System prompts.** For every hat, the first block of its system prompt equals its agent file's body, apart from surrounding whitespace. All four parts match exactly.
- **`Agent` prompts.** Each prompt, with local paths trimmed:
  - `f2s-agents-sonnet`, Skeptic: `Hat: skeptic. Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md. Earlier rounds: none. Today's date: 2026-11-12.`
  - `f2s-agents-sonnet`, Rival: `Hat: rival. Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md. Earlier rounds: none. Today's date: 2026-11-12.`
  - `f2s-agents-sonnet`, Customer: `Hat: customer. Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md. Earlier rounds: none. Today's date: 2026-11-12.`
  - `f2o-agents-opus`, Skeptic: `Hat: skeptic` ⏎ `Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md` ⏎ `Earlier rounds: none` ⏎ `Today's date: 2026-11-12`
  - `f2o-agents-opus`, Rival: `Hat: rival` ⏎ `Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md` ⏎ `Earlier rounds: none` ⏎ `Today's date: 2026-11-12`
  - `f2o-agents-opus`, Customer: `Hat: customer` ⏎ `Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md` ⏎ `Earlier rounds: none` ⏎ `Today's date: 2026-11-12`

  Each holds the hat's name, the dossier path, "Earlier rounds: none" and the date, and nothing else.
- **Tools, model and reading.** The three `Agent` calls in each run share one `message.id`. No hat made a `Bash`, `Write`, `Edit` or `NotebookEdit` call, or called `ToolSearch`. Each hat ran on the session's model and read the whole dossier with `Read`. Five of the six made one `Glob` call inside the dossier's folder.
- **Denials and `<root>`.** `permission_denials` is empty in both runs. No tool call by the parent or a hat names the build folder. Neither parent looked for `link_check.py`, and both rounds say the next `scout` pass runs the link check.
- **The rounds.** Each run wrote one `challenge/round-1.md`, with the template's headings in order, opening with "What holds up". Both parents copied each hat's concerns and lens lines as the hat replied them, and said every disposition is proposed. Each added "Round 1 proposes:" notes under the readings it touched, and the Opus parent also indexed the hats' new entries in the Evidence section. One slip: the Sonnet round ends by saying those notes "are not yet added", although its dossier has them.
- **Replies.** Every reply meets AC 4, with no word from its list. Every `grounded` entry cites a page the same hat opened.

The hats, beside the first runs and AC 1's runs:

| Run | Hat | Type, model | Whole dossier | Writes, Bash | Searches | Pages opened | New entries (grounded) | AC 4 | Tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| `f2s-agents-sonnet` | Skeptic | `coaster:skeptic`, sonnet-5-5 | yes | 0, 0 | 2 | 1 | 4 (1) | pass | 23k | 36s |
| `f2s-agents-sonnet` | Rival | `coaster:rival`, sonnet-5-5 | yes | 0, 0 | 2 | 0 | 3 (0) | pass | 23k | 39s |
| `f2s-agents-sonnet` | Customer | `coaster:customer`, sonnet-5-5 | yes | 0, 0 | 2 | 0 | 6 (0) | pass | 23k | 38s |
| `f2o-agents-opus` | Skeptic | `coaster:skeptic`, opus-5-5 | yes | 0, 0 | 4 | 6 | 8 (6) | pass | 31k | 90s |
| `f2o-agents-opus` | Rival | `coaster:rival`, opus-5-5 | yes | 0, 0 | 2 | 6 | 7 (6) | pass | 29k | 102s |
| `f2o-agents-opus` | Customer | `coaster:customer`, opus-5-5 | yes | 0, 0 | 5 | 9 | 9 (7) | pass | 35k | 126s |
| `f1s-agents-sonnet` | Skeptic | `coaster:skeptic`, sonnet-5-5 | yes | 0, 0 | 1 | 1 | 3 (1) | pass | 22k | 37s |
| `f1s-agents-sonnet` | Rival | `coaster:rival`, sonnet-5-5 | yes | 0, 0 | 1 | 0 | 5 (0) | pass | 21k | 40s |
| `f1s-agents-sonnet` | Customer | `coaster:customer`, sonnet-5-5 | yes | 0, 0 | 1 | 0 | 1 (0) | pass | 21k | 41s |
| `f1o-agents-opus` | Skeptic | `coaster:skeptic`, opus-5-5 | yes | 0, 0 | 3 | 6 | 8 (6) | pass | 29k | 93s |
| `f1o-agents-opus` | Rival | `coaster:rival`, opus-5-5 | yes | 0, 0 | 3 | 6 | 5 (4) | pass | 29k | 94s |
| `f1o-agents-opus` | Customer | `coaster:customer`, opus-5-5 | yes | 0, 0 | 2 | 4 | 5 (4) | pass ('kill' literal, about plants) | 26k | 67s |
| `a1e-explore-sonnet` | Skeptic | `Explore`, sonnet-5-5 | yes | 0, 1 | 1 | 1 | 3 (1) | pass | 32k | 46s |
| `a1e-explore-sonnet` | Rival | `Explore`, sonnet-5-5 | yes | 0, 1 | 2 | 0 | 3 (0) | pass | 33k | 46s |
| `a1e-explore-sonnet` | Customer | `Explore`, sonnet-5-5 | yes | 0, 1 | 1 | 1 | 3 (1) | pass ('kill' literal, about plants) | 32k | 47s |
| `a1g-gp-sonnet` | Skeptic | `general-purpose`, sonnet-5-5 | yes | 0, 2 | 1 | 1 | 3 (1) | pass | 47k | 39s |
| `a1g-gp-sonnet` | Rival | `general-purpose`, sonnet-5-5 | yes | 0, 1 | 2 | 0 | 3 (0) | pass | 50k | 43s |
| `a1g-gp-sonnet` | Customer | `general-purpose`, sonnet-5-5 | yes | 0, 1 | 2 | 0 | 3 (0) | pass | 50k | 49s |
| `a1o-explore-opus` | Skeptic | `Explore`, opus-5-5 | yes | 0, 1 | 3 | 9 | 9 (7) | pass | 42k | 93s |
| `a1o-explore-opus` | Rival | `Explore`, opus-5-5 | yes | 0, 1 | 4 | 4 | 7 (4) | pass | 42k | 96s |
| `a1o-explore-opus` | Customer | `Explore`, opus-5-5 | yes | 0, 1 | 4 | 7 | 7 (5) | pass | 44k | 93s |

Per hat in the judged runs, the Sonnet agents made 2 searches, opened 0.3 pages and returned 4.3 entries (0.3 `grounded`), against 1.5 to 1.7 searches, 0.5 pages and 3 entries for the built-in types at Sonnet. The Opus agents made 3.7 searches, opened 7 pages and returned 8 entries (6.3 `grounded`), against `Explore`'s 3.7, 6.7 and 7.7 (5.3). The Sonnet agents used about 23k tokens a hat, against 33k for `Explore` and 49k for `general-purpose`.

### `f2s-agents-sonnet`: the hat agents, Sonnet, at cbe06fc (002-04, judged)

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 12 | result events: 4 | cost: 0.67
- plugin: coaster coaster@inline 0.1.0-pre.12; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: []
- parent:
  - `Bash: find . -path ./.git -prune -o -type f -print | head -50`
  - `Bash: cd ./docs/prospects/houseplant-watering-reminder && cat dossier.md && ls -R`
  - `Agent: Skeptic hat review` (coaster:skeptic)
  - `Agent: Rival hat review` (coaster:rival)
  - `Agent: Customer hat review` (coaster:customer)
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription unlimited plants`
  - `WebSearch: reddit "how do you remember to water" houseplants app reminder`
  - `WebFetch: https://github.com/ruuda/sempervivum`
- Rival hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
  - `WebSearch: Apple Reminders repeating reminders water plants; Google Home / Alexa plant watering reminder built in`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: reddit houseplants what app do you use to remember to water plants`
  - `WebSearch: free plant watering reminder iPhone no account no subscription app`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `f2o-agents-opus`: the hat agents, Opus, at cbe06fc (002-04, judged)

- model: claude-opus-5-5 | cc: 2.1.322 | turns: 14 | result events: 4 | cost: 2.03
- plugin: coaster coaster@inline 0.1.0-pre.12; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: []
- parent:
  - `Bash: find docs -type f | head -50`
  - `Agent: Skeptic hat challenge` (coaster:skeptic)
  - `Agent: Rival hat challenge` (coaster:rival)
  - `Agent: Customer hat challenge` (coaster:customer)
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebSearch: reddit how do you remember to water your houseplants app`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
  - `WebFetch: https://apps.apple.com/iq/app/remindew/id1546126954`
  - `WebFetch: https://apps.apple.com/app/id6769872312`
  - `WebFetch: https://apps.apple.com/app/id6759828509`
  - `WebSearch: Planta app change reminder notification time of day setting`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
  - `WebSearch: iOS web push notifications PWA home screen requirement Safari limitations 2026`
- Rival hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/*.md (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: Planta app free version plant limit reminders notification time setting`
  - `WebSearch: Greg plant app free no plant limit watering reminders pricing`
  - `WebFetch: https://apps.apple.com/us/app/id1512912236`
  - `WebFetch: https://apps.apple.com/us/app/plantir-plant-reminders/id1539300483`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebFetch: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/`
  - `WebFetch: https://apps.apple.com/us/app/planta-plant-garden-care/id1410126781`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: reddit houseplants how do you remember to water app deleted subscription`
  - `WebSearch: Planta app reminder notification time setting "time of day" watering reminders`
  - `WebSearch: iOS web push notifications home screen web app requirements Safari 16.4`
  - `WebFetch: https://apps.apple.com/app/id6763580398`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
  - `WebFetch: https://apps.apple.com/app/id6755929354`
  - `WebFetch: https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers`
  - `WebSearch: Notification Triggers API showTrigger scheduled notifications status Chrome abandoned Safari support`
  - `WebFetch: https://developer.chrome.com/docs/web-platform/notification-triggers`
  - `WebFetch: https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide`
  - `WebSearch: site:reddit.com r/houseplants watering reminder app recommendation free no subscription`
  - `WebFetch: https://apps.apple.com/us/app/tierra/id1519045472`
  - `WebFetch: https://apple.co/3L8Mzd7`
  - `WebFetch: https://apps.apple.com/us/app/ploi-plant-care/id1624280409`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `f1s-agents-sonnet`: the hat agents, Sonnet, at b6052c4 (002-04, first run)

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 12 | result events: 4 | cost: 0.60
- plugin: coaster coaster@inline 0.1.0-pre.12; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: []
- parent:
  - `Bash: find . -path ./.git -prune -o -type f -print | head -50`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Agent: Skeptic hat review` (coaster:skeptic)
  - `Agent: Rival hat review` (coaster:rival)
  - `Agent: Customer hat review` (coaster:customer)
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder PWA no account open source github`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
- Rival hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app iPhone no account no subscription`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app no account no subscription iPhone`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `f1o-agents-opus`: the hat agents, Opus, at b6052c4 (002-04, first run)

- model: claude-opus-5-5 | cc: 2.1.322 | turns: 14 | result events: 4 | cost: 1.76
- plugin: coaster coaster@inline 0.1.0-pre.12; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: []
- parent:
  - `Bash: find docs -type f | sort`
  - `Agent: Skeptic hat challenge` (coaster:skeptic)
  - `Agent: Rival hat challenge` (coaster:rival)
  - `Agent: Customer hat challenge` (coaster:customer)
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebSearch: reddit how do you remember to water houseplants app`
  - `WebSearch: free plant watering reminder iPhone no account no subscription app`
  - `WebFetch: https://apps.apple.com/iq/app/remindew/id1546126954`
  - `WebFetch: https://apps.apple.com/app/id6769872312`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
  - `WebSearch: Planta app notification time setting reminders "time of day" summary`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
  - `WebFetch: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/`
- Rival hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: Planta app reminder notification time setting "reminder time" premium free plants limit`
  - `WebSearch: Greg plant app free unlimited plants watering reminders pricing`
  - `WebFetch: https://apps.apple.com/us/app/id1512912236?l=en-us`
  - `WebFetch: https://support.getplanta.com/do-planta-offer-a-free-trial-of-premium`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebFetch: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/`
  - `WebSearch: Planta free version how many plants limit watering reminders free`
  - `WebFetch: https://support.apple.com/guide/iphone/set-up-reminders-iph1ac0b6d0b/ios`
  - `WebFetch: https://support.apple.com/guide/iphone/set-a-reminder-iph2e2b7b9a2/ios`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: reddit houseplants how do you remember to water app`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebSearch: Planta app notification time setting reminders "time of day"`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
  - `WebFetch: https://www.mumsnet.com/talk/gardening/5484261-looking-for-an-app-to-remind-me-to-water`
  - `WebFetch: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

## Slice 002-02: the installed runs (2026-11-12)

`0.1.0-pre.12` was pushed to `main` at `8dbc2f7`, and the test profile updated to it with `claude plugin marketplace update coaster` and `claude plugin update coaster@coaster`. The installed folder matches `hosts/claude` (`diff -rq`). `claude plugin list` showed coaster enabled and the three synced plugins disabled, and the profile's deny rules still block both research skills. Two runs of `/coaster:challenge challenge this`, with no `--plugin-dir` and no `--settings`: `i1s` on Sonnet and `i1o` on Opus. `<root>` is the `path` the `init` event gives for coaster, the profile's `plugins/cache/coaster/coaster/0.1.0-pre.12`.

- **AC 8, the load.** Every `init` event lists `coaster@coaster` `0.1.0-pre.12` and the five built-in plugins, and nothing else. Its agents include `coaster:skeptic`, `coaster:rival` and `coaster:customer`. Its skills list holds `deep-research` and `anthropic-skills:deep-research`, both blocked by the profile's deny rules, and no grilling skill. No `Skill` call was made. `permission_denials` is empty in every `result` event, and no tool call reads, lists or searches `<root>`. Every hat search ran.
- **AC 3.** In each run the three `Agent` calls have the `subagent_type`s `coaster:skeptic`, `coaster:rival` and `coaster:customer` and share one `message.id`. No hat made a `Bash`, `Write`, `Edit` or `NotebookEdit` call. Each hat's own assistant events are on the session's model, and each hat read the whole dossier with `Read`. Each run wrote one `challenge/round-1.md`, the only file under `challenge/`.
- **AC 6, the system prompts.** For every hat in both runs, the first block of its system prompt equals the installed `agents/<hat>.md` body, apart from surrounding whitespace. All four parts match exactly.
- **AC 6, the `Agent` prompts.** With local paths trimmed:
  - `i1s-installed-sonnet`, Skeptic: `Hat: skeptic. Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md (lane files are in the scout/ folder beside it). Earlier rounds: none. Today: 2026-11-12.`
  - `i1s-installed-sonnet`, Rival: `Hat: rival. Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md (lane files are in the scout/ folder beside it). Earlier rounds: none. Today: 2026-11-12.`
  - `i1s-installed-sonnet`, Customer: `Hat: customer. Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md (lane files are in the scout/ folder beside it). Earlier rounds: none. Today: 2026-11-12.`
  - `i1o-installed-opus`, Skeptic: `Hat: skeptic` ⏎ `Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md` ⏎ `Earlier rounds: none` ⏎ `Today: 2026-11-12`
  - `i1o-installed-opus`, Rival: `Hat: rival` ⏎ `Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md` ⏎ `Earlier rounds: none` ⏎ `Today: 2026-11-12`
  - `i1o-installed-opus`, Customer: `Hat: customer` ⏎ `Dossier: ./docs/prospects/houseplant-watering-reminder/dossier.md` ⏎ `Earlier rounds: none` ⏎ `Today: 2026-11-12`

  The `i1o` prompts hold only the hat's name, the dossier path, "Earlier rounds: none" and the date. Each `i1s` prompt also says "(lane files are in the scout/ folder beside it)", the same kind of note as in `f1s`, though `cbe06fc` added "and nothing else: no notes". The note only says where the dossier's own files are. It restates no part of the rules and adds no rule, limit, lens instruction or reply shape, but it is not on the list the amended AC 6 allows.
- **AC 4.** Every reply leads with what holds up, covers the six lenses, has at most five concerns, each with why it matters, a cheapest test and an urgency, and uses no word from AC 4's list. Every entry carries the hat's prefix, and every `grounded` entry cites a page the same hat opened. One entry breaks the evidence rules' format: `i1s`'s Skeptic tagged S-01 `[grounded-lead, unverified until opened]`, not one of the five tags. The entry itself says the apps are search summaries and stay `unverified`, and it carries links and a date.
- **AC 5.** Each round has the template's headings in order and opens with "What holds up". Every concern and lens line under a hat's heading appears in that hat's reply. Each says all its dispositions are proposed. In each dossier no line was removed or changed: `i1s` added two "Round 1 proposes:" notes, and `i1o` added four, plus an index of the hats' new entries in the Evidence section. `i1o`'s round adds two headings of its own: "Parent's notes on the evidence" and "Concern groups".

The hats:

| Run | Hat | Type, model | Whole dossier | Writes, Bash | Searches | Pages opened | New entries (grounded) | AC 4 | Tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| `i1s-installed-sonnet` | Skeptic | `coaster:skeptic`, sonnet-5-5 | yes | 0, 0 | 2 | 1 | 3 (1) | CHECK | 23k | 36s |
| `i1s-installed-sonnet` | Rival | `coaster:rival`, sonnet-5-5 | yes | 0, 0 | 3 | 0 | 3 (0) | pass | 24k | 44s |
| `i1s-installed-sonnet` | Customer | `coaster:customer`, sonnet-5-5 | yes | 0, 0 | 2 | 0 | 4 (0) | pass | 22k | 33s |
| `i1o-installed-opus` | Skeptic | `coaster:skeptic`, opus-5-5 | yes | 0, 0 | 3 | 6 | 8 (5) | pass | 29k | 88s |
| `i1o-installed-opus` | Rival | `coaster:rival`, opus-5-5 | yes | 0, 0 | 3 | 3 | 5 (3) | pass | 28k | 84s |
| `i1o-installed-opus` | Customer | `coaster:customer`, opus-5-5 | yes | 0, 0 | 3 | 6 | 6 (4) | pass | 30k | 92s |

`i1s`'s Skeptic returned four entries; the table counts three because S-01's tag is not one of the five.

### `i1s-installed-sonnet`: installed 0.1.0-pre.12, Sonnet (002-02, ACs 3 to 8)

- model: claude-sonnet-5-5 | cc: 2.1.322 | turns: 12 | result events: 4 | cost: 0.69
- plugin: coaster coaster@coaster 0.1.0-pre.12; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: []
- parent:
  - `Bash: git status --short; find docs -maxdepth 4 | head -50`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Agent: Skeptic hat` (coaster:skeptic)
  - `Agent: Rival hat` (coaster:rival)
  - `Agent: Customer hat` (coaster:customer)
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app no account no subscription iPhone open source PWA`
  - `WebSearch: reddit houseplants "what app do you use" remind water plants deleted app subscription`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
- Rival hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app no account no subscription iOS`
  - `WebSearch: Planta app notification time of day setting reminders batch daily`
  - `WebSearch: Apple Reminders Google Tasks Alexa houseplant watering recurring reminder plants Reminders app feature`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: **/* (in ./docs/prospects/houseplant-watering-reminder)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: free plant watering reminder app no account no subscription iPhone`
  - `WebSearch: reddit how do you remember to water your plants calendar reminder app`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

### `i1o-installed-opus`: installed 0.1.0-pre.12, Opus (002-02, ACs 3 to 8)

- model: claude-opus-5-5 | cc: 2.1.322 | turns: 15 | result events: 4 | cost: 1.80
- plugin: coaster coaster@coaster 0.1.0-pre.12; built-in: cc-plugin-agents-md, cc-plugin-telemetry, cc-plugin-privacy, cc-plugin-plugin-authoring, cc-plugin-easel
- research/grill skills: ['deep-research', 'anthropic-skills:deep-research'] (blocked by the profile's deny rules)
- denials: []
- parent:
  - `Bash: find docs -type f | head -50`
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Agent: Skeptic hat round 1` (coaster:skeptic)
  - `Agent: Rival hat round 1` (coaster:rival)
  - `Agent: Customer hat round 1` (coaster:customer)
  - `Write: ./docs/prospects/houseplant-watering-reminder/challenge/round-1.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Edit: ./docs/prospects/houseplant-watering-reminder/dossier.md`
- Skeptic hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebFetch: https://github.com/ruuda/sempervivum`
  - `WebSearch: reddit houseplants app remind water free no subscription iPhone`
  - `WebFetch: https://www.janeperrone.com/blog/2023/9/20/plant-apps`
  - `WebFetch: https://apps.apple.com/app/id6759828509`
  - `WebFetch: https://apps.apple.com/app/id6759524664`
  - `WebSearch: site:reddit.com houseplants "watering app" stopped using OR deleted OR notifications`
  - `WebFetch: https://www.popsci.com/diy/are-plant-care-apps-good/`
  - `WebFetch: https://ruuda.github.io/sempervivum/`
  - `WebSearch: webkit blog web push iOS 16.4 home screen web apps`
- Rival hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/*`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: Planta app free version reminders limit plants premium what's included`
  - `WebSearch: Greg plant app free unlimited plants watering reminders notification time setting`
  - `WebFetch: https://apps.apple.com/us/app/plantir-plant-reminders/id1539300483`
  - `WebFetch: https://apps.apple.com/us/app/planta-plant-garden-care/id1410126781`
  - `WebSearch: Planta app change reminder notification time setting help`
  - `WebFetch: https://support.getplanta.com/im-not-getting-notifications-task-reminders`
- Customer hat:
  - `Read: ./docs/prospects/houseplant-watering-reminder/dossier.md`
  - `Glob: docs/prospects/houseplant-watering-reminder/**/* (in .)`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/landscape.md`
  - `Read: ./docs/prospects/houseplant-watering-reminder/scout/demand.md`
  - `WebSearch: reddit houseplants watering app stopped using just check soil instead of schedule`
  - `WebSearch: iOS home screen web app push notifications support Safari 16.4 limitations`
  - `WebFetch: https://www.popsci.com/diy/are-plant-care-apps-good/`
  - `WebFetch: https://www.indiehackers.com/post/the-product-decision-behind-stop-watering-every-plant-on-sunday-in-growbook-b0e8fdf5f1`
  - `WebFetch: https://www.producthunt.com/p/leafy-3/leafy-5`
  - `WebSearch: Notification Triggers API showTrigger abandoned scheduled local notifications web PWA without server`
  - `WebFetch: https://web.dev/notification-triggers`
  - `WebFetch: https://developer.chrome.com/docs/web-platform/notification-triggers`
  - `WebFetch: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/`

Files under `docs/` after the run: `docs/prospects/houseplant-watering-reminder/challenge/round-1.md`, `docs/prospects/houseplant-watering-reminder/dossier.md`, `docs/prospects/houseplant-watering-reminder/scout/demand.md`, `docs/prospects/houseplant-watering-reminder/scout/landscape.md`

