# Product Orchestration Lifecycle

Use this reference when the user asks for a broad product outcome, autonomous research program, or build-from-scratch objective.

## Product Program Mode

A broad product goal is not complete after one patch. It requires an operating loop, milestone gates, and non-terminal handoffs.

Use exit statuses:

- `RUN_CONTINUES`: useful progress landed and next work is defined.
- `MILESTONE_ACCEPTED`: named milestone gate passed and next milestone is defined.
- `BLOCKED_REQUIRES_HUMAN`: blocked by credentials, legal/licensing, destructive/paid action, hardware, or a user decision.
- `PRODUCT_READY`: product gate passed.

Do not use `complete` unless `PRODUCT_READY` or the user explicitly closes the program.

## Required docs for product programs

Add or maintain:

- Product objective, constraints, non-goals, and acceptance gates.
- Milestone roadmap.
- Track portfolio/backlog.
- Evidence taxonomy and parked/negative lanes.
- Agent operating model.
- Handoff/resume instructions.
- Compact prompt plus bulk instructions if goal field limits exist.

## Product loop

1. Resume current state.
2. Refresh track portfolio.
3. Select safe parallel batch.
4. Write task cards.
5. Execute via branch/worktree workers, read-only scouts, execution runners, and reviewers.
6. Integrate one branch at a time.
7. Validate cheapest sufficient proof first.
8. Classify evidence.
9. Update state/ledger/context index.
10. Return exit status.

## Dynamic orchestrator-worker split

The orchestrator should not freeze the team shape at session start. Re-split the work whenever new evidence changes independence, risk, resource locks, or cost:

- promote a read-only finding into a branch/worktree worker only after the write scope is clear;
- split a worker lane when two implementation or execution targets become independent;
- collapse or serialize lanes when they contend for the same branch, worktree, device, GPU, browser, dataset, or central config;
- add a `mar_program_auditor` review when the team is drifting toward early completion, under-parallelization, over-spend, or unclear milestone gates.

For cloud or branch-visible coding agents, require source-control-visible proof before integration: commits, diffs, logs, check results, PRs, or source-controlled reports.

## Budget and usage reporting

Budget reporting is part of the work product, not a retrospective nicety. Each product-program batch should record:

- intended versus actual parallelism;
- models/reasoning used and why they were sufficient;
- token or usage budget status when available;
- branches/worktrees opened and closed;
- artifacts, logs, PRs, checks, and demos used as evidence;
- work kept local and the cost or resource-lock reason.

## Completion guard

At the end of any broad product session, ask:

- Did a named product or milestone gate pass?
- Are artifacts/source-controlled evidence sufficient for a future agent to verify?
- Are next tasks defined if not finished?
- Would a human reasonably consider the requested product built?

If not, return `RUN_CONTINUES` or `BLOCKED_REQUIRES_HUMAN`.
