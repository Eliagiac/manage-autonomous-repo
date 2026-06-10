# Related Projects and References

Manage Autonomous Repo is a workflow skill, not a framework dependency. It is intended to compose with Codex, Git, GitHub, and project-specific tools.

## Primary References

- OpenAI Codex subagents and custom agents.
- OpenAI Codex skills.
- Git branches and worktrees.
- GitHub pull requests, protected branches, and merge workflows.
- Agent-oriented workflow projects that use explicit procedures, task readiness checks, and review gates.

## Concepts Used

- Orchestrator/worker separation.
- Track portfolios for parallel autonomous work.
- Durable repository memory.
- Branch-isolated implementation.
- Evidence-based review gates.
- Restartable handoffs.
- Cost-aware model selection.

## Adjacent Tools

Useful companion capabilities include:

- GitHub plugin for issues, PRs, CI, and publication.
- Browser or Chrome tooling for web UI validation.
- Computer Use for desktop-app validation.
- Document, spreadsheet, and presentation plugins for generated artifact workflows.
- Project-specific test, benchmark, and demo scripts.

## Non-Goals

This repository does not provide:

- an autonomous agent runtime;
- a CI platform;
- a replacement for Git/GitHub;
- project-specific implementation logic;
- guarantees that a given Codex session exposes every custom-agent feature without a fresh project-root session.
