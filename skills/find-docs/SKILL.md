---
name: find-docs
description: Use when a task depends on current library, framework, SDK, CLI, or cloud-service behavior that must be verified from installed or official documentation.
---

# Documentation Lookup

Resolve version-sensitive technical questions from the strongest available
primary source instead of model memory.

## Source Order

1. Inspect the repository's lockfile, package manifest, generated types,
   installed source, and local documentation to identify the actual version.
2. Read bundled framework documentation when it exists.
3. Use an official documentation connector or official product website.
4. Use an official source repository, release notes, or specification.
5. Use Context7 only as an optional discovery aid when it is already available;
   verify material claims against the official source.

Do not install a global tool merely to answer one question. Do not send secrets,
private code, customer data, or proprietary identifiers to a documentation
service.

## Workflow

1. State the library/product and installed or requested version.
2. Turn the question into one narrow lookup: API signature, configuration,
   migration, error behavior, or supported pattern.
3. Find the exact relevant official page or installed definition.
4. Check whether the answer differs across versions.
5. Apply the result to the repository's current stack and conventions.
6. Cite or link the supporting source when the user benefits from verification.

For debugging, separate framework behavior from repository behavior. Reproduce
the local failure and use documentation to test a hypothesis; documentation
alone is not runtime proof.

## Fallback

If the official source is unavailable:

- try one meaningful alternative such as installed types, release notes, or the
  source repository;
- state what could not be verified;
- label any memory-based answer as potentially stale;
- avoid repeating searches that return the same failure.

Prefer a bounded, evidence-backed answer over a large dump of loosely related
documentation.
