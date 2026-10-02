# Foundation plan

This phase establishes the Codex package and preference contract. It adds no skills or runtime behavior.

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

Future phases implement setup and rigorous workflows, verify host invocation syntax, and prepare public distribution. Model availability stays a host concern. A distribution source and license still need selection before public release.
