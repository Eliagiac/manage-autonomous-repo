# 05 — Codex Implementer Contracts

## Purpose

Codex implementers are scarce execution resources. Their prompts should be small, bounded, and artifact-oriented.

A Codex implementer should not be asked to “continue the repo toward the roadmap” unless it is the thin integration agent for a cycle. Ordinary workers receive execution packets.

## Integration agent contract

The integration agent may read more context than workers, but it is still not the director. Its job is to execute the Pro Director’s batch plan safely.

It may:

- verify branch/worktree status;
- create worker branches/worktrees;
- dispatch workers;
- merge worker branches into `integrate/<milestone>`;
- resolve conflicts;
- run validation;
- update compact state and batch ledger;
- report invalidated assumptions.

It must not:

- silently replace the director’s portfolio with its own broad plan;
- spend the whole run implementing one worker’s task while safe workers exist;
- keep broad, redundant context in its prompt;
- let workers write on `main`;
- accept chat-only worker claims when branch-visible proof is possible.

## Worker contract

A worker receives:

```text
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
```

A worker returns:

```text
Status: ready_to_integrate | parked | blocked | rejected | needs_split
Branch/worktree:
Changed files:
Commands run:
Proof artifacts:
Validation result:
Risks:
Docs updated:
Integration recommendation:
Next action:
```

## Prompt rules

- Put stable role instructions first and variable task context later.
- Do not paste whole roadmaps, giant ledgers, raw logs, or entire research corpora.
- Tell workers which files to read and which to avoid.
- Require artifact paths, not transcripts.
- Require workers to list relied-on files.
- Require workers to stop if the task scope becomes invalid.
- For write tasks, require a branch/worktree.
- For execution tasks, require command, output path, timeout/stop conditions, and resource lock.

## Codex subagents inside a worker

A branch-owning worker may spawn helper subagents only when allowed by the environment and useful for independent subtasks. Helpers must remain within the parent worker’s scope. They cannot become a second global orchestration layer.

Good helper uses:

- test discovery for the worker’s files;
- focused code review of the worker branch;
- log analysis for a failing command;
- artifact QC for the worker’s demo;
- dependency/API lookup for the worker’s narrow task.

Bad helper uses:

- broad roadmap review;
- overlapping implementation in the same files;
- rewriting the task scope;
- duplicating another active worker’s lane.

## Worker done conditions

A worker is done only when it has one of these outcomes:

- `ready_to_integrate` — proof exists and scope stayed valid.
- `parked` — useful but not worth integrating now; evidence is summarized.
- `blocked` — named blocker prevents progress.
- `rejected` — negative evidence says do not repeat without new hypothesis.
- `needs_split` — safe sub-scope found, but current task is too broad or conflicting.

“Made progress” is not enough.
