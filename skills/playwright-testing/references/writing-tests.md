# Writing Playwright Tests

## Choose The Test Layer

- Use API tests for request/response contracts and setup that does not need a
  browser.
- Use component tests when one rendered component and its states are the real
  contract and the project's installed Playwright version supports its current
  component-testing model.
- Use end-to-end tests for critical flows spanning routing, browser state,
  backend behavior, and persistence.
- Use visual comparisons only for stable, controlled rendering environments.

## Locators And Assertions

Prefer locators that match how a user finds an element:

```ts
const submit = page.getByRole("button", { name: "Submit" });
await expect(submit).toBeEnabled();
await submit.click();
await expect(page.getByRole("status")).toHaveText("Saved");
```

Use `getByLabel` for form controls and `getByTestId` for stable contracts that
have no useful accessible name. Chain and filter locators before reaching for
CSS. Avoid XPath and selectors tied to layout or generated class names.

Await web-first assertions:

```ts
await expect(page.getByText("Welcome")).toBeVisible();
```

Avoid immediate checks such as
`expect(await locator.isVisible()).toBe(true)` when the UI may settle
asynchronously.

## Isolation And Data

- Give each test its own browser context and independent data.
- Create data through supported APIs or fixtures when that is faster and more
  reliable than UI setup.
- Clean up only data created by the test.
- Reuse authentication through a setup project or storage state, but keep roles
  and accounts isolated where tests can mutate shared state.
- Freeze or control time when behavior depends on dates, timers, or expiration.

## Network Boundaries

Exercise the application's own backend unless the test explicitly targets a
frontend-only state. Mock third-party services, unstable callbacks, or expensive
external systems at a narrow boundary. Assert the request contract when the
mock is part of the test.

## Visual And Accessibility Checks

- Keep browser, operating system, fonts, viewport, data, and animations stable
  for screenshot comparisons.
- Mask only truly dynamic regions; do not mask the behavior under test.
- Use semantic locators and ARIA snapshots to catch structural regressions.
- Use an accessibility engine such as axe for rule scanning, then manually
  verify keyboard flow, focus order, names, error states, and contrast where
  relevant.

Official references:

- <https://playwright.dev/docs/best-practices>
- <https://playwright.dev/docs/locators>
- <https://playwright.dev/docs/test-assertions>
- <https://playwright.dev/docs/auth>
- <https://playwright.dev/docs/accessibility-testing>
