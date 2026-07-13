# Context and Memory

Use this reference to minimize token waste while keeping the project restartable across long runs, subagents, compaction, parallel branches, and future threads.

## Core Rule

Treat chat history as working memory, not project memory. The repository is the durable source of truth. Context passed to any agent should be a curated working set assembled from repo docs, source files, current task scope, and recent validated results.

## Memory Tiers

Maintain these tiers separately:

- Active brief: the small current-task packet an agent needs now. Store the global pointer in `docs/ai/state.md`; for parallel work store lane-specific briefs in `docs/ai/batches/<batch-id>/lanes/<lane-id>.md`.
- Stable memory: architecture, feature map, decisions, roadmap, testing, demos, and runbooks in `docs/ai/`.
- Context index: `docs/ai/context-index.md`, mapping concepts, subsystems, commands, docs, and tests to paths.
- Lane memory: per-lane objective, branch/worktree, owned/avoid scope, locks, proof artifact, validation, output status, and receipt or PR links.
- Session notes: temporary findings from the current run or subagent. Promote only reusable facts.
- Archive: raw logs, long research notes, old plans, and superseded designs. Link to them; do not load by default.

## Required Context Docs

Add these docs if the project is large, long-running, parallel, or DCDF-managed:

- `docs/ai/context-index.md`: short index of what to read for each subsystem, feature, workflow, command, and decision area.
- `docs/ai/objectives.md`: durable product goals, non-goals, constraints, success metrics, and current priority ordering.
- `docs/ai/memory.md`: curated long-term notes that are not naturally part of architecture or roadmap docs.
- `docs/ai/branch-map.md`: active branch, worktree, integration target, base/head, ownership, shared-file, and merge-order map.
- `docs/ai/locks.md`: active and known resource locks with owners, release conditions, and stale-lock policy.
- `docs/ai/batches/`: dated or ID-scoped batch directories with one `index.md` and one lane file per active lane.
- `docs/ai/evidence/`: curated evidence manifests for artifacts that influence acceptance.
- `docs/ai/handoffs/`: optional dated handoff briefs for major milestones or compactions.

Do not duplicate stable facts across all files. Choose one owner document and link to it.

## Parallel Memory Discipline

Use a single-writer model for shared memory during parallel work.

- The orchestrator owns `state.md`, `branch-map.md`, `locks.md`, and batch `index.md`.
- Each lane owner writes or reports deltas for its own lane file only.
- Review and evidence workers create evidence manifests or review files rather than editing another lane's active state.
- `agent-ledger.md` records final utilization and integrated outcomes after a batch; it is not the live lane database.
- If branch/worktree or lock facts change, update the shared map once and point lane files to it.
- If a lane discovers that its owned scope, avoid scope, or lock map is wrong, it stops and reports the mismatch instead of silently widening scope.

## Context Budgeting

Before loading or sending context, classify each item:

- Must include: current objective, constraints, acceptance criteria, owned files, known hazards, validation commands.
- Link only: stable docs, long logs, prior research, full roadmaps, old PR discussions.
- Omit: obsolete plans, raw command output after summarization, repeated boilerplate, unrelated docs, closed issues.

For the orchestrator:

- Start each major phase by reading `docs/ai/state.md`, `docs/ai/context-index.md`, the current batch index, branch map, lock map, and only the docs/files tied to the active task.
- Use a resume fast path after long runs: read current state, context index, recent ledger entries, branch status, active lane files, and only the changed docs or files needed for the selected batch.
- Use search to retrieve facts instead of loading whole directories.
- Summarize noisy tool output into state docs or task notes, then stop carrying the raw output in the prompt.
- Replace stale summaries; do not append endlessly.
- Keep stable instructions in the skill or repo docs and pass subagents links plus a short task packet.

For subagents:

- Give a narrow active brief instead of the full orchestrator context.
- Include paths to read, paths to avoid, owned scope, expected output, and acceptance criteria.
- Ask for deltas: facts found, files changed, commands run, risks, and next actions.
- For execution lanes, ask for artifact paths, command outcomes, timing, resource locks used, and concise failure evidence rather than raw logs.
- Forbid dumping long logs unless the logs are the deliverable.
- Require subagents to state which docs/files they actually relied on.
- Require branch/worktree and lock mismatch reports before any scope expansion.

## Token Budget Protocol

Use token budget as an engineering resource:

- Spend orchestration tokens on decisions, integration, conflict resolution, and synthesis.
- Spend cheaper subagent tokens on bounded reading, execution, test discovery, artifact inspection, and well-scoped implementation.
- Give each worker a short active brief plus file paths. Require a concise artifact-backed report instead of a transcript.
- Prefer repository artifacts over chat memory for large outputs: reports, manifests, logs, screenshots, benchmark tables, and handoff briefs should be written to files and summarized by path.
- For long command sequences, decide explicitly whether the main thread should wait quietly, delegate an execution lane, or do unrelated critical-path work.
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

- `agents.max_threads = 10` is the standalone MAR baseline for repos that can safely absorb that many direct worker threads.
- `agents.max_depth = 2` is required only when depth-1 workers should be able to spawn helper lanes.
- In DCDF Lane Compatibility Mode, the `lane-task.v2`, project budget, and DCDF controller policy override these standalone defaults. Do not raise a DCDF lane's thread/depth budget from MAR docs alone.
- Use profile files for personal experiments and project `.codex/config.toml` only for settings that should be reproducible for future agents.
- Keep subagent prompts stable and narrow. Static role instructions should come first; variable repo context should come later.
- Keep final user-facing status short. Put full command lists, artifact paths, and batch utilization details in `docs/ai/`.

## Long-Term Memory Pattern

Use session notes as a staging area and curated memory as a reviewed store:

1. Capture candidate notes during work only when they are likely to matter later.
2. Consolidate at phase end: dedupe, resolve conflicts, attach sources, and delete trivia.
3. Promote notes to the correct owner doc.
4. Add metadata for memory-only notes: id, type, claim, source, scope, confidence, last verified, supersedes, expires, tags, and linked paths.
5. Prune or decay stale notes. A memory that is no longer true is worse than no memory.

Use `docs/ai/memory.md` only for durable facts that do not fit better in architecture, decisions, testing, demos, roadmap, branch map, lock map, lane files, or evidence manifests.

## Handoff Brief

Create a handoff brief before major pauses, compaction, branch integration, or thread transfer. Keep it under roughly 300 to 800 words unless the project is unusually large.

Include: goal, current state, branch/worktree/PR, constraints, decisions, files changed, validation, demos, risks, next actions, docs to read first, and do-not-redo items.

If creating a new thread or subagent from a handoff, pass the handoff plus links to the top two or three relevant docs, not the whole repository memory.

## Redundancy Control Checklist

- Is each durable fact stored in exactly one owner doc?
- Did this prompt include only the relevant slice of memory?
- Did noisy output get summarized and linked instead of pasted?
- Did a subagent return a concise delta rather than a transcript?
- Did a stale plan, old state, or superseded memory get removed or marked superseded?
- Can a fresh agent find the right context via `docs/ai/context-index.md` without reading everything?
- Is active lane state in lane files rather than scattered across one shared doc?
- Are branch/worktree and lock maps current before new workers write?
- Are local absolute paths, secrets, account metadata, raw model output, and private session artifacts absent from durable memory?
