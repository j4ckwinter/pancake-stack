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

Read [performance guidance](experiments-performance.md) for this experiment.

### Prototype

Read [prototype guidance](experiments-prototype.md) for this experiment.

### Skill evaluation

Read [skill evaluation guidance](experiments-skill-evaluation.md) for this experiment.

## Decide and clean up

Report baseline and resulting observations, the comparison method, correctness checks, and limitations. Distinguish a supported improvement, a rejected hypothesis, and an inconclusive result. Preserve enough evidence to inspect the decision without retaining secrets or unrelated data.

For a numerical claim, include units, successful-work and failure counts, sample count and spread where relevant, and the conditions and limiting mechanism that support its interpretation. Do not turn an observed difference into a causal claim without evidence that distinguishes alternative explanations.

Remove or revert only experimental changes and resources owned by the run, preserving unrelated work and useful evidence. Do not use broad reset or cleanup commands. If a candidate change was made in the working tree, inspect the diff before removing it. Keep accepted production changes only within authorized implementation scope, then review and verify them through [the implementation sequence](implementation.md). Do not commit them without authorization.
