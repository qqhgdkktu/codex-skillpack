---
name: codebase-design
description: Use when designing or refactoring module interfaces, choosing seams, reducing pass-through abstractions, or making code easier to test and navigate.
---

# Codebase Design

Design deep modules: small, stable interfaces that hide meaningful behavior.
Use the repository's existing language and architecture; do not impose a new
vocabulary where the code already has a precise one.

## Workflow

1. Inspect the current behavior, callers, tests, failure paths, and recent
   changes in the requested area.
2. State the problem in terms of observable friction: duplicated policy,
   leaky details, pass-through layers, scattered changes, or tests coupled to
   implementation.
3. Identify the current interface and everything callers must know to use it.
4. Apply the deletion test: if removing the abstraction merely moves its
   complexity into every caller, it is earning depth; if complexity disappears,
   it is probably a pass-through.
5. Choose a seam only where behavior or implementation truly varies.
6. Propose the smallest interface that preserves required behavior, error
   modes, ordering, performance, and compatibility.
7. Explain migration risk and a reversible implementation order.
8. Verify through the public interface with focused tests and representative
   callers.

For dependency categories and testing strategy, read
[references/deepening.md](references/deepening.md).

## Design Rules

- Treat an interface as the full caller contract, not only a type signature.
- Prefer fewer entry points with stronger defaults over many thin wrappers.
- Keep policy close to the data and side effects it governs.
- Do not add an adapter for a single implementation unless a real test or
  deployment variant justifies the seam.
- Inject remote or external dependencies at a narrow port; keep transport
  details out of domain logic.
- Test observable outcomes through the interface. Avoid tests that must change
  for internal refactors.
- Preserve existing public contracts unless the user authorizes a breaking
  change.
- Compare at least two materially different interfaces when the trade-off is
  consequential; do not create alternatives for a trivial refactor.

## Output

Return:

1. current friction with repository evidence;
2. proposed interface and seam;
3. what complexity moves behind it;
4. compatibility and migration plan;
5. focused verification.

Do not generate a visual report, edit code, or start a broad refactor unless
the user requested that action.
