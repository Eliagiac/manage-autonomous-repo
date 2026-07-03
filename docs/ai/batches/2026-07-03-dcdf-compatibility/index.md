# Batch 2026-07-03: DCDF Compatibility and Memory Hardening

## Objective

Apply the MAR/DCDF interaction updates identified in Pro review:

- keep MAR lane-local under DCDF;
- add direct DCDF compatibility doctrine;
- replace sequential-only memory with parallel-safe lane-indexed docs;
- sanitize durable memory;
- support DCDF ledger registration in a separate branch.

## Selected Tracks

| Track | Mode | Owner | Branch/worktree | Status |
| --- | --- | --- | --- | --- |
| MAR DCDF doctrine | documentation | orchestrator | `dcdf/mar-dcdf-mode-memory-20260703` | active |
| Parallel-safe memory | documentation | orchestrator | `dcdf/mar-dcdf-mode-memory-20260703` | active |
| DCDF ledger registration | GitHub orchestration / ledger docs | separate DCDF branch | `dcdf/mar-ledger-registration-20260703` | active |
| Local validation | execution | future controller/Codex or local maintainer agent | not run in connector-only pass | pending |

## Lane Files

- `docs/ai/batches/2026-07-03-dcdf-compatibility/lanes/mar-dcdf-mode-docs.md`

## Resource Locks

See `docs/ai/locks.md`.

## Evidence

- `docs/ai/evidence/2026-07-03-dcdf-compatibility-review.md`

## Validation Ladder

Connector-only Pro updates can create reviewable source changes but cannot prove local execution.

Required validation before merge:

1. `git status --short --branch`
2. `git diff --check`
3. `python scripts/install_agent_presets.py --help`
4. Manual review for local absolute paths, secrets, raw logs, raw model output, and private session artifacts
5. DCDF controller validation on the separate DCDF branch before treating ledger registration as published

## Output Status

`RUN_CONTINUES`: documentation and ledger-registration branches are staged for review. Controller receipts are still required for production DCDF validation claims.
