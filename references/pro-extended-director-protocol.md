# Pro Extended Director Protocol

Use this reference when the user wants to exploit abundant ChatGPT Pro Extended reasoning while minimizing Codex usage.

## Core split

- **Pro Extended Director:** read-only. Owns broad research, roadmap synthesis, context pruning, track portfolio selection, execution-packet writing, budget review, and post-batch review.
- **Codex Integration Agent:** bounded repo mutation. Owns branch/worktree verification, integration branch setup, worker dispatch, merge sequencing, validation, compact docs update, and source-control-visible handoff.
- **Codex Workers:** branch/worktree-scoped execution. Own one implementation, execution, review, demo, or read-only lane.

Do not make Codex pay for broad strategy that Pro has already performed unless repo state invalidates the Pro packet.

## When a Pro packet is present

If the prompt contains a Pro-generated context capsule, track portfolio, execution packets, or integration plan:

1. Treat it as the starting plan, not as optional inspiration.
2. Verify current repo state before acting.
3. If current repo state contradicts the packet, write a short invalidation report and stop or re-scope narrowly.
4. If valid, create/select the integration branch and worker branches/worktrees.
5. Dispatch workers with the packet scopes.
6. Avoid re-reading full roadmaps, giant ledgers, or raw research unless the packet points there.
7. Do not broaden worker scopes into global orchestration.
8. Report back in a Pro-review packet.

## Pro Director responsibilities

The Pro Director should produce:

- compact context capsule;
- current branch/worktree/PR assumptions;
- active/candidate/blocked/parked track portfolio;
- selected batch sized by safe concurrency and integration bandwidth;
- one task card per lane;
- resource locks;
- validation ladder;
- integration order;
- known negative evidence not to repeat;
- budget/model notes;
- post-Codex review checklist.

## Codex Integration Agent responsibilities

The integration agent should:

- verify `git status --short --branch`, remotes, worktrees, and branch bases;
- create/select `integrate/<milestone>`;
- create worker branches/worktrees for write lanes;
- dispatch subagents or perform narrowly assigned integration work;
- never duplicate a dispatched worker lane locally;
- merge worker branches one at a time;
- run narrow then broad validation;
- update compact `docs/ai/state.md`, batch ledger, context index, tests, demos, and decisions as needed;
- produce the Pro-review packet.

## Worker responsibilities

Workers receive an execution packet and stay inside it. They should not read broad context or reinterpret the roadmap. They must return artifacts, changed files, commands, validation, risks, and an integration recommendation.

## Invalid packet conditions

Stop or re-scope if:

- branch/worktree state differs materially from the packet;
- files named by the packet are missing or already changed by another active lane;
- resource locks conflict;
- validation commands no longer exist;
- the task requires credentials, paid/destructive actions, or human decisions;
- the worker would need to edit avoid-scope files;
- the packet repeats a known negative route without a new hypothesis.

## Output contract: Pro-review packet

```text
Integration branch:
Worker branches:
Merged:
Parked/rejected/blocked:
Changed files:
Validation:
Demos/evidence:
Docs updated:
Resource locks used:
Budget/model notes:
Packet assumptions invalidated:
Next recommended Pro review questions:
```
