# Documentation System

Use this reference when creating or maintaining the repository memory.

## Required Docs

Create `docs/ai/` if the repo lacks an equivalent agent-oriented documentation system. Prefer these files:

- `docs/ai/state.md`: concise current working state, active branch, latest verified commands, known breakages, and next action.
- `docs/ai/objectives.md`: durable goals, non-goals, constraints, success metrics, and priority order.
- `docs/ai/context-index.md`: concise map from subsystem, feature, command, and decision area to the docs/source/tests to read first.
- `docs/ai/roadmap.md`: high-level milestones, active milestone, planned features, deferred ideas, dependency ordering.
- `docs/ai/feature-roadmaps.md`: feature-specific plans with acceptance criteria and validation paths.
- `docs/ai/architecture.md`: system map, major modules, runtime flows, data ownership, integration points.
- `docs/ai/feature-map.md`: user-visible and operator-visible features, status, entry points, tests, demos.
- `docs/ai/decisions.md`: decision log with date, context, options, chosen path, rollback signal.
- `docs/ai/testing.md`: test commands, coverage expectations, manual smoke paths, flaky tests, missing test debt.
- `docs/ai/demos.md`: demo commands, local URLs, screenshots/videos paths, feature coverage, known demo limitations.
- `docs/ai/research.md`: research questions, sources, findings, discarded options, follow-up investigations.
- `docs/ai/memory.md`: curated long-term notes that do not belong in more specific owner docs.
- `docs/ai/agent-ledger.md`: append-style batch summaries, subagents used, model/effort, branch/scope, output summary, and integration status.

If the repo already has equivalents, update those instead of duplicating.

## Parallel-Safe Memory

For repos with parallel branches, worktrees, subagents, DCDF lanes, or long-running evidence batches, do not make a single `docs/ai/state.md` or `docs/ai/agent-ledger.md` the only active coordination surface.

Add these lane-indexed files when parallel work exists:

```text
docs/ai/batches/<batch-id>/index.md
docs/ai/batches/<batch-id>/lanes/<lane-id>.md
docs/ai/branch-map.md
docs/ai/locks.md
docs/ai/evidence/<artifact-id>.md
```

Contracts:

- `state.md` stays short and points to the current batch, active branch/worktree map, lock map, and next actions.
- `agent-ledger.md` is append-style history and utilization review, not a shared mutable lane database.
- Each active lane owns one lane file with objective, owner, branch/worktree, owned scope, avoid scope, resource locks, proof artifact, validation, status, and integration recommendation.
- `branch-map.md` records stable branch, integration branch, worker branches, bases, heads, worktree status, shared files, and merge order.
- `locks.md` records shared resource locks, current owner, allowed concurrent readers/writers, release condition, and stale-lock policy.
- Evidence docs record artifact identity, provenance, hash when available, status class, promotion gate, and receipt or PR links.
- If two lanes need to update the same shared memory file, freeze that file under orchestrator ownership and require lanes to report deltas into lane files instead.

## DCDF-Managed Repositories

When a repository is managed through DCDF:

- Treat the DCDF `lane-task.v2` as authoritative for branch, worktree, owned scope, avoid scope, locks, validation, helper limits, and output schema.
- Keep DCDF global ledger state separate from repository-local memory.
- Do not store raw controller DBs, raw JSON-RPC, raw model output, credentials, private ChatGPT/session material, or local absolute paths in repo memory.
- Link to `run-receipt.v2`, `decision-request.v2`, PRs, commits, and sanitized evidence rather than pasting raw logs.
- Use `decision-request.v2` or an explicit authorization request when an agent action needs approval; do not encode "human will perform GitHub/local work" as a stop condition.

## Abstraction Layers

Maintain documentation at multiple altitudes:

- Project: purpose, users, value, non-goals, roadmap.
- Architecture: components, data/control flow, external dependencies, deployment shape.
- Subsystem: ownership, invariants, extension points, failure modes.
- Feature: behavior, UX/API contract, acceptance criteria, tests, demo.
- File/module: only when local complexity would slow future agents.
- Operation: setup, commands, credentials expected but not stored, deployment, rollback.
- Lane/batch: ownership, locks, branch/worktree, proof artifact, validation, receipt.

## State Page Contract

`docs/ai/state.md` should let a fresh agent resume in under five minutes. Include:

- Current goal and latest concrete progress.
- Links to the objective slice and context-index entries relevant to the active work.
- Branch/worktree status and whether the tree is clean.
- Active batch, lane docs, branch map, and lock map when parallel work exists.
- Commands last run and their pass/fail result.
- Current demos and how to launch them.
- Known risks, blockers, and assumptions.
- Next three recommended actions.
- Links to relevant roadmap, decision, issue, PR, receipt, or evidence entries.

Update this page before ending a long run, before handing work to subagents, after integrations, and after failed tests reveal a new truth.

## Roadmap Rules

- Maintain both a high-level roadmap and feature-specific roadmaps.
- Mark dependencies explicitly. Do not build dependent features on unreviewed foundations.
- Include "definition of done" for each milestone: code, tests, docs, demo, source-control state.
- Keep a "discarded or parked" section so future agents do not rediscover rejected ideas.
- Convert abstract user goals into testable outcomes as early as possible.
- For broad programs, keep the independent track portfolio separate from the currently active lane list.

## Demo Rules

Maintain a demo index for every meaningful feature. Demos may be UI flows, CLI commands, API calls, notebooks, screenshots, short videos, generated fixtures, or hosted preview links.

For each demo, record:

- Feature covered.
- Setup command.
- Run command or URL.
- Expected observable result.
- Last verified date and command.
- Known limitations.

For frontend apps, use Browser or Chrome tools to visually inspect after major changes. For APIs and CLIs, provide reproducible commands. For documents, spreadsheets, and presentations, render or open outputs where the relevant plugin supports it.

## Documentation Hygiene

- Delete obsolete docs when replacing architecture.
- Link docs to source files and tests when useful.
- Keep examples executable or clearly marked as illustrative.
- Put volatile status in `state.md`, lane files, and batch files, not in stable architecture docs.
- Keep raw logs and bulky outputs outside docs unless they are curated artifacts.
- Do not store secrets, account metadata, private session artifacts, or local absolute paths in docs. Document secret names, locations, and setup procedures only.
