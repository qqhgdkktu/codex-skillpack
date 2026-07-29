---
name: playwright-testing
description: Use when writing, debugging, reviewing, or migrating Playwright tests for end-to-end, API, component, visual, accessibility, or CI workflows.
---

# Playwright Testing

Build reliable Playwright Test suites from user-visible behavior and runtime
evidence. This skill is for test code and test infrastructure, not general web
scraping or browser control.

## Start With The Installed Project

1. Inspect `package.json`, the lockfile, Playwright config, test directories,
   fixtures, and existing commands.
2. Determine the installed `@playwright/test` version. Verify version-sensitive
   APIs against local package types/docs or the matching official release notes.
3. Run the smallest existing test that exercises the target behavior before
   changing code.
4. Preserve the project's runner, package manager, naming, fixtures, reporters,
   browsers, and CI conventions unless the task requires changing them.

## Core Loop

1. Define one observable behavior and its preconditions.
2. Choose the cheapest useful layer: API, component, or end-to-end.
3. Arrange isolated test data and authentication.
4. Use resilient user-facing locators and web-first assertions.
5. Run the narrow test and inspect the first meaningful failure.
6. Use traces, console, network, screenshots, and DOM snapshots to diagnose
   failures; do not guess or hide flakiness with waits.
7. Re-run the narrow test, then the affected suite and configured project
   matrix.

Read [references/writing-tests.md](references/writing-tests.md) for locators,
assertions, fixtures, auth, API, visual, and accessibility patterns.

Read [references/debugging-and-ci.md](references/debugging-and-ci.md) for trace
analysis, retries, CI artifacts, sharding, and failure triage.

Read [references/migration.md](references/migration.md) only when migrating from
Cypress or Selenium/WebDriver.

## Invariants

- Test applications the user owns or is authorized to test.
- Verify user-visible behavior; avoid implementation-detail selectors.
- Keep tests isolated and safe to run in any order.
- Prefer `getByRole`, `getByLabel`, `getByText`, and explicit test IDs over
  brittle CSS or XPath.
- Use Playwright's auto-waiting and awaited web-first assertions. Do not add
  `waitForTimeout` to make a failure disappear.
- Mock third-party dependencies when needed; do not mock the application path
  the test is meant to prove.
- Never use production credentials or mutate production data unless the user
  explicitly authorizes that exact test.
- Treat retries as diagnostic containment, not proof that a flaky test is fixed.

## Verification

Report the exact tests and browser projects run, their result, and any untested
browser, environment, or external dependency. A passing generated test is not
enough if the intended user flow was not observed.
