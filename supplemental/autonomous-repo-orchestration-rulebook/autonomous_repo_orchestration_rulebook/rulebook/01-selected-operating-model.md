# 01 — Selected Operating Model

## Final decision

Use **Pro Director + Codex Branch Federation**.

This is a two-plane architecture:

- **Director plane:** a ChatGPT Pro Extended session that is read-only. It reads broad context, compares docs, reasons about strategy, selects the next branch batch, writes task cards, reviews worker outputs, and decides what to integrate or park.
- **Execution plane:** Codex agents that work from compact execution packets. Each Codex implementer owns one branch/worktree or one read-only/execution lane and returns source-control-visible evidence.

The director plane is allowed to be intellectually broad. The execution plane must be operationally narrow.

## Why this is better than the alternatives

| Candidate | Description | Speed | Budget | Parallelism | Merge safety | Context risk | Verdict |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Single global Codex orchestrator | One Codex agent reads everything, plans, implements, tests, updates docs | Low | Poor | Low | Medium | High | Deprecated |
| Multiple global Codex orchestrators | Several Codex agents each try to own broad strategy on separate branches | Medium | Poor | Medium | Poor | High | Reject |
| Pro-only planning + sequential Codex | Pro writes plans; one Codex agent applies them one by one | Medium | Good | Low | High | Low | Useful fallback |
| Full autonomous swarm | Many Codex agents with no single director/integration owner | High at first | Poor | High | Poor | High | Reject for long-running repos |
| **Pro Director + Codex Branch Federation** | Pro plans/reviews; Codex agents implement bounded branch packets; one integration branch | High | Best | High | High | Low | **Selected** |

## Why not “multiple main agents”?

Multiple main agents are useful only when “main” means **branch owner for a bounded goal**. They are harmful when each one becomes a global orchestrator with its own interpretation of the roadmap. That creates duplicate reasoning, divergent docs, abandoned branches, and expensive merges.

The selected model therefore allows many active Codex agents, but only one director of record and one integration owner per milestone.

## Authority hierarchy

1. **Human owner** decides product direction, paid/destructive actions, credentials, legal/licensing questions, and final acceptance.
2. **Pro Director** owns read-only strategic synthesis, batch selection, task cards, and review recommendations.
3. **Codex Integration Agent** owns the integration branch, merge sequencing, conflict resolution, and final validation commands for a batch.
4. **Codex Worker Agents** own branch/worktree-scoped implementation, execution, research, review, or demo proof.
5. **Repo docs and Git history** are the durable source of truth after integration.

## Primary objects

### Context capsule

A compact director-authored packet containing only the facts a worker or integration agent needs now.

### Track portfolio

A flat set of candidate work lanes scored by value, independence, proof clarity, resource locks, and integration cost.

### Execution packet

A branch-specific contract for a Codex agent. It includes objective, branch/worktree, owned scope, avoid scope, validation, proof artifact, stop conditions, and handoff format.

### Integration branch

The orchestrator-owned branch named `integrate/<milestone>` where worker outputs are merged one by one.

### Batch ledger

A short dated record of selected tracks, agents, models, branches, resource locks, validation, integration status, budget notes, and next split points.

## Operating principle

A Codex agent should never need to understand the whole project to complete a branch. A Pro Director should never need to mutate the repo to make a good strategy decision.
