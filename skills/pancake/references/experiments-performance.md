# Performance

Tie each hypothesis to a specific mechanism in the implementation. Change one meaningful factor at a time and measure with the same method. Check relevant behavior and regression constraints alongside the target metric. Retain an optimization only when its benefit exceeds observed noise and its complexity is justified. A correctness regression invalidates a performance win.

Inspect what the measurement tool times, counts, and excludes. Confirm that the intended work completes inside the timed region and produces correct results. Count failures, rejected requests, skipped work, and retries separately from successful work. Lazy operations, unawaited calls, cached results, or fast failures can produce plausible numbers without doing the claimed work.

Compare configurations representative of the intended use, including build mode, batching, indexes, concurrency, and cache state. When choosing between options, do not treat one untuned default as evidence against the option itself. Check machine contention and interleave comparable runs when drift could favor one side. Collect profiling or tracing evidence in separate runs when instrumentation affects timing. Inspect the load generator as well as the measured application before attributing a limit.

Use runtime evidence to identify the resource or code path that limits the result. Check the claimed gain against available bandwidth, cores, and the measured share of work changed. Removing a step that consumes 10% of total time cannot reduce total time by more than 10%. Report end-to-end impact alongside a microbenchmark when the decision concerns user-visible performance. If a missing limiter or an unfair comparison prevents attributing a result, narrow the claim to the observation or report it as inconclusive. A requested single-run estimate remains an estimate, with its work and failure checks reported.

For an iterative improvement request, record each hypothesis, change, measurement, correctness result, and keep-or-reject decision in the conversation or an authorized artifact. Stop at the stated target or limit, when useful hypotheses are exhausted, or when further progress needs unavailable evidence or authorization. Do not relax success criteria to claim completion or require an arbitrary minimum attempt count.

