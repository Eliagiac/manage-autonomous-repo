# AI State

Last updated: 2026-06-16

## Current Goal

Add `C:\Users\eliag\Downloads\autonomous-repo-orchestration-rulebook.zip` to the repo as a repo-only supplemental archive: preserve the extracted contents and file structure unchanged, include the original zip alongside it, document the contents outside the archive subfolder, commit, and push.

## Branch and Tree

- Repo: `C:\Users\eliag\OneDrive\Documenti\GitHub\manage-autonomous-repo`
- Branch: `main`
- Remote: `origin/main`
- Current change set: `SKILL.md`, new evidence/context reference docs, and this compact AI state/ledger.

## Latest Progress

- Added repo-only supplemental rulebook material under `supplemental/autonomous-repo-orchestration-rulebook/`.
- Preserved the original provided zip as `supplemental/autonomous-repo-orchestration-rulebook/autonomous-repo-orchestration-rulebook.zip`.
- Extracted the archive to `supplemental/autonomous-repo-orchestration-rulebook/autonomous_repo_orchestration_rulebook/` without modifying its internal files.
- Documented handling rules in `docs/SUPPLEMENTAL.md` and linked them from `README.md`.
- The supplemental rulebook is not part of the installed skill and was not copied to the loaded skill directory or target project repositories.
- `SKILL.md` now includes Pro Director Packet Mode for workflows where ChatGPT Pro/Pro Extended performs wide read-only planning and Codex performs bounded branch/worktree execution.
- Added Pro Director references:
  - `references/pro-extended-director-protocol.md`
  - `references/orchestration-budget-ledger.md`
- Added copy-ready templates:
  - `templates/pro-director-context-capsule.md`
  - `templates/codex-execution-packet.md`
- `SKILL.md` now includes Product Program Mode for broad product/research/autonomous objectives, including non-terminal statuses: `RUN_CONTINUES`, `MILESTONE_ACCEPTED`, `BLOCKED_REQUIRES_HUMAN`, and `PRODUCT_READY`.
- Added long-horizon orchestration references:
  - `references/product-orchestration-lifecycle.md`
  - `references/agentic-orchestration-landscape.md`
  - `references/goal-prompt-and-handoff-contracts.md`
- Added the `mar_program_auditor` preset and installer/config docs so project-local agents can be version-controlled with the new auditor role.
- Updated usage and preset docs to require branch-visible evidence from cloud/external coding agents, worktree isolation for parallel writes, explicit termination/resume status, and token/usage budget reporting.
- Applied the update to the loaded skill and aforementioned project references:
  - `C:\Users\eliag\.codex\skills\manage-autonomous-repo` synced from this repo.
  - `C:\Users\eliag\OneDrive\Documenti\GitHub\gaussian-splatting` received `mar_program_auditor` and docs status notes.
  - `C:\Users\eliag\OneDrive\Documenti\GitHub\gaussian-splatting-wg-backend-route-plan` received `mar_program_auditor` and docs status notes.
  - `C:\Users\eliag\OneDrive\Documenti\GitHub\3d` received `mar_program_auditor` and docs status notes.
- `SKILL.md` now links two new references:
  - `references/high-parallel-evidence-development.md`
  - `references/goal-prompt-and-context-bundles.md`
- The new references add evidence-status taxonomy, promotion gates, external workdir contracts, resource locks, branch-stack maps, context capsules, and goal-prompt guidance.
- This repo now has a minimal `docs/ai/` state and agent ledger for autonomous continuation.
- The canonical skill package was copied to `C:\Users\eliag\.codex\skills\manage-autonomous-repo`.
- Related GS/3d project references were updated or checked:
  - `C:\Users\eliag\OneDrive\Documenti\GitHub\gaussian-splatting`: applied-status note added to the skill reflection doc.
  - `C:\Users\eliag\OneDrive\Documenti\GitHub\gaussian-splatting-wg-backend-route-plan`: applied-status note added; project-local presets/config already matched canonical templates.
  - `C:\Users\eliag\OneDrive\Documenti\GitHub\3d`: state and agent ledger now record the refreshed loaded skill; project-local presets/config already matched canonical templates.

## Validation

Run before finish:

- `git status --short --branch`
- `git diff --check`
- targeted file presence checks for installed/project-local propagated copies

## Active Risks and Assumptions

- Project-local copies may be stale if they vendored the skill rather than using the loaded `$USERPROFILE\.codex\skills` copy.
- Existing project `.codex/agents` files may contain local edits; do not overwrite them unless the installer is intentionally run with `--overwrite`.

## Next Actions

1. Run final validation.
2. Verify the supplemental extracted tree matches the provided archive file list.
3. Commit and push the canonical repo.
