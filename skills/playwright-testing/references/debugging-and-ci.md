# Debugging And CI

## Failure Triage

Run one failing test and one configured browser project first:

```bash
npx playwright test path/to/example.spec.ts --project=chromium
```

Prefer the repository's package-manager command when it differs. Inspect the
first causal failure, not the final cascade.

Use:

- `--debug` or UI mode for local interactive diagnosis;
- the HTML report for suite-level context;
- Trace Viewer for action timeline, DOM snapshots, console, and network;
- screenshots and video as supporting evidence, not the only diagnosis.

Open a trace with:

```bash
npx playwright show-trace path/to/trace.zip
```

Do not add arbitrary delays. Replace them with a user-visible condition, URL
transition, response contract, or web-first assertion.

## Stable CI Defaults

Start from the repository's current config. A common baseline is:

```ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  retries: process.env.CI ? 2 : 0,
  use: {
    trace: "on-first-retry",
  },
});
```

Adjust retries to project policy. A retry that passes marks a test as flaky; it
does not resolve the root cause.

In CI:

- install the Playwright browsers and OS dependencies for the locked package
  version;
- use the project's supported Node and package-manager versions;
- upload HTML reports, traces, screenshots, and videos on failure;
- shard only after the suite is isolated and deterministic;
- keep secrets in the CI secret store and redact them from artifacts;
- pin third-party actions and container images according to repository policy.

When browsers differ, run the configured Chromium, Firefox, and WebKit projects
that matter to the product. Do not call a Chromium-only pass cross-browser
verification.

Official references:

- <https://playwright.dev/docs/debug>
- <https://playwright.dev/docs/trace-viewer-intro>
- <https://playwright.dev/docs/test-retries>
- <https://playwright.dev/docs/test-sharding>
- <https://playwright.dev/docs/ci>
