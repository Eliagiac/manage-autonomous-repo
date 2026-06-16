# 02 — Canonical Operating Loop

Every autonomous repo cycle follows this loop. The loop applies to new repos, existing repos, and long-running research/product programs.

## Phase 0 — Baseline snapshot

The Pro Director or a read-only Codex explorer gathers only the minimum baseline:

- current repo path and default branch;
- `git status --short --branch`;
- active branches/worktrees/PRs;
- current `docs/ai/state.md` and `docs/ai/context-index.md`;
- latest batch ledger entry;
- current tests/demos/CI surface;
- known dirty files, resource locks, and external artifacts.

Do not read the entire docs tree unless the context index fails.

## Phase 1 — Pro Director synthesis

The Pro Director:

1. Builds or refreshes the track portfolio.
2. Detects stale state, contradictory docs, duplicate plans, and dead branches.
3. Scores candidate tracks by independence, user value, unblock value, proof clarity, resource locks, risk, integration cost, and expected Codex spend.
4. Chooses a safe batch.
5. Writes one context capsule and one execution packet per lane.
6. Defines integration order and validation ladder.

This phase should absorb most wide-context reasoning that would otherwise be spent inside Codex.

## Phase 2 — Codex integration setup

A thin Codex integration agent receives the Pro Director’s integration packet. It:

- verifies repo state and branch bases;
- creates or updates `integrate/<milestone>`;
- creates worker branches/worktrees if the environment supports them;
- installs/refreshes project-local agent presets if needed;
- dispatches worker agents using the execution packets;
- records branch/worktree ownership in the batch ledger.

The integration agent should not independently rewrite the Pro plan unless the repo state invalidates it. If invalidated, it writes a short correction and stops or asks for a new Pro pass.

## Phase 3 — Codex worker execution

Each worker:

- reads only the context capsule plus named files;
- owns exactly one branch/worktree or read-only/execution lane;
- respects owned scope and avoid scope;
- stops if scope becomes unsafe;
- produces code, tests, docs, demos, reports, or retained evidence;
- commits or clearly reports changed files;
- returns the required handoff.

A worker is not a second orchestrator. It should not broaden the roadmap, merge unrelated work, or modify central docs outside its scope unless explicitly assigned.

## Phase 4 — Integration

The integration agent:

1. Reviews each worker handoff.
2. Confirms proof artifacts exist.
3. Merges worker branches into `integrate/<milestone>` one at a time.
4. Runs narrow validation after each merge.
5. Runs broader validation after the batch.
6. Updates compact state and batch ledger.
7. Parks, rejects, or splits branches that fail proof or conflict too heavily.

## Phase 5 — Pro Director review

The Pro Director reviews the batch output:

- integration branch diff or PR summaries;
- validation output;
- demo/artifact paths;
- batch ledger;
- budget notes;
- negative or parked evidence;
- updated state/context index.

The Pro Director then selects the next batch or declares a milestone status.

## Phase 6 — Status and handoff

Every cycle ends with one of:

- `RUN_CONTINUES` — useful progress landed or was parked; next batch is known.
- `MILESTONE_ACCEPTED` — a named milestone gate passed; next milestone is known.
- `BLOCKED_REQUIRES_HUMAN` — blocked by credentials, paid/destructive action, legal/licensing, missing hardware/data, or an explicit product decision.
- `PRODUCT_READY` — the product gate passed.

Do not use “complete” for broad projects unless `PRODUCT_READY` is true or the human closes the program.

## Minimum loop artifact set

A complete cycle leaves:

- updated `docs/ai/state.md` dashboard;
- dated batch ledger file;
- branch/worktree map;
- worker summaries;
- validation command results;
- demo/evidence pointers where applicable;
- next batch proposal.
