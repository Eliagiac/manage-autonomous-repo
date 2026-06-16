# 09 — Standard Repo Docs

## Required structure

Every long-running Codex-managed repo should maintain this structure or clear equivalents:

```text
docs/ai/
  README.md
  state.md
  context-index.md
  objectives.md
  roadmap.md
  track-portfolio.md
  architecture.md
  feature-map.md
  decisions.md
  testing.md
  demos.md
  memory.md
  batches/
    YYYY-MM-DD-<slug>.md
  agent-ledger/
    index.md
  plans/
    active/
    archive/
  evidence/
    index.md
  program/
    operating-model.md
    budget-policy.md
    prompt-contracts.md
```

## File roles

### `README.md`

Explains how future agents should use the docs.

### `state.md`

Compact dashboard. Replace it as facts change.

### `context-index.md`

Map from concept/subsystem/command/demo/test to the files to read first.

### `objectives.md`

Durable goals, non-goals, constraints, success metrics.

### `roadmap.md`

Milestones, gates, deferred work, dependencies.

### `track-portfolio.md`

Active/candidate/blocked/parked lanes and scoring.

### `architecture.md`

System map, data/control flows, extension points, invariants.

### `feature-map.md`

User/operator-visible capabilities and where to test/demo them.

### `decisions.md`

Decision log. Include context, alternatives, decision, rollback signal.

### `testing.md`

Validation ladder and command index, not every historical command transcript.

### `demos.md`

Current trusted demos and how to reproduce them.

### `memory.md`

Curated durable facts that do not belong elsewhere.

### `batches/`

Dated append-only cycle ledgers.

### `agent-ledger/`

Index plus dated or batch-specific agent records. Avoid one giant table.

### `plans/active/` and `plans/archive/`

Only active plans should be prominent. Superseded plans move to archive or are marked clearly.

### `evidence/index.md`

Accepted, parked, rejected, and external evidence pointers.

## Migration from huge docs

When existing docs are too large:

1. Freeze them as archive snapshots.
2. Create a new compact `state.md` dashboard.
3. Create `context-index.md` entries that point to archived detail.
4. Split giant ledgers into dated batch files only when needed; otherwise preserve as archive.
5. Move superseded plans to `plans/archive/`.
6. Create `evidence/index.md` for accepted/parked/rejected artifacts.
7. Add a decision noting the memory-system migration.

Do not delete potentially valuable evidence until a human or integration policy says it is safe.
