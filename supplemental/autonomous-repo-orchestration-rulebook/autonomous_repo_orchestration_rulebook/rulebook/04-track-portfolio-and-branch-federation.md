# 04 — Track Portfolio and Branch Federation

## Portfolio, not queue

A long-running autonomous repo should not ask “what is the next task?” It should ask “which independent tracks can safely advance in the next batch?”

A track is any separable effort that can produce evidence without duplicating another active lane.

## Track scoring

Score each candidate track from 0 to 3:

- **User value** — does this move toward visible product capability or a milestone gate?
- **Unblock value** — does it clear a blocker for several future tracks?
- **Evidence clarity** — can it produce a concrete proof artifact?
- **Independence** — can it run without overlapping active writers?
- **Reversibility** — can it be parked, reverted, or discarded cleanly?
- **Cost fit** — is the expected Codex/tool/hardware spend justified?
- **Integration cost** — lower is better; high-conflict work should be serialized.

Select the batch by value and safe concurrency, not by a fixed number.

## Batch size defaults

Use 3–6 active lanes for broad repo work when safe.

Use 1–2 lanes when:

- the repo is dirty and ownership is unclear;
- all useful work depends on one serial blocker;
- several tracks need the same GPU/browser/device/dataset/external workdir;
- a risky merge or root-cause debug is in progress;
- the integration agent cannot safely absorb more output.

Use more than 6 lanes only when most lanes are read-only, execution-only, or extremely disjoint and the integration branch can absorb them one at a time.

## Branch federation

A branch federation has:

- `main` — stable baseline;
- `integrate/<milestone>` — integration branch owned by the integration agent;
- `feat/<topic>`, `fix/<topic>`, `test/<topic>`, `demo/<topic>`, `docs/<topic>`, `research/<topic>` — worker-owned branches;
- one worktree per active write branch when supported;
- read-only lanes without branches;
- execution lanes with explicit artifact/resource ownership.

## Worker branch rules

Each worker branch must have:

- one owning agent;
- branch base;
- owned files/modules/artifacts;
- avoid scope;
- resource locks;
- expected proof artifact;
- validation command;
- stop conditions;
- handoff format;
- integration recommendation.

Workers do not merge into `main` or into each other. They do not broaden scope unless they create a new task card and stop for integration review.

## Resource locks

Every execution or write-heavy lane names locks. Common locks:

- `gpu_training`
- `browser_runtime`
- `server_port:<port>`
- `external_workdir:<name>`
- `source_payload:<name>`
- `runs_root:<name>`
- `central_config`
- `schema_or_migration`
- `dependency_manifest`
- `integration_branch`
- `submodule:<name>`

Two active writers may share a lock only if the integration agent explicitly serializes them.

## Track types

### Implementation track

A branch that changes source-controlled files and proves behavior with tests, demos, or reports.

### Execution track

A lane that runs commands, captures logs, generates artifacts, benchmarks, screenshots, or QC reports. It should not edit source unless assigned.

### Read-only scout track

A lane that maps files, docs, tests, logs, dependencies, or external options. Its output should become task cards, decisions, or parked/rejected findings.

### Review track

A lane that inspects a branch or artifact and returns blocking findings first.

### Demo track

A lane that proves a user/operator-visible result. Demo tracks are not optional for product-facing milestones.

## Stop/replan triggers

Stop and replan when:

- two workers need the same file or resource;
- a branch’s base is stale or ambiguous;
- a worker discovers the task is broader than its execution packet;
- the proof artifact cannot be produced;
- a branch repeats known negative evidence without a material new hypothesis;
- integration cost exceeds expected value;
- the director/integration agent cannot explain how this branch improves a milestone, demo, or evidence gate.
