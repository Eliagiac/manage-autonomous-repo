# Agentic Orchestration Landscape

Use this reference when updating the skill or designing a product-level orchestration plan.

## Patterns to borrow

- Branch-visible autonomous coding: agents should produce reviewable branches, diffs, logs, and PR-ready outputs.
- Worktree isolation: use separate worktrees for independent branches when multiple agents write code.
- Project-local subagents: keep reusable agent definitions in the repo when the project depends on them, and version-control those definitions with the source they operate on.
- Orchestrator-worker: orchestrator breaks down work, workers own slices, orchestrator synthesizes and integrates.
- Parallelization for confidence: independent scouts can analyze different risks or run A/B alternatives.
- Team termination: define stop/continue/completion conditions explicitly.
- Manager/crew metrics: record token/cost, branches, artifacts, and integration outcomes.
- Prompt-cache economics: stable instructions first, variable task context last.

## Sources to re-check when changing permanent policy

- OpenAI Codex subagents: https://developers.openai.com/codex/subagents
- GitHub Copilot cloud agent: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
- Git worktree: https://git-scm.com/docs/git-worktree
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- LangGraph workflows and agents: https://docs.langchain.com/oss/python/langgraph/workflows-agents
- AutoGen teams: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
- CrewAI crews: https://docs.crewai.com/en/concepts/crews
- OpenHands overview: https://docs.openhands.dev/overview/introduction
- OpenAI prompt caching: https://developers.openai.com/api/docs/guides/prompt-caching

## Translation into repo practice

- Use branches and worktrees as the unit of risky implementation.
- Prefer Git worktrees over ad hoc directory copies for parallel branch isolation.
- Use docs and task cards as the unit of durable intent.
- Use reports, tests, logs, and demos as the unit of proof.
- Use integration branches as the unit of synthesis.
- Use evidence status taxonomy to prevent parked/negative routes from being retried.
- Treat parallel subagents as useful but not free: record why the batch size was worth the extra model cost, and prefer cheaper read-only workers before expensive implementation or synthesis workers.
