---
name: spec-driven-development
description: Use when a new project or significant feature needs an explicit objective, scope, constraints, acceptance criteria, and implementation plan before coding.
---

# Spec-Driven Development

Create the smallest specification that removes material ambiguity before
implementation. Do not turn a clear one-file change into a document project.

## When To Write A Spec

Use a spec when the task introduces a new product flow, crosses several
components, changes a public contract, contains unresolved product decisions,
or would be expensive to reverse. Skip it for trivial, fully specified fixes.

## Workflow

1. Inspect the repository, existing behavior, instructions, schemas, tests, and
   relevant documentation before asking questions.
2. State the user-visible outcome and observable success criteria.
3. List material assumptions and open questions. Ask only for user-owned
   decisions that cannot be discovered safely.
4. Define scope and explicit non-goals.
5. Record compatibility, data, security, performance, accessibility, and
   operational constraints that actually apply.
6. Map the smallest implementation slices and verification for each.
7. Save a spec only when the user requested a durable artifact or the
   repository has an established spec location; otherwise present it in chat.
8. Keep the spec aligned when accepted scope or architecture changes.

## Compact Template

```markdown
# [Feature]

## Outcome
[What changes for the user and why.]

## Success criteria
- [Observable condition]

## Scope
- In: [...]
- Out: [...]

## Existing evidence
- [Current behavior, files, APIs, or constraints]

## Decisions and assumptions
- [Decision or assumption, with owner/status]

## Design
- [Interfaces, data flow, states, errors, compatibility]

## Implementation slices
1. [Small vertical slice] — Verify: [...]

## Risks and rollback
- [Risk, mitigation, rollback]
```

## Quality Gate

Before implementation, confirm:

- each success criterion is testable or directly observable;
- open questions are either resolved or explicitly deferred;
- the design follows existing repository patterns;
- authority boundaries and external writes are clear;
- verification covers the changed behavior, not only compilation;
- the plan is small enough to implement incrementally.

Do not claim the spec is approved unless the user or repository process
actually approved it.
