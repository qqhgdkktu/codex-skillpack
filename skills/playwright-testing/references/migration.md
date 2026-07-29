# Migrating To Playwright

Migrate incrementally. Keep the old suite runnable until the replacement proves
equivalent coverage.

## From Cypress

Map behavior, not syntax:

- Cypress queries become Playwright locators.
- Chained retries become awaited web-first assertions.
- `cy.intercept` becomes `page.route` or `browserContext.route`.
- Custom commands usually become fixtures or focused helpers.
- Shared login setup becomes a setup project or storage state.

Do not mechanically preserve Cypress command chains or global state.

## From Selenium/WebDriver

- Replace element handles and explicit waits with locators and auto-waiting.
- Replace driver lifecycle boilerplate with Playwright fixtures.
- Replace implicit waits with awaited assertions on the expected state.
- Replace broad page objects with focused helpers when a full object adds no
  useful abstraction.

## Migration Loop

1. Inventory critical flows, browser coverage, fixtures, and CI behavior.
2. Pick one representative, stable flow.
3. Reproduce its assertions in Playwright.
4. Run old and new tests against the same controlled environment.
5. Compare coverage, runtime, artifacts, and failure clarity.
6. Migrate in small batches and remove old tests only after equivalence is
   observed.

Official starting point: <https://playwright.dev/docs/intro>
