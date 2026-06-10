# Branch and Worktree Run

Use this prompt when a repo has several independent implementation tracks:

```text
[$manage-autonomous-repo](C:\Users\<you>\.codex\skills\manage-autonomous-repo\SKILL.md)
Use subagents as per skill instructions.

Split the current roadmap into independent implementation, testing, documentation, and demo tracks. Use branches or worktrees for disjoint write scopes. Keep the orchestrator on integration and conflict prevention.
```

Expected behavior:

- The orchestrator creates a portfolio before choosing local work.
- Workers get explicit owned scopes and avoid scopes.
- Branches or worktrees isolate independent write tasks.
- Returned work is merged one branch at a time through an integration branch.
