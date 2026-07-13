# DCDF Lane Compatibility

Use this reference when `manage-autonomous-repo` is invoked inside a DCDF-controlled lane.

## Activation

Activate this mode only when the caller supplies one of:

- a schema-valid `lane-task.v2` with a verified `task_hash`;
- a source-controlled Codex execution packet that explicitly references a validated `lane-task.v2`;
- a `dcdf-run-lane` prompt that identifies `project_id`, `order_id`, `task_id`, `lane_id`, repository id, branch, worktree, owned scope, avoid scope, locks, validation, and output contract.

A prose planning request, raw prompt, ChatGPT thread, or standalone MAR objective is not enough to activate DCDF authority.

## Authority Split

DCDF owns:

- Director Order validation and lane materialization;
- official Codex lifecycle and thread/turn state;
- global ledger, registry, index, publication locks, and receipts;
- project tuple, repository facts, scope policy, helper policy, validation ladder, and stop conditions.

`manage-autonomous-repo` contributes only lane-local doctrine:

- branch/worktree hygiene inside the lane;
- independent-track thinking within the lane's allowed scope;
- evidence classification and promotion discipline;
- compact context capsules and lane-local memory;
- task-card quality, review gates, and cost-aware helper routing.

If these conflict, DCDF wins.

## Required DCDF Inputs

The active lane brief must identify:

```text
project_id:
order_id:
task_id:
lane_id:
task_hash:
repository_id:
branch:
worktree:
base ref/commit:
owned_scope:
avoid_scope:
protected_paths:
artifact policy:
resource_locks:
helper limit:
validation commands:
proof artifact:
stop conditions:
output schema:
```

Missing or contradictory values are blockers. Do not infer missing authority from MAR defaults.

## Forbidden Authority

In DCDF mode, this skill must not:

- parse, accept, reject, or repair `dcdf.director_order.v2`;
- schedule cross-project work or additional DCDF lanes;
- mutate `REGISTRY.json`, `INDEX.json`, global publisher state, Director inbox state, or runtime projections unless those files are explicitly in the accepted lane's owned scope;
- acquire global publisher locks or publish the ledger;
- create, resume, or operate official Codex thread/turn lifecycle state;
- operate ChatGPT or browser UI automation;
- perform legacy teardown;
- merge `main`, release, deploy, force-push, change account settings, or perform paid/credentialed/destructive actions unless the lane task and an approval gate explicitly authorize the agent action.

## Output Mapping

Standalone MAR status is not the DCDF output contract.

| Standalone condition | DCDF-mode output |
| --- | --- |
| Work completed and proof passed | `run-receipt.v2` with `COMPLETED` or `COMPLETED_WITH_CONCERNS` |
| Validation failed | `run-receipt.v2` with `FAILED` and validation evidence |
| Scope, lock, helper, base, or protected-path mismatch | `decision-request.v2` or terminal blocker with the exact DCDF failure state |
| Human approval needed | `decision-request.v2` requesting authorization for an agent action |
| Human manual work would be needed | Stop and rewrite as an agent-action authorization request or a controller/tooling blocker |
| Product still not done | `RUN_CONTINUES` may appear only as a human summary, not as a substitute for lane receipt status |

Every DCDF-mode final handoff must include `project_id`, `order_id`, `task_id`, `lane_id`, and `task_hash`.

## Parallel Memory in DCDF Mode

Use lane-indexed memory:

```text
docs/ai/state.md                         # short pointer only
docs/ai/batches/<batch-id>/index.md      # orchestrator-owned batch state
docs/ai/batches/<batch-id>/lanes/*.md    # one owner per lane
docs/ai/branch-map.md                    # orchestrator-owned branch/worktree map
docs/ai/locks.md                         # orchestrator-owned resource lock map
docs/ai/evidence/*.md                    # evidence manifests
```

Rules:

- A lane may update only its own lane file unless the lane task grants broader scope.
- The orchestrator owns shared branch/lock maps.
- `agent-ledger.md` records batch utilization after integration; it is not the live lane database.
- Evidence manifests must state artifact identity, provenance, status class, promotion gate, and receipt/PR link.
- Do not store local absolute paths, credentials, account metadata, raw controller databases, raw JSON-RPC, raw model output, private ChatGPT artifacts, or raw logs.

## Budget and Helpers

Standalone MAR defaults do not raise a DCDF lane's limits. Use the `lane-task.v2` helper policy and the current DCDF project budget. If a lane needs more threads, return a decision request; do not silently spawn beyond the lane cap.

## Stop Conditions

Stop immediately on:

- task hash mismatch;
- branch/worktree/base mismatch;
- owned/avoid/protected scope conflict;
- resource-lock conflict;
- helper count/depth overflow;
- validation command missing or unsafe compared with the lane task;
- requested write outside owned scope;
- credentialed, paid, destructive, release, deploy, or account action without an explicit lane approval;
- need to publish or mutate the global ledger outside lane authority.
