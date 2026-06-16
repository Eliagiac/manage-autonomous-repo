# 06 — Integration, Review, and CI

## Integration branch

Use `integrate/<milestone>` whenever more than one branch or worker output is active.

The integration branch is the only branch that combines worker outputs. It is owned by the integration agent.

## Merge order

Merge one branch at a time.

Default order:

1. tests/fixtures that clarify expected behavior;
2. low-conflict foundations;
3. feature branches with narrow owned scope;
4. docs/demo branches that depend on the features;
5. cleanup/refactor branches last unless they unblock integration.

High-conflict branches should be reviewed before merging. Park low-value branches rather than delaying validated high-value branches.

## Pre-merge checklist

Before merging a worker branch:

- read worker handoff;
- inspect changed files;
- compare changed files against other active branches;
- verify branch base;
- confirm proof artifacts exist;
- run or review narrow validation;
- check docs/demos/test updates where required;
- decide merge, park, reject, or split.

## Conflict policy

Conflicts are semantic decisions, not line-edit chores.

When a conflict appears:

1. Freeze overlapping writes.
2. Identify semantic ownership of each file.
3. Read both sides and the merge base.
4. Preserve both valid behaviors when possible.
5. If behaviors conflict, record the product/architecture decision.
6. Run narrow validation.
7. Update docs or decisions if a new invariant was discovered.

Escalate to Pro Director review for large or ambiguous conflicts.

## CI policy

Every long-running repo should define a validation ladder:

1. formatting or syntax checks;
2. unit/smoke tests;
3. focused subsystem tests;
4. integration tests;
5. demo or runtime proof;
6. acceptance gate.

Worker branches run the cheapest sufficient proof. Integration branches run broader validation.

## Pull requests

When GitHub is available, PRs are durable coordination objects. Each PR should include:

- goal and scope;
- branch base;
- files/modules touched;
- tests/demos run;
- evidence artifacts;
- docs updated;
- risks and rollback plan;
- agents involved;
- integration recommendation.

## Post-merge state update

After a batch merge:

- update `docs/ai/state.md` as a compact dashboard;
- add a dated batch ledger;
- update `docs/ai/context-index.md` only if paths changed;
- update test/demo indexes if coverage changed;
- mark branches as merged, parked, rejected, blocked, or continued;
- remove or document worktrees;
- produce a Pro-review packet.

## Pro review packet

After integration, give Pro:

```text
Integration branch:
Merged branches:
Parked/rejected branches:
Diff summary:
Validation:
Demos/evidence:
Docs updated:
Budget/agent usage:
Known risks:
Next candidate tracks:
```
