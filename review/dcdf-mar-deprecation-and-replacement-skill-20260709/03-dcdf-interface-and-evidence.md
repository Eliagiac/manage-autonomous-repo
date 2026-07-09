# DCDF Interface And Evidence

## Intended Boundary

The intended relationship was:

- DCDF decides whether a lane exists, what authority it has, what it may touch,
  what proof is required, and how receipts bind to task/repo facts.
- MAR helps an accepted lane organize repository execution through tracks,
  subagents, branches/worktrees, evidence, docs, and integration.

This is a sensible authority split. MAR should not parse Director Orders,
operate the global ledger, become an outbox target, or own official Codex
lifecycle.

## How The Boundary Developed

### Pass 1.1 Compatibility

DCDF Pass 1.1 explicitly deferred MAR compatibility to a later phase after
controller/order/lifecycle stabilization. The 2026-06-22 MAR compatibility
branch then added:

- DCDF mode to the skill;
- lane-task and run-receipt templates;
- validator script;
- examples;
- documentation saying DCDF overrides MAR.

This was the first attempt to make the two frameworks compose formally.

### MAR Onboarding Orders

DCDF then tried to onboard/register MAR through Director Orders:

- onboarding 0002 used unstable repository facts and produced deadletter/
  receipt ambiguity;
- onboarding 0003 reached controller/lane execution;
- its top-level receipt said completed;
- its lane receipt recorded `OUTPUT_SCHEMA_INVALID`;
- archived task `019f2457-...` contains no valid terminal output.

This is the canonical false-green example in the July 5 DCDF review.

### Ledger Registration PR

[DCDF PR #14](https://github.com/Eliagiac/dcdf/pull/14), opened 2026-07-03,
proposed:

- registering MAR in the single global DCDF ledger;
- setting DCDF architecture helper budget to six threads/depth two;
- keeping MAR lane-local under DCDF.

The PR remained draft until terminal watcher/controller evidence existed.
Three validation handoffs were published on 2026-07-04.

### MAR Parallel-Memory PR

[MAR PR #1](https://github.com/Eliagiac/manage-autonomous-repo/pull/1)
opened minutes before DCDF PR #14. It adds DCDF mode plus parallel-safe memory
files and says its controller-bound validation is delegated through PR #14.

The two PRs therefore form a coupled validation pair:

- DCDF attempts to register and validate MAR;
- MAR changes itself to be safer inside DCDF;
- each depends on the other's doctrine/evidence.

### 2.0.0 Closure

On 2026-07-08, DCDF PR #14 was closed unmerged as superseded. Its closing
comment states:

- schema-accepted lane skills remain `dcdf-run-lane` and
  `dcdf-codex-lifecycle`;
- MAR may be non-authoritative lane-local doctrine;
- MAR must not become scheduler, ledger owner, outbox target, Director Order
  parser, or lifecycle authority.

MAR PR #1 remained open/draft without review or checks. Its stated validation
path was now stale.

## What The Linked Pro Chat Adds

The exact DCDF vNext/2.0.0 conversation does not call for full MAR
deprecation. It says MAR has value inside DCDF, but only as repo-local execution
doctrine.

It credits MAR with:

- independent tracks;
- branch/worktree isolation;
- task cards;
- resource locks;
- evidence classification;
- integration review;
- durable repo docs;
- model/cost discipline;
- Pro/Codex packet separation.

It also identifies that MAR's two-file active memory is not enough for
DCDF-scale parallel work and recommends context indexes, per-batch/per-lane
files, locks, branch maps, and evidence manifests. MAR PR #1 implements that
direction.

This is direct evidence for constraining MAR. The further decision to deprecate
MAR as a standalone framework is a later synthesis based on the owner's
experience and the repository history.

## Why The Coupling Was Unsuccessful

### 1. Two Frameworks Had To Be Loaded

A lane needed:

- DCDF task schema and authority;
- DCDF scope/capability/receipt rules;
- MAR orchestration/memory/source-control doctrine;
- compatibility rules deciding which default wins.

The combination increased rigor but also increased context and failure surface.

### 2. Validation Became Self-Referential

DCDF used its own outbox/controller/lifecycle to validate MAR's registration
and memory changes. During the same period, DCDF was repairing:

- stale repository facts;
- moving `main` heads;
- capability grants;
- project association;
- async lifecycle terminality;
- output schemas.

MAR integration evidence therefore depended on the reliability of the system
under repair.

### 3. The Memory Critique Produced More Memory

The Pro chat correctly found that shared `state.md` plus append-style
`agent-ledger.md` could not safely hold many active lanes. MAR PR #1's
solution creates per-lane and supporting state files.

That is internally coherent inside DCDF. It is externally impractical for the
owner's desired workflow because GitHub already has issues, PRs, refs, checks,
reviews, and projects. The compatibility fix deepened the dual-source problem.

### 4. Model And Thread Policies Could Conflict

MAR's baseline recommended ten threads, depth two, and a medium-reasoning main
orchestrator. DCDF had its own helper budget and task-bound model policy.

The correct rule was "DCDF wins," but that makes MAR presets/defaults advisory
and means the lane cannot be understood from MAR alone.

### 5. External State Never Closed

The final GitHub state is revealing:

- DCDF PR #14: closed unmerged;
- MAR PR #1: still draft;
- no MAR issue tracking the supersession;
- no PR review/check explaining the final MAR disposition.

The durable coordination story ended in a Pro chat and a comment in the other
repository, not in MAR's own GitHub workflow.

## What Survives The Interface

The successful boundary is still worth preserving:

- Pro performs wide read-only planning/review.
- Codex executes bounded repo work.
- task scope and proof are explicit.
- branches/worktrees isolate writers.
- evidence is source-control/GitHub-visible.
- a lane cannot accept itself.
- high-impact decisions use high reasoning.

Those principles do not require either DCDF runtime or MAR's full memory/
bridge system.

## Evidence Classification

High-confidence GitHub facts:

- MAR PR #1 state/body/commits/files;
- DCDF PR #14 state/body/closing comment;
- DCDF PRs #29, #30, #35, and #36;
- no MAR issues/checks/reviews.

High-confidence tracked/local-ref facts:

- MAR public and local commit graphs;
- medium orchestrator default;
- local compatibility/privacy refs;
- public/local/installed divergence;
- closed-loop reference/template drift.

Local-only task facts:

- false-green onboarding task;
- Pass 1.1 compatibility work;
- long-horizon dogfood;
- ARO control-plane implementation.

Reviewer inference:

- maintaining permanent DCDF compatibility would preserve too much combined
  context and state surface.

User decision:

- both frameworks are deprecated in favor of a future GitHub-native skill.
