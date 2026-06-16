# 08 — Budget and Model Policy

## Core budget strategy

Use the abundant read-only Pro Extended layer for wide reasoning. Use limited Codex capacity for actions only Codex can perform well inside the repo: edits, tests, command execution, demos, source-control operations, and branch-visible evidence.

## Spend hierarchy

Spend Pro tokens on:

- broad research;
- roadmap and architecture review;
- doc comparison and context pruning;
- track portfolio selection;
- execution packet writing;
- review of diffs, reports, demos, and ledgers;
- next-batch planning.

Spend Codex tokens on:

- source edits;
- test writing/running;
- command execution;
- demo capture/validation;
- CI/PR/source-control operations;
- local debugging;
- evidence materialization.

Do not spend Codex tokens on repeated broad context synthesis when Pro can prepare the context capsule first.

## Model allocation by role

Use the cheapest sufficient model/effort available in the current environment. Avoid hard-coding product limits into repo docs; record the role and reason instead.

| Role | Default reasoning need | Notes |
| --- | --- | --- |
| Pro Director | high judgment, read-only | wide context, planning, review |
| Codex Integration Agent | medium/high judgment | branch state, merge, validation |
| Read-only scout | cheap/high or medium | bounded docs/source/test mapping |
| Code worker | medium | clear scoped implementation |
| Deep code worker | high | subtle debugging/cross-module work |
| Execution runner | cheap/medium | commands, artifacts, logs |
| Reviewer | high, read-only | blocks first, suggestions second |
| Senior synthesis | rare high | only for ambiguous high-value decisions |

## Budget ledger

Every batch records:

```text
Planned lanes:
Actual lanes:
Models/effort by lane:
Why each was sufficient:
Codex runs avoided by Pro planning:
Orchestrator-local heavy work:
Resource locks:
Validation artifacts:
Branches integrated/parked/rejected:
Spend concerns:
Next budget adjustment:
```

## Cost anti-patterns

- One Codex orchestrator rereads the full docs tree every cycle.
- Several Codex agents independently perform the same broad research.
- Agents produce long prose with no branch, artifact, command, or decision.
- High-reasoning models do rote JSON/doc edits.
- Execution runs begin before cheap readiness gates.
- Raw logs are pasted into chat instead of summarized by path.
- Branches are too tiny to prove anything but still require full orchestration overhead.
- Branches are too broad to review or merge safely.

## Budget gates

Before starting a Codex batch, ask:

- Can Pro shrink this context further?
- Does every Codex lane have a proof artifact?
- Does every write lane have a branch/worktree?
- Is there a cheaper test before heavy execution?
- Are resource locks named?
- Is the integration agent able to absorb this many outputs?

Stop or replan when the answer is no.
