# Manage Autonomous Repo

Manage Autonomous Repo is a Codex skill for running software repositories as autonomous engineering programs. It is designed for projects where Codex agents may plan, implement, test, document, demo, refactor, and coordinate GitHub work with minimal human supervision.

The skill emphasizes:

- parallel-first orchestration with subagents;
- durable repository memory for future agents;
- branch and worktree isolation for independent work;
- branch-visible evidence from cloud or external coding agents;
- explicit model and reasoning choices for cost control;
- explicit token/usage reporting and non-terminal product-program exit statuses;
- documentation, roadmaps, demos, tests, and handoffs that live in the repo;
- Pro Director + Codex execution packet workflows for separating wide read-only planning from bounded repository mutation;
- GitHub-oriented source-control hygiene.

## Contents

- `SKILL.md` - the main Codex skill entry point.
- `references/` - detailed workflow playbooks loaded only when needed.
- `templates/` - copy-ready packet templates for Pro Director capsules and Codex execution lanes.
- `assets/agents/` - reusable custom-agent templates for autonomous repo work.
- `scripts/install_agent_presets.py` - copies and registers the bundled agents in a target project.
- `agents/openai.yaml` - Codex app metadata for the skill.

## Install

Copy this folder into your Codex skills directory:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.codex\skills\manage-autonomous-repo"
```

Then start a new Codex session and reference the skill:

```text
[$manage-autonomous-repo](C:\Users\<you>\.codex\skills\manage-autonomous-repo\SKILL.md)
Use subagents as per skill instructions.
```

For full setup details, see [INSTALL.md](INSTALL.md).

## Project Agent Presets

For a repository that should use this skill long-term, install the bundled subagent presets into that project:

```powershell
python C:\Users\<you>\.codex\skills\manage-autonomous-repo\scripts\install_agent_presets.py C:\path\to\project --write-config
```

This creates:

- `.codex/agents/mar-*.toml`
- `.codex/config.toml` entries for `[agents.mar_*]`
- `agents.max_threads = 10`
- `agents.max_depth = 2`

Start a fresh Codex session from the project root after installing project presets.

## Recommended Runner

Use `gpt-5.5` with `medium` reasoning for the main orchestrator. The bundled worker presets use cheaper models where appropriate:

- `gpt-5.4-mini high` for read-heavy exploration and execution support;
- `gpt-5.4 medium` for well-scoped implementation;
- `gpt-5.4 high` for deeper code/debug/review work;
- `gpt-5.4 high` for product-program audits with `mar_program_auditor`;
- `gpt-5.5 medium` for rare senior synthesis.

## Usage

Typical prompt:

```text
[$manage-autonomous-repo](C:\Users\<you>\.codex\skills\manage-autonomous-repo\SKILL.md)
Use subagents as per skill instructions.

Continue this repository toward its roadmap. Keep docs, demos, tests, and source control current. Use parallel agents where useful.
```

See [docs/USAGE.md](docs/USAGE.md) for workflow examples.

## Related Projects and Prior Art

This skill draws from Codex subagent workflows, Git/GitHub branch and worktree practices, and agent workflow projects that emphasize explicit procedures, review gates, and durable handoffs. See [docs/RELATED.md](docs/RELATED.md).

## License

Released under the MIT License. See [LICENSE](LICENSE).
