# AI Roadmap

Last updated: 2026-07-03

## Product Objective

Maintain `manage-autonomous-repo` as a reusable Codex skill for running repositories as autonomous engineering programs while making it safe to invoke inside DCDF lanes.

## Non-Goals

- Do not make MAR a DCDF Director Order parser.
- Do not make MAR a global ledger publisher or official Codex lifecycle operator.
- Do not replace DCDF `dcdf-run-lane` or `dcdf-codex-lifecycle`.
- Do not require the human to operate GitHub, local shells, or controller state manually.
- Do not copy private local paths, secrets, raw controller databases, raw model output, or private session artifacts into durable docs.

## Milestones

### M1: DCDF compatibility doctrine

Definition of done:

- `SKILL.md` has explicit DCDF Lane Compatibility Mode.
- A dedicated reference explains authority, forbidden operations, output mapping, parallel memory, and helper budget overrides.
- Standalone statuses remain available, but DCDF mode maps blockers to lane-valid receipts or decision requests.

Status: active in `docs/ai/batches/2026-07-03-dcdf-compatibility/index.md`.

### M2: Parallel-safe memory

Definition of done:

- `docs/ai/state.md` is a concise pointer, not the only lane database.
- `docs/ai/context-index.md`, `docs/ai/branch-map.md`, `docs/ai/locks.md`, batch docs, lane docs, and evidence manifests exist.
- Documentation references instruct future agents to use lane-indexed memory and single-writer shared maps.

Status: active in this branch.

### M3: DCDF ledger onboarding

Definition of done:

- DCDF ledger has a `manage-autonomous-repo` project entry.
- Project files exist under `dcdf-ledger/projects/manage-autonomous-repo/`.
- Registration uses sanitized public facts and no raw local/private artifacts.
- DCDF architecture budget records six direct threads for lane-capable work.
- Controller validation is run and receipt-bound before any production claim.

Status: tracked in the DCDF branch `dcdf/mar-ledger-registration-20260703`.

## Parked or Negative Evidence

- Prior DCDF onboarding attempts must not be reprocessed by old handoff id.
- Earlier receipts showed an `OUTPUT_SCHEMA_INVALID` lane failure; do not treat that as completed Codex execution.
- Historical local absolute paths in old state notes are superseded by sanitized repo-relative docs in this branch.
