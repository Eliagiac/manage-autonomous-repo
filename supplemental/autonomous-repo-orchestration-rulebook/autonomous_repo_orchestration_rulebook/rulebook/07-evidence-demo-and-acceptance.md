# 07 — Evidence, Demo, and Acceptance

## Principle

Plans, requests, contracts, and smoke tests are not acceptance evidence. They are useful only when their status is explicit and they lead to implementation, execution, parking, or rejection.

## Evidence taxonomy

| Status | Meaning | Can support acceptance? |
| --- | --- | --- |
| `plan` | proposed route | No |
| `request` | instruction for later execution | No |
| `contract` | schema/provenance/handoff requirement | Only as a gate |
| `readiness` | checks execution eligibility | Only as a gate |
| `smoke` | small proof of path viability | Rarely; only if milestone says so |
| `diagnostic` | measures or classifies behavior | Routes future work |
| `execution` | real command run with retained output | Only with required QC/gates |
| `demo` | human/operator-visible output | Only with matching QC/gates |
| `visual_qc` | independent review of exact demo/media pair | Yes within scope |
| `acceptance` | formal gate result | Yes within scope |
| `parked` | retained but inactive | Prevents repetition |
| `rejected` | negative evidence | Prevents repetition |
| `accepted` | passed the current gate | Yes within stated scope |

## Promotion rule

Evidence moves upward only through a named gate. A detailed plan cannot become execution evidence. A smoke cannot become acceptance because it “looks fine.”

## Artifact identity checklist

Before promoting evidence, verify:

- run id;
- source/input id;
- config and commit/branch;
- command and output path;
- artifact completeness;
- provenance and external workdir identity;
- demo/QC pair matching;
- validation gate versions;
- known negative evidence was checked.

## Demo ladder

Every product-facing milestone should include a demo ladder:

1. **Internal proof** — command/test/report proves feature logic.
2. **Operator proof** — a future agent/human can run the feature from documented commands.
3. **User-facing proof** — screenshot/video/API output/UI flow shows the observable behavior.
4. **Regression proof** — a test or gate prevents silent breakage.
5. **Accepted proof** — milestone acceptance gate passes.

A batch that only modifies internal infrastructure should still say which future demo it unlocks.

## Negative evidence

Negative evidence is valuable. Record it compactly:

```text
Route:
Hypothesis:
Evidence path:
Why it failed:
What it rules out:
What would make it worth retrying:
Date/branch:
```

Do not repeat a rejected route unless the new task card names a materially new hypothesis.

## External evidence

For external repos, models, datasets, runtimes, or large workdirs, require a contract before execution where practical:

- external root;
- upstream URL and commit/version;
- license/provenance status;
- input identity;
- command template;
- expected outputs;
- import/summary script;
- hashes where feasible;
- stop conditions;
- authorization status.

External payloads should enter the main repo through small import/summary manifests, not raw bulk copies into docs.
