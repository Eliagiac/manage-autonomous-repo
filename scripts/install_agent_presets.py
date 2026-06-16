#!/usr/bin/env python3
"""Install Manage Autonomous Repo custom-agent presets into a project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


AGENTS_CONFIG = """[agents]
max_threads = 10
max_depth = 2
"""

AGENT_REGISTRATIONS = [
    ("mar_explorer", "mar-explorer.toml", "Cheap read-only discovery, docs drift checks, test inventory, log digestion, and task-card preparation."),
    ("mar_code_worker", "mar-code-worker.toml", "Cost-efficient branch/worktree implementation for well-scoped code, tests, scripts, fixtures, or docs."),
    ("mar_deep_code_worker", "mar-deep-code-worker.toml", "Higher-reasoning implementation and debugging for cross-module work or subtle integration risk."),
    ("mar_execution_runner", "mar-execution-runner.toml", "Artifact-producing execution lanes for tests, benchmarks, imports, captures, demos, reports, CI/log collection, and QC."),
    ("mar_reviewer", "mar-reviewer.toml", "Read-only review for correctness, maintainability, security/privacy, performance, docs/test, and integration risk."),
    ("mar_program_auditor", "mar-program-auditor.toml", "Read-only product-program audit for milestone gates, portfolio balance, completion status, and cost/parallelization drift."),
    ("mar_senior_synthesizer", "mar-senior-synthesizer.toml", "Rare senior synthesis for architecture, roadmap, conflict, or ambiguous product-state decisions."),
]


def copy_presets(skill_dir: Path, project_dir: Path, overwrite: bool) -> list[str]:
    source_dir = skill_dir / "assets" / "agents"
    target_dir = project_dir / ".codex" / "agents"
    target_dir.mkdir(parents=True, exist_ok=True)

    actions: list[str] = []
    for source in sorted(source_dir.glob("*.toml")):
        target = target_dir / source.name
        if target.exists() and not overwrite:
            actions.append(f"kept existing {target}")
            continue
        shutil.copy2(source, target)
        actions.append(f"copied {source.name} -> {target}")
    return actions


def ensure_agent_config(project_dir: Path) -> str:
    config_path = project_dir / ".codex" / "config.toml"
    config_path.parent.mkdir(parents=True, exist_ok=True)

    if not config_path.exists():
        config_path.write_text(AGENTS_CONFIG + "\n" + agent_registration_text(), encoding="utf-8")
        return f"created {config_path} with agents.max_threads=10, agents.max_depth=2, and preset registrations"

    text = config_path.read_text(encoding="utf-8")
    if "[agents]" not in text:
        separator = "" if text.endswith("\n") or not text else "\n"
        text = text + separator + "\n" + AGENTS_CONFIG
        changed = True
        lines = text.splitlines()
    else:
        changed = False
        lines = text.splitlines()

    start = next(i for i, line in enumerate(lines) if line.strip() == "[agents]")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            end = i
            break

    block = "\n".join(lines[start:end])
    insert_at = end
    if "max_threads" not in block:
        lines.insert(insert_at, "max_threads = 10")
        insert_at += 1
        changed = True
    if "max_depth" not in block:
        lines.insert(insert_at, "max_depth = 2")
        changed = True

    existing_sections = {line.strip() for line in lines if line.strip().startswith("[agents.") and line.strip().endswith("]")}
    missing = [(name, filename, description) for name, filename, description in AGENT_REGISTRATIONS if f"[agents.{name}]" not in existing_sections]
    if missing:
        lines.append("")
        lines.extend(agent_registration_lines(missing))
        changed = True

    if changed:
        config_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        details = "updated missing [agents] settings"
        if missing:
            details += f" and {len(missing)} preset registration(s)"
        return f"{details} in {config_path}"
    return f"kept existing [agents] settings and preset registrations in {config_path}"


def agent_registration_text() -> str:
    return "\n".join(agent_registration_lines(AGENT_REGISTRATIONS)) + "\n"


def agent_registration_lines(registrations: list[tuple[str, str, str]]) -> list[str]:
    lines: list[str] = []
    for name, filename, description in registrations:
        if lines:
            lines.append("")
        lines.extend(
            [
                f"[agents.{name}]",
                f'description = "{description}"',
                f'config_file = "./agents/{filename}"',
            ]
        )
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path, help="Repository/project root where .codex/agents should be created.")
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Manage Autonomous Repo skill directory. Defaults to this script's parent skill.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing project agent preset files.")
    parser.add_argument(
        "--write-config",
        action="store_true",
        help="Create or update .codex/config.toml with agents.max_threads=10, agents.max_depth=2, and named preset registrations when missing.",
    )
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    skill_dir = args.skill_dir.resolve()
    if not project_dir.exists():
        raise SystemExit(f"Project directory does not exist: {project_dir}")
    if not (skill_dir / "assets" / "agents").exists():
        raise SystemExit(f"Skill agent presets not found under: {skill_dir}")

    for action in copy_presets(skill_dir, project_dir, args.overwrite):
        print(action)
    if args.write_config:
        print(ensure_agent_config(project_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
