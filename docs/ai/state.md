# AI State

Last updated: 2026-06-16

## Current Goal

Document and push the latest manage-autonomous-repo skill updates, then propagate the canonical repo copy into the local Codex loaded skill directory and project-local references that depend on it.

## Branch and Tree

- Repo: `C:\Users\eliag\OneDrive\Documenti\GitHub\manage-autonomous-repo`
- Branch: `main`
- Remote: `origin/main`
- Current change set: `SKILL.md`, new evidence/context reference docs, and this compact AI state/ledger.

## Latest Progress

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
2. Commit and push the canonical repo.
3. Leave project repos dirty only with the targeted status-note additions made during this propagation run.
