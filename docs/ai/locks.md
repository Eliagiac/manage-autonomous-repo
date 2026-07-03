# Resource Locks

Last updated: 2026-07-03

## Active Locks

| Lock | Owner | Mode | Release condition | Notes |
| --- | --- | --- | --- | --- |
| `mar-skill-doctrine` | orchestrator | write | MAR PR reviewed | Covers `SKILL.md` and reference docs in the MAR repo. |
| `mar-docs-ai-memory` | orchestrator | write | MAR PR reviewed | Covers parallel-safe `docs/ai` memory updates. |
| `dcdf-ledger-registration:manage-autonomous-repo` | DCDF ledger branch | write | DCDF PR reviewed and controller validation complete | Covers the separate DCDF branch that registers MAR. |
| `dcdf-architecture-budget` | DCDF ledger branch | write | DCDF PR reviewed and controller validation complete | Covers changing DCDF architecture max thread budget to six. |

## Rules

- Do not assign another writer to a locked path without updating this file and `docs/ai/branch-map.md`.
- Read-only reviewers may inspect locked files but must report comments rather than editing locked files directly.
- If a lock owner stops responding or a branch is abandoned, mark the lock stale and create a new branch before continuing.
- In DCDF mode, the `lane-task.v2` lock declarations override this repository-local map.
