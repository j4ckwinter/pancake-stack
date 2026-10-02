# Deliver a verified change

Read this when the user requests merging, releasing, publishing, or deploying a change, or preparing it for delivery. Preparation remains read-only unless edits are requested. Identify which delivery action is authorized; implementation or merge readiness alone does not authorize publication or deployment.

## Establish the delivery target

Resolve the repository, exact revision or artifact, destination, and applicable delivery process from the request and project evidence. Follow repository merge policies, release procedures, and required approvals. Do not infer that “ship” means both merging and production deployment when the context leaves the destination unclear. Complete independent preparation while a required decision remains pending.

Inspect current workspace and remote state before acting. Preserve unrelated work. Prefer existing delivery tools and procedures; do not add a release pipeline or install infrastructure to carry out one delivery. Identify consequential prerequisites such as migrations, compatibility, required configuration, or artifact provenance when implicated by the change.

## Establish a current verdict

Use the implementation review and verification guidance to assess the actual artifact being delivered. Inspect relevant test evidence, required checks, review requirements, and current merge or delivery blockers. Seek independent review for consequential changes when available and permitted; report a direct review accurately when independence is unavailable. Do not imply that a green CI summary proves product behavior or supplies a required human approval.

Tie the verdict to the inspected revision, base, and environment. Recheck when code, base, dependencies, configuration, or artifacts change in a way that could invalidate the evidence. Matching commit messages or an old passing result cannot establish current readiness. When a delivery tool supports a revision guard, use it to avoid acting on a head that changed after inspection. If the state changes or a prerequisite remains unverified, stop the affected action and report what needs checking.

## Deliver in dependency order

For dependent PRs or releases, identify the actual dependency order. Deliver only the verified prefix whose prerequisites are satisfied; a ready descendant cannot bypass an unverified dependency. After each delivery, read back the resulting state and reassess the next item's base, artifact, checks, and requirements. Independent changes need no artificial stack.

Use the authorized merge method and existing repository process. Do not assume squash merging, retarget branches, force-push, bypass protections, or delete branches as incidental cleanup. Reuse existing authorization when it covers a necessary action. Obtain any missing required authorization only after preparing the concrete action and evidence.

Enable auto-merge or equivalent delayed delivery only when requested and supported. Confirm which item is armed and what conditions remain. An armed action is pending, not completed. Use bounded waits with updates when observing delivery; do not create background automation without a request.

For release or deployment, confirm the intended environment and artifact and complete required checks before the write. Respect required approval and stop conditions. Inspect existing rollback or recovery procedures when material to the change; do not assume rollback is possible or execute one without authorization covering it. If an operation fails or its outcome is ambiguous, inspect actual state before retrying to avoid duplicate delivery.

## Confirm and report

Read back the authoritative delivery state. For a merge, confirm the PR's merged state and resulting destination revision. For publication or deployment, confirm the version or artifact and target state through the supported system. Distinguish an accepted request, pending operation, completed delivery, and verified runtime behavior. A successful command alone may establish only request acceptance.

Report what was delivered and where, the resulting revision or version, verification performed, pending actions, and remaining gaps. Link actual PR or delivery records when available. Stop at the requested outcome. Delivery does not authorize unrelated releases, customer messages, or resource cleanup.
