# Agent Presets

Use this reference when a managed repo lacks project-local autonomous-repo agent templates or when subagent model choices are drifting too expensive.

## Install Presets

At the start of a broad autonomous repo session, check for `.codex/agents/` in the target repo. If the repo does not already define equivalent agent templates, copy this skill's presets into the project:

```powershell
python <skill-dir>\scripts\install_agent_presets.py <project-root> --write-config
```

Rules:

- Do not overwrite existing project agent files unless the user explicitly asks or the project docs say these presets own the agent definitions.
- Use `--overwrite` only after reading the existing `.codex/agents/*.toml` files and confirming replacement is intended.
- Prefer project-local `.codex/agents/` over user-global `~/.codex/agents/` so the workflow is reproducible for future agents in the repo.
- Keep `.codex/config.toml` trusted and source-controlled when the repo is meant to be autonomous. The recommended baseline is `[agents] max_threads = 10` and `max_depth = 2`.
- If project config already defines `[agents]`, preserve its values unless they block the skill. If `max_depth` is below `2`, record that depth-2 helper lanes are unavailable.

## Preset Roles

The skill bundles these custom-agent template files under `assets/agents/`:

| File | Agent name | Default use |
| --- | --- | --- |
| `mar-explorer.toml` | `mar_explorer` | Cheap read-only discovery, docs drift checks, test inventory, log digestion, and task-card preparation. |
| `mar-code-worker.toml` | `mar_code_worker` | Cost-efficient depth-1 branch/worktree implementation for well-scoped code/test/docs changes. |
| `mar-deep-code-worker.toml` | `mar_deep_code_worker` | Higher-reasoning depth-1 implementation/debug work with cross-module tracing or subtle integration risk. |
| `mar-execution-runner.toml` | `mar_execution_runner` | Artifact-producing execution lanes: tests, benchmarks, imports, captures, demos, report generation, QC, CI/log collection. |
| `mar-reviewer.toml` | `mar_reviewer` | Read-only correctness, maintainability, security/privacy, performance, docs/test, and integration review. |
| `mar-senior-synthesizer.toml` | `mar_senior_synthesizer` | Rare senior synthesis for architecture, roadmap, conflict, or ambiguous product-state decisions. |

## Selection Rules

- The installer must write both `.codex/agents/*.toml` files and `.codex/config.toml` `[agents.mar_*]` registrations. The config registrations are what make `mar_*` usable as `agent_type` names in a fresh session.
- In a fresh session from the project root, spawn by preset name; for example, use `agent_type = "mar_explorer"` for read-only audits.
- If `spawn_agent` returns `unknown agent_type`, the session did not load the project registrations. Run the installer with `--write-config`, confirm the `[agents.mar_*]` entries, and start a fresh session from the project root.
- If work must continue in a stale session, use the temporary built-in fallback mapping below and set explicit model/reasoning overrides. Do not stop parallelizing because custom names are unavailable in the current session.
- Use `mar_explorer` by default for read-only audits. This is the main cost-control preset.
- Use `mar_code_worker` for clear implementation task cards with owned files and known validation.
- Use `mar_deep_code_worker` only when the task needs deeper code reasoning, broad tracing, complex debugging, or risky integration repair.
- Use `mar_execution_runner` for long-running command sequences or artifact-producing proof work. Give it resource locks and artifact paths.
- Use `mar_reviewer` after worker branches or risky generated artifacts, not as a substitute for implementation.
- Use `mar_senior_synthesizer` sparingly when cheaper workers return conflicting evidence or the decision is project-level.

## Built-In Fallback Mapping

Use this mapping when `spawn_agent` exposes only `default`, `explorer`, and `worker`:

| Desired preset | `agent_type` | Required overrides |
| --- | --- | --- |
| `mar_explorer` | `explorer` | `model = "gpt-5.4-mini"`, `reasoning_effort = "high"` |
| `mar_code_worker` | `worker` | `model = "gpt-5.4"`, `reasoning_effort = "medium"` |
| `mar_deep_code_worker` | `worker` | `model = "gpt-5.4"`, `reasoning_effort = "high"` |
| `mar_execution_runner` | `worker` | `model = "gpt-5.4-mini"`, `reasoning_effort = "high"` |
| `mar_reviewer` | `explorer` | `model = "gpt-5.4"`, `reasoning_effort = "high"` |
| `mar_senior_synthesizer` | `default` | `model = "gpt-5.5"`, `reasoning_effort = "medium"` |

## Output Contract

All preset agents should return compact deltas:

```text
Delta:
Evidence:
Files changed:
Commands:
Risks:
Recommendation:
Status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED
```

For read-only agents, `Files changed` must be `none`.

For execution agents, `Evidence` must include artifact paths and command results, not pasted logs.

For depth-2 helpers, the parent depth-1 worker must synthesize this output and report it to the main orchestrator. Depth-2 helpers do not report directly to the main orchestrator unless the parent is blocked or unavailable.

## Config Notes

Codex custom agent templates are standalone TOML files in `.codex/agents/` or `~/.codex/agents/`. Each custom agent must define `name`, `description`, and `developer_instructions`; fields such as `model`, `model_reasoning_effort`, and `sandbox_mode` can override inherited settings. Project `.codex/config.toml` must register them with `[agents.<name>] config_file = "./agents/<file>.toml"` for reliable discovery.

`agents.max_depth` defaults to `1` in Codex, which allows direct child agents but prevents deeper nesting. This skill needs `max_depth = 2` only when depth-1 workers are expected to spawn helper lanes. Do not raise depth above `2` unless the user explicitly changes the policy.
