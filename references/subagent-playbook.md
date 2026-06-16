# Subagent Playbook

Use this reference when coordinating multiple Codex agents, choosing models, or controlling cost. For broad repository work, this playbook is mandatory.

## Non-Negotiable Rules

- Spawn subagents only when the user prompt or skill invocation explicitly authorizes subagents or parallel agent work.
- When authorization is present, treat subagents as the default for broad repo work. Do not fall back to single-agent sequential work without a written reason.
- Never assign a task to a subagent and then do the same task locally. This is duplicate spend and usually produces stale or conflicting reasoning.
- The main orchestrator owns project-level planning, sequencing across independent tracks, integration, conflict resolution, final validation, and handoff. Direct branch/worktree workers are the default for active implementation tracks.
- Use project-local autonomous-repo presets when available. If `.codex/agents/` is absent or missing equivalent presets, install the bundled presets from `assets/agents/` using `scripts/install_agent_presets.py`; see `agent-presets.md`. The live `spawn_agent` tool surface is authoritative: use `mar_*` custom agent types only when listed, otherwise use the mapped built-in role with explicit model/reasoning overrides and preset-equivalent instructions.
- For broad autonomous goals, identify independent tracks before choosing the next task. Batch size is determined by safe independent work and integration capacity, not by a fixed minimum.
- Treat long-running proof work as possible subagent work. Captures, imports, browser runs, benchmarks, profiling, report generation, artifact QC, and log collection should be assigned as execution lanes when targets or resources can be separated.
- Prefer read-heavy parallelism first, then promote clear work into branch-separated implementation lanes. Use write-heavy parallelism only with disjoint file/module ownership and separate branches or worktrees.
- Close subagents after their outputs are integrated or explicitly rejected.

## Model Palette

Use only these five configurations unless the user or environment explicitly expands the palette:

| Model and effort | Use for | Avoid for |
| --- | --- | --- |
| `gpt-5.4-mini high` | Cheapest default for bounded support work: repo maps, read-heavy exploration, docs audits, test discovery, log digestion, dependency research, visual-QA setup notes, and summarizing large artifacts. High reasoning compensates for the smaller model while preserving cost efficiency. | Final architecture calls, broad refactors, security-sensitive changes, ambiguous product decisions, or writes spanning many modules. |
| `gpt-5.4 medium` | Balanced coding worker for well-scoped implementation in known files, mechanical refactors, small bug fixes, test additions, fixture updates, and codebase-local changes with clear acceptance criteria. | Ambiguous requirements, cross-cutting migrations, conflicts between architecture options, or fragile production behavior. |
| `gpt-5.4 high` | Deeper coding work: complex debugging, cross-module tracing, risky refactors, integration repair, performance investigation, and code review where subtle interactions matter. | Cheap bulk exploration or routine edits where `medium` is enough. |
| `gpt-5.5 medium` | Main orchestrator default and senior generalist subagent: planning, architecture, roadmap decisions, conflict mediation, synthesis of subagent reports, GitHub integration strategy, and ambiguous multi-step tasks. | Bulk scans that can be handled by cheaper agents. |
| `gpt-5.5 high` | Rare escalation: project-defining architecture, failed integrations after cheaper attempts, high-risk migrations, security/privacy decisions, irreversible data changes, or reconciling conflicting expert reports. | Routine orchestration. Do not leave the main agent here by default. |

Recommended skill runner: `gpt-5.5 medium`. The orchestrator needs strong judgment, but `high` is too expensive for a long-running management thread unless the current decision truly warrants it.

## Preset Agents

Prefer these project-local preset templates after installing `assets/agents/*.toml` into `.codex/agents/`. They define the desired role, model, reasoning, sandbox, and output contract; the actual `agent_type` must match the live `spawn_agent` tool surface.

- `mar_explorer`: default read-only audit/research agent; use for repo maps, docs drift, test inventory, log digestion, dependency research, and task-card preparation.
- `mar_code_worker`: default write-capable branch/worktree worker for clear implementation tasks.
- `mar_deep_code_worker`: higher-reasoning code/debug worker for subtle cross-module work.
- `mar_execution_runner`: artifact-producing execution/proof worker for long commands, benchmarks, imports, captures, demos, reports, CI/log collection, and QC.
- `mar_reviewer`: read-only review gate for correctness, test gaps, maintainability, security/privacy, performance, and integration risk.
- `mar_program_auditor`: read-only product-program audit for milestone gates, portfolio balance, completion status, token/cost drift, and under-parallelization.
- `mar_senior_synthesizer`: rare senior synthesis worker for conflicting evidence, architecture decisions, roadmap prioritization, or high-value ambiguity.

The installer registers these presets in project `.codex/config.toml` as `[agents.mar_*]` entries. In a fresh session from that project root, spawn by preset name:

```text
agent_type = "mar_explorer"
agent_type = "mar_code_worker"
agent_type = "mar_deep_code_worker"
agent_type = "mar_execution_runner"
agent_type = "mar_reviewer"
agent_type = "mar_program_auditor"
agent_type = "mar_senior_synthesizer"
```

If `spawn_agent` returns `unknown agent_type` for a `mar_*` name, the current session did not load the project registrations. Run the installer with `--write-config`, confirm `.codex/config.toml` contains `[agents.mar_explorer]` through `[agents.mar_senior_synthesizer]`, and start a fresh Codex session from the project root. If progress must continue in the current stale session, use this temporary fallback and record it:

| Desired preset | Built-in `agent_type` fallback | Explicit overrides |
| --- | --- | --- |
| `mar_explorer` | `explorer` | `model = "gpt-5.4-mini"`, `reasoning_effort = "high"` |
| `mar_code_worker` | `worker` | `model = "gpt-5.4"`, `reasoning_effort = "medium"` |
| `mar_deep_code_worker` | `worker` | `model = "gpt-5.4"`, `reasoning_effort = "high"` |
| `mar_execution_runner` | `worker` | `model = "gpt-5.4-mini"`, `reasoning_effort = "high"` |
| `mar_reviewer` | `explorer` | `model = "gpt-5.4"`, `reasoning_effort = "high"` |
| `mar_program_auditor` | `explorer` | `model = "gpt-5.4"`, `reasoning_effort = "high"` |
| `mar_senior_synthesizer` | `default` | `model = "gpt-5.5"`, `reasoning_effort = "medium"` |

## Parallelization Checkpoint

Run this checkpoint before substantial implementation, debugging, refactoring, or repo exploration:

1. State the current objective and immediate blocker.
2. Identify the independent track portfolio for the project. Do not assume the active blocker is the only useful track. A track is any separable effort that can be advanced, tested, researched, or integrated without duplicating another active agent's scope.
3. Use role labels such as capability, quality, performance, reliability, experience, operations, research, documentation, or repo hygiene only as descriptors. Do not create category layers; two tracks with the same descriptor can run independently when their scopes are separable.
4. Split broad goals into additional independent tracks when several inputs, approaches, modules, user journeys, platforms, experiments, or risk areas can be advanced separately.
5. Mark each track as `active`, `candidate`, `blocked`, or `parked`, with a one-line reason.
6. Score candidate tracks by independence, user value, unblock value, risk, proof artifact clarity, write-scope safety, and expected integration cost.
7. Select the batch by capacity:
   - Include every high-value independent track that has a safe scope until limited by `agents.max_threads`, cost, integration bandwidth, shared-state risk, or unclear acceptance criteria.
   - Prefer 3-6 active agents for broad projects when enough safe tracks exist.
   - Do not stop at two tracks merely because the rule says parallelism exists.
   - If fewer than three agents are spawned for a broad project, record the limiting factor.
8. For each selected track, create a task card:
   - `track`: repo-specific name.
   - `descriptor`: capability expansion, quality improvement, performance/scalability, reliability/testing, user experience, operations/tooling, research/prototyping, documentation, repo hygiene, or repo-specific concern.
   - `mode`: research, implementation, debugging, testing, documentation, demo, review, or integration support.
   - `agent preset`: `mar_explorer`, `mar_code_worker`, `mar_deep_code_worker`, `mar_execution_runner`, `mar_reviewer`, `mar_senior_synthesizer`, or documented fallback.
   - `branch/worktree`: exact branch and checkout path for writes, or read-only.
   - `owned scope`: files/modules/questions/artifacts.
   - `resource locks`: browser, GPU, server port, device, dataset, credentials, external service, or none.
   - `avoid scope`: what the worker must not touch or decide.
   - `conflict risk`: low, medium, or high; name likely overlap points.
   - `proof`: tests, demo, report, manifest, benchmark, screenshot, PR, or other concrete artifact.
   - `done condition`: what makes the track ready to integrate, park, or split.
9. Split selected work into lanes:
   - `orchestrator`: decisions, sequencing, integration, final validation, user handoff.
   - `explore`: repo maps, API surfaces, prior docs, dependencies, external research.
   - `debug`: reproduction, logs, failing tests, environment comparison.
   - `test`: test inventory, missing coverage, focused test design.
   - `review`: risk scan, security/privacy, maintainability, performance.
   - `demo`: browser/chrome/computer-use validation path, screenshots, artifacts.
   - `docs`: stale docs, roadmap update, state/handoff consistency.
   - `program audit`: milestone gate fit, exit status, portfolio balance, token/cost drift, and parallelization health.
   - `implementation`: disjoint code slices with explicit branch/worktree and write ownership.
10. For implementation lanes, assign each worker a branch or worktree before it writes code.
11. Record track, lane ownership, branch/worktree ownership, and any depth-2 helper relationships in the plan or `docs/ai/agent-ledger.md`.
12. Spawn the batch.
13. Immediately switch the orchestrator to a non-overlapping lane, integration prep, or wait if all useful lanes are delegated.

Valid reasons not to spawn:

- The task is small enough that delegation overhead exceeds expected savings.
- The next step is a true serial blocker and no independent sidecar lane exists yet.
- Available tools do not permit spawning in this session.
- The only possible parallel tasks would write the same files or make the same decision.
- The work is high-risk and requires a single controlled path until the first baseline is safe.
- The repo state is not yet understood enough to assign implementation branches; in that case, spawn parallel track-discovery lanes, not only audits of the same task.

When skipping subagents for a substantial task, write the reason explicitly. Do not use vague phrasing such as "not needed" without explaining why.

## Orchestrator Discipline

After spawning subagents, the orchestrator must not inspect, patch, test, or research the delegated lane except to:

- Clarify subagent scope.
- Prepare integration infrastructure that does not decide or solve the delegated task.
- Review returned output.
- Resolve conflicts after the subagent is done.
- Run final validation after integration.

Examples:

- If a subagent is auditing a visual-QA failure, the orchestrator must not also diagnose that same failure. It can instead prepare test commands, inspect unrelated roadmap state, or wait.
- If a subagent is mapping auth entry points, the orchestrator must not perform an auth map locally. It can define acceptance criteria or work on a separate UI slice.
- If a worker owns `src/parser/*`, the orchestrator and other workers must not edit that path until integration.

## Track Task Cards

Create task cards before spawning a broad-session batch. Keep them short enough to fit in the plan or `docs/ai/agent-ledger.md`, but specific enough that a worker does not need hidden chat context.

```markdown
### Track: <repo-specific name>
Status: active | candidate | blocked | parked
Descriptor: <capability expansion | quality improvement | performance/scalability | reliability/testing | user experience | operations/tooling | research/prototyping | documentation | repo hygiene | repo-specific>
Mode: research | implementation | execution | debugging | testing | documentation | demo | review
Objective: <one concrete outcome>
Worker: <model/effort and why it is sufficient>
Agent preset: <mar_explorer | mar_code_worker | mar_deep_code_worker | mar_execution_runner | mar_reviewer | mar_senior_synthesizer | fallback with reason>
Branch/worktree: <branch and path, or read-only>
Owned scope: <files/modules/questions/artifacts>
Resource locks: <browser | GPU | port | dataset | credentials | external service | none>
Avoid scope: <files/modules/questions/decisions reserved for others>
Conflict risk: <low | medium | high, with likely overlap points>
Inputs: <docs, commands, artifacts, prior facts>
Proof artifact: <test, demo, report, manifest, benchmark, PR, screenshot>
Validation: <exact command/check or evidence standard>
Done condition: integrate | continue | split | park | blocked
Integration order: <before/after dependencies>
```

Definition of ready for a worker:

- Objective is specific enough to finish without interpreting the whole roadmap.
- Owned and avoid scopes are explicit.
- Write tasks have a branch/worktree decision following `references/source-control-and-github.md#branch-placement-decision`.
- Execution tasks name their resource locks, artifact paths, time budget, and whether outputs are source-controlled or ignored.
- Conflict risk and likely shared files are named.
- The expected proof artifact and validation are named.
- The model choice is cost-aware and justified.

If a track is not ready, assign a read-only worker to make it ready instead of letting the orchestrator absorb it silently.

## Lane Selection Patterns

Use these patterns to avoid duplicate work. The pattern headings describe modes of work, not the full portfolio of possible track descriptors. Always scan the broader portfolio descriptors before selecting a batch.

### Broad New Goal

- Agent A, `gpt-5.4-mini high`: map repo structure, existing docs, commands, and likely entry points.
- Agent B, `gpt-5.4-mini high`: identify tests/demos/CI gaps for the stated goal.
- Agent C, `gpt-5.4-mini high`: research current libraries/tools or platform constraints.
- Orchestrator: create roadmap, source-control plan, and integration criteria from current facts. Do not redo A/B/C.

### Debugging

- Agent A: reproduce and minimize the failure.
- Agent B: inspect recent changes and suspicious code paths.
- Agent C: review logs/environment/dependency versions.
- Orchestrator: define hypotheses and wait for evidence, or work on unrelated cleanup. Do not patch until evidence returns unless a production blocker requires immediate action.

### Feature Implementation

- Agent A, `test/<topic>`: test plan and missing coverage.
- Agent B, `feat/<topic-a>` worktree: implementation slice 1 with owned files.
- Agent C, `feat/<topic-b>` worktree: implementation slice 2 with disjoint owned files.
- Agent D, `demo/<topic>`: demo/browser validation lane when user-visible behavior is involved.
- Orchestrator, `integrate/<milestone>`: API contract decisions, merge order, conflict resolution, final tests. Do not edit worker-owned files until results return.

### Refactor

- Agent A: inventory public APIs and behavior constraints.
- Agent B: identify test coverage and missing regression tests.
- Agent C, `refactor/<route-a>` worktree: prototype one route.
- Agent D, `refactor/<route-b>` worktree: prototype a competing route when the decision is consequential.
- Orchestrator: choose route, integrate in batches, update docs.

### Broad Autonomous Project

Assign workers by independent track. Role labels are descriptors, not hierarchy or limits. A single role can have multiple concurrent tracks when scopes are separable.

- Capability workers: advance separate user-visible or operator-visible capability tracks.
- Quality workers: improve correctness, fidelity, usability, or output quality in tracks that do not duplicate capability workers.
- Reliability workers: strengthen tests, gates, fixtures, failure reporting, CI, or validation in separable areas.
- Experience workers: maintain demos, UI/API ergonomics, screenshots, Browser/Chrome validation, or user-facing state for separate surfaces.
- Research workers: evaluate independent external approaches, dependencies, standards, or competing designs.
- Foundation workers: refactor isolated foundations, remove obsolete infrastructure, or improve developer tooling in disjoint modules.
- Documentation and repo-hygiene workers: improve durable memory, roadmap clarity, dependency health, cleanup, packaging, or repository organization when those tracks materially improve autonomous continuation.
- Orchestrator: keep `main` stable, merge worker branches in evidence order through `integrate/<milestone>`, and maintain roadmap/state docs.

Do not use these as fixed branch names, exhaustive categories, or one-worker-per-role limits. Infer actual tracks, branch names, and concurrency from the repository, roadmap, risks, and current evidence.

Portfolio batch protocol for a broad autonomous project:

- Enumerate candidate tracks before picking the local task.
- Select all safe, high-value independent tracks that fit the current thread and integration budget.
- Assign direct track workers to implementation, prototype, execution, or concrete preparation branches when safe write scopes exist.
- Split execution by independent targets when possible: separate inputs, platforms, fixtures, benchmark scenarios, browser flows, import/export jobs, reports, or demo surfaces can each be a track if they do not contend for the same exclusive resource.
- Assign read-only workers to convert vague or risky candidates into task cards for the next batch.
- Use audit/test/docs/demo lanes as proof mechanisms attached to selected tracks, not as the whole batch by default.
- Decide what remains local only after the portfolio batch is selected.
- End the batch by classifying each track as `integrate`, `continue`, `split`, `park`, or `blocked`.

### Execution or Proof Work

Execution lanes run commands or tools that produce evidence or artifacts: long test suites, imports, captures, headful/browser flows, screenshots, benchmarks, profiling, report generation, demo exports, artifact manifests, release packaging, CI/log collection, and quality-control passes.

Use an execution worker when all are true:

- The command sequence is expected to take long enough that the orchestrator would spend material time or attention supervising it.
- The worker can access or create the required checkout, environment, input, and output paths.
- The task has a concrete proof artifact and pass/fail condition.
- Any exclusive resource is named and can be reserved for that worker.

Prefer target-level execution tracks over one serial execution lane. If several inputs, environments, browser flows, benchmarks, fixtures, or report sections can run independently, assign them separately until limited by hardware, ports, disk, credentials, model cost, or integration bandwidth.

Execution workers may use the same source branch as the orchestrator only when they are not editing source-controlled files and are writing artifacts to ignored or assigned output paths. If execution requires source edits, generated source-controlled files, or fixture updates, use a branch/worktree decision from `source-control-and-github.md`.

Keep execution local only when one of these is true:

- A resource is inherently single-owner for the session, such as the only interactive desktop focus, only available GPU slot, or only credentialed browser session.
- Artifact locality makes delegation slower or riskier than the run itself.
- The command is short and blocks an immediate integration decision.
- The task requires orchestrator-only judgment during each step, and the judgment cannot be converted into criteria, checkpoints, or a bounded worker prompt.

When execution stays local, record the reason in the utilization review and run another independent track in parallel if any safe track exists. Treat "orchestrator judgment" as a last resort after attempting to express the task as objective commands, artifact checks, or escalation checkpoints.

### UI or Demo Validation

- Agent A: Browser/Chrome visual QA plan and selectors.
- Agent B: test/demo command inventory.
- Agent C: docs/demo index update proposal.
- Orchestrator: implement or integrate the UI change, then use the plugin evidence from A/B.

## Prompt Template

Use this shape for subagents:

```text
You are working inside a Codex-managed repository. Other agents may be editing other branches or files; do not revert unknown work.

Task: <specific objective>
Track: <repo-specific track name>
Mode: <research | implementation | execution | debugging | testing | documentation | review | demo>
Model intent: <why this model/effort is sufficient>
Owned lane: <exact question/files/modules/branch>
Branch/worktree: <branch name and path, or read-only/no-branch>
Resource locks: <browser | GPU | port | dataset | credentials | external service | none>
Artifacts: <expected source-controlled and/or ignored paths>
Orchestrator will not duplicate this lane locally.
Scope to avoid: <files/modules/branches/questions>
Context: <minimal stable facts, links to docs, commands already run>
Expected output:
- Delta
- Evidence paths or exact file references
- Files changed, if any
- Commands run and results
- Risks or follow-up tasks
- Recommendation for integration, rejection, split, or park
- Status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED
```

For write tasks, add:

```text
Edit files directly in your workspace. Keep changes inside your assigned scope. Commit only if explicitly asked. Do not reformat unrelated files. If you discover that your assigned scope overlaps another active lane, stop and report the conflict.
```

Add this for branch-separated implementation workers:

```text
Work only on your assigned branch/worktree. Keep commits logically small if committing is requested. Do not merge to main or the integration branch. In your final answer, report branch name, changed files, commands run, tests passed/failed, and whether the branch is ready to integrate.
```

For read-only tasks, add:

```text
Do not edit files. Return concise findings with file paths, commands, and confidence levels. Do not include raw logs unless a specific log line is necessary evidence.
```

## Worker Status Handling

Require each worker to end with one status:

- `DONE`: output is ready for orchestrator review and possible integration.
- `DONE_WITH_CONCERNS`: output is complete, but the worker found risks, weak evidence, or follow-up work.
- `NEEDS_CONTEXT`: the task is still viable, but the worker needs a specific missing fact, artifact, command result, credential, or decision.
- `BLOCKED`: the worker cannot progress without changing scope, model, environment, dependency, or plan.

Orchestrator response:

- For `DONE`, verify the stated proof artifact and integrate or park.
- For `DONE_WITH_CONCERNS`, address concerns before merging; classify each as accept, fix, split, or park.
- For `NEEDS_CONTEXT`, provide only the missing context or split the track if the prompt was too broad.
- For `BLOCKED`, decide whether to escalate model, narrow scope, create a prerequisite track, change environment, or ask the user if the blocker is external.

Do not retry the same failed worker prompt unchanged. If a worker gets blocked, change the task card, model, scope, or environment before continuing.

## Wait and Integration Policy

- Do not call wait reflexively if there is useful non-overlapping orchestrator work.
- Do wait when the next safe step depends on a delegated result.
- When a subagent returns, classify its output as `integrate`, `continue`, `split`, `needs follow-up`, `reject`, `park`, or `blocked`.
- Verify important claims with targeted reads/tests before merging, but do not redo the full investigation.
- Merge implementation branches into `integrate/<milestone>` one at a time. Run narrow validation after each merge and broader validation after the full batch.
- Update `docs/ai/agent-ledger.md` with agent role, model/effort, lane, output status, files changed, and integration result.
- Close the subagent after integration or rejection.

## Batch Utilization Review

At the end of each broad batch, record a concise utilization note in `docs/ai/agent-ledger.md` or `docs/ai/state.md`:

```text
Batch:
Objective:
Candidate tracks found:
Selected tracks:
Agents spawned:
Workers by mode: implementation / execution / research / docs / test / review
Orchestrator-local heavy work:
Reasons local work was not delegated:
Resource locks or bottlenecks:
Model and reasoning choices:
Token/usage budget status:
Outputs integrated:
Tracks parked or split:
Next batch split points:
```

The note is not bureaucracy; it is the feedback loop that prevents the next agent from repeating a low-parallelism pattern. If the batch used only audit/review workers while the orchestrator performed implementation or execution, explain why that was optimal or split the next batch differently.

## Cost Rules

- Start with the cheapest configuration likely to succeed; escalate after evidence, not anxiety.
- Parallel subagents are useful but more expensive than single-threaded work. Spend them on independent lanes with clear proof artifacts, and record the expected value of the parallelism in the utilization review.
- Keep the orchestrator quiet while subagents work. Waiting is cheaper than filling the main context with speculative reasoning.
- Ask subagents for distilled deltas, not transcripts.
- Put stable instructions before variable repo/task details in subagent prompts to improve prompt-cache friendliness where applicable.
- Reuse existing subagents for related follow-ups when their lane context matters.
- Avoid one-agent-at-a-time delegation for broad work. If three independent lanes exist, spawn the batch together.
- For broad autonomous repos, target 3-6 active subagents when there are enough independent lanes: 1-2 read-only/research lanes, 1-4 implementation branches across independent tracks, and 1 validation/docs/demo lane.
- Do not spend the main orchestrator context on supervising long-running commands that can be delegated as execution lanes with artifact summaries.

## Depth Workflow

Use a strict three-layer shape:

- Depth 0: main orchestrator.
- Depth 1: direct track owners for independent implementation, execution/proof, research, documentation, review, or integration-support tracks.
- Depth 2: helper agents spawned by one depth-1 parent for worker-local subtasks only.

Depth 1 owns tracks. A depth-1 worker should have a task card, owned scope, avoid scope, proof artifact, model choice, branch/worktree decision, and integration recommendation. If the worker writes source-controlled files, it should normally own a separate branch/worktree. If it runs commands, it should own resource locks and artifact paths.

Depth 2 helps one depth-1 worker. Use it only when the parent worker can split its assigned track into at least two disjoint helper lanes and synthesize the result without making the main orchestrator manage those helpers. Good depth-2 helpers include:

- read-only audit of the parent worker's planned change,
- targeted test discovery or fixture inspection,
- log/profiling digestion for a command the parent owns,
- demo/visual-QA capture for a parent-owned UI or artifact task,
- dependency/API lookup needed by the parent worker,
- small execution proof that writes only assigned artifacts.

Do not use depth 2 for:

- independent project tracks that should be depth 1,
- broad repo exploration,
- another management or track-orchestration layer,
- hiding architecture decisions from the main orchestrator,
- adding reviewers around a task that lacks a concrete implementation/execution owner.

Never exceed depth 2 unless the user explicitly changes the project policy and config. Do not set `max_depth = 3` by default; it increases coordination cost, weakens accountability, and can hide important implementation decisions from the main orchestrator. Consider depth 3 only for an exceptional, explicitly approved program where the project is too large for flat-first orchestration and the repo already has strong docs, branch discipline, and integration gates.

A depth-1 subagent may spawn depth-2 subagents only when all are true:

- The parent subtask contains at least two independent subtasks.
- Each child has a disjoint read/write scope or a read-only question.
- The parent can synthesize the child results without asking the main orchestrator to manage them.
- The parent has enough context and authority to accept, reject, or retry child outputs inside its own lane.
- The parent records the child tasks, models, and outputs in its final summary.

Depth-2 agents must not spawn further agents. They report to their depth-1 parent, not directly to the main orchestrator, unless the parent is blocked or unavailable.

The main orchestrator should see depth-2 activity only as summarized evidence in the parent worker's final output and in `docs/ai/agent-ledger.md`. If the main orchestrator needs to steer several child agents directly, the work was split incorrectly; promote those lanes to independent depth-1 tracks.

Do not increase depth merely to create extra coordination layers. Prefer splitting work into independent depth-1 tracks, each with optional depth-2 helpers.

## Anti-Patterns

- Spawning one subagent, then doing the same investigation locally.
- Spawning a read-only explorer and immediately patching the suspected fix before the explorer returns, unless a separate blocker requires it.
- Keeping all implementation in the orchestrator while subagents only audit. For broad projects, subagents should also own branch-separated implementation when scopes are separable.
- Keeping all execution/proof work in the orchestrator while subagents only review. Long captures, benchmarks, imports, browser runs, and report generation are tracks when they can be split safely.
- Using depth 2 for independent tracks that should be visible to the main orchestrator as depth-1 owners.
- Letting a depth-1 worker spawn helpers and then return unsynthesized child transcripts.
- Using subagents as a review panel around one local task while ignoring other independent tracks in the roadmap.
- Treating the current blocker as the whole project when independent roadmap tracks can progress in parallel.
- Treating role labels as hierarchy, exclusive buckets, or one-worker limits.
- Assigning multiple workers to the same files without an integration owner.
- Asking a subagent to "understand the whole repo."
- Waiting with no timeout or no plan.
- Treating subagent agreement as validation without tests or source evidence.
- Letting subagent output remain only in chat instead of updating repo memory.

## Official References

- OpenAI Codex subagents: https://developers.openai.com/codex/concepts/subagents
- OpenAI reasoning effort: https://developers.openai.com/api/docs/guides/reasoning
- OpenAI prompt caching: https://developers.openai.com/api/docs/guides/prompt-caching
- OpenAI Agents SDK orchestration: https://developers.openai.com/api/docs/guides/agents
