---
name: manage-autonomous-repo
description: Design, build, refactor, document, test, demo, and maintain repositories intended to be managed primarily or entirely by Codex agents with minimal human supervision. Use when Codex is asked to run an autonomous software project, create or manage a Codex-only repository, coordinate subagents, create living technical documentation and roadmaps, maintain GitHub branches/PRs, explore multiple implementation directions, perform large refactors, or keep a project understandable for future agents.
---

# Manage Autonomous Repo

## Mission

Run the repository as an autonomous engineering program, not as a one-off patch. Optimize for future agent restartability: every major decision, current state, feature surface, test path, demo, and unresolved risk must be visible from the repo itself.

Prefer proactive progress over waiting for user input. Make reversible decisions, record assumptions, validate them, and escalate only when the next action would be destructive, paid, credential-dependent, legally sensitive, or impossible to reverse with source control.

## Product Program Mode

When the user asks for a product, research program, autonomous project, or broad objective rather than a patch, switch to Product Program Mode.

Product Program Mode means:

1. Define the product gate, milestone ladder, and active portfolio before implementation.
2. Treat ordinary sessions as progress cycles, not completion events.
3. Use explicit exit statuses: `RUN_CONTINUES`, `MILESTONE_ACCEPTED`, `BLOCKED_REQUIRES_HUMAN`, or `PRODUCT_READY`.
4. Never mark a broad goal complete because instructions were read, a plan was written, a first slice landed, or one branch was merged.
5. Keep the long-horizon operating model in repo docs so future agents can resume without chat memory.
6. Maintain an independent track portfolio and choose batches by safe parallelism, user value, unblock value, proof clarity, integration cost, and resource locks.
7. Record negative and parked evidence as first-class progress when it prevents repeated expensive routes.

For Product Program Mode, write or update a small set of management docs when absent:

- Product objective and non-goals.
- Milestone roadmap with gates.
- Track portfolio and parked/negative lanes.
- Agent operating model with roles, branch/worktree policy, resource locks, and exit statuses.
- Compact goal prompt plus bulk instruction file when platform prompt limits apply.

## Load References

Read only the references needed for the current phase:

- `references/subagent-playbook.md`: delegation, model selection, subagent depth, cost control, prompt templates.
- `references/agent-presets.md`: bundled custom-agent TOML presets, installation command, and project `.codex/agents/` plus `.codex/config.toml` registration policy.
- `references/documentation-system.md`: required living docs, roadmaps, demos, restart handoff structure.
- `references/context-and-memory.md`: context redundancy control, long-term memory, compaction, handoff briefs.
- `references/source-control-and-github.md`: repository setup, GitHub/PR/worktree policy, branch-separated subagent work, integration branches, conflict handling.
- `references/high-parallel-evidence-development.md`: evidence-status taxonomy, external workdir contracts, resource locks, branch-stack maps, and stop rules for planning-only chains.
- `references/goal-prompt-and-context-bundles.md`: context capsules, goal-prompt structure, branch-doc bundle ingestion, and token-budgeted handoffs.
- `references/autonomous-workflows.md`: planning, research, implementation, debugging, testing, foundation review, refactor strategy.
- `references/product-orchestration-lifecycle.md`: long-horizon product gates, milestone loops, completion statuses, and product-program docs.
- `references/agentic-orchestration-landscape.md`: external patterns from Codex, GitHub agents, Claude Code, LangGraph, AutoGen, CrewAI, OpenHands, and Git worktrees.
- `references/goal-prompt-and-handoff-contracts.md`: compact goals, bulk instruction files, session handoffs, and non-terminal exit statuses.

## Default Runner Model

Recommend `gpt-5.5` with `medium` reasoning for the main agent running this skill. The main agent is the orchestrator and integrator: it must make architecture, sequencing, merge, risk, and product-state decisions. `medium` avoids paying the continuous cost of `high` while still being strong enough to supervise cheaper subagents. Escalate the main agent to `gpt-5.5 high` only for rare project-defining decisions or failed integration attempts.

While subagents run, avoid burning orchestrator tokens on speculative narration or duplicating their work. Either do useful non-overlapping critical-path work, prepare integration/validation, or wait deliberately and summarize only when results arrive.

Subagent spawning still depends on active tool policy. The recommended invocation/default prompt includes explicit user authorization to use subagents as per this skill; when that authorization is present, follow the parallelization rules without asking again.

## Parallel-First Orchestration

For broad repo goals, treat parallelization as a required workflow stage, not an optional optimization.

1. Before choosing the next implementation task, create the independent track portfolio from the roadmap and current state. Do this even when one blocker looks obvious.
2. Select as many active tracks as can safely advance within thread, branch, and integration capacity. Do not treat two tracks as a target; it is only the smallest useful parallel batch.
3. For each selected track, write a task card before spawning:
   - Track name, objective, mode, branch/worktree, owned files/modules/questions, avoid scope, model, proof artifact, validation command, and integration order.
4. Before implementation, create a delegation map with owned lanes:
   - Orchestrator lane: sequencing, architecture decisions, integration, conflict resolution, final validation, user-facing handoff.
   - Subagent lanes: bounded exploration, test discovery, failure reproduction, log analysis, execution/proof runs, plugin/browser validation, documentation audit, program audit, dependency research, or disjoint code changes.
5. Before spawning, select the desired autonomous-repo preset for each lane. If `.codex/agents/` or `.codex/config.toml` lacks the registered `mar_*` presets, run `python <skill-dir>/scripts/install_agent_presets.py <project-root> --write-config`; see `references/agent-presets.md`.
6. Spawn subagents as an initial batch when tools and policy permit. In a fresh registered project session, use preset names directly, such as `agent_type = "mar_explorer"` or `agent_type = "mar_code_worker"`.
7. If a `mar_*` name is rejected with `unknown agent_type`, treat the current session as stale or unregistered: fix the project registration and start a fresh session. Only use built-in fallback roles with explicit model/reasoning overrides when work must continue in the stale session.
8. For broad implementation, create separate branches or worktrees for independent worker lanes before assigning writes. Prefer multiple concurrent implementation branches over forcing all code changes through the orchestrator.
9. Treat long-running proof work as delegable execution, not automatic orchestrator work. If captures, benchmarks, imports, browser runs, report generation, or artifact QC can be split by target or resource, assign execution lanes with explicit resource locks and artifact paths.
10. After spawning, do not work on the same task locally. The orchestrator must switch to a different lane, prepare integration, or wait.
11. Integrate subagent outputs explicitly: inspect summaries, verify evidence, merge one branch at a time into an integration branch, run tests, update docs, and close agents.
12. If no subagent is spawned for a substantial task, record the concrete reason before proceeding.

## Independent Track Portfolio

For broad autonomous projects, do not let the orchestrator collapse the whole roadmap into the single currently active blocker. Maintain a flat portfolio of independent tracks and keep multiple viable tracks active when the repo state allows it.

1. Identify separable tracks from the roadmap, docs, and evidence. A track is any independent effort that can be advanced, tested, or researched without duplicating another active agent's scope.
2. Scan for tracks across all relevant descriptors: capability expansion, quality improvement, performance/scalability, reliability/testing, user experience, operations/tooling, research/prototyping, documentation, repo hygiene, and repo-specific concern areas.
3. Treat descriptors as discovery prompts, not hierarchy or limits. A track's descriptor is different from its work mode; any descriptor may be advanced by implementation, execution, research, testing, documentation, demo, review, or integration work.
4. Split broad goals into more independent tracks whenever several inputs, approaches, modules, user journeys, platforms, experiments, or risk areas can advance separately.
5. Choose which tracks can advance concurrently without sharing risky write scopes.
6. Default implementation-ready tracks to direct depth-1 branch/worktree workers, so each worker can use depth-2 helper lanes for audits, tests, demos, research, or debugging when useful.
7. Build portfolio batches by capacity, not by a fixed count. Include every high-value independent track that has a safe scope until limited by `agents.max_threads`, model cost, integration bandwidth, shared-state risk, or unclear acceptance criteria.
8. Use audit/test/docs/demo lanes as proof mechanisms for tracks. They are not a substitute for selecting multiple tracks unless the repo is still in baseline discovery or every concrete track is blocked.
9. Assign read-only/research agents to tracks that still need scoping.
10. Keep `main` stable. After the GitHub baseline is established, substantial code changes should normally happen on worker branches and merge through `integrate/<milestone>`.
11. If only one track is active, document why: no clean baseline yet, every path depends on the same blocker, the repo is too dirty to split safely, or no path has a separable write scope.


## Evidence-Contract and Context-Capsule Addendum

For long-running repos that accumulate planning contracts, external evidence, run manifests, and PR-stack branches, treat evidence integrity as a first-class workflow concern.

1. Before dispatching workers, build a context capsule instead of rereading the full repository memory. Include current branch/worktree/PR stack, active objective, source-of-truth docs, known negative evidence, resource locks, selected tracks, and stop conditions. Link long docs and logs instead of pasting them.
2. Classify artifacts before using them: `plan`, `request`, `contract`, `readiness`, `smoke`, `diagnostic`, `execution`, `demo`, `visual_qc`, `acceptance`, `parked`, `rejected`, or `accepted`. Do not let workers promote an artifact beyond its status without a named promotion gate.
3. Distinguish source-controlled contracts from ignored external payloads. External workdir evidence needs identity, provenance, hashes when available, exact command/log paths, and repo-owned import/summary contracts before it can influence acceptance.
4. Name shared resource locks in task cards: GPU/training, browser/headful runtime, external workdir, dataset/source payload, large `runs/` root, PR-stack branch, and central config/schema files.
5. In active PR stacks, map branch ancestry and current merge target before assigning write lanes. Workers should not write on stale bases or ambiguous worktrees.
6. For planning-heavy projects, every planning chain must end as one of: implementation task card, execution task card, parked idea with blocker, or explicit rejection. Avoid producing more contracts when the next useful step is already clear.
7. When a repo has a non-hallucination, safety, legal, privacy, or source-fidelity covenant, put that covenant in each relevant task card and review gate. Treat violations as stop conditions, not review comments.

Use `references/high-parallel-evidence-development.md` and `references/goal-prompt-and-context-bundles.md` for detailed templates.

## Autonomous Program Protocol

Use this positive workflow for broad repo sessions:

1. **Baseline:** inspect repo state, current docs, branch status, tests, demos, and recent agent ledger entries.
2. **Portfolio:** enumerate candidate tracks, split broad goals into independent tracks, classify each as `active`, `candidate`, `blocked`, or `parked`, and choose a batch by safe concurrency capacity.
3. **Task cards:** write one task card per selected track with exact ownership, branch/worktree, resource locks, expected artifact, validation, and handoff format.
4. **Dispatch:** spawn direct workers for selected tracks. Prefer implementation/prototype/execution workers when safe scopes exist; use read-only workers to turn vague candidates into future task cards.
5. **Orchestrate:** keep the main agent on sequencing, integration prep, conflict prevention, state docs, and final proof. Do not convert the orchestrator into the only implementer while agents only audit.
6. **Depth discipline:** use depth 1 for direct track owners and depth 2 only for worker-local helpers that the depth-1 parent can synthesize. Never let depth 2 become another orchestration layer.
7. **Review gates:** require each worker to self-review, report evidence, and identify risks. For substantial code changes, run a spec/acceptance review before code-quality or cleanup review.
8. **Integrate:** merge or copy worker results one at a time through `integrate/<milestone>`, running narrow validation after each and broader validation after the batch.
9. **Utilization review:** record actual parallelism versus possible parallelism, workers by mode, orchestrator-local heavy work, reasons not delegated, cost/model choices, token/usage budget status, and next batch split points.
10. **Memory:** update state, roadmap, test matrix, demo index, and agent ledger with what changed, what was proven, what remains blocked, and which tracks should enter the next batch.

## Operating Loop

1. Establish the baseline.
   - Inspect the repo, `git status`, existing instructions, build/test scripts, docs, CI, and deployment surface.
   - If no Git repo exists, create one before meaningful edits. If no GitHub remote exists and GitHub tools or `gh` are available, create or propose one according to the current environment.
   - Preserve unknown existing work; do not erase or rewrite it without a recoverable branch or commit.
   - If `.codex/agents/` is absent or `.codex/config.toml` lacks equivalent `[agents.mar_*]` registrations, install the bundled presets into the project with `python <skill-dir>/scripts/install_agent_presets.py <project-root> --write-config`. Do not overwrite existing project agent files unless explicitly intended.
   - Before doing substantial sequential work, perform the parallelization checkpoint from `references/subagent-playbook.md`. Spawn subagents when tools and policy permit; if none are spawned, record the reason in the plan or state doc.

2. Create the project memory.
   - If absent, create the documentation system from `references/documentation-system.md`.
   - Maintain a current-state page, feature map, architecture map, roadmap, decision log, demo index, test matrix, and agent ledger.
   - Use `references/context-and-memory.md` to keep durable memory concise, deduplicated, searchable, and separate from raw conversation history.
   - Keep docs close to code changes. A future agent should be able to understand what exists, what is trusted, what is broken, and where to continue.

3. Separate work modes.
   - Label active tasks as research, planning, implementation, debugging, testing, documentation, demo, source-control integration, or review.
   - Do not blend speculative research with implementation commits unless the branch is explicitly experimental.
   - Convert research into decisions, discarded options, and next actions.

4. Plan before expanding.
   - Build a roadmap with high-level milestones and feature-specific plans.
   - Define acceptance criteria, risk areas, validation commands, demo expectations, and rollback points before broad implementation.
   - Review foundational features before stacking dependent work: build system, data model, persistence, authentication/authorization, API contracts, state management, test harness, deployment path, and observability.
   - Include an independent track portfolio and delegation map: active tracks, parked tracks, subagent lanes, orchestrator lane, write ownership, wait points, and integration order.

5. Delegate for speed and cost.
   - Make parallelization a first-class priority. For broad repo goals, default to using subagents for bounded work that can run independently, including exploration, test discovery, log analysis, execution/proof runs, documentation audits, and disjoint implementation slices.
   - Prefer the project-local preset agents from `references/agent-presets.md`: cheap read-only explorers for audits, branch/worktree code workers for owned writes, execution runners for long proof commands, reviewers for gates, and senior synthesis only for ambiguous high-value decisions.
   - For disjoint implementation slices, prefer separate branches or worktrees owned by worker subagents. Keep the orchestrator out of worker-owned files until integration.
   - For long-running command sequences, create execution lanes when targets, datasets, environments, reports, browser sessions, or validation artifacts can be separated. Keep them local only when a resource is single-owner or artifact locality makes delegation more expensive than the run itself; record that reason.
   - Do not duplicate delegated work locally. Once a task is assigned to a subagent, the orchestrator may only clarify scope, prepare integration, or work on a non-overlapping lane until the result returns.
   - Use the cheapest sufficient model from `references/subagent-playbook.md`; escalate only when validation fails or risk justifies it.
   - Assign explicit ownership of files, modules, branches, or questions. Avoid overlapping writes.
   - Allow subagents to create their own subagents only to depth 2 total, and only for independent subtasks with clear outputs.

6. Explore boldly, integrate carefully.
   - Use branches/worktrees for experiments and parallel implementation. It is acceptable to replace or discard existing infrastructure when the branch is recoverable and the reason is documented.
   - Maintain a single integration branch per milestone when multiple worker branches are active. Merge worker branches deliberately, one at a time.
   - Compare alternatives with evidence: complexity, testability, performance, maintainability, migration cost, and demo quality.
   - Merge only through a deliberate integration step with tests, docs, and state updates.

7. Prove the current state.
   - Run tests, linters, type checks, build commands, migrations, and smoke tests appropriate to the stack.
   - Maintain demos for all relevant user-facing or operator-facing features. Assume installed Codex plugins are available even when the user did not explicitly name them; proactively use the right plugin when it improves research, implementation, validation, demos, or source-control work. Prioritize GitHub for repo/PR/CI work, Browser or Chrome for web UI inspection, and Computer Use for desktop-app validation.
   - If useful software or libraries are missing, install project-local dependencies independently when safe and reversible. Avoid global/system installs, paid services, or credentialed external changes unless necessary and authorized by the environment or user.
   - For branch-visible cloud coding agents or external coding workers, require reviewable evidence in source control: commits, logs, branch summaries, PRs, check results, or equivalent artifacts. Chat-only claims are not sufficient proof.

8. Report and hand off.
   - Keep user-facing status concise: current capability, latest demo path, roadmap position, important risks, and next recommended work.
   - Record a batch utilization note in `docs/ai/agent-ledger.md` or `docs/ai/state.md`: selected tracks, agents spawned, local heavy work, reasons for skipped delegation, model/cost choices, token/usage budget status, and next split points.
   - For broad Product Program Mode goals, end with `RUN_CONTINUES`, `MILESTONE_ACCEPTED`, `BLOCKED_REQUIRES_HUMAN`, or `PRODUCT_READY`; reserve completion claims for a passed product gate or an explicit user closeout.
   - Before ending a major run, update the state docs and leave the repo on a named branch or clean merge state.

## Quality Bar

- Prefer structured docs and source-controlled artifacts over chat-only memory.
- Prefer reproducible commands and demos over assertions.
- Prefer parallel research and cheap subagents over one expensive agent reading everything.
- Prefer small integration batches over unreviewable giant merges.
- Prefer deleting obsolete code when tests, docs, and source control make the change recoverable.
- Prefer explicit uncertainty over hidden assumptions.

## Grounding

This skill is informed by OpenAI guidance on Codex subagents, reasoning effort, prompt caching, conversation state, compaction, context personalization, and agent orchestration; Git/GitHub guidance on branches, worktrees, PR merges, and protected branches; and reusable workflow concepts from agent skill projects such as Superpowers, including workflow ladders, task readiness, isolated worktrees, worker statuses, review gates, and verification-before-completion. When tool behavior or platform policy may have changed, verify current official docs before encoding a new permanent workflow.
