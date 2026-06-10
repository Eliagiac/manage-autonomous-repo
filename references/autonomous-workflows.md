# Autonomous Workflows

Use this reference for planning, execution, review, testing, debugging, and large refactors.

## Phase Separation

Keep these modes distinct in docs, branches, commits, and subagent prompts:

- Research: gather facts, compare options, inspect dependencies, read docs, test feasibility.
- Planning: define roadmap, acceptance criteria, sequencing, ownership, rollback, validation.
- Implementation: change source files inside a scoped branch.
- Execution: run command sequences that produce evidence or artifacts, such as imports, captures, benchmarks, reports, packages, profiling, browser flows, or quality-control manifests.
- Debugging: reproduce, isolate, hypothesize, test one variable at a time, record root cause.
- Testing: add or run automated and manual checks; update the test matrix.
- Documentation: update durable repo memory and user-facing docs.
- Demo: prove behavior in a way a user or future agent can inspect.
- Review: inspect correctness, maintainability, security, performance, and docs/test gaps.
- Integration: merge branches, resolve conflicts, rerun validation, update state.

## Planning Template

For any nontrivial milestone, write:

- Objective.
- Current facts.
- Assumptions to validate.
- Portfolio descriptors scanned: capability expansion, quality improvement, performance/scalability, reliability/testing, user experience, operations/tooling, research/prototyping, documentation, repo hygiene, and repo-specific concern areas.
- Work breakdown by phase.
- Subagent delegation map: owned lanes, model choices, resource locks, scope to avoid, orchestrator lane, wait points, and integration order.
- Source-control plan: branches, worktrees, PRs, integration owner.
- Acceptance criteria.
- Foundation gates.
- Test and demo plan.
- Documentation updates required.
- Risks, rollback plan, and stop conditions.

## Foundation Gates

Before building dependent features, review foundations:

- Build and package system.
- Runtime configuration and environment loading.
- Data model, migrations, persistence, backup/restore expectations.
- API contracts and compatibility.
- Authentication, authorization, and secret handling.
- State management and concurrency assumptions.
- Error handling, logging, and observability.
- Test harness, fixtures, CI, and smoke tests.
- Deployment and rollback path.
- Demo path for the current product surface.

If a foundation is weak, either fix it first or explicitly mark the dependent work as experimental.

## Research Rules

- Use online sources when facts may have changed, when choosing libraries, when dealing with legal/security/deployment matters, or when docs are not present locally.
- Prefer primary sources: official docs, upstream repos, standards, release notes, and source code.
- Record sources and dates in `docs/ai/research.md` when they influence durable decisions.
- Convert research into a decision, experiment branch, or parked idea. Do not leave useful findings only in chat.

## Implementation Rules

- Make small vertical slices when possible: source, tests, docs, demo.
- For broad work, split implementation into branch/worktree-owned worker lanes whenever scopes are separable. The orchestrator should integrate worker branches rather than personally implementing every slice.
- Create or select an `integrate/<milestone>` branch before merging multiple worker branches.
- Preserve working behavior unless the branch is explicitly experimental.
- Install dependencies project-locally and update lockfiles intentionally.
- Use existing framework and style unless replacing them is the point of the branch.
- Remove dead code after replacement is validated.
- Keep migrations reversible when practical.

## Execution Rules

- Treat execution as separate from implementation. A command-heavy proof task can be delegated even when no source files need edits.
- Give each execution lane a target, resource lock, time budget, exact command or workflow, artifact paths, and pass/fail evidence standard.
- Split execution by independent targets when safe: inputs, environments, benchmark cases, browser flows, import/export jobs, reports, generated artifacts, platforms, or demos.
- Use ignored output paths for transient artifacts and source-controlled paths only when the artifact is intended to become durable repo evidence.
- If execution requires source edits, fixture changes, generated committed files, or config changes, assign a branch/worktree as for implementation.
- Keep execution local only for short blockers, inherently single-owner resources, credentialed interactive state that cannot be handed off, or tasks requiring orchestrator judgment that cannot be converted into criteria, checkpoints, or a bounded worker prompt. Record the reason in the batch utilization review.
- Summarize results into the test matrix, demo index, agent ledger, or state doc. Link artifact paths instead of carrying raw logs in chat.

## Debugging Rules

- Reproduce before fixing unless the failure is obvious and cheap to validate.
- For nontrivial failures, delegate at least one independent lane before patching: reproduction, log analysis, recent-change review, environment comparison, or test minimization.
- After delegating a debugging lane, do not diagnose the same lane locally. Work a separate hypothesis or wait.
- Isolate the failing layer.
- Write or update a regression test when the bug is meaningful.
- Record root cause, fix, and verification in the PR or state doc.
- Use subagents for parallel log review, environment comparison, and test minimization.

## Testing Rules

- Maintain a test matrix that lists unit, integration, end-to-end, smoke, lint, type, build, migration, and manual checks.
- Delegate test discovery, long test execution, benchmark runs, or visual/manual QA as separate lanes when implementation is nontrivial and resources allow it.
- Run narrow tests during development and broader tests before integration.
- For UI, inspect real rendered output with Browser/Chrome after significant changes.
- For generated artifacts, render or open them with the relevant plugin.
- If a test cannot be run, document why and what evidence substitutes for it.

## Review Rules

Use review as a gate before stacking more work on top of a foundation or merging broad changes. Check:

- Correctness and edge cases.
- Security and privacy.
- Data loss and migration risk.
- Performance and scalability.
- Maintainability and deletion opportunities.
- Documentation and demo accuracy.
- Test adequacy.
- Source-control cleanliness.

For high-risk reviews, use `gpt-5.4 high` for code-focused review or `gpt-5.5 high` for architecture/product-risk review.

For broad changes, run review lanes in parallel: one subagent for correctness/test gaps, one for maintainability/performance, and one for security/privacy when relevant. The orchestrator should synthesize findings, not perform each review locally.

## Plugin and Tool Rules

- Assume installed Codex plugins are available even when the user did not explicitly name them. Use available plugins proactively when they materially improve research, implementation, validation, demos, source control, or deliverables.
- Use GitHub tools for repo, issue, PR, CI, and review workflows.
- Use Browser or Chrome for web app demos, visual QA, authenticated browser flows, and UI debugging.
- Use Computer Use for desktop app validation when browser/shell is insufficient.
- Use Documents, Spreadsheets, or Presentations for those artifact types.
- Search for and suggest useful missing plugins only when directly relevant.
- Install project-local software/libraries independently when safe and reversible; avoid global installs or external paid services without explicit authorization.

## End-of-Run Handoff

Before stopping substantial work:

- Ensure `docs/ai/state.md` is current.
- Record branch, commit, PR, or worktree status.
- List tests and demos last run.
- Identify the next three actions.
- Close or record subagents.
- Leave the repo in a clean or clearly explained dirty state.
