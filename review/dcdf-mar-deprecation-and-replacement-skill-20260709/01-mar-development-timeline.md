# MAR Development Timeline

This timeline distinguishes public Git history, local-only refs, remote draft
history, and archived Codex task evidence.

## Pre-Repository Work

### 2026-06-01

Archived task `019e854b-...`, titled `Manage autonomous repo`, invoked the
skill before the public repository existed. The turn was interrupted. It
establishes prehistory, not a successful public baseline.

### 2026-06-07

Two read-only audits examined the skill after a parallelization update:

- `019e9fc2-...` found no hard contradiction but warned that an
  "orchestrator-only judgment" exception could leave proof work local.
- `019ea3d8-...` audited a Gaussian Splatting run. It found good research,
  setup, demo, and evidence separation, but incomplete proof delegation, late
  branch separation, and less write-lane parallelism than the skill intended.

These findings predate public MAR and show the framework was tuned in response
to real orchestration behavior.

## Public Main

### 2026-06-10 - `4901952`

`Initial public Manage Autonomous Repo skill`

- 27 files;
- 1,949 inserted lines;
- 147-line `SKILL.md`;
- subagent, workflow, memory, docs, and source-control references;
- six agent presets plus installer;
- examples and installation docs;
- `gpt-5.5 medium` orchestrator recommendation.

The initial public release was already a substantial operating kit, not a
minimal skill.

### 2026-06-16 - `da260dc`

`Document evidence workflow skill updates`

- adds high-parallel evidence workflow;
- adds goal/context bundle reference;
- creates `docs/ai/state.md` and `docs/ai/agent-ledger.md`.

This is the start of repository memory as an explicit product surface.

### 2026-06-16 - `9a04ecd`

`Add long-horizon product program orchestration`

- adds Product Program Mode;
- adds program auditor preset;
- adds product lifecycle and handoff contracts;
- expands state and ledger.

The skill now owns continuing product-program decisions, not only repo
maintenance.

### 2026-06-16 - `7c82eaa`

`Add Pro Director packet workflow`

- adds Pro context capsule;
- adds Codex execution packet;
- adds model/budget ledger;
- formalizes wide Pro planning and bounded Codex execution.

This is one of MAR's strongest conceptual contributions.

### 2026-06-16 - `c6f6115`

`Add supplemental orchestration rulebook archive`

- adds 29 supplemental files plus an archive;
- adds operating model, branch federation, evidence, CI, budgeting, prompts,
  adoption, schemas, and templates.

This remains public `origin/main`.

## Dogfood And Control-Plane Expansion

### 2026-06-16 onward - Long-Horizon Gaussian Task

Archived task `019ecf8c-...` uses MAR to advance a measurement-bound Gaussian
Splatting research program. It produces real source and test changes across
multiple continuation turns and repeatedly ends `RUN_CONTINUES`.

Nearly every batch also updates some combination of:

- `docs/ai/state.md`;
- `docs/ai/context-index.md`;
- `docs/ai/agent-ledger.md`.

The task proves that MAR can sustain a long program. It also demonstrates the
maintenance cost of source-controlled active memory.

### 2026-06-16 to 2026-06-17 - ARO Foundation Task

Archived task `019ed299-...` implements a closed-loop foundation from an
attached packet:

- creates `autonomous-repo-orchestration-control-plane`;
- applies MAR overlays;
- applies a Gaussian Splatting orchestration note;
- validates bridge tests and smoke bootstrap;
- ends with three branch commits and 253,977 reported tokens.

This is the point where MAR's scope expands from repo doctrine to local
cross-repository infrastructure.

## Local-Only MAR Refs

### 2026-06-17 - `8c543a5`

`Add closed-loop control plane skill overlays`

Adds:

- closed-loop control-plane reference;
- project-resource mirror;
- Codex Director deferral queue;
- thread run record;
- Director query template.

### 2026-06-19 - `c51dd15`

`Align closed-loop control plane skill docs`

Refines installation, docs, templates, and bridge protocol.

### 2026-06-22 - `151f91a`

`Add DCDF lane-task compatibility mode`

Adds:

- explicit DCDF override behavior;
- task/receipt templates and examples;
- compatibility docs;
- validator script;
- preset and state changes.

### 2026-06-22 - `4d0bf00`, `f51f301`

Scrubs local paths and normalizes encoding in compatibility artifacts.

The fixes demonstrate good privacy discipline, but also show that portable
examples and state had already captured host-specific content.

### 2026-06-25 to 2026-06-26 - `ec579d9`, `5ed607e`, `562018a`

These commits remove private operational history, sanitize docs/templates, and
refresh the supplemental archive.

They remain local. Public main therefore does not embody the repository's own
later portable-memory policy.

## Remote Draft PR #1

### 2026-07-03

PR #1, `Harden DCDF lane compatibility and parallel repo memory`, opens
against `main`. Its 14 commits are:

| Commit | Change |
| --- | --- |
| `15a25a4` | DCDF mode in MAR skill |
| `4a234fa` | DCDF lane compatibility reference |
| `d4b2f50` | parallel-safe memory guidance |
| `80055b3` | sanitized state and parallel-memory pointer |
| `6dc3504` | agent ledger converted to batch history |
| `eeffa1b` | context index |
| `fa995b9` | roadmap |
| `1b7145d` | durable memory |
| `72e2677` | branch/worktree map |
| `7f3c704` | resource lock map |
| `b92a6a8` | compatibility batch index |
| `b020c82` | docs lane record |
| `a786869` | compatibility readiness evidence |
| `4f5431f` | context memory reference update |

The PR changes 14 files and creates a much larger `docs/ai` hierarchy. It is
the clearest artifact of the framework responding to insufficient active
memory with more structured active memory.

The PR body says validation is delegated through DCDF PR #14.

## Coupling Becomes Stale

### 2026-07-08

DCDF PR #14 is closed unmerged as superseded by the 2.0.0 workflow. Its closing
comment says MAR should remain lane-local doctrine, not a scheduler, ledger
owner, outbox target, Director Order parser, or lifecycle authority.

MAR PR #1 remains draft with no review, comment, or check. Its stated
controller-bound validation dependency is no longer active.

## Deprecation Review

### 2026-07-08 to 2026-07-09

The first deprecation task creates an untracked MAR review packet and a matching
DCDF packet. The copies drift and include replacement design plus a subagent
ledger.

### 2026-07-09

The second pass:

- audits public, local, installed, and draft state separately;
- reconstructs archived dogfood history;
- adds the DCDF/MAR coupling review;
- labels the medium-default conclusion as user rationale;
- removes replacement implementation from scope;
- publishes review files from a branch based on `origin/main`, leaving local
  feature commits untouched.

## Timeline Conclusion

MAR evolved in less than three weeks from a large repo-management skill into:

- a product-program operating model;
- a Pro/Codex packet system;
- a supplemental rulebook;
- a local bridge/mirror/queue control-plane design;
- a DCDF compatibility mode;
- a privacy/sanitization program;
- a proposed parallel-memory hierarchy.

The pace produced useful ideas quickly. It also left the authoritative state
split across public main, local refs, the installed skill, and a draft PR. That
split is central to the deprecation case.
