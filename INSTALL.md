# Installation

## Requirements

- Codex Desktop or Codex CLI with skill support.
- Python 3.11+ for the agent preset installer.
- Git for repository and worktree workflows.
- GitHub CLI or the Codex GitHub plugin if you want publication, PR, issue, or CI automation.

## Install the Skill

From a local checkout of this repository:

```powershell
$skillHome = "$env:USERPROFILE\.codex\skills\manage-autonomous-repo"
New-Item -ItemType Directory -Force -Path (Split-Path $skillHome) | Out-Null
Copy-Item -Recurse -Force . $skillHome
```

Restart Codex or start a fresh session so the skill list refreshes.

## Verify Installation

In a new Codex session, reference:

```text
[$manage-autonomous-repo](C:\Users\<you>\.codex\skills\manage-autonomous-repo\SKILL.md)
```

Codex should load `SKILL.md` and follow the autonomous repository workflow.

## Install Project-Local Agent Presets

For each repository that should be run with this skill:

```powershell
python C:\Users\<you>\.codex\skills\manage-autonomous-repo\scripts\install_agent_presets.py C:\path\to\project --write-config
```

The installer copies the bundled custom-agent templates into `.codex/agents/` and registers them in `.codex/config.toml`.

Expected config shape:

```toml
[agents]
max_threads = 10
max_depth = 2

[agents.mar_explorer]
config_file = "./agents/mar-explorer.toml"
```

The actual config contains entries for all bundled `mar_*` presets.

## Fresh Session Requirement

After installing project-local presets, start a new Codex session from the project root. Existing sessions may not reload newly registered custom agent names.

## Updating

To update the installed skill:

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\manage-autonomous-repo"
```

To refresh project-local presets after a skill update:

```powershell
python C:\Users\<you>\.codex\skills\manage-autonomous-repo\scripts\install_agent_presets.py C:\path\to\project --write-config --overwrite
```

Use `--overwrite` only when you want to replace existing project-specific agent templates.
