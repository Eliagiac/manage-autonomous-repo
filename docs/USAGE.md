# Usage

## When to Use This Skill

Use Manage Autonomous Repo when Codex is expected to manage a repository over time, not just make a small patch. Good fits include:

- building a new project from an abstract goal;
- continuing a long-running autonomous project;
- refactoring a large repo;
- coordinating multiple subagents;
- maintaining agent-readable docs, roadmaps, demos, tests, and GitHub state;
- exploring multiple implementation directions in parallel.

## Starting Prompt

```text
[$manage-autonomous-repo](C:\Users\<you>\.codex\skills\manage-autonomous-repo\SKILL.md)
Use subagents as per skill instructions.

Continue work on this repository toward the current roadmap. Keep source control, docs, tests, demos, and handoffs current.
```

For a broad product or research-program goal, include the product gate and the expected non-terminal status behavior:

```text
[$manage-autonomous-repo](C:\Users\<you>\.codex\skills\manage-autonomous-repo\SKILL.md)
Use subagents as per skill instructions.

Run this repository as a Product Program Mode project. Treat ordinary sessions as progress cycles. End with RUN_CONTINUES, MILESTONE_ACCEPTED, BLOCKED_REQUIRES_HUMAN, or PRODUCT_READY, and only claim completion when the product gate passes.
```

## First-Run Checklist

1. Confirm the repository is trusted and under Git.
2. Install project-local agent presets with `scripts/install_agent_presets.py`.
3. Start a fresh Codex session from the project root.
4. Ask Codex to create or update the `docs/ai/` memory system.
5. Ask Codex to identify the independent track portfolio before implementation.

## Expected Workflow

The main agent acts as orchestrator:

- inspect current repo state;
- identify independent tracks;
- create task cards;
- spawn subagents for bounded work;
- keep branches and worktrees separated;
- keep branch-visible agent outputs reviewable through commits, logs, PRs, check results, or source-controlled reports;
- integrate outputs deliberately;
- update durable docs;
- leave a clear handoff.

Subagents should own scoped work:

- exploration;
- implementation;
- execution/proof runs;
- reviews;
- documentation audits;
- product-program audits;
- test planning;
- debugging;
- demo validation.

## Branching

For meaningful work, prefer named branches:

- `feat/<topic>`
- `fix/<topic>`
- `refactor/<topic>`
- `test/<topic>`
- `demo/<topic>`
- `research/<topic>`
- `integrate/<milestone>`

Use worktrees when independent subagents need isolated checkouts.

Cloud or branch-visible coding workers should leave source-control evidence. Prefer commits, logs, PR-ready branch summaries, check results, or source-controlled reports over chat-only claims.

## Durable Memory

The skill expects the target project to maintain docs such as:

- `docs/ai/state.md`
- `docs/ai/roadmap.md`
- `docs/ai/architecture.md`
- `docs/ai/feature-map.md`
- `docs/ai/testing.md`
- `docs/ai/demos.md`
- `docs/ai/agent-ledger.md`

Future agents should be able to restart from those docs without reading the full chat history.
