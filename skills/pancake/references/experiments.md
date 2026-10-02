# Run a measured experiment

Read this reference for performance improvements, empirical design decisions, or skill evaluations. Ordinary implementation follows [the implementation sequence](implementation.md). A read-only explanation does not authorize building a prototype or executing an evaluation.

## Frame the question

State the uncertainty, a falsifiable hypothesis, and the observable result that would support or refute it. Choose a realistic workload or task, the metric or decision criteria, and relevant correctness constraints before making changes. Use requested targets and limits. Otherwise choose a proportionate local stopping condition and state it. Do not invent business targets or treat a subjective preference as a measurement.

Use existing tools first. Keep experiments within the authorized scope and host capabilities. Isolate scratch files, application state, and candidate writes from production and unrelated work. Do not install dependencies, spend money, invoke external services, or publish results merely because an experiment would benefit from them. When an essential capability is unavailable, report the gap instead of manufacturing evidence.

## Establish a useful baseline

Observe the current behavior before changing it. Confirm that the workload exercises the symptom or distinguishes the approaches being considered. A measurement that cannot detect a meaningful difference cannot justify a winner.

Keep inputs, environment, build, and measurement method comparable. Record relevant versions and conditions. For noisy timing or stochastic behavior, collect repeated observations and report their spread or an appropriate summary. Distinguish cold and warm runs where that affects the result. Do not declare a gain from a single favorable sample.

## Choose the experiment

### Performance

Tie each hypothesis to a specific mechanism in the implementation. Change one meaningful factor at a time and measure with the same method. Check relevant behavior and regression constraints alongside the target metric. Retain an optimization only when its benefit exceeds observed noise and its complexity is justified. A correctness regression invalidates a performance win.

For an iterative improvement request, record each hypothesis, change, measurement, correctness result, and keep-or-reject decision in the conversation or an authorized artifact. Stop at the stated target or limit, when useful hypotheses are exhausted, or when further progress needs unavailable evidence or authorization. Do not relax success criteria to claim completion or require an arbitrary minimum attempt count.

### Prototype

Build only what can resolve the stated question. Use an isolated scratch location and clearly distinguish the prototype from production code. Compare alternatives under the same conditions when the decision needs them. For visual choices, exercise the relevant interaction and inspect the rendered result; for behavioral choices, capture actual outputs or state changes. Do not infer measured performance from a simplified prototype without accounting for its differences from the real system.

Return the evidence, recommendation, tradeoffs, and scratch location. State which decision remains a user preference. A successful prototype is not authorization to ship or to implement a larger feature.

### Skill evaluation

Use realistic requests and raw task artifacts, with explicit observable success criteria. Evaluate results and relevant side effects rather than required headings, claimed reasoning, or a model's report that it followed instructions. When comparing variants, keep the task and environment constant and isolate each run. Avoid providing the expected answer or suspected defect to the agent being evaluated.

Where available, use independent fresh runs and assess outputs without knowing the model or variant identity. Read actual tool records or generated artifacts when available; do not assume a host transcript path or search unrelated sessions. Record unavailable independence or blinding as a limitation. One successful case does not establish general effectiveness. Use additional cases when variability or the intended coverage warrants them, without turning a focused evaluation into an unrestricted benchmark.

## Decide and clean up

Report baseline and resulting observations, the comparison method, correctness checks, and limitations. Distinguish a supported improvement, a rejected hypothesis, and an inconclusive result. Preserve enough evidence to inspect the decision without retaining secrets or unrelated data.

Remove or revert only experimental changes and resources owned by the run, preserving unrelated work and useful evidence. Do not use broad reset or cleanup commands. If a candidate change was made in the working tree, inspect the diff before removing it. Keep accepted production changes only within authorized implementation scope, then review and verify them through [the implementation sequence](implementation.md). Do not commit them without authorization.
