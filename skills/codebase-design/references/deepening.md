# Deepening Modules

Use this reference when a refactor crosses dependencies or needs a testable
seam.

## Dependency Categories

### In-process

Pure computation or in-memory state can usually stay behind the module
interface. Test it through the public behavior without an adapter.

### Local substitutable

For databases, filesystems, queues, or clocks with faithful local stand-ins,
keep the stand-in behind the same internal seam. Prefer a real lightweight
implementation over mocks when it preserves production semantics.

### Remote but owned

For services the team owns, define a narrow port around the behavior the module
needs. Use the production transport as one adapter and an in-memory or local
adapter for tests. Keep retries, serialization, and transport errors at the
edge.

### External service

For third-party APIs, inject a narrow client or port. Contract-test the real
adapter when feasible and use a controlled fake for deterministic tests. Never
let vendor types spread through the core model without a reason.

## Seam Checks

- Does more than one real implementation or test mode justify the seam?
- Can callers use the module without knowing transport, storage, or sequencing
  details?
- Are invariants and error modes explicit?
- Does the interface reduce the number of places changed for a common feature?
- Can tests assert behavior without reaching into internal state?

## Migration

1. Characterize existing behavior at the current public boundary.
2. Introduce the new interface beside the old one when compatibility is needed.
3. Move one representative caller and prove the behavior.
4. Migrate remaining callers in small batches.
5. Remove the old interface only after usage and compatibility checks.
6. Re-run repository-wide tests and inspect the final dependency graph.
