# AI Context Index

Last updated: 2026-07-03

## Start Here

- Current state: `docs/ai/state.md`
- Active roadmap: `docs/ai/roadmap.md`
- Active batch: `docs/ai/batches/2026-07-03-dcdf-compatibility/index.md`
- Branch/worktree map: `docs/ai/branch-map.md`
- Resource locks: `docs/ai/locks.md`
- Historical utilization ledger: `docs/ai/agent-ledger.md`

## Skill Doctrine

- Main skill entry point: `SKILL.md`
- DCDF lane compatibility: `references/dcdf-lane-compatibility.md`
- Documentation system: `references/documentation-system.md`
- Context and memory: `references/context-and-memory.md`
- Subagent playbook: `references/subagent-playbook.md`
- Source control and GitHub: `references/source-control-and-github.md`
- Evidence contracts: `references/high-parallel-evidence-development.md`
- Goal prompts and context bundles: `references/goal-prompt-and-context-bundles.md`
- Pro Director packet mode: `references/pro-extended-director-protocol.md`
- Budget ledger: `references/orchestration-budget-ledger.md`

## Project Surfaces

- Agent presets: `assets/agents/`
- Preset installer: `scripts/install_agent_presets.py`
- Templates: `templates/`
- Usage docs: `docs/USAGE.md`
- Install docs: `INSTALL.md`
- Supplemental archive policy: `docs/SUPPLEMENTAL.md`

## Validation and Review

- Minimal no-write command: `python scripts/install_agent_presets.py --help`
- Diff hygiene command: `git diff --check`
- Branch state command: `git status --short --branch`
- Current compatibility evidence: `docs/ai/evidence/2026-07-03-dcdf-compatibility-review.md`

## Do Not Load by Default

- `supplemental/` contains preserved external material. Treat it as provenance/archive unless a task explicitly asks to inspect it.
- Raw logs, local paths, private workspace details, and chat transcripts are not project memory.
