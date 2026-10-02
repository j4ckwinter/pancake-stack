# Technical writing

Read this when drafting or editing technical documentation. Apply sift's substance and clarity rules throughout. Keep the requested audience, repository conventions, and edit scope.

## Choose what the reader needs

Identify the reader's goal and assumed knowledge. Choose the dominant purpose of the document or section:

- A tutorial teaches through a bounded exercise. State what the learner will build, include necessary prerequisites, and give visible checkpoints. Keep background brief and link deeper explanations.
- A task guide helps a competent reader achieve an outcome. Order steps by dependency, put conditions before the affected actions, and include expected results or relevant recovery paths. Avoid teaching unrelated concepts.
- Reference material supports lookup. Organize facts around the actual interface, configuration, or data shape. Describe supported values, defaults, constraints, and errors consistently. Preserve uncertainty where facts are unverified.
- An explanation builds understanding. Define a bounded question, explain the mechanism and constraints, and distinguish documented rationale from inference. Include alternatives when they explain the decision.

A README can serve several purposes. Use clear sections or links when that helps readers find the relevant material. Do not split files or impose a fixed template merely to classify the content. Short updates, PR descriptions, and commit messages need a clear purpose rather than one of these document structures.

## Make instructions executable and claims traceable

Use actual commands, symbols, paths, and interface labels. State the working directory or prerequisites when needed to run a command correctly. Distinguish literal input, placeholders, and expected output. Explain consequential side effects before the action. Do not present proposed host commands or untested examples as confirmed behavior.

Keep terminology consistent. Place conditions and words such as "only" beside the action they qualify. Replace ambiguous pronouns and long noun strings with explicit relationships. Keep grammatical words that prevent ambiguity. Follow the repository's code-block language and formatting conventions rather than imposing a universal indentation style.

For factual documentation changes, check relevant implementation, contracts, and existing evidence within the authorized scope. Exercise examples when practical and permitted. State untested examples or unavailable checks honestly. A prose-only rewrite preserves existing claims without presenting them as freshly verified; do not turn it into an unrelated investigation.

## Return a useful document

Check whether the reader can find the intended action or answer, follow the dependencies, and recognize success or remaining uncertainty. Keep requested detail and existing useful links. Cut repetitions and digressions without deleting essential prerequisites or caveats. Return or edit the requested text; do not create additional documentation, reorganize the repository, or change product behavior without authorization.
