# Executive Synthesis

## Verdict

Deprecate `manage-autonomous-repo` as an active standalone framework. Preserve
its branch/worktree, subagent, task-card, evidence, and Pro/Codex separation
principles in a smaller future skill.

This is not a claim that MAR lacked value. MAR was closer than DCDF to the
desired delivery mechanism because it was already a reusable skill. Its failure
was scope: it evolved from repo-maintainer guidance into a long-horizon
operating system plus an optional local control plane.

## Strongest Facts

- Public history spans five commits from `4901952` to `c6f6115`.
- The initial 27-file skill grew by 49 changed files and 2,747 insertions before
  public main stopped on 2026-06-16.
- Public main contains 69 files; the audited local feature state contains 74,
  including 16 references and 29 supplemental files.
- The first public commit already assigns architecture, sequencing,
  integration, merge, risk, and product-state decisions to a
  `gpt-5.5 medium` orchestrator.
- Later bridge, mirror, deferral, DCDF compatibility, privacy, and sanitization
  work remained local or draft-only.
- The globally installed skill matched the later local feature version, not
  public main.
- GitHub contains zero MAR issues and one draft PR with no reviews, comments,
  or checks.
- PR #1 has 14 commits and addresses parallel-memory weakness by adding a
  context index, roadmap, branch map, locks, batches, lanes, and evidence files.
- PR #1 delegates validation to DCDF PR #14, which is closed unmerged.
- Local deferral queue directories existed without queue records.
- Local closed-loop references and templates disagree on several field names.

## Strongest Local Task Evidence

The June 7 Gaussian dogfood audit found that:

- portfolio decomposition improved;
- the orchestrator still retained heavy final proof work;
- substantial writes moved to a named branch later than ideal;
- parallel write capacity was underused.

The June 16 long-horizon Gaussian task then demonstrated both MAR's value and
its cost. It advanced real measurement-bound work over many continuation turns,
but repeatedly updated `docs/ai/state.md`, `context-index.md`, and
`agent-ledger.md`. The repository memory became part of every batch.

The ARO control-plane task implemented a real bridge foundation across three
repos and recorded 253,977 tokens. This shows the closed-loop design was not
empty speculation. It also shows how far the framework expanded beyond a
portable repo skill.

## Interpretation

MAR's best ideas arrived early:

- parallel independent tracks;
- branch/worktree isolation;
- explicit task ownership;
- evidence and acceptance separation;
- wide Pro planning plus bounded Codex execution;
- non-terminal long-program status.

Later work mostly added machinery to preserve, synchronize, and route those
ideas:

- active memory and ledgers;
- product-program modes;
- supplemental rulebooks;
- custom-agent installation;
- bridge run records;
- project-resource mirror;
- Director deferral queue;
- DCDF compatibility;
- privacy/sanitization passes;
- parallel-memory repair.

The resulting system was richer but less portable in practice. Public,
installed, local, and draft state diverged. The repo that advocated GitHub
coordination did not use issues or reviewed PRs to manage itself.

## Model Policy

The medium default must be described accurately:

- **Fact:** it was an explicit cost compromise from the first public commit.
- **Fact:** the orchestrator owned high-impact and cross-cutting decisions.
- **Local-only fact:** dogfood still showed under-delegated proof and
  long-running management state.
- **User rationale:** medium proved inadequate for that role.

The future rule is high reasoning for orchestration, architecture, review,
conflict resolution, and ambiguous integration. Smaller or medium workers
remain appropriate for bounded tasks with clear validation.

## Preserve

- skill-centered reuse;
- parallel-first lane portfolios;
- branch and worktree ownership;
- task cards with objective, scope, locks, proof, validation, and done state;
- context capsules and bounded execution packets;
- evidence promotion and negative evidence;
- independent review before acceptance;
- non-terminal long-program status;
- explicit model/budget reporting.

## Retire

- one long-horizon orchestrator as the default project manager;
- append-style progress ledgers as active truth;
- mandatory full `docs/ai` scaffolds;
- broad mode and reference routing in the default invocation;
- project-local custom agent installation as a prerequisite;
- ARO bridge, project mirror, and deferral queue as core dependencies;
- DCDF compatibility as a continuing mode;
- medium reasoning as the orchestration default.

## Boundary

This review does not remove the global installed skill, close MAR PR #1, delete
local branches/worktrees, archive the repo, or modify the ARO control-plane
repository. Those are separate deprecation-execution decisions.
