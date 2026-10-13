# TypeScript patterns

Use the existing project's names and conventions. These examples illustrate modeling choices, not mandatory rewrites.

## Lifecycle variants

```ts
type RunState =
  | { kind: "queued"; id: string }
  | { kind: "running"; id: string; startedAt: string }
  | { kind: "complete"; id: string; count: number }
  | { kind: "failed"; id: string; error: string };
```

Use a discriminated union only when these variants reflect the actual contract. A frontend type cannot establish that a worker has started.

## Total operations

```ts
function first<T>(items: readonly T[]): T | undefined {
  return items[0];
}

type NonEmpty<T> = readonly [T, ...T[]];
function requiredFirst<T>(items: NonEmpty<T>): T {
  return items[0];
}
```

Choose the signature the domain needs. An empty array can be valid; do not invent a non-empty requirement.

## Truthful validation

```ts
type ApiError = { error: string };
function isApiError(value: unknown): value is ApiError {
  return typeof value === "object" && value !== null &&
    "error" in value && typeof value.error === "string";
}
```

When an existing schema library owns validation, reuse that schema and its inferred type instead of maintaining a duplicate guard. Keep unknown data at the parsing boundary.

## Exhaustive handling

```ts
function label(state: RunState): string {
  switch (state.kind) {
    case "queued": return "Queued";
    case "running": return "Running";
    case "complete": return "Complete";
    case "failed": return "Failed";
    default: {
      const unreachable: never = state;
      return unreachable;
    }
  }
}
```

For value constraints, prefer satisfies when it verifies the shape without an assertion. Brand a primitive only when validated construction prevents a real mix-up; a type assertion alone is not runtime validation. A start-plus-duration representation still needs validation of a non-negative duration at its boundary.
