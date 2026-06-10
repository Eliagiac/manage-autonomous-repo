# Troubleshooting Agent Presets

If a session reports:

```text
unknown agent_type 'mar_explorer'
```

Check that the target project has registered presets:

```powershell
Get-Content -Raw .codex\config.toml
Get-ChildItem .codex\agents
```

If missing, run:

```powershell
python C:\Users\<you>\.codex\skills\manage-autonomous-repo\scripts\install_agent_presets.py C:\path\to\project --write-config
```

Then start a fresh Codex session from the project root.
