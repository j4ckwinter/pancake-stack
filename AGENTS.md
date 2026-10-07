# Contributor instructions

Keep this project focused on Codex and Claude Code plugin foundations and the requested setup, how, wtf, check, fix, tdd, pancake, balls, design, why, verify, handoff, pr, scope, sift, challenge, reflect, recap, and teach skills.

- The setup guide, how, wtf, check, fix, tdd, pancake, balls, design, why, verify, handoff, pr, scope, sift, challenge, reflect, recap, and teach skills are authorized. Do not add other skills, commands, or hooks until requested.
- Use the current official portable plugin contract for `plugin.json` and the documented Codex marketplace format.
- Keep native Claude manifests consistent with the portable package identity. Both hosts use the same skill tree and workflow rules. Delegate settings inherit from the active host unless the task explicitly overrides them.
- Follow the shared values in `skills/pancake/references/values.md`.
- Keep the library declarative. Do not add bundled executable helpers, tests, or evaluation evidence. Keep task settings ephemeral and leave legacy preference files untouched.
- Preserve the absence of global side effects. Do not write user preferences or register a marketplace as part of repository checks.
- Distinguish proposed commands from host commands. Do not claim an alias or installation flow works without testing it on the named host.
- Use Conventional Commits: `type(scope): concise imperative description`. Scope is optional. Describe the actual change, such as `docs: link evaluation references to the hosted repository`.
- Do not select a license, publish, commit, or install the Pancake Stack plugin without authorization.

Validate JSON parsing, marketplace source resolution, and all skills after changes. Use the external evaluator in [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals). With that repository checked out beside this one, run `../pancake-stack-evals/run_checks.py --source .`; its historical helper tests use isolated temporary storage. Tests and evidence belong in that separate repository. Installation remains a separate host check.
