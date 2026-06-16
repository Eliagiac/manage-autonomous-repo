# Autonomous Repo Orchestration Rulebook

This bundle defines the project-agnostic workflow I recommend for repositories that are intended to be managed mostly or entirely by Codex agents while using ChatGPT Pro Extended sessions as the abundant, read-only orchestration layer.

**Selected operating model:** **Pro Director + Codex Branch Federation**.

That means future Pro Extended chats do the expensive wide-context work: research synthesis, roadmap review, track selection, budget planning, branch/merge strategy, and prompt/context-packet generation. Codex agents do bounded repository execution: source edits, command runs, demos, tests, evidence capture, and branch-visible handoffs. The old pattern of one long-horizon Codex orchestrator reading everything and slowly doing all implementation is explicitly deprecated.

## Files

- `rulebook/00-current-workflow-findings.md` — what the current workflow does well and where it wastes budget or slows iteration.
- `rulebook/01-selected-operating-model.md` — proposal review and the final chosen approach.
- `rulebook/02-operating-loop.md` — the canonical end-to-end loop for every autonomous repo cycle.
- `rulebook/03-context-and-memory-budgeting.md` — how to keep repo memory restartable without making every agent read megabytes of stale docs.
- `rulebook/04-track-portfolio-and-branch-federation.md` — how to split work into independent branch/worktree lanes.
- `rulebook/05-codex-implementer-contracts.md` — how to prompt and constrain Codex implementation agents.
- `rulebook/06-integration-review-and-ci.md` — merge, PR, CI, and conflict rules.
- `rulebook/07-evidence-demo-and-acceptance.md` — how demos, artifacts, negative evidence, and acceptance gates should work.
- `rulebook/08-budget-and-model-policy.md` — model/agent budgeting with Pro as the cheap strategic layer and Codex as the scarce execution layer.
- `rulebook/09-standard-repo-docs.md` — the recommended `docs/ai/` structure for all future repos.
- `rulebook/10-prompts.md` — reusable Pro and Codex prompts.
- `rulebook/11-adoption-plan.md` — how to migrate an existing repo to this system.

Templates and schemas are under `templates/` and `schemas/`. A copy-ready generic repo starter pack is under `repo-starter-pack/`.

## Non-negotiable defaults

1. **One director of record per planning cycle.** The director is a Pro Extended chat unless unavailable. It is read-only and owns synthesis, prioritization, task cards, and review of returned evidence.
2. **Many Codex implementers, not many global orchestrators.** Parallel Codex agents should own branches/worktrees or read-only/execution lanes. They should not each reinterpret the full project roadmap.
3. **One integration branch per milestone.** Worker branches merge into `integrate/<milestone>` one at a time. `main` stays stable.
4. **Execution packets replace broad goals.** Codex gets a compact context capsule plus a branch-specific task card, not the entire research corpus.
5. **Repo memory is a dashboard plus append-only evidence, not an append-only novel.** `state.md` and `context-index.md` stay compact; raw logs, old plans, giant ledgers, and run manifests move to dated batch files or archives.
6. **Every branch has a proof artifact.** A branch that produces only prose is usually a failed use of Codex budget unless it was explicitly read-only research.
7. **Planning must terminate.** Every planning chain ends in an implementation card, execution card, parked/rejected lane, or human-blocked decision.
8. **Pro reviews before Codex spends again.** After each branch batch, Pro should review summaries/diffs/artifacts and choose the next batch before another broad Codex run.
