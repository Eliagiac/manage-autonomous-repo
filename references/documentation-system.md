# Documentation System

Use this reference when creating or maintaining the repository memory.

## Required Docs

Create `docs/ai/` if the repo lacks an equivalent agent-oriented documentation system. Prefer these files:

- `docs/ai/state.md`: current working state, active branch, latest verified commands, known breakages, next action.
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
- `docs/ai/agent-ledger.md`: subagents used, model/effort, task, branch/scope, output summary, integration status.

If the repo already has equivalents, update those instead of duplicating.

## Abstraction Layers

Maintain documentation at multiple altitudes:

- Project: purpose, users, value, non-goals, roadmap.
- Architecture: components, data/control flow, external dependencies, deployment shape.
- Subsystem: ownership, invariants, extension points, failure modes.
- Feature: behavior, UX/API contract, acceptance criteria, tests, demo.
- File/module: only when local complexity would slow future agents.
- Operation: setup, commands, credentials expected but not stored, deployment, rollback.

## State Page Contract

`docs/ai/state.md` should let a fresh agent resume in under five minutes. Include:

- Current goal and latest concrete progress.
- Links to the objective slice and context-index entries relevant to the active work.
- Branch/worktree status and whether the tree is clean.
- Commands last run and their pass/fail result.
- Current demos and how to launch them.
- Known risks, blockers, and assumptions.
- Next three recommended actions.
- Links to relevant roadmap, decision, issue, or PR entries.

Update this page before ending a long run, before handing work to subagents, after integrations, and after failed tests reveal a new truth.

## Roadmap Rules

- Maintain both a high-level roadmap and feature-specific roadmaps.
- Mark dependencies explicitly. Do not build dependent features on unreviewed foundations.
- Include "definition of done" for each milestone: code, tests, docs, demo, source-control state.
- Keep a "discarded or parked" section so future agents do not rediscover rejected ideas.
- Convert abstract user goals into testable outcomes as early as possible.

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
- Put volatile status in `state.md`, not in stable architecture docs.
- Do not store secrets in docs. Document secret names, locations, and setup procedures only.
