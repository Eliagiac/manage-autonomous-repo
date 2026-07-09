# MAR Deprecation Review

## Architecture At Public Main

At `c6f6115`, MAR consists of:

- [SKILL.md](../../SKILL.md) as a broad orchestrator entry point;
- `references/` for subagents, autonomous workflows, memory, docs, source
  control, evidence, product lifecycle, Pro Director, and budgets;
- `assets/agents/` and an installer for project-local custom agents;
- `templates/` for context and execution packets;
- `docs/ai/state.md` and `docs/ai/agent-ledger.md`;
- a 29-file supplemental rulebook/starter pack.

The audited local feature refs add:

- closed-loop ARO bridge doctrine;
- project-resource mirror;
- Director deferral queue;
- run-record/query templates;
- DCDF compatibility;
- privacy/sanitization fixes.

Remote PR #1 adds a proposed parallel-safe memory hierarchy.

No single one of these layers is unreasonable. The deprecation problem is that
future agents must understand which layers are normative, installed,
supplemental, optional, local-only, DCDF-overridden, or draft.

## Useful Mechanisms

### Portfolio Before Execution

MAR requires the orchestrator to identify independent tracks and choose a safe
parallel batch. This is superior to serially discovering work after each task.

### Task Ownership

The task-card shape is strong:

- objective;
- owned and avoid scope;
- branch/worktree;
- resource locks;
- proof artifact;
- validation;
- model/reasoning;
- done condition.

These fields should remain in a smaller skill.

### Branch Federation

The supplemental rulebook's selected Pro Director plus Codex branch-federation
model is directionally correct. Work should be reviewable, isolated, and
integrated one branch at a time.

### Evidence Discipline

MAR distinguishes weak evidence from acceptance. It promotes:

- claims to traces;
- traces to reproduction/validation;
- validation to acceptance by a separate reviewer or policy.

It also recognizes negative evidence as useful progress.

### Context And Restartability

Compact context capsules, state summaries, and continuation status solve a
real long-program problem. Chat history alone is not a durable project memory.

### Model Awareness

MAR deliberately chooses cheaper high-reasoning scouts, medium code workers,
high deep workers/reviewers, and a stronger orchestrator. Explicit selection is
better than silently inheriting one model for every lane.

## Deprecation Drivers

### 1. Entry-Point Breadth

The skill grew to cover:

- ordinary autonomous repo maintenance;
- Product Program Mode;
- Pro Director Packet Mode;
- Closed-Loop Director Bridge Mode;
- custom-agent installation;
- high-parallel evidence batches;
- repo memory and docs;
- source control;
- model/budget accounting;
- deferral queues and project mirror synchronization;
- DCDF compatibility.

Progressive disclosure limits what is loaded immediately, but the orchestrator
still owns the interaction among these modes.

### 2. Progress Artifacts Became A Second Management System

The user's complaint about untracked or overgrown progress artifacts is not a
claim that all docs are bad. It is a claim about active truth.

Evidence:

- the long-horizon dogfood updated state/context/ledger on repeated turns;
- public state and ledger captured host-specific propagation history;
- privacy cleanup required later local-only commits;
- PR #1 adds context, roadmap, memory, branch map, locks, batch, lane, and
  evidence files to solve two-file concurrency limits.

At scale, agents and humans must navigate both GitHub and the framework's
parallel source-controlled management tree. External tools cannot reliably know
which file is current without loading MAR doctrine first.

### 3. The Parallel-Memory Fix Reinforces The Problem

PR #1 is technically thoughtful. Per-lane files reduce merge conflicts, branch
maps expose ownership, and locks make resources explicit.

Architecturally, however, it is a local optimum. It fixes insufficient active
memory by creating more active-memory objects. Issues, PRs, branches, review
threads, checks, and project boards already provide most of those concepts in a
shared collaboration system.

### 4. GitHub-Native Doctrine Was Not Dogfooded In MAR

As audited on 2026-07-09:

- zero issues;
- one draft PR;
- zero PR reviews, comments, or checks;
- no protected branch;
- no integration branch;
- several important local-only refs.

The repo's own work was not tracked in the way it asked managed repos to work.
This weakens confidence that the doctrine is ergonomic from outside the
original local environment.

### 5. Portability Was Aspirational On Public Main

Public main includes machine-specific paths and propagation targets in active
memory. Later local commits fix this, but are not public. The installed skill
uses a later local variant, while an external reader sees the old state.

The framework treats source-controlled memory as durable truth, yet its own
truth is split among:

- `origin/main`;
- local branches;
- globally installed skill files;
- remote draft PR #1.

This is the same class of external navigability problem the memory system was
meant to solve.

### 6. Optional Control Plane Expanded The Mental Model

The closed-loop design adds:

- local MCP/Apps bridge;
- repo registry and read tools;
- Codex task control;
- project-resource mirror;
- Project UI sync requests;
- audit JSONL;
- run records;
- deferral queue lifecycle;
- singleton Director lease.

These mechanisms may be useful in specialized deployments. They should not be
part of the core model for ordinary repo collaboration.

No queue records were found in the local MAR queue directories. That means the
review can establish setup and intent, not sustained closed-loop success.

### 7. Contract Surface Drifted

The local closed-loop reference and templates disagree on run-record and
Director-query field names. This is not a cosmetic issue: agents following the
reference can emit a payload that does not match the template.

The more schemas, templates, and doctrine variants a skill ships, the more
maintenance effort is required to keep them aligned.

### 8. DCDF Compatibility Added Another Authority Layer

MAR's compatibility rule correctly says DCDF wins on task scope, model budget,
validation, and output. But that means a MAR invocation can only be understood
after reading both frameworks.

The compatibility path later produced:

- local-only compatibility commits;
- three MAR ledger validation handoffs in DCDF;
- DCDF PR #14;
- MAR PR #1;
- false-green onboarding evidence;
- a closing decision that MAR should remain non-authoritative doctrine.

The result demonstrates why compatibility should not become permanent core
behavior.

### 9. Medium Reasoning Was Too Weak For The Role

The historical claim:

- MAR recommended `gpt-5.5 medium`;
- the orchestrator owned architecture, sequencing, integration, risk, and
  product-state decisions;
- high was reserved for rare escalation.

The retrospective decision:

- this compromise proved inadequate;
- orchestration, architecture, review, and ambiguous integration now require
  high reasoning by default;
- cheaper settings remain useful for bounded scouts and mechanical workers.

The repository does not contain a controlled benchmark proving medium's
failure. The owner observed the workflow and is changing policy. This review
records that decision without mislabeling it as an empirical metric.

## Why Not Simply Trim MAR

A trim is possible: delete bridge references, supplemental materials, active
ledgers, compatibility mode, and many presets. What remains would be a smaller
parallel orchestration skill.

That work is effectively the requested replacement. Performing it inside MAR
would preserve ambiguity about old modes, old install instructions, and
compatibility. A new framework can start with the proven invariants and no
legacy default.

## Counterargument

The deprecation must not collapse into chat-only improvisation. A future skill
still needs:

- concise durable state for restartability;
- branch/worktree ownership;
- evidence/acceptance distinctions;
- explicit model choices;
- task cards for delegated lanes;
- integration sequencing;
- a clear handoff when a session ends.

The difference is that GitHub should hold active collaboration, while repo docs
hold only durable project knowledge.

## Recommendation

Stop MAR feature development and do not merge PR #1 as the active framework
direction. Preserve the repo and refs as evidence. When replacement
implementation resumes, copy only mechanisms with a demonstrated need and a
clear GitHub mapping.

No install removal, branch deletion, PR closure, or archive action is performed
by this review.
