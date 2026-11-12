---
status: Accepted
dependencies: [adr-0001]
last_verified: 2026-11-12
frame_review: true
---

# ADR-0003: Run challenge's hats as plugin agents

## Status

Accepted (2026-11-12). Julien chose Option F on 2026-11-12, after slice 002-02's AC 6 failed, and accepted this record the same day.

## Context

The packaged rules reached the hats intact in four runs of `challenge` out of five, so ADR-0001's kill criterion for the paste has fired. ADR-0001 renders each skill with its packaged text built in, and has `challenge`'s parent paste the hats' rules, the evidence rules and the round template into each hat's prompt. Its kill criterion reads: "A `challenge` run's log shows a hat prompt that omits or condenses the packaged rules. Option F then replaces the paste." Spec 002's slice 002-02 made that check. Its AC 7 asks Julien to choose, in a new ADR, between Option F and another remedy.

The runs, on Claude Code 2.1.322 from local builds of a draft that told the parent to paste the sections "unchanged, placeholders included" and not to "shorten, summarize or reword them" (slice 002-02's evidence, 2026-11-12):

- In one run of five, with Sonnet and `Explore` hats, the parent condensed the evidence rules and the round template in all three prompts. The evidence rules lost their opening note, two of their tables, and the rule to check links. The other four runs pasted every part byte for byte.
- In every run, at least one hat tried to read the dossier with a compound Bash command. Background hats cannot ask for permission, so it was denied. Nine of fifteen hats had one such denial.
- In the Opus run, the parent searched the loaded plugin's folder for `link_check.py`, because the pasted evidence rules say to run it. The search was denied.

Two probes on 2.1.322 (headless, `--plugin-dir`, `--allowedTools "WebSearch,WebFetch"`, one Sonnet session and one Opus session, 2026-11-12) ran a plugin agent with `tools: Read, Grep, Glob, WebSearch, WebFetch` and `model: inherit`. It was told to read a file, try `ls` with Bash, try to create a file, and run one web search:

- the `init` event listed it as `coaster:probe-hat` among the session's agents, and an `Agent` call with that `subagent_type` started it;
- it ran on the session's model in both sessions, Sonnet and Opus;
- its only tool calls were `Read` and `WebSearch`. It called `WebSearch` directly, without the `ToolSearch` step the built-in hats needed. It made no Bash or write call, and it replied that it had no tool for either;
- its `WebSearch` ran under the session's grant, with no denial;
- its system prompt held the agent file's body, equal to it apart from surrounding whitespace. The stream-json log does not carry it. The subagent's own transcript in the profile does, in an attachment of type `prompt_snapshot`.

`claude plugin validate --strict` passed on the package with an `agents/` folder added. A prototype of the build that renders three hat agents came to 188 lines.

## Decision Options Considered

### Option F1: Three plugin agents, one per hat
`hosts/claude/agents/skeptic.md`, `rival.md` and `customer.md` are rendered by the build. Each holds a short instruction to the hat, the hats' rules, that hat's own section, the evidence rules and the round template. `challenge` starts `coaster:skeptic`, `coaster:rival` and `coaster:customer` and gives each only the dossier path, the earlier rounds and the date.
- **Pros:** The rules no longer pass through the parent: the build writes them, and Claude Code loads them as each hat's system prompt. The parent still writes each hat's prompt, so that prompt stays under check, but it only has to carry the run's details. The `tools` line removes Bash and every write tool from the hats. That enforces "write nothing" and "run no helper", and ends the denied Bash reads. The log names each hat by its type.
- **Cons:** It widens the package and the build script. It adds three agents to the agent list of every session that has coaster installed. The check that each hat received its rules moves from the stream-json log to the subagent transcripts in the profile. Chat ignores plugin agents, so the chat path still writes paste-in prompts.

### Option F2: One plugin agent for all three hats
`hosts/claude/agents/hat.md` holds every hat's section, and the parent names the hat in each prompt.
- **Pros:** One rendered file and a smaller build change. One entry in the agent list.
- **Cons:** Which hat a subagent plays rests on the parent's prompt again. The log shows three identical types, so telling the hats apart means reading their prompts.

### Option P: Keep the paste and strengthen the wording
- **Pros:** No change to the package's shape or the build.
- **Cons:** The run that condensed already had explicit wording against it. Passing runs cannot show that the paste holds, because a condensation is a choice the parent can make in any run. The hats keep Bash, so the denials and the risk of a write remain.

## Recommended Decision

Option F1, chosen by Julien on 2026-11-12.

- **Rendering.** The build renders the three agents into `hosts/claude/agents/` from source. A short Claude-only instruction kept in source gives each agent its frontmatter and the hat's brief: read the whole dossier, write nothing, use the evidence rules only to format its own new entries, and reply with its section in the round template's shape. The link check and every change to the dossier belong to the parent and `scout`. The build appends four parts from the same files the skills use: the hats' rules, that hat's own section, the evidence rules and the round template. `--check` covers the agents like the skills.
- **Tools and model.** Each agent has `tools: Read, Grep, Glob, WebSearch, WebFetch` and `model: inherit`.
- **`challenge`.** In Claude Code, `challenge` starts the three agents in one message. Their prompts carry only the hat's name, the dossier path, the paths of earlier rounds and today's date, and restate, shorten or add to none of the hats' rules. It still writes `challenge/round-N.md` from their replies, and it says it does not run the link check, which belongs to `scout`. The chat path still writes one paste-in prompt per hat from `challenge`'s packaged sections. Those sections stay in the rendered skill for that path, for the grilling hand-off and for the round, so the parent still has the rules in front of it.
- **The release check.** "Each hat received the packaged rules intact" now has two halves, because the parent still writes each hat's prompt. Each hat's system prompt, in its subagent transcript, holds the four parts as the installed agent file renders them. And each hat's `Agent` prompt, recorded in full with local paths trimmed, carries only the items above, with at most one line asking the hat to begin, and states no rule, limit, lens instruction or reply shape of its own.
- **The build's bound.** ADR-0001's bound on the script, Claude-only and under 200 lines, stays. Its text changes widen from the skill-to-files map and the two helper paths to also include rendering the three agents from source.

ADR-0001 otherwise stands. Its Option A still renders every skill. This ADR replaces only the paste for the hats, which is what ADR-0001's kill criterion named Option F for.

## Consequences

**Becomes easier:**
- Trusting that each hat works from the full rules, which the build now writes and `--check` guards.
- Keeping hats from writing, running helpers or reading with Bash, since their tools exclude it.
- Telling the hats apart in a log, by `subagent_type`.

**Becomes harder:**
- The package and the build script grow, and the script sits closer to its 200-line bound.
- Every session with coaster installed lists three more agents. Their descriptions must keep the main model from starting them for other work.
- Checking a run means reading the subagent transcripts in the profile, not only the stream-json log.
- The Claude Code path and the chat path no longer give the hats their rules the same way.

## Assumptions

- **B1.** A plugin agent installed from the marketplace behaves as the `--plugin-dir` probes did: listed as `coaster:<name>`, limited to its `tools`, on the session's model, and with the file's body as its system prompt. ADR-0001 notes that the sibling packs already ship plugin agents. Slice 002-02's installed runs check it for coaster.
- **B2.** The main model does not start the hats for work outside `challenge` when their descriptions say they are only for it. R-04's activation test, which lands before the tag, can show a leak only if it tries. So its prompts include some that could pull in agents named `skeptic`, `rival` and `customer`, such as "be skeptical about this plan" or "how would a competitor react", and its record lists every `Agent` call.
- **B3.** Claude Code keeps recording a subagent's system prompt in its transcript. If it stops, the check falls back to comparing the installed agent files with `hosts/claude`, which proves what was installed but not what each hat received.
- **B4.** The parent follows the instruction to keep each hat's prompt to the run's details. That is wording, as in Option P, but a breach now shows in a short prompt checked against a list of what it may hold, and it is a kill criterion below.

## Kill criteria

- A hat's system prompt in its transcript omits or condenses any of the four parts of its installed agent file.
- A hat's `Agent` prompt restates, shortens or alters any of the four parts, or adds a rule, limit, lens instruction or reply shape of its own.
- A hat makes a Bash, `Write`, `Edit` or `NotebookEdit` call, so the `tools` line is not enforced.
- A hat reads, lists or searches the installed plugin's folder, with `Read`, `Glob` or `Grep`.
- A hat runs on a model other than the session's.
- The main model starts a coaster hat for work outside `challenge` in R-04's activation test.
- The build outgrows its 200-line bound.

A breach of the `Agent` prompt list is met first by tightening `challenge`'s wording and running again. It reopens this choice only if it recurs after that.

## Open questions

- How the chat path gives its hats their rules when it is built. It keeps the paste for now.
