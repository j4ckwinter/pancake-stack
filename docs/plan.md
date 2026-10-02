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

Architecture prototypes are skipped because this phase has no runtime logic or function boundaries. Adversarial design review is skipped because no design is contested. Commit, rebase, and PR work are skipped because this directory has no Git repository or publication request.

Full JSON Schema validation and installation in VS Code remain unverified. Repository checks do not prove host installation.

Future phases implement setup and rigorous workflows, verify host invocation syntax, and prepare public distribution. Model availability stays a host concern. A distribution source and license still need selection before public release.
