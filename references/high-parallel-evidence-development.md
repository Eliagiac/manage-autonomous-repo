# High-Parallel Evidence Development

Use this reference for repositories where progress depends on many evidence artifacts, external workdirs, stacked branches, command runs, demos, and acceptance gates. It complements `subagent-playbook.md` and `source-control-and-github.md`.

## 1. Evidence status taxonomy

Classify every artifact before using it.

| Status | Meaning | May influence acceptance? |
| --- | --- | --- |
| `plan` | Proposed direction or sequence. | No. |
| `request` | A bounded instruction for future execution. | No. |
| `contract` | Schema, input/output, provenance, or handoff requirement. | No, except as a gate. |
| `readiness` | Checks whether execution is allowed. | No, except as a gate. |
| `smoke` | Small execution proof, often one frame/one command. | No, unless an acceptance gate explicitly allows smoke evidence. |
| `diagnostic` | Measures or classifies behavior. | No, except to route next work. |
| `execution` | Real command run with retained outputs. | Only if paired with required QC/gates. |
| `demo` | Human- or browser-viewable output. | Only with matching source/QC/gates. |
| `visual_qc` | Independent source/render inspection. | Yes, when matched to the exact demo/run. |
| `acceptance` | Formal gate result. | Yes, if all prerequisites pass. |
| `parked` | Retained but not active. | No. |
| `rejected` | Negative evidence. | No, except to prevent repetition. |
| `accepted` | Passed current gate contract. | Yes, within stated scope. |

Rule: an artifact can only move upward through the taxonomy by a named promotion gate. A plan cannot become evidence by being detailed. A smoke cannot become acceptance by looking plausible.

## 2. Promotion gates

Before promoting any evidence, verify:

1. Artifact identity: run id, source id, source frames, config, branch, command, and output paths match.
2. Provenance: external workdir and source-controlled import contract agree.
3. Completeness: all required files exist and are non-empty.
4. Scope: the artifact claims no more than it proves.
5. Visual/source match: demos and QC refer to the same media pair.
6. Runtime/training gates: if relevant, runtime telemetry and learned-training evidence are present.
7. Negative-evidence check: the action is materially different from known parked/rejected paths.

## 3. External workdir contracts

For external repos, models, datasets, renderers, or long-running evidence directories, require a source-controlled contract before execution when practical.

Minimum contract fields:

- external root path;
- upstream repo URL and commit or version;
- license/provenance status;
- model/checkpoint paths and hashes when available;
- source input identity and frame mapping;
- exact command or command template;
- expected output paths;
- import/summary script path;
- stop conditions;
- whether execution is authorized.

External outputs should enter the repo through import/summary manifests, not by copying large raw payloads into `docs/`.

## 4. Resource locks

Every execution or write-heavy task card should list locks.

Common locks:

- `gpu_training`: CUDA/VRAM-bound training or inference.
- `browser_runtime`: headful/headless browser, WebGL/WebGPU, screenshots, runtime telemetry.
- `external_workdir:<name>`: outside-repo dependency or evidence directory.
- `source_payload:<name>`: downloaded/raw media or dataset payload.
- `runs_root:<name>`: large run artifact directory.
- `central_config`: shared config/schema/registry files.
- `acceptance_gate`: source/render/demo/QC acceptance logic.
- `pr_stack:<branch>`: stacked branch or integration target.

Do not dispatch two active writers that share a lock unless the orchestrator explicitly serializes them.

## 5. Branch-stack map

Before assigning branch/worktree writers in an active PR stack, record:

```text
Main/stable branch:
Integration branch:
Active PR branches:
Each branch base:
Each branch head:
Open worktrees:
Submodule state:
Known dirty/untracked state:
Worker branch owners:
Shared files:
Merge order:
```

If this map is unknown, spawn a read-only explorer first.

## 6. Planning-chain stop rules

Planning is useful only when it reduces execution risk. Stop adding plan artifacts when any of these is true:

- A safe implementation task card is already available.
- A safe execution task card is already available.
- The current blocker is external permission, license, model download, missing data, or hardware.
- The plan repeats a known negative route without a materially new hypothesis.
- The next artifact would merely restate an existing contract.

End each planning chain as one of:

- `ready_for_implementation`
- `ready_for_execution`
- `blocked_until_<specific_gate>`
- `parked_negative_or_superseded`
- `rejected_do_not_repeat`

## 7. Parallel evidence batches

For broad evidence work, split by target or artifact type:

- docs/contracts worker;
- implementation worker for each independent module;
- execution worker for each independent target/run;
- visual/QC worker;
- review worker for acceptance/provenance;
- integration worker only if explicitly delegated.

Workers should report artifact paths and verdicts, not transcripts.

## 8. Evidence handoff summary

Every worker handling evidence should return:

```text
Lane:
Branch/worktree:
Status:
Artifacts created or inspected:
Commands run:
Evidence status classification:
Promotion allowed? yes/no and why:
Known negative evidence checked:
Resource locks used:
Risks:
Next action:
```
