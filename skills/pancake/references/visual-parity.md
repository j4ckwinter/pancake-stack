# Verify visual parity

Read this when matching an existing interface or preserving appearance during an authorized migration. Establish the reference, required states, and acceptance criteria before changing the implementation. A redesign needs its own criteria; it cannot claim parity by replacing the reference.

## Capture comparable states

Use supplied reference images or capture the current interface through an available supported harness. Record the viewport, device scale, theme, fonts, data, interaction state, and relevant application version. Include the states implicated by the task, such as loading, empty, error, focus, and responsive layouts. Do not imply that one screenshot covers the whole interface.

Keep reference images separate from candidate captures. Wait for stable rendering and use deterministic fixtures where available. If animation, timestamps, or other dynamic regions prevent comparison, establish a justified stabilization or mask before judging candidates and retain the original evidence. Do not mask the changed region or alter a baseline merely to hide a regression.

## Compare and diagnose

Compare equivalent states with existing image-diff tools when available. Inspect the rendered images alongside differences for layout, typography, spacing, color, clipping, and interaction-state mistakes. Pixel differences locate discrepancies; a count alone does not explain their cause or user impact. A visual match does not prove behavior or accessibility.

For an exact-match request, require the agreed exact comparison under matching capture conditions. Distinguish capture noise from product differences using repeated stable captures or known rendering differences. Do not quietly replace exactness with a tolerance. For broader visual equivalence, agree or state the applicable criteria before comparison and explain material deviations. Do not invent a universal acceptable pixel threshold.

Correct mismatches within authorized implementation scope, then recapture and compare the affected states. Changes to shared styles or primitives warrant checks of affected consumers. Keep useful reference evidence and inspect the diff for behavior changes. If tools, fonts, or reference conditions are unavailable, name the limitation rather than claiming parity from source inspection.

## Report coverage

Report the reference and candidate artifacts, capture conditions, states compared, comparison method, observed discrepancies, and remaining gaps. Distinguish verified states from untested ones. Use the implementation sequence for authorized corrections and verification guidance for behavior and accessibility checks appropriate to the change. Preserve unrelated work and clean up only resources owned by the task. This reference does not authorize installing tooling, updating baselines, committing, or publishing.
