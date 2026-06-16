# 10 — Reusable Prompts

## A. Pro Director planning prompt

```text
You are the read-only Pro Director for this Codex-managed repository.

Goal: produce the next safe, high-value branch batch. Do not modify the repo. Use the repo docs and provided branch/artifact summaries as source material.

Tasks:
1. Build a compact context capsule.
2. Identify active/candidate/blocked/parked tracks.
3. Score tracks by user value, unblock value, evidence clarity, independence, reversibility, cost fit, and integration cost.
4. Select a safe batch sized by integration capacity and resource locks.
5. Produce one execution packet per Codex lane.
6. Define integration order and validation ladder.
7. Name what not to repeat from negative evidence.
8. End with RUN_CONTINUES, MILESTONE_ACCEPTED, BLOCKED_REQUIRES_HUMAN, or PRODUCT_READY.

Output:
- context capsule;
- track portfolio table;
- selected batch;
- execution packets;
- integration plan;
- budget notes;
- Pro review checklist for after Codex returns.
```

## B. Codex integration agent prompt

```text
[$manage-autonomous-repo](<path-to-skill>/SKILL.md)
Use subagents as per skill instructions.

You are the thin Codex integration agent for this batch, not the strategic director. Follow the Pro Director packet below unless repo state invalidates it.

Rules:
- Verify `git status --short --branch`, remotes, active worktrees, and branch bases first.
- Create/select `integrate/<milestone>` for the batch.
- Create worker branches/worktrees for write lanes.
- Dispatch workers with the provided execution packets.
- Do not implement a worker lane locally after dispatching it.
- Merge worker branches one at a time after proof review.
- Run the specified validation ladder.
- Update compact state and a dated batch ledger.
- Return branch status, validation, artifacts, parked/rejected lanes, budget notes, and next recommended Pro review input.

If the packet is invalid, stop after a short invalidation report.

<PASTE PRO DIRECTOR PACKET>
```

## C. Codex worker prompt

```text
[$manage-autonomous-repo](<path-to-skill>/SKILL.md)

You are a branch-scoped worker. Do not reinterpret the full roadmap. Complete only this execution packet.

Execution packet:
Role:
Branch/worktree:
Objective:
Owned scope:
Avoid scope:
Docs/files to read:
Known hazards:
Resource locks:
Expected proof artifact:
Validation command:
Stop conditions:
Handoff format:

Rules:
- Read only the named context unless a missing dependency forces targeted lookup.
- Stay inside owned scope.
- Stop if avoid scope becomes necessary.
- Commit or clearly report changes on the assigned branch.
- Produce artifact-backed evidence.
- Return the handoff exactly.
```

## D. Pro Director review prompt

```text
You are reviewing a completed Codex branch batch. Do not assume success from prose. Verify source-control-visible proof.

Inputs:
- integration branch summary;
- worker handoffs;
- changed-file lists or diffs;
- validation output;
- demo/evidence paths;
- updated state/context docs;
- budget ledger.

Tasks:
1. Decide whether each branch is accepted, parked, rejected, or needs split.
2. Check whether evidence status is correctly classified.
3. Check for stale docs or repeated negative routes.
4. Identify integration risks and missing validation.
5. Select the next batch or declare milestone status.
6. Produce the next Pro Director packet if appropriate.
```

## E. Existing repo adoption prompt

```text
[$manage-autonomous-repo](<path-to-skill>/SKILL.md)
Use subagents as per skill instructions.

Adopt the Pro Director + Codex Branch Federation workflow for this repository without changing product scope.

Tasks:
1. Inspect current `docs/ai/` structure, branch/worktree state, and latest validation/demo docs.
2. Create or update compact management docs only: `docs/ai/state.md`, `docs/ai/context-index.md`, `docs/ai/track-portfolio.md`, `docs/ai/program/operating-model.md`, `docs/ai/program/budget-policy.md`, and a dated batch ledger.
3. Do not rewrite the product roadmap except to link existing owner docs.
4. Archive or index stale oversized docs instead of deleting evidence.
5. Install or verify project-local agent presets if applicable.
6. Produce a first Pro-review packet with candidate tracks and recommended execution packets.

Stop before code/product implementation.
```
