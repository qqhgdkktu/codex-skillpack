# Changelog

## 0.3.0 - 2026-07-22

- Refreshed retained Addy Osmani and ok-skills imports to their latest upstream
  commits, including major security, TDD, review, architecture, and docs updates.
- Added `debugging-and-error-recovery`, `frontend-ui-engineering`,
  `observability-and-instrumentation`, and upstream's focused
  `skill-personalizer` replacement.
- Removed 24 stale, upstream-deleted, exact-duplicate, Codex-superseded, or
  connector-owned skills to reduce routing noise; the bundle now contains 37
  focused skills.
- Migrated GitHub CI/comment and Netlify/Render deployment skills from the
  deprecated `openai/skills` catalog to the current `openai/plugins` source.
- Fixed broken architecture references by importing the current upstream
  resources and reduced plugin starter prompts to Codex's supported maximum of
  three.

## 0.2.3 - 2026-05-09

- Added wrapper license, privacy policy, terms, security policy, contribution
  rules, and third-party notices.
- Improved plugin metadata for Codex/plugin discovery queries around TDD,
  debugging, review, docs, frontend, CI/CD, deployment, observability, and
  security.
- Refreshed README and website copy with clearer install, usage, legal, and
  trust sections.
- Extended validation to require legal/discovery documentation.

## 0.2.2 - 2026-05-09

- Pruned the bundle from 83 to 56 skills to reduce routing noise.
- Kept the strongest day-to-day engineering workflows.

## 0.2.1 - 2026-05-09

- Refreshed pinned upstream skills and added practical skills from selected
  public sources.

## 0.2.0 - 2026-05-09

- Added a broader practical Agent Skills bundle and GitHub Pages site.

## 0.1.0 - Initial

- Created the initial local Codex plugin package.
