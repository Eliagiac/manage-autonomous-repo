# Goal Prompt and Handoff Contracts

Use this when a platform goal field is too small or when a broad goal was completed too early.

## Compact goal pattern

A compact goal should include:

1. Skill invocation.
2. Repo path.
3. Product objective.
4. Link to bulk instruction file.
5. Completion rule and exit statuses.
6. Current milestone default.
7. Core invariants and stop conditions.

Do not paste full roadmaps or research notes into the goal field. Put them in source-controlled docs and reference them.

## Bulk instruction file

The bulk file should include:

- Mission and product gate.
- Reading order.
- Current baseline facts.
- Operating loop.
- Immediate default milestone.
- Parallelization/branch policy.
- Validation ladder.
- Handoff requirements.
- Stop conditions.

## Handoff contract

End each session with:

```text
Status: RUN_CONTINUES | MILESTONE_ACCEPTED | BLOCKED_REQUIRES_HUMAN | PRODUCT_READY
Branch/worktree:
Integrated changes:
Evidence:
Validation:
Parked/negative routes:
Next batch:
Resource locks:
Budget/usage:
```

## Anti-early-completion rule

For broad goals, the agent must not say the goal is complete unless the product gate passes. If only a slice is complete, the correct status is `RUN_CONTINUES`.

## Resume rule

A resume prompt should name the current status, product gate, active milestone, authoritative state docs, branch/worktree/PR stack, known negative evidence, remaining resource locks, and the next batch. Do not rely on chat memory or an agent's prior intent as proof of completion.
