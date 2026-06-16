# 00 — Current Workflow Findings

## Scope of this assessment

The current workflow was assessed from three inputs:

1. The current `manage-autonomous-repo` skill repository.
2. The Gaussian Splatting repository as a structural example of a long-running Codex-managed project.
3. The uploaded `ai/` agent-memory archive.

The Gaussian Splatting project content is treated only as a workflow example. This document does not change that project’s technical roadmap.

## What the current workflow already gets right

The workflow is not primitive. Its strongest pieces are worth preserving:

- It treats the repository as a long-running engineering program, not a one-shot patch.
- It stores durable state in the repo rather than relying only on chat memory.
- It has real evidence discipline: run artifacts, demos, visual checks, acceptance gates, and negative-evidence records.
- The current skill already pushes parallel-first orchestration, branch/worktree isolation, explicit task cards, model/cost choices, evidence taxonomy, context capsules, and non-terminal program statuses.
- The GS example shows serious care around source fidelity, artifact provenance, retained demos, and failure classification.

These are foundational. The new workflow should not throw them away; it should make them cheaper and more composable.

## Where the current workflow is inefficient

### 1. Codex is being used as the global memory engine

The present pattern gives a long-horizon goal to a Codex orchestrator and asks it to keep the whole program moving. That forces scarce Codex usage to pay for repeated reading, synthesis, roadmap interpretation, and context maintenance. Those are exactly the jobs that Pro Extended sessions can do more cheaply for the user.

The new rule is: **Pro does wide read-only reasoning; Codex does bounded repo execution.**

### 2. Parallelism exists in principle but collapses in practice

The current skill supports branch-separated work, but the applied workflow still often behaves like one main agent moving one large branch forward. Two separate repo copies/branches are not useful by themselves if one becomes abandoned while the other becomes the de facto main line. Parallelism requires active, owned lanes with branch base, worktree path, owned scope, avoid scope, proof artifact, resource locks, and integration order.

The new rule is: **parallel branches are a managed portfolio, not a pile of alternate checkouts.**

### 3. Documentation has become too large to be operational memory

The uploaded archive contained about 160 files, 3.26 MB, and roughly 47,600 lines under `ai/`. The top-level `state.md`, `agent-ledger.md`, `testing.md`, and `demos.md` were each large enough to make repeated full reads wasteful. The `plans/` directory alone contained 129 files and about 1.69 MB of content.

The problem is not that these artifacts exist. The problem is that they are not tiered aggressively enough. A fresh agent should not have to read a huge state page and a huge ledger to learn the next three actions.

The new rule is: **compact dashboards first, archived evidence second, targeted retrieval only.**

### 4. Append-only state creates contradictions and stale instructions

The GS repo example shows the risk: durable docs include high-value facts, but also old status sections that can disagree with newer sections. In a long-running project, “latest update” paragraphs appended over time become both evidence and a hazard. Stale branch, remote, artifact, and path facts are expensive because future agents must reconcile them.

The new rule is: **replace dashboards, append ledgers.** Current state is overwritten and kept small; dated batch ledgers preserve history.

### 5. Planning artifacts can outnumber execution artifacts

The uploaded branch docs showed many `request`, `contract`, `readiness`, `smoke`, and diagnostic plan artifacts. This is useful for complex evidence projects, but it becomes costly when a planning chain keeps creating more contracts instead of ending in a runnable implementation/execution packet or a parked/rejected route.

The new rule is: **every planning chain must terminate into action, parking, rejection, or a named human/external blocker.**

### 6. Micro-scoped runs are not the same as fast iteration

The current implementation pattern sometimes creates narrow runs that are too small to create a meaningful demo or integration delta, while still paying orchestration overhead. The right unit is not “tiny task” but **reviewable branch packet**: one coherent change that can be validated, merged, or parked independently.

The new rule is: **scope branches around proof-producing deltas, not arbitrary smallness.**

## Root cause

The core structural issue is a mismatch between responsibilities:

- **Pro Extended capacity** is abundant for the user, but it is not the layer currently doing most ongoing orchestration.
- **Codex capacity** is scarce, but it is being asked to repeatedly reload context, maintain long-horizon strategy, generate docs, and implement.
- **Repo memory** is durable but too append-heavy, so it becomes a context burden rather than a context accelerator.

## Design requirements for the replacement workflow

The replacement workflow must:

1. Move wide-context planning and review to Pro Extended.
2. Keep Codex prompts small, branch-specific, and proof-oriented.
3. Support several simultaneous implementation branches without uncoordinated global agents.
4. Preserve one authoritative integration branch per milestone.
5. Make demos improve incrementally through validated branch packets.
6. Convert stale documentation into compact dashboards plus dated evidence archives.
7. Keep model choice and agent count visible as a budget ledger.
8. Treat evidence status, provenance, and negative results as first-class state.
9. End every cycle with an explicit next batch and non-terminal status unless a product gate truly passes.
