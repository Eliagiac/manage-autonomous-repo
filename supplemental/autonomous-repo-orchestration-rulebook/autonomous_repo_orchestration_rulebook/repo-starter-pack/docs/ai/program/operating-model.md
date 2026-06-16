# Operating Model

This repo uses Pro Director + Codex Branch Federation.

- Pro Director: read-only strategy, context capsules, track portfolio, execution packets, review.
- Codex Integration Agent: integration branch, worker dispatch, merges, validation, state update.
- Codex Workers: branch/worktree-scoped implementation, execution, review, demos, or research.

Normal status is `RUN_CONTINUES` until a named milestone or product gate passes.
