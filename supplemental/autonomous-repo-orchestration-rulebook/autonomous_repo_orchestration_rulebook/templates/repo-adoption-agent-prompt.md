[$manage-autonomous-repo](<path-to-skill>/SKILL.md)
Use subagents as per skill instructions.

Adopt the project-agnostic Pro Director + Codex Branch Federation workflow in this repository without changing product scope or roadmap content.

Tasks:
1. Inspect `git status --short --branch`, active remotes, worktrees, and `docs/ai/`.
2. Create or update compact management docs only: `docs/ai/state.md`, `docs/ai/context-index.md`, `docs/ai/track-portfolio.md`, `docs/ai/program/operating-model.md`, `docs/ai/program/budget-policy.md`, and one dated batch ledger.
3. If existing docs are large, preserve them as archives or link them from indexes. Do not delete evidence unless clearly safe.
4. Do not change the technical roadmap except to point to its current owner document.
5. Install/verify project-local `mar_*` agent presets if the skill provides them.
6. Produce a Pro-review packet with candidate branch packets for the next implementation cycle.
7. Stop before product/code implementation.

Return:
- files changed;
- old docs archived/indexed;
- current compact state;
- candidate track portfolio;
- recommended first branch batch;
- validation run;
- risks.
