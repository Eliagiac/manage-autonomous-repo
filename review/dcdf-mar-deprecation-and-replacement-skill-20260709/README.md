# Manage Autonomous Repo Deprecation Review

Date: 2026-07-09

Status: second-pass review, finalized for publication

This packet is the MAR-local companion to the canonical cross-project review
in the DCDF repository under
`review/dcdf-mar-deprecation-and-replacement-skill-20260709/`.

It is not a mirror. It concentrates on MAR's own history, public/local/draft
state split, dogfood evidence, and coupling to DCDF.

This is a retrospective and deprecation packet. It does not implement or
evaluate the replacement framework.

## Audited State

Public repository:

- `origin/main`: `c6f6115`;
- five public commits from 2026-06-10 through 2026-06-16;
- 69 tracked files;
- no issues, tags, releases, or protected branch;
- one open draft PR with no reviews, comments, or checks.

Local evidence refs:

- `feat/closed-loop-control-plane-overlays`: `ec579d9`;
- `fix/dcdf-lane-task-compat`: `f51f301`;
- `work/pass1.3.7-mar-sanitization`: `562018a`.

Remote draft evidence:

- PR #1, `dcdf/mar-dcdf-mode-memory-20260703`, head `4f5431f`;
- 14 commits adding DCDF compatibility and parallel-memory files.

This review branch starts from `origin/main`. The local feature/sanitization
commits are evidence only and are not included in the push.

## Evidence Labels

- **Fact**: Git/GitHub state or a tracked file.
- **Local-only fact**: a local ref, installed skill, or archived task.
- **Inference**: architectural conclusion from facts.
- **User rationale**: the owner's usability and model-policy decision.

## Read Order

1. [00-executive-synthesis.md](00-executive-synthesis.md)
2. [01-mar-development-timeline.md](01-mar-development-timeline.md)
3. [02-mar-deprecation-review.md](02-mar-deprecation-review.md)
4. [03-dcdf-interface-and-evidence.md](03-dcdf-interface-and-evidence.md)
5. [04-second-pass-amendments-and-method.md](04-second-pass-amendments-and-method.md)

## Superseded First Pass

The earlier 2026-07-09 packet was untracked and drifted from the DCDF copy. It
also devoted two active documents to replacement design and a subagent ledger.
This packet replaces that structure with history, evidence, and corrections.

## Bottom Line

MAR's central ideas remain useful: parallel-first decomposition,
branch/worktree ownership, evidence promotion, compact task cards, explicit
model choices, and Pro/Codex role separation.

The active framework should end because those ideas became embedded in a
larger operating kit of references, presets, progress memory, supplemental
rulebooks, bridge/mirror/queue contracts, and compatibility modes. Public,
installed, local, and draft states diverged, while GitHub was barely used to
coordinate MAR itself.

The owner also rejects the documented `gpt-5.5 medium` orchestrator default.
That is a retrospective decision: high reasoning should own orchestration,
architecture, review, and ambiguous integration from now on.
