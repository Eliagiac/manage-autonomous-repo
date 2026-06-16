# Orchestration Budget Ledger

Use this reference when a project combines Pro Extended planning with Codex implementation or when Codex usage needs explicit control.

## Budget principle

Spend wide read-only reasoning in Pro. Spend Codex only on bounded repository execution and source-control-visible evidence.

## Batch budget fields

Record these fields in `docs/ai/agent-ledger.md`, a dated `docs/ai/batches/*.md` file, or an equivalent PR description:

```text
Batch objective:
Pro Director packet path/chat summary:
Planned Codex lanes:
Actual Codex lanes:
Models/reasoning/agent presets:
Reason each model was sufficient:
Branches/worktrees opened:
Resource locks:
Codex-local broad reading avoided:
Orchestrator-local heavy work:
Validation commands:
Artifacts/demos:
Integrated branches:
Parked/rejected branches:
Spend concerns:
Next budget adjustment:
```

## Budget checkpoints

Before dispatching Codex lanes, verify:

1. Every Codex lane has a proof artifact.
2. Every write lane has a branch/worktree or an explicit reason not to.
3. Every execution lane has resource locks and output paths.
4. The integration agent can absorb the outputs.
5. Pro has already removed stale/irrelevant context from the packet.
6. No lane duplicates another lane's scope.

## Avoidable spend signals

- Codex rereads the entire docs tree.
- Several agents map the same files/questions.
- The main agent implements after delegating the same task.
- Workers return transcripts instead of artifacts.
- A planning chain creates another plan when a task card or execution command is already clear.
- Heavy execution starts before cheap readiness gates.
- State docs grow without compaction or indexing.

## Model selection rule

Use role-based selection rather than fixed model names when the available palette changes:

- Director/senior synthesis: strongest available reasoning, read-only.
- Integration: strong enough for branch/merge decisions, usually medium/high.
- Read-only scout: cheaper model with enough reasoning for bounded mapping.
- Code worker: medium unless cross-module subtlety requires high.
- Deep debug/review: high.
- Execution runner: cheapest sufficient, strict artifact contract.

Escalate only after failed cheaper evidence or when the decision changes architecture, safety, data integrity, or irreversible actions.
