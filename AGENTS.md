# Contributor instructions

Keep this project focused on Codex and Claude Code plugin foundations and the requested setup, how, wtf, check, fix, tdd, pancake, balls, design, why, verify, handoff, pr, scope, sift, challenge, reflect, recap, and teach skills.

- The setup helpers, how, wtf, check, fix, tdd, pancake, balls, design, why, verify, handoff, pr, scope, sift, challenge, reflect, recap, and teach skills are authorized. Do not add other skills, commands, or hooks until requested.
- Use the current official portable plugin contract for `plugin.json` and the documented Codex marketplace format.
- Keep native Claude manifests consistent with the portable package identity. Both hosts use the same skill tree and workflow rules. Keep provider preferences separate.
- Follow the shared values in `skills/pancake/references/values.md`.
- Keep preference examples and their contract consistent.
- Preserve the absence of global side effects. Do not write user preferences or register a marketplace as part of repository checks.
- Distinguish proposed commands from host commands. Do not claim an alias or installation flow works without testing it on the named host.
- Use concise imperative commit subjects that describe the actual change, such as `Add structural-quality design and review guidance`.
- Do not select a license, publish, or commit without authorization.

Validate JSON parsing, marketplace source resolution, and all skills after changes. Run the preference helper tests in isolated temporary storage. Installation remains a separate host check.
