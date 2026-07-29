# Changelog

## 0.4.0 - 2026-07-29

- Audited the current `codex-skills` GitHub topic and deeply reviewed the
  strongest licensed candidates against the existing catalog.
- Added a concise, version-aware `playwright-testing` skill based on
  TestDino's Playwright guidance and current official Playwright documentation.
- Replaced the non-self-contained `improve-codebase-architecture` workflow
  with `codebase-design`, which has no missing skill or harness dependencies.
- Removed six broad, duplicate, or non-core skills: `doubt-driven-development`,
  `idea-refine`, `incremental-implementation`,
  `planning-and-task-breakdown`, `jupyter-notebook`, and `transcribe`.
- Reworked `find-docs` to prefer installed and official documentation instead
  of requiring Context7, and made `spec-driven-development` self-contained.
- Compressed every retained routing description and added validator limits for
  per-skill metadata, total catalog size, body length, and frontmatter keys.
  The bundle now contains 32 skills with materially lower always-loaded
  routing metadata.

## 0.3.1 - 2026-07-26

- Refreshed five retained Addy Osmani engineering skills to the current
  upstream commit while preserving the lean 37-skill catalog.
- Replaced npm-only verification assumptions with repository-native test,
  build, type-check, lint, and dependency-audit commands.
- Strengthened performance optimization guidance: re-measure under comparable
  conditions, require gains beyond run-to-run variance, and revert neutral or
  regression-causing changes.
- Adapted upstream cross-references to the bundle's existing `tdd` workflow and
  refreshed source pins and selection metadata.
- Removed stale references to two unbundled skills and extended validation to
  reject missing `skills/<name>/SKILL.md` references.

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
