# Context and Memory

Use this reference to minimize token waste while keeping the project restartable across long runs, subagents, compaction, and future threads.

## Core Rule

Treat chat history as working memory, not project memory. The repository is the durable source of truth. Context passed to any agent should be a curated working set assembled from repo docs, source files, current task scope, and recent validated results.

## Memory Tiers

Maintain these tiers separately:

- Active brief: the small current-task packet an agent needs now. Store it in `docs/ai/state.md` or pass it in a subagent prompt.
- Stable memory: architecture, feature map, decisions, roadmap, testing, demos, and runbooks in `docs/ai/`.
- Context index: `docs/ai/context-index.md`, mapping concepts, subsystems, commands, docs, and tests to paths. This prevents agents from pasting or rediscovering the same large context.
- Session notes: temporary findings from the current run or subagent. Promote only reusable facts.
- Archive: raw logs, long research notes, old plans, and superseded designs. Link to them; do not load by default.

## Required Context Docs

Add these docs if the project is large or long-running:

- `docs/ai/context-index.md`: short index of what to read for each subsystem, feature, workflow, command, and decision area.
- `docs/ai/objectives.md`: durable product goals, non-goals, constraints, success metrics, and current priority ordering.
- `docs/ai/memory.md`: curated long-term notes that are not naturally part of architecture or roadmap docs.
- `docs/ai/handoffs/`: optional dated handoff briefs for major milestones or compactions.

Do not duplicate stable facts across all files. Choose one owner document and link to it.

## Context Budgeting

Before loading or sending context, classify each item:

- Must include: current objective, constraints, acceptance criteria, owned files, known hazards, validation commands.
- Link only: stable docs, long logs, prior research, full roadmaps, old PR discussions.
- Omit: obsolete plans, raw command output after summarization, repeated boilerplate, unrelated docs, closed issues.

For the orchestrator:

- Start each major phase by reading `docs/ai/state.md`, `docs/ai/context-index.md`, and only the docs/files tied to the active task.
- Use a resume fast path after long runs: read current state, context index, recent ledger entries, branch status, and only the changed docs or files needed for the selected batch. Do not reload the full skill, full roadmap, or whole documentation tree unless the task requires it.
- Use `rg`/file search to retrieve facts instead of loading whole directories.
- Summarize noisy tool output into state docs or task notes, then stop carrying the raw output in the prompt.
- Replace stale summaries; do not append endlessly.
- Keep stable instructions in the skill or repo docs and pass subagents links plus a short task packet.
- Keep repeated status comments and PR updates delta-based. Link prior evidence instead of restating the full project background, complete test matrix, or unchanged roadmap.

For subagents:

- Give a narrow active brief instead of the full orchestrator context.
- Include paths to read, paths to avoid, owned scope, expected output, and acceptance criteria.
- Ask for deltas: facts found, files changed, commands run, risks, and next actions.
- For execution lanes, ask for artifact paths, command outcomes, timing, resource locks used, and concise failure evidence rather than raw logs.
- Forbid dumping long logs unless the logs are the deliverable.
- Require subagents to state which docs/files they actually relied on.

## Token Budget Protocol

Use token budget as an engineering resource:

- Spend orchestration tokens on decisions, integration, conflict resolution, and synthesis.
- Spend cheaper subagent tokens on bounded reading, execution, test discovery, artifact inspection, and well-scoped implementation.
- When spawning a batch, put stable boilerplate first and variable repo/task context later. Stable prefixes improve prompt-cache friendliness where platform caching applies.
- Give each worker a short active brief plus file paths. Require a concise artifact-backed report instead of a transcript.
- Prefer repository artifacts over chat memory for large outputs: reports, manifests, logs, screenshots, benchmark tables, and handoff briefs should be written to files and summarized by path.
- For long command sequences, decide explicitly whether the main thread should wait quietly, delegate an execution lane, or do unrelated critical-path work. Do not fill the main context with speculative progress commentary.
- At batch end, record the model/effort choices and any avoidable orchestrator-local heavy work in the utilization review.

## Codex Config Cost Controls

Use project or profile configuration to support this workflow when the repo is intended for long autonomous runs:

```toml
model_verbosity = "low"

[agents]
max_threads = 10
max_depth = 2
```

Guidance:

- `agents.max_threads = 10` matches the baseline you asked to standardize on for this skill.
- `agents.max_depth = 2` is required only when depth-1 workers should be able to spawn helper lanes. If unset, Codex defaults to depth 1 and depth-2 helper workflows are unavailable.
- `model_verbosity = "low"` can reduce status and final-answer output for Responses API providers; still write durable details into repo docs.
- Do not set `model_context_window` unless a provider/catalog mismatch requires it.
- Use profile files for personal experiments and project `.codex/config.toml` only for settings that should be reproducible for future agents.
- Keep subagent prompts stable and narrow. Static role instructions should come first; variable repo context should come later.
- Keep final user-facing status short. Put full command lists, artifact paths, and batch utilization details in `docs/ai/`.

## Long-Term Memory Pattern

Use session notes as a staging area and curated memory as a reviewed store:

1. Capture candidate notes during work only when they are likely to matter later.
2. Consolidate at phase end: dedupe, resolve conflicts, attach sources, and delete trivia.
3. Promote notes to the correct owner doc.
4. Add metadata for memory-only notes:

```text
id:
type: constraint | preference | invariant | decision | hazard | environment | workflow
claim:
source:
scope:
confidence:
last_verified:
supersedes:
expires:
tags:
linked_paths:
```

5. Prune or decay stale notes. A memory that is no longer true is worse than no memory.

Use `docs/ai/memory.md` only for durable facts that do not fit better in architecture, decisions, testing, demos, or roadmap docs.

## Objective Management

Keep objectives durable but compact:

- Store project-level goals and non-goals in `docs/ai/objectives.md`.
- Store current run goal and next actions in `docs/ai/state.md`.
- Store feature-level acceptance criteria in `docs/ai/feature-roadmaps.md`.
- When priorities change, update the owner document and add a decision-log entry if the change affects architecture, scope, or user-visible behavior.

Do not paste the full objective tree into every subagent prompt. Pass the relevant slice and link to the owner doc.

## Handoff Brief

Create a handoff brief before major pauses, compaction, branch integration, or thread transfer. Keep it under roughly 300 to 800 words unless the project is unusually large.

Use this structure:

```text
Goal:
Current state:
Branch/worktree/PR:
Important constraints:
Decisions made:
Files changed:
Validation run:
Demos:
Known risks:
Next actions:
Docs to read first:
Do not redo:
```

If creating a new thread or subagent from a handoff, pass the handoff plus links to the top two or three relevant docs, not the whole repository memory.

## Compaction and API State

When platform compaction is available, use it for long-running conversations to reduce context size while preserving continuation state. Do not treat opaque compaction items as a substitute for human-readable repo memory.

When using Responses API state features:

- Conversations and `previous_response_id` can preserve state across turns, but previous inputs in a chain may still count as billed input tokens.
- Server-side or standalone compaction can reduce context size in long workflows.
- Prompt caching favors stable shared prefixes, so keep reusable instructions stable and put task-specific variable context later.

For Codex repository work, still write durable state into `docs/ai/`. API state can help a run continue; repo memory helps any future agent restart.

## Redundancy Control Checklist

- Is each durable fact stored in exactly one owner doc?
- Did this prompt include only the relevant slice of memory?
- Did noisy output get summarized and linked instead of pasted?
- Did a subagent return a concise delta rather than a transcript?
- Did a stale plan, old state, or superseded memory get removed or marked superseded?
- Can a fresh agent find the right context via `docs/ai/context-index.md` without reading everything?

## Official References

- OpenAI conversation state: https://developers.openai.com/api/docs/guides/conversation-state
- OpenAI compaction: https://developers.openai.com/api/docs/guides/compaction
- OpenAI prompt caching: https://developers.openai.com/api/docs/guides/prompt-caching
- OpenAI context personalization cookbook: https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization
