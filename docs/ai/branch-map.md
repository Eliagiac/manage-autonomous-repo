# Branch and Worktree Map

Last updated: 2026-07-03

## Stable Branches

| Repository | Stable branch | Current review branch | Integration branch |
| --- | --- | --- | --- |
| `Eliagiac/manage-autonomous-repo` | `main` | `dcdf/mar-dcdf-mode-memory-20260703` | none |
| `Eliagiac/dcdf` | `main` | `dcdf/mar-ledger-registration-20260703` | none |

## Worker Branches

No worker branches are active inside this repository-local MAR batch. This Pro pass made connector-authored documentation changes on a single review branch.

## Shared Files

Shared docs currently owned by the orchestrator for this batch:

- `SKILL.md`
- `references/documentation-system.md`
- `references/dcdf-lane-compatibility.md`
- `docs/ai/state.md`
- `docs/ai/context-index.md`
- `docs/ai/roadmap.md`
- `docs/ai/locks.md`
- `docs/ai/agent-ledger.md`
- `docs/ai/batches/2026-07-03-dcdf-compatibility/**`
- `docs/ai/evidence/2026-07-03-dcdf-compatibility-review.md`

## Merge Order

1. Review MAR branch for doctrine and memory safety.
2. Run local validation commands.
3. Merge or publish MAR branch.
4. Review DCDF ledger branch.
5. Run controller validation for ledger registration.
6. Merge or publish DCDF branch only after validation evidence is available.

## Stale Branch Policy

If either review branch moves or is superseded, create a new branch and update this map. Do not reprocess old DCDF outbox handoff ids.
