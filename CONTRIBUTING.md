# Contributing

Contributions should keep the skill practical, concise, and reliable under real Codex sessions.

## Guidelines

- Keep `SKILL.md` focused on core workflow and navigation.
- Put detailed procedures in `references/`.
- Keep installer behavior deterministic and easy to validate.
- Avoid clutter, warnings, and historical commentary in durable skill text.
- Prefer concrete workflows over long lists of anti-patterns.
- Preserve the public repo as a directly installable skill folder.

## Validation

Before proposing changes:

```powershell
python -m py_compile scripts\install_agent_presets.py
python scripts\install_agent_presets.py $env:TEMP\mar-install-test --write-config
```

Also inspect the generated `.codex/config.toml` and `.codex/agents/*.toml` files for expected custom-agent registrations and model choices.
