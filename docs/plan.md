# Foundation plan

The foundation phase established the Codex package and preference contract without skills or runtime behavior. The setup phase below adds the first skill.

## Work completed

- [x] Check official plugin packaging documentation and local Codex CLI help.
- [x] Define the plugin identity, marketplace entry, and proposed preferences object.
- [x] Delegate foundation files to one writer.
- [x] Review the files independently.
- [x] Verify JSON parsing, matching plugin names, marketplace path resolution, the preference example, and absence of skills.

## Throughput checkpoint

- Blocking first steps. Verify the packaging contract before writing metadata.
- Independent workstreams. n/a. The package metadata and documentation need one consistent contract.
- Shared mutable state. One writer owns the foundation files.
- Smallest safe decomposition. One delegated owner writes the files. The lead reviews and checks them.

## Deferred work

Architecture prototypes were skipped because the foundation phase had no runtime logic or function boundaries. Adversarial design review was skipped because no design was contested. Commit, rebase, and PR work were skipped during that phase because the directory did not yet have a Git repository or publication request.

Full JSON Schema validation remains unverified. Local installation passed through the Codex CLI bundled with the VS Code extension. Workflow invocation in the VS Code composer remains unverified. See [installation verification](installation-verification.md).

The setup phase implements preference storage and a conversational setup skill. Future phases implement rigorous workflows, verify live host invocation, and prepare public distribution. Model availability stays a host concern. A distribution source and license still need selection before public release.

## Setup phase

- [x] Compare a conversational setup skill with a terminal wizard.
- [x] Implement the conversational skill and a deterministic Python preference helper.
- [x] Verify public helper behavior with temporary storage.
- [x] Refresh the local plugin and verify backend discovery of `pancake-stack:setup`.
- [ ] Verify live setup invocation in the VS Code composer.
- [ ] Test installation and setup from a clean user environment.

The conversational design keeps model discovery and user choices in Codex. The helper owns validation, inheritance, and atomic persistence. A terminal wizard would duplicate the conversation and still need host model metadata. The selected design therefore uses no interactive terminal wizard.

The throughput checkpoint uses one implementation owner for the skill, helper, tests, and documentation. Read-only design comparisons run independently. The parent reviews the actual diff and reruns isolated checks. Repository verification must not write user preferences or install the updated package. A separate host installation check refreshed version `0.1.0` and verified skill discovery.
