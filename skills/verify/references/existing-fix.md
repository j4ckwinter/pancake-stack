# Verify an existing fix

Use this for a named PR, commit, or patch that is claimed to resolve a defect. Identify the reported scenario, expected behavior, and concrete artifact. A tracker status or claim of resolution is not a substitute for inspecting the change. Verification does not authorize a competing repair.

Resolve exact baseline and patched revisions, including relevant uncommitted changes. Choose a baseline that represents the reported behavior before the fix; do not assume a moving branch name identifies it. If several changes are bundled, distinguish evidence that the patched artifact resolves the symptom from evidence attributing that result to one change.

Use isolated checkouts or the project's existing comparison harness. Preserve user edits and keep mutable data separate. Record the build, configuration, dependency, and data inputs needed to compare results. If a migration prevents identical inputs, describe the difference and its effect on the conclusion.

Exercise the reported scenario through the relevant supported interface on the baseline, then on the patched artifact. Check both the absence of the original failure and the presence of the expected result. A check that avoids the action entirely does not prove a fix. Reset state between attempts and choose repetitions based on observed intermittency; no fixed run count proves a nondeterministic failure absent.

Report one of these outcomes with the observations supporting it:

- Confirmed for the exercised scenario: the baseline exhibits the defect and the patched artifact produces the expected result under comparable conditions.
- Insufficient fix: the reported defect persists on the patched artifact.
- Inconclusive: the baseline does not reproduce, either artifact cannot be exercised, or environmental differences prevent the comparison. Report any useful patched-build result separately without calling the causal claim proven.

Retain evidence tied to both artifacts and apply Verify's cleanup requirements. Report product failures without editing the fix, opening another PR, or posting external updates unless those actions were separately requested.
