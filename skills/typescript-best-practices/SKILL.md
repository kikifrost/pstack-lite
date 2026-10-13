---
name: typescript-best-practices
description: "Use when explicitly requested as typescript-best-practices to improve TypeScript domain models, boundary parsing, and type safety in a concrete frontend change."
metadata:
  source: "cursor/plugins/pstack"
  adaptation: "Codex curated workflows"
---

# Model TypeScript data without hiding invalid states

Read the applicable design and repository instructions, the current types, and the existing package scripts before proposing changes.

- Use discriminated unions when several booleans and optional fields permit contradictory lifecycle states. Keep a simple type when its operations already handle every value.
- Parse external data as unknown at the boundary with existing validation code or the repository's schema library. Derive types from the authoritative schema where possible. Do not add a dependency for a single guard by default.
- Prefer narrowing and satisfies over casts that silence uncertainty. A guard must check every property it claims. Use a justified assertion only when validation or an unavoidable library boundary establishes the invariant.
- Use never for exhaustive handling of meaningful variants. Do not hide a new state behind a silent fallback.
- Add branded IDs or non-empty collections only when they prevent a demonstrated confusion or partial operation. Preserve local naming conventions; do not refactor every primitive into a brand.
- Keep API response and frontend route contracts stable. Types should describe the approved contract, not change it implicitly.
- Keep state and lifetime ownership clear. Model loading, queued, running, failed, and complete according to actual persisted behavior when these states exist; enqueue success is not completion.

Read [Patterns](references/patterns.md) for examples only when useful. Validate with the relevant existing test, typecheck, lint, or build script. Test observable behavior when runtime semantics change, without creating tests that merely repeat type declarations. An interaction-flow change still needs the project's required confirmation.
