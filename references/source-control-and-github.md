# Source Control and GitHub

Use this reference when creating the repository, branching, integrating work, or coordinating GitHub state.

## Baseline Setup

1. Run `git status --short --branch`.
2. If `.git` is absent, run `git init`, create a sensible `.gitignore`, and make an initial baseline commit after confirming generated/vendor files are excluded.
3. If a remote is absent and GitHub tools or `gh` are available, create or propose a GitHub repository. Prefer private unless the project clearly belongs public.
4. Protect the default branch when repository settings allow it: require status checks, PRs, conversation resolution, and no force pushes for important branches.
5. Create `docs/ai/state.md` before large autonomous work begins.

## Branch Policy

Use named branches for all meaningful changes:

- `plan/<topic>` for planning/doc-only preparation.
- `research/<topic>` for experiments and investigation notes.
- `feat/<topic>` for feature work.
- `fix/<topic>` for bug fixes.
- `refactor/<topic>` for structural changes.
- `test/<topic>` for test harness work.
- `demo/<topic>` for demo and showcase work.
- `integrate/<milestone>` for merging multiple agent outputs.

Make small, coherent commits with messages that explain intent and validation. Avoid committing secrets, local machine paths, generated caches, or unrelated formatting.

## Worktrees

Use Git worktrees for parallel branches when multiple agents or experiments need isolated checkouts. Prefer one worktree per independent worker. Remove worktrees with `git worktree remove` after integration, and use `git worktree list` to audit active work.

Good uses:

- Competing architecture prototypes.
- Independent feature slices.
- Risky refactors that should not disturb the main checkout.
- Emergency fixes while a larger branch remains dirty.

Avoid worktree sprawl. Record active worktrees in `docs/ai/agent-ledger.md` or `docs/ai/state.md`.

Worktree lifecycle:

1. Confirm current branch and dirty state before creating a worktree.
2. Create or select a branch whose name matches the track role and scope.
3. Run the repo's setup or baseline checks in the worktree before assigning implementation.
4. Record branch, path, owner, owned scope, avoid scope, and validation command in the agent ledger.
5. Keep generated caches and run artifacts ignored or outside tracked source unless they are deliberate fixtures.
6. After integration, classify the worktree as merged, parked, discarded, or continued, then remove or document it.

## Branch Placement Decision

Decide branch placement before assigning any write task.

Use a separate worker branch/worktree when any of these are true:

- A subagent will write source-controlled files.
- The task can run independently from the orchestrator or another worker.
- The change is substantial, risky, experimental, long-running, or likely to be parked/discarded.
- Multiple implementation/prototype tracks are active in the same session.
- The task touches shared architecture, dependencies, migrations, generated fixtures, tests with broad blast radius, or user-facing behavior.
- The work needs separate validation, PR review, or rollback history.

Use the orchestrator's current branch only when all of these are true:

- There is exactly one active writer for the affected files.
- The change is small, sequential, and tightly coupled to orchestration or integration.
- The work is low-risk baseline/setup/docs/state work, or the branch is already the integration branch for merging worker outputs.
- The task is expected to finish in the current session and does not need to be parked as an independent result.
- The branch role matches the task, such as `plan/<topic>` for planning docs or `integrate/<milestone>` for integration fixes.

Read-only subagents do not need branches. If a read-only lane discovers a safe write scope, create a task card and branch before promoting it to implementation.

Do not let worker subagents write on the orchestrator's branch by default. Allow it only for explicitly delegated integration fixes, tiny docs/state updates, or when the task card records why a separate branch would add more risk than value.

## Branch-Separated Subagents

For broad autonomous repo goals, prefer branch-separated worker agents over a single orchestrator making all implementation changes.

Recommended structure:

- `main`: stable baseline. Do not let worker agents write here directly.
- `integrate/<milestone>`: orchestrator-owned branch where worker outputs are merged and validated.
- `feat/<topic>`, `fix/<topic>`, `refactor/<topic>`, `test/<topic>`, `demo/<topic>`: worker-owned branches, preferably checked out in separate worktrees.

Worker branch rules:

- Assign exactly one owning agent per worker branch.
- Assign owned files/modules and explicit avoid scopes before writes begin.
- Assign a conflict risk level before writes begin: `low`, `medium`, or `high`, with the likely overlap point.
- Keep branch changes coherent and independently testable.
- Do not merge worker branches into each other.
- Do not let workers merge into `main` or `integrate/<milestone>` unless the orchestrator explicitly delegates that integration step.
- Require final worker summaries to include branch name, worktree path, changed files, tests/commands run, risks, and integration recommendation.

Orchestrator branch rules:

- Create or choose `integrate/<milestone>` before merging multiple workers.
- Merge worker branches one at a time, starting with low-conflict foundations or tests.
- Run narrow validation after each merge; run broad validation after the batch.
- Resolve conflicts semantically, not by blindly preferring one branch.
- Update `docs/ai/agent-ledger.md`, `docs/ai/state.md`, roadmap, tests, and demos after integration.
- Delete or archive stale worker branches/worktrees after merge or rejection.

Use branch-separated work when at least two independent implementation lanes exist. Whether those lanes share a role label or product area does not matter; separable scope and safe integration order matter. Use read-only subagents only when the work is still too ambiguous to assign safe write scopes.

Main-branch exception:

- It is acceptable to use `main` for initial publication, repository relocation, baseline documentation, or tiny source-control setup commits that establish a clean shared starting point.
- Once `origin/main` is stable, substantial implementation should normally move to worker branches/worktrees. If the orchestrator keeps implementing on `main`, it must record why branch-separated work is currently unsafe or unnecessary.

## PR and Integration Policy

When GitHub is available, use pull requests as durable review and integration objects, even if all authors are agents.

Each PR should include:

- Goal and scope.
- Branch it started from.
- Files/modules touched.
- Tests and demos run.
- Docs updated.
- Risks and rollback plan.
- Subagents involved, if any.

Prefer squash merge for small feature branches and merge commits for integration branches where preserving subagent history helps future archaeology. Avoid repeated squash merges from long-running branches because they can make recurring conflicts more likely.

Use an integration branch when multiple subagents produce changes. The main orchestrator owns conflict resolution and final validation.

## Finish Protocol

Before ending a broad autonomous session:

1. Run the narrow validations for changed tracks and the broad validation that best proves the repo still works.
2. Inspect `git status --short --branch`, active worktrees, and untracked/generated artifacts.
3. Update `docs/ai/state.md`, roadmap, test matrix, demo index, and `docs/ai/agent-ledger.md`.
4. Classify each active branch/worktree as `ready to integrate`, `continued`, `parked`, `discard candidate`, or `blocked`.
5. If GitHub is available, create or update PRs for integration-ready work when useful.
6. Leave the repo on a named branch or explicit clean baseline and report next recommended batch.

## Conflict Prevention

Prevent conflicts before they happen:

1. Partition write ownership by files, modules, generated artifacts, migrations, schemas, docs pages, or test fixtures.
2. Mark shared files as orchestrator-owned unless one worker has explicit ownership. Common shared files include dependency manifests, lockfiles, schema definitions, generated indexes, central exports, config files, and global docs.
3. For unavoidable shared files, assign a merge order and one semantic owner before workers start.
4. Give every worker an avoid scope and instruct it to stop if the scope becomes inaccurate.
5. Prefer additive extension points over competing edits to the same central module when several tracks are active.
6. Keep formatting-only changes, dependency updates, and broad mechanical rewrites in their own branches so they do not collide with feature work.
7. Update `docs/ai/agent-ledger.md` when a worker claims a file or discovers overlap.

## Pre-Merge Conflict Check

Before merging a worker branch into `integrate/<milestone>`:

1. Inspect the worker summary, changed files, and validation evidence.
2. Compare changed files against active branches and the integration branch.
3. If the branch is stale, update or rebase only when the repo's policy allows it and the worker branch has no unknown user work.
4. Run a dry merge or local merge attempt in the integration branch before touching `main`.
5. If conflicts appear, stop merging other branches that touch the same area until the conflict is resolved.

## Conflict Resolution

Use this protocol when a merge conflict or semantic conflict appears:

1. Stop new overlapping writes in the conflicted area and record the freeze in the agent ledger.
2. Identify the semantic owner for each conflicting file/module and the reason each branch changed it.
3. Read both sides and the merge base. Do not resolve by blindly choosing `ours` or `theirs`.
4. Preserve behavior from both branches when both are still valid. If behavior conflicts, make the architecture or product decision explicit before editing.
5. Resolve locally for complex conflicts; use GitHub conflict editor only for simple line conflicts.
6. Run the narrowest relevant tests first, then broader validation for the affected subsystem.
7. Update docs, tests, or decision logs if the conflict exposed a new invariant, ownership rule, or integration order.
8. Document the final resolution in the PR, state doc, or agent ledger, including any branch whose work was superseded.

If the conflict is large or unclear:

- Spawn a read-only review worker to compare both branches and recommend a semantic merge plan.
- Split the integration into smaller commits if several unrelated conflicts are tangled.
- Park the lower-value branch if resolving it would delay higher-value validated work.
- Escalate the orchestrator model only if the conflict requires project-level architectural judgment.

After resolving:

- Resume or re-scope affected workers with updated avoid scopes.
- Re-run the portfolio batch selection if the conflict changes track independence.
- Avoid repeated conflict churn by merging foundational/shared-file branches before dependent feature branches in the next batch.

## Experimental Replacement

Agents may discard or replace existing infrastructure when:

- The work is on a recoverable branch or worktree.
- The current implementation is documented or preserved in history.
- The replacement has explicit acceptance criteria.
- Migration and rollback paths are written down.
- Tests or demos compare old and new behavior where relevant.

Do not destroy the only working path before the replacement has passed foundation review.

## Official References

- Git worktree manual: https://git-scm.com/docs/git-worktree
- Git branch manual: https://git-scm.com/docs/git-branch
- GitHub protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub PR merges: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
- GitHub merge conflicts: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts
