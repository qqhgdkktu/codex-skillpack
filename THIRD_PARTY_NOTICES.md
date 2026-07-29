# Third-Party Notices

Codex Skillpack redistributes selected Agent Skills from upstream public
repositories. This file summarizes attribution and license handling. The
machine-readable source of truth is `SKILL_SOURCES.json`.

## Summary

| Upstream repository | Skills included | License handling |
|---|---:|---|
| `addyosmani/agent-skills` | 14 | MIT license copied into each imported skill directory |
| `openai/plugins` | 4 | upstream per-skill or plugin license preserved |
| `openai/skills` | 6 | legacy per-skill `LICENSE.txt` preserved |
| `mxyhi/ok-skills` | 5 | per-skill MIT or Apache-2.0 license preserved |
| `hqhq1025/skill-optimizer` | 1 | MIT license copied into imported skill directory |
| `testdino-hq/playwright-skill` | 1 | MIT license copied into imported skill directory |

## Included Skills By Source

### `addyosmani/agent-skills`

Pinned commit: `7829ffd90d973b6325f5f12f1b1226dcace74443`

Included skills: `api-and-interface-design`, `ci-cd-and-automation`,
`code-review-and-quality`, `code-simplification`, `deprecation-and-migration`,
`debugging-and-error-recovery`, `documentation-and-adrs`,
`frontend-ui-engineering`, `performance-optimization`,
`observability-and-instrumentation`, `security-and-hardening`,
`shipping-and-launch`, `source-driven-development`, `spec-driven-development`.

### `openai/plugins`

Pinned commit: `11c74d6ba24d3a6d48f54a194cd00ef3beea18f9`

Included skills: `gh-address-comments`, `gh-fix-ci`, `netlify-deploy`,
`render-deploy`.

### `openai/skills` (legacy pins)

The remaining skills have no direct replacement in `openai/plugins` and remain
pinned to the exact historical commits recorded in `SKILL_SOURCES.json`.

Included skills: `chatgpt-apps`, `cli-creator`, `cloudflare-deploy`,
`migrate-to-codex`, `security-threat-model`, `vercel-deploy`.

### `mxyhi/ok-skills`

Pinned commit: `94707b6ecc7774933a20c5a8d485ade7190e3bbe`

Included skills: `ai-elements`, `better-icons`, `find-docs`,
`codebase-design`, `tdd`.

### `hqhq1025/skill-optimizer`

Pinned commit: `b9ffd1513e84136b72e2b6f041dc1ebfd9e23a84`

Included skill: `skill-personalizer`.

### `testdino-hq/playwright-skill`

Pinned commit: `d3be9ca4d7303e2aee3eba4842963abf573117b0`

Included skill: `playwright-testing`.

## Redistribution Notes

Keep every imported skill's `LICENSE.txt` file intact when redistributing,
forking, copying, or repackaging this bundle. Do not remove attribution metadata
from `SKILL_SOURCES.json`, `NOTICE.md`, or this file.
