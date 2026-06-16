# 11 — Adoption Plan

## For a new repo

1. Create a baseline Git repo and `.gitignore`.
2. Add the standard `docs/ai/` starter docs.
3. Add the project objective and product gate.
4. Create the first context index.
5. Install or verify `manage-autonomous-repo` skill and project-local agent presets.
6. Ask Pro Director for the first track portfolio and execution packets.
7. Run Codex integration agent with the generated batch packet.
8. Merge through `integrate/<milestone>` and update batch ledger.

## For an existing long-running repo

1. Snapshot current branch/worktree/PR state.
2. Identify the live branch and abandoned/parked branches.
3. Freeze giant docs as archive snapshots if needed.
4. Replace `state.md` with a compact dashboard.
5. Create or repair `context-index.md`.
6. Create `track-portfolio.md` with active/candidate/blocked/parked lanes.
7. Move old plan piles into active/archive categories.
8. Create `evidence/index.md` for accepted/parked/rejected artifacts.
9. Add `program/operating-model.md` and `program/budget-policy.md`.
10. Run one Pro Director cycle before launching new Codex implementation.

## For the current GS-style workflow pattern

Do not start by changing the technical roadmap. Start by changing the operating shape:

- compact current state;
- index huge evidence;
- split active work into branch packets;
- keep abandoned branch docs marked as provenance, not live state;
- use Pro for batch selection;
- give Codex implementers execution packets;
- require every branch to produce proof or a parked/rejected summary.

## Success criteria for adoption

The adoption is successful when:

- a fresh Pro chat can understand the repo state from `state.md`, `context-index.md`, and latest batch ledger;
- a Codex worker can complete a branch without reading the whole roadmap;
- at least three safe independent lanes can be identified when the repo has enough work;
- integration branch rules are written down;
- the next batch is clear;
- oversized docs are indexed rather than repeatedly re-read;
- budget/model choices are recorded.
