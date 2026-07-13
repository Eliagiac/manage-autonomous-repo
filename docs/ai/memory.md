# AI Memory

Last updated: 2026-07-03

## Durable Invariants

- MAR is a standalone autonomous-repo skill unless a DCDF lane task activates compatibility mode.
- In DCDF mode, `dcdf-run-lane` remains the authority skill for admission, scope enforcement, helper policy, and receipt output.
- MAR must not parse Director Orders, publish the global ledger, operate ChatGPT, or own official Codex lifecycle state.
- Repo memory should be source-controlled, concise, lane-indexed for parallel work, and free of local absolute paths or private artifacts.
- `agent-ledger.md` records batch history; it is not the live database for concurrent lanes.

## Superseded Notes

- Earlier state docs with local checkout paths are superseded by repository-relative state and branch-map docs.
- Prior two-file memory (`state.md` plus `agent-ledger.md`) is now considered a bootstrap only; broad parallel work requires batch, lane, branch-map, lock-map, and evidence docs.
