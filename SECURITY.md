# Security

## Supported Scope

This repository contains a Codex skill, documentation, and local installer utilities. It does not run a hosted service.

## Reporting Issues

Open a private GitHub security advisory if available, or contact the repository owner directly.

Do not include secrets, tokens, private repository contents, or sensitive logs in public issues.

## Security Guidance for Users

- Review any autonomous-agent changes before merging them into important branches.
- Keep secrets out of `docs/ai/`, prompts, demos, logs, and committed config files.
- Prefer project-local installs and source-controlled configuration for reproducibility.
- Do not grant agents access to paid services, production credentials, or destructive infrastructure without explicit review.
