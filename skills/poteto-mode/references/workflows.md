# Task workflows

Read only the section matching the actual request. Steps describe outcomes, not mandatory tool calls or a fixed number of agents.

## Investigation

Anchor the question to current code and docs. Trace behavior for a how question, history for a why question. Return supported findings and meaningful gaps. Do not implement an exploratory suggestion without authorization.

## Bug fix

Reproduce the observable failure with an existing local flow or fixture. Trace the mechanism and rule out competing hypotheses with evidence. Implement the smallest root-cause fix. Add a regression test when the failure is reproducible, following the repository's implementation-before-test convention. Verify the original trigger and affected integration path, not just compilation. If the original surface is unavailable, state what the local proof establishes and what remains unverified.

## Feature

Identify the user's operation, success criteria, and existing contract. Choose the data model and state owner before adding logic. Implement in the established layer, synchronize affected callers and current docs, then run scope-appropriate checks. Get required approval before changing a protected public contract, interaction flow, or architecture boundary. Do not automatically open a PR.

## Refactoring

Identify behavior that must remain unchanged and the complexity the restructure removes. Reuse existing behavior checks; add characterization coverage only where there is a material gap. Move in small steps and migrate all authorized internal callers. Check indirect references in strings, config, and docs. Preserve external compatibility unless the task authorizes changing it. Verify behavior and boundaries, not only lint.

## Performance

Use a representative local dataset and reproducible measurement. Establish a baseline, identify the limiting resource, form a hypothesis, and measure the proposed change. Consult benchmark-checklist before reporting a comparison. Keep only changes supported by correct results and a meaningful measured improvement; explain inconclusive outcomes.

## Review

Use interrogate for requested review and blast-radius when hidden consumers or invariants determine safety. Reviews do not implicitly authorize fixes or external comments.

## Documentation or planning

Read current implementation and applicable docs, then produce the requested artifact at the requested destination. Use technical-writing when useful. A plan describes ordered work and validation without starting implementation.
