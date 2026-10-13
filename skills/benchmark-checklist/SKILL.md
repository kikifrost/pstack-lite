---
name: benchmark-checklist
description: "Use when explicitly requested as benchmark-checklist to validate a measured speedup, slowdown, throughput, or latency comparison."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Verify a performance claim

Write the proposed claim with its metric, unit, data size, and environment before interpreting the result. Read the measurement script and establish what it times, counts, and excludes.

- Confirm the work happened inside the timed region. Await promises, consume generators, and check stored rows, returned values, or bytes processed.
- Count failures, timeouts, and retries. Compare correct outputs; fast rejection is not faster success.
- Make the sides comparable. Match runtime versions, builds, realistic settings, dataset, warmup, cache conditions, and concurrency. State configuration differences instead of calling them implementation wins.
- Identify the limiting resource using a separate profiling run when needed. Check the load generator as well as the target. Do not include profiling overhead in reported timings.
- Check physical and arithmetic limits. Saving a small share of the total cannot produce an unexplained large end-to-end gain.
- For a substantive comparison, alternate both sides across at least five runs where practical. Report median and range, or the existing harness's uncertainty estimate. A single requested ballpark is permitted when labeled as such.
- Measure the end-to-end path that matters to the user when a microbenchmark is being used to justify a product claim.

Use local fixtures or disposable databases rather than real user data. Do not install profilers or load-test production by default. Keep the outcome inconclusive if missing evidence could reverse the conclusion. Report measured behavior, environmental limits, and inference separately.
