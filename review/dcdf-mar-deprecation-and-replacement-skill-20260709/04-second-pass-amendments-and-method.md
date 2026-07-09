# Second-Pass Amendments And Method

## Corrections To The First MAR Packet

### The Packet Was Unpublished

The earlier 2026-07-09 review directory was untracked. It was not part of MAR
history or GitHub state.

### The DCDF And MAR Copies Had Drifted

The first-pass DCDF README called the packets mirrors. The MAR README called
this one a self-contained companion. The files were already not byte-for-byte
equivalent.

This pass defines a clear relationship:

- DCDF holds the canonical cross-project chronology;
- MAR holds a project-local history and DCDF interface review.

### Public And Local MAR Were Conflated

The earlier review described closed-loop references, sanitized memory, and
later compatibility behavior as current architecture without clearly stating
that public main stopped at `c6f6115`.

This pass separates:

- public `origin/main`;
- local feature/sanitization refs;
- globally installed skill content;
- remote draft PR #1.

### GitHub Practice Was Missing

The earlier review praised GitHub-oriented doctrine but did not record that MAR
had:

- zero issues;
- one draft PR;
- no reviews, comments, checks, or protected branch;
- important local-only branches.

That doctrine/practice gap is now a primary finding.

### PR #1 Was Missing

The earlier review did not reconstruct the 14-commit PR that responds to
parallel-memory concerns with context, roadmap, branch, lock, batch, lane, and
evidence files. It also did not note that the PR's DCDF validation dependency
was closed unmerged.

### Privacy And Contract Drift Were Missing

This pass adds:

- public main's path-heavy operational memory;
- local-only privacy cleanup;
- installed/public skill hash divergence;
- run-record and Director-query reference/template field mismatches;
- empty local queue buckets as setup evidence, not execution evidence.

### Model Claim Was Reclassified

The first pass treated "medium was too weak" like an established repository
fact.

The corrected classification is:

- repository fact: `gpt-5.5 medium` was deliberately recommended;
- task evidence: dogfood retained proof work and management state;
- user rationale: medium was inadequate for orchestration ownership;
- policy decision: default important orchestration/review lanes to high.

### Replacement Design And Agent Ledger Were Removed

The replacement framework brief is out of scope. The live subagent ledger was
also removed from the durable packet. This review records only method and
evidence limits.

## Method

The second pass used:

- complete Git history across local refs;
- GitHub PR/issue/release/protection state through `gh`;
- file/reference/template inventory;
- archived Codex task reads;
- DCDF committed review and receipt evidence;
- direct reading of the linked Pro share;
- five independent `gpt-5.4 high` read-only research lanes.

Research lanes covered:

- DCDF history;
- MAR history;
- prior-review audit;
- archived-task archaeology;
- Pro-chat interpretation.

The parent agent retained synthesis, edits, branch strategy, validation, and
publication. All completed agents were closed.

## Publication Isolation

At review start, the MAR checkout was on local
`feat/closed-loop-control-plane-overlays` at `ec579d9`.

The review branch was created from `origin/main` at `c6f6115`. The untracked
review packet was carried onto that branch and rewritten there. This avoids
publishing:

- closed-loop overlay commits;
- privacy/sanitization commits;
- DCDF compatibility commits;
- unrelated local branch history.

Only `review/dcdf-mar-deprecation-and-replacement-skill-20260709/` belongs in
the review commit.

## Limitations

- Local refs are evidence but are not remotely reproducible until explicitly
  published.
- The installed skill is outside this repo and is compared only by hash/content
  observed on this machine.
- Archived tasks are sampled by historical significance; raw transcripts are
  not committed.
- Queue directories show no records, but absence does not prove the bridge was
  never exercised elsewhere.
- The linked Pro chat supports narrowing MAR, not full standalone deprecation.
- The owner's usability/model judgment is a product decision, not a controlled
  benchmark.

## Validation Criteria

The packet is valid only if:

- the commit contains review files only;
- public and local MAR state remain distinguished;
- PR #1 and DCDF PR #14 are represented accurately;
- medium-reasoning claims are labeled correctly;
- no replacement implementation is included;
- no private raw transcript or host-specific secret is added.
