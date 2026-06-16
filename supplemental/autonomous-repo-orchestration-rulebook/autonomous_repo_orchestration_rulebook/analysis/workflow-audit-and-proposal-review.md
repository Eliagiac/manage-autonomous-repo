# Workflow Audit and Proposal Review

## Observed workflow shape

Current pattern:

1. Pro model gathers research notes, orchestration plans, and long-horizon prompts.
2. The docs are integrated into the repo.
3. A single Codex orchestrator is given the skill and a broad goal.
4. The orchestrator performs baseline reading, planning, implementation, tests, demos, and docs updates.
5. Branches/worktrees may exist, but long-horizon ownership tends to collapse back to one active branch.

This works for correctness and restartability, but it is slow because scarce Codex sessions carry too much strategic context and too much historical documentation.

## Evidence from the provided example

The uploaded memory archive shows both the strengths and the problem:

- about 160 files under `ai/`;
- about 3.26 MB of memory/plans/research;
- about 47,600 total lines;
- 129 plan files under `ai/plans/`;
- top-level state, testing, demos, artifact-retention, and agent-ledger docs are very large;
- many artifacts are contracts, requests, readiness reports, diagnostics, smokes, negative evidence, and acceptance-like records.

This is a sophisticated evidence project, but not an efficient context surface for every Codex run.

## Proposal A — Keep one global Codex orchestrator

### Implementation

Continue giving Codex the skill and long-horizon product goal. Improve prompts and maybe add more subagents.

### Benefits

- Simple mental model.
- One agent has full continuity.
- Lower merge conflict risk than uncoordinated multi-agent work.

### Costs

- Codex pays for repeated broad reading.
- Slow iteration because one context owns planning and implementation.
- Subagents tend to become audits instead of independent implementation lanes.
- Abandoned branch copies can accumulate because the orchestrator naturally focuses on one main line.

### Verdict

Reject as the primary workflow. Keep only as a fallback for small repos or true serial blockers.

## Proposal B — Multiple independent main Codex agents

### Implementation

Start several Codex sessions, each on a separate branch, each with the broad goal and skill.

### Benefits

- More raw parallelism.
- Several implementation directions can progress independently.

### Costs

- Each agent pays the broad-context tax.
- Branches diverge semantically.
- Docs drift and duplicate.
- Merge cost becomes unpredictable.
- Agents may each believe they are the program owner.

### Verdict

Reject in this unrestricted form. It solves wall-clock speed by worsening budget and integration risk.

## Proposal C — Pro-only planning, one sequential Codex implementer

### Implementation

Pro writes detailed plans and prompts. Codex runs one packet at a time.

### Benefits

- Much better Codex budget use.
- Stronger prompts and less context waste.
- Simple merges.

### Costs

- Does not exploit safe independent branches.
- Iteration still bottlenecks on one implementer.
- Heavy execution/demos can block code progress.

### Verdict

Good fallback when branch independence is low. Not enough for ground-up projects with several independent tracks.

## Proposal D — Pro Director + Codex Branch Federation

### Implementation

Pro Director prepares context capsules, track portfolio, execution packets, integration order, and budget plan. A thin Codex integration agent verifies repo state, creates an integration branch and worker branches/worktrees, dispatches bounded workers, merges one by one, validates, and reports back to Pro.

### Benefits

- Best budget alignment: Pro does wide reading; Codex does bounded repo action.
- High parallelism without multiple global orchestrators.
- Branch/worktree isolation turns parallel work into reviewable units.
- Clear integration branch prevents abandoned branch chaos.
- Pro can review outputs before another Codex batch spends tokens.

### Costs

- Requires stricter packet writing.
- Requires branch/worktree discipline.
- Requires a compact docs migration for existing large repos.

### Verdict

Selected.

## Proposal E — Fully autonomous swarm

### Implementation

Let many agents plan, implement, review, and merge dynamically with minimal central control.

### Benefits

- Maximum theoretical concurrency.
- Useful for very large, highly modular codebases with mature CI and automated merging.

### Costs

- Poor fit for research/product repos where evidence status and product gates require judgment.
- High context duplication.
- High merge and docs drift risk.
- Hard to budget.

### Verdict

Reject for the target use case.

## Interaction effects in the selected model

### Pro planning + context capsules reduces Codex scope

When Pro supplies short execution packets, Codex workers avoid reading large docs. This compounds with prompt-cache-friendly stable prefixes and with smaller handoffs.

### Branch federation + evidence taxonomy reduces abandoned work

Every branch has an explicit proof status: ready, parked, blocked, rejected, or accepted. This prevents the current pattern where a branch copy is left behind without being a useful alternative result.

### Batch ledger + compact state reduces future reading

The more branches run in parallel, the more important it is to keep a compact batch ledger. Otherwise parallelism creates more docs than progress.

### Demo ladder + proof-oriented branch packets prevents fake iteration

A branch is not considered useful because it changed files; it must improve a proof, demo, gate, test, or evidence classification.

### Pro review after integration controls Codex overspend

The system should not automatically start another Codex batch after a large merge. Pro should inspect what happened and reselect the portfolio.

## Conclusive recommendation

Adopt Proposal D as the default for all Codex-managed ground-up projects:

> Pro Extended is the read-only director of record. Codex is a branch-federated implementation and evidence engine. Repo docs are compact dashboards plus indexed archives. Every cycle starts with Pro track selection and ends with Pro review.
