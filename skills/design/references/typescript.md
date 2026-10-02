# TypeScript design guidance

Use when TypeScript data shapes or boundary handling materially affect the requested design or implementation. Follow repository conventions, compiler configuration, installed TypeScript version, and existing schema libraries. Do not migrate languages, add dependencies, or change compiler flags merely to apply this reference.

Model meaningful alternatives with discriminated unions when callers need different fields or behavior for each state. Optional properties are appropriate for genuinely optional data; avoid combinations that admit contradictory states. Use exhaustive handling where adding a variant should require caller changes. Introduce branded identifiers or stronger collection types only when they prevent an observed domain mistake or express a real API requirement.

Treat untrusted JSON, configuration, and persisted values as unknown until the owning boundary validates them. Reuse the project's runtime parser and derive types from its schema when possible. A type assertion, non-null assertion, or user-defined type predicate does not itself validate a value. Check that predicates establish every invariant they claim. Keep assertions justified by an inspected invariant narrow and explicit rather than banning all assertions or hiding them in wrappers.

Prefer inference and reuse authoritative types when they describe the intended contract. Use utility types to express actual relationships; avoid deriving a public domain contract from incidental implementation details. Use satisfies for compile-time compatibility checks when supported and useful, while remembering that it performs no runtime validation. Preserve intentional public type boundaries and avoid a utility-type puzzle that is harder to read than a small named shape.

Choose function arguments from caller usage. An options object can clarify several independent settings; a simple positional argument can remain clear. Do not impose one signature style everywhere. Keep framework and transport details at the relevant boundary and avoid unnecessary wrappers.

Check the requested behavior with the project's existing compiler and behavioral harness. Type checking covers static contracts, not runtime input validity, concurrency, or user-facing behavior. Include relevant invalid inputs and valid variants when testing boundary changes. Use the installed version's supported features, and report unavailable checks without installing tooling or weakening types to obtain a pass.
