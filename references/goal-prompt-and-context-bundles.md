# Goal Prompts and Context Bundles

Use this reference when starting a new long-running agent session, ingesting branch-doc bundles, or handing a broad goal to an orchestrator.

## 1. Context capsule protocol

Before implementation, create a capsule of the smallest context that lets a fresh agent act safely.

Recommended capsule fields:

```text
Goal:
Repo path:
Live branch/worktree:
Stable/main branch:
Active PR stack:
Docs to read first:
Prior research to link only:
Current accepted evidence:
Known negative/parked evidence:
Non-goals and covenants:
Selected tracks:
Resource locks:
Validation ladder:
Stop conditions:
Next handoff target:
```

Do not paste huge state docs, agent ledgers, or raw logs into the capsule. Link paths and quote only the decision-critical facts.

## 2. Branch-doc bundle ingestion

When a user provides local branch docs or archived notes:

1. Extract file lists and timestamps.
2. Identify the newest/live baseline and older provenance snapshots.
3. Compare `docs/ai/state.md`, `docs/ai/memory.md`, `docs/ai/roadmap.md`, `docs/ai/feature-roadmaps.md`, `docs/ai/plans/`, and `docs/ai/testing.md` before reading huge ledgers.
4. Summarize differences into a new synthesis note or handoff capsule.
5. Mark superseded and negative evidence explicitly.
6. Do not assume uploaded docs match the current working tree; tell the next agent to verify `git status`, branch, and file contents before editing.

## 3. Goal prompt structure

A high-quality goal prompt for an autonomous repo session should include:

- skill invocation and subagent authorization;
- exact repo path;
- current objective;
- first docs to read;
- non-goals and hard covenants;
- known negative evidence;
- desired implementation tracks;
- branch/worktree/integration policy;
- task-card requirements;
- validation ladder;
- stop conditions;
- definition of done.

Put stable boilerplate first and variable repo details later for prompt-cache friendliness.

## 4. Token budgeting for new sessions

- Start with `docs/ai/state.md`, `docs/ai/context-index.md`, and targeted plan docs.
- Use `rg`, headings, and JSON summaries before reading entire files.
- Delegate broad document comparisons to read-only workers.
- Ask workers to report deltas and relied-on files.
- Promote reusable findings into docs; do not rely on chat memory.
- Keep handoff briefs under 300-800 words unless the project is unusually large.

## 5. Prompt quality checklist

Before sending a goal prompt, check:

- Does it say what not to do?
- Does it name negative evidence that must not be repeated?
- Does it require branch/worktree verification?
- Does it authorize and bound subagents?
- Does it name validation commands or how to discover them?
- Does it define done in source-controlled artifacts?
- Does it prevent planning-only artifacts from being mistaken for acceptance?
