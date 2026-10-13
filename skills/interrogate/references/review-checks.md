# Review checks

Apply only lenses relevant to the change. A finding needs a reachable trigger and consequence, not a preference for another implementation.

## Correctness and lifecycle

Trace empty and boundary inputs, retry and crash behavior, cancellation, status transitions, worker ownership, and concurrency. Confirm that persisted state and runtime behavior agree. Follow error propagation; a fetch failure must not become an apparently successful empty result.

## Contracts and boundaries

Follow actual callers and serialized consumers. Check stable API shapes, CLI options, schemas, and routes. Confirm layer ownership and direction from repository instructions. Look for scattered validation, SQL outside its owner, framework coupling in business logic, and new process-local state shared across requests.

## Verification

Check whether the test exercises the user's observable operation and would detect the stated failure. Use offline fixtures and temporary databases where suitable. Distinguish source reasoning, executed local checks, and CI evidence. New test files must satisfy the repository's registration requirements.

## Complexity

Flag a structural problem only when its cost is concrete. Prefer removing unjustified wrappers, duplicate state, and unnecessary parallel APIs. Do not impose arbitrary file-length thresholds, blanket abstraction bans, or broad cleanup unrelated to the diff.

## Security when affected

Trace actual input to SQL, shell, rendered HTML, or privileged operations. Check authorization, secret handling, and races where the change affects them. Do not invent a generic security checklist for a text-only edit.

## Filter before reporting

Re-read context before accepting a concern. Dismiss impossible inputs, validated upstream states, conventional patterns without a defect, and optional redesigns presented as blockers. A single well-supported defect is actionable without reviewer consensus. There is no finding quota.
