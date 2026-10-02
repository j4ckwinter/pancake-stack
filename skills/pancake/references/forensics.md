# Diagnose runtime signals and captured traces

Read this for a requested diagnosis of CPU activity, memory growth, stalls, or runtime glitches from a running application or supplied capture. The deliverable is an evidence-backed diagnosis. Repair follows only when requested, using the implementation or experiment guidance as appropriate.

## Establish the evidence

Identify the symptom, relevant workload, application version, environment, and capture interval. Inspect the supplied artifact's format, completeness, and available symbols before choosing a supported parser or viewer. Use existing tools; do not require a database conversion or new parser when a focused query suffices. Keep large outputs bounded to relevant threads, events, frames, or objects.

For a supplied capture, analyze that dataset first. Do not assume it represents current code or recreate the workload without a reason and authorization. For a live symptom, use the matching surface and capture a relevant signal with available host capabilities. Profiling can perturb behavior; record material observation limits. A diagnosis request does not authorize hotpatching code, injecting scripts, restarting shared services, or changing global settings. Use existing read-only telemetry where possible and obtain missing authorization before intrusive instrumentation.

## Narrow and attribute

For CPU activity, distinguish elapsed time from sampled CPU time and inclusive from self time. Follow expensive frames and callers in the affected interval. For stalls, inspect thread or task state, wait reasons, and the dependency holding progress. For memory growth, distinguish allocation rate from retained memory; follow reachable objects and retention paths across comparable snapshots where available. High allocation alone does not prove a leak. For visual glitches, relate event timing to observed frames and state rather than guessing from source.

Map the narrowed signal to the relevant build's symbols and source. Cite artifact locations and inspected implementation. A hot frame, retained object, or temporal correlation is evidence, not automatically the root cause. Separate observations, the mechanism they suggest, and competing explanations. Missing symbols or capture coverage remain explicit limits; never invent a source line.

## Confirm within scope

Seek a distinguishing observation for the proposed mechanism. Use relevant existing telemetry, comparable paired captures, or an authorized targeted experiment. A paired capture supports causality only when the workload and changed conditions justify the comparison. Distinguish a confirmed mechanism from the strongest supported hypothesis. Source inspection can explain a trace but cannot replace absent runtime evidence.

Report the signal, reduced finding, source attribution, artifact location, confirmation performed, and remaining uncertainty. State the cheapest useful next check when the evidence is inconclusive. Do not label a fix complete or change files merely to finish a diagnosis. If repair is also authorized, carry the evidence into the implementation sequence and repeat the relevant scenario after correction.
