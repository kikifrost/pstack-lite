# Design checks

- Does the caller perform one domain operation, or coordinate internal stages and invariants?
- Does the interface hide substantial policy or complexity, or add a pass-through layer?
- Are storage representations, transport details, and framework objects contained at their owning boundary?
- Does each mutable state have a clear owner and lifecycle, including retries, restarts, and multiple workers?
- Are repeated invalid combinations better represented by a type, state machine, or registry?
- Are abstractions justified by current callers rather than hypothetical extensions?
- Can authorized internal callers migrate together without leaving duplicate paths? Preserve stable public interfaces unless changing them is authorized.
- Can a contributor make the ordinary correct change from the local module, or must they synchronize hidden lists and shared assumptions? Prefer one authoritative list or an enforced consistency check.

For a consequential choice, record the caller's usage, recommended shape, concrete alternative, accepted tradeoff, migration effect, and verification. A sketch can remain in the conversation unless the user requests a saved artifact.
