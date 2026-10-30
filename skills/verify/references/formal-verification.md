# Model and formal verification

Use this optional guidance when the user explicitly requests model checking, formal verification, or maintenance of an existing model or proof. Follow [recipe maintenance](maintenance.md) for audit and edit boundaries. Routine verification does not require a model, proof, or new toolchain.

## Choose the claim and method

Identify a concrete property from the intended contract and the code that implements it. State the prohibited outcome or required progress, including when it must hold. Choose a method suited to that property, the implementation, and available evidence. Prefer existing project tooling and models; explain any proposed addition and its limits before relying on it. No particular language, solver, or framework is required. If tooling is unavailable, report the unexecuted check rather than presenting a proposed proof as evidence.

Map model state, transitions, and assertions to implementation symbols and observable behavior. Explain which code steps each transition combines and why treating them as atomic is justified. Include relevant interleavings, failures, retries, and external interactions, or name their omission. A model that assumes away the suspected race cannot establish its absence.

Record assumptions and bounds: initial states, input domains, participant counts, queue sizes, exploration depth, scheduling or fairness, and environmental guarantees as applicable. Distinguish exhaustive exploration within those bounds from an unbounded proof. State abstractions and the argument connecting them to the implementation; a property proved only for an abstract model does not by itself prove the running product correct.

## Check the check

Run the stated property with recorded tool versions, configuration, commands, and outcomes. Distinguish a completed proof or exploration from timeout, incomplete search, unsupported features, and tool failure. A run with no reported counterexample may still be inconclusive. Check that the property is reachable and meaningful under its assumptions, rather than passing because the triggering condition is excluded.

Where authorized, use an isolated workspace for a known broken variant or negative control that should violate the property. Confirm the checker detects the expected failure and retain enough evidence to identify it. Do not mutate shared or product state to demonstrate sensitivity. If a control cannot be run, state that limitation.

For a counterexample, preserve the trace and replay its relevant steps against the implementation through an appropriate test or supported interface when feasible. Record the code state and observed outcome. If replay is unavailable or the trace relies on an abstraction, describe the remaining gap; a model trace alone is not a confirmed product defect.

## Maintain the connection to code

Before updating a model or expectation, classify the discrepancy using source, contract, and execution evidence. Model drift means the representation no longer matches the supported implementation. A product bug means the implementation violates the intended contract. An intended contract change needs supporting requirements or an explicit decision. If the evidence cannot distinguish these, preserve the discrepancy and report the missing decision.

Repair only authorized model or recipe drift and rerun affected checks. Never weaken a property or change assumptions merely to pass, or silently repair product code. Record the last checked implementation revision, relevant dirty changes, model state, assumptions, results, and replay evidence so later readers can identify exactly what was checked. Leave unsupported claims and stale evidence explicitly unverified.
