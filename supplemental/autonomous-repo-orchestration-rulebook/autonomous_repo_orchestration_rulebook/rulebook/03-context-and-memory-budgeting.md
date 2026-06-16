# 03 — Context and Memory Budgeting

## Principle

Repository memory should make future agents faster. If a fresh agent must read megabytes of stale state before acting, the memory system has failed.

## Memory tiers

### Tier 1 — Dashboard memory

Small files read at the start of most cycles:

- `docs/ai/state.md`
- `docs/ai/context-index.md`
- `docs/ai/track-portfolio.md`
- latest file under `docs/ai/batches/`

These must remain compact and current. They are replaced, not endlessly appended.

### Tier 2 — Stable reference memory

Files that change when durable facts change:

- `docs/ai/objectives.md`
- `docs/ai/roadmap.md`
- `docs/ai/architecture.md`
- `docs/ai/feature-map.md`
- `docs/ai/testing.md`
- `docs/ai/demos.md`
- `docs/ai/decisions.md`

These should have clear owners. Do not duplicate the same fact in every file.

### Tier 3 — Batch memory

Dated, append-only records:

- `docs/ai/batches/YYYY-MM-DD-<slug>.md`
- `docs/ai/agent-ledger/index.md`
- PR descriptions and comments
- branch summaries

Batch memory preserves history without bloating the current-state dashboard.

### Tier 4 — Evidence archive

Large, old, or raw material:

- raw logs;
- full JSON manifests;
- screenshots/videos;
- external workdir contracts;
- superseded plans;
- negative-evidence details.

These are linked from indexes. They are not read by default.

## Size budgets

These are guidelines, not hard limits, but a repo that exceeds them should have a pruning pass:

| File | Target |
| --- | ---: |
| `state.md` | 150–350 lines; no huge tables |
| `context-index.md` | 100–250 lines |
| `track-portfolio.md` | 50–200 lines |
| latest batch ledger | 300–900 words |
| worker handoff | 150–500 words plus artifact paths |
| Codex execution packet | as short as possible while safe |

Large projects may need more, but size growth should be intentional and indexed.

## Dashboard replacement rule

`state.md` is a dashboard, not a ledger. It should contain:

- current objective;
- current branch/worktree/PR state;
- latest accepted proof or demo;
- current blockers;
- current resource locks;
- next three actions;
- docs to read first;
- warnings about known stale/negative paths.

Old “latest update” paragraphs should be moved into a dated batch ledger or archived note. Do not leave contradictory old state in the dashboard.

## Context capsule protocol

Every Pro-to-Codex handoff should include a context capsule:

```text
Goal:
Repo path:
Current branch/worktree:
Integration branch:
Docs to read first:
Files likely touched:
Known hazards:
Known negative/parked evidence:
Resource locks:
Validation ladder:
Stop conditions:
Expected proof artifact:
Handoff format:
```

The capsule links long docs instead of pasting them.

## Reading order for future agents

1. `docs/ai/state.md`
2. `docs/ai/context-index.md`
3. latest batch ledger
4. the exact task card or execution packet
5. only the source/docs/tests named by the task card
6. archived evidence only when needed to verify a claim

## Redundancy controls

- Store each stable fact in one owner doc.
- Link rather than paste long plans.
- Replace stale summaries.
- Use indexes for large evidence directories.
- Keep batch ledgers dated and immutable except for typo fixes.
- Move superseded plans to `docs/ai/archive/` or mark them clearly as superseded.
- Never make workers read a huge ledger to discover their branch scope.

## When to trigger a memory cleanup

Trigger cleanup when any of these occur:

- `state.md` contains contradictory branch/path/remote/demo facts.
- an agent must read more than three large docs just to understand the next task;
- `agent-ledger.md` becomes a massive table with multi-kilobyte rows;
- plan artifacts greatly outnumber implementation/execution artifacts for the current milestone;
- a branch was abandoned but still appears active;
- a negative route was repeated because the parked evidence was hard to find.
