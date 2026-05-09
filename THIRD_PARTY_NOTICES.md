# Third-Party Notices

Codex Skillpack redistributes selected Agent Skills from upstream public
repositories. This file summarizes attribution and license handling. The
machine-readable source of truth is `SKILL_SOURCES.json`.

## Summary

| Upstream repository | Skills included | License handling |
|---|---:|---|
| `addyosmani/agent-skills` | 15 | MIT license copied into each imported skill directory |
| `openai/skills` | 29 | upstream per-skill `LICENSE.txt` preserved |
| `mxyhi/ok-skills` | 10 | Apache-2.0 license copied into each imported skill directory |
| `hqhq1025/skill-optimizer` | 1 | MIT license copied into imported skill directory |

## Included Skills By Source

### `addyosmani/agent-skills`

Pinned commit: `4c585c3721a3da180f760a91142d704c9b97c80c`

Included skills: `api-and-interface-design`, `ci-cd-and-automation`,
`code-review-and-quality`, `code-simplification`, `deprecation-and-migration`,
`documentation-and-adrs`, `doubt-driven-development`, `idea-refine`,
`incremental-implementation`, `performance-optimization`,
`planning-and-task-breakdown`, `security-and-hardening`,
`shipping-and-launch`, `source-driven-development`,
`spec-driven-development`.

### `openai/skills`

Most included OpenAI skills are pinned to
`4c4058ebf44f6734e62c70ab4a81246d4d093fc8`. The `doc` skill is pinned to
`fb7b56dff09cb2a44dd390cde69c717e8a319eb7`.

Included skills: `chatgpt-apps`, `cli-creator`, `cloudflare-deploy`, `doc`,
`figma`, `figma-implement-design`, `figma-use`, `gh-address-comments`,
`gh-fix-ci`, `jupyter-notebook`, `linear`, `migrate-to-codex`,
`netlify-deploy`, `notion-knowledge-capture`,
`notion-research-documentation`, `notion-spec-to-implementation`,
`openai-docs`, `pdf`, `playwright`, `plugin-creator`, `render-deploy`,
`screenshot`, `security-threat-model`, `sentry`, `skill-creator`,
`skill-installer`, `transcribe`, `vercel-deploy`, `yeet`.

### `mxyhi/ok-skills`

Pinned commit: `0cab7e8a7cddc187e627604e6ce384077c7f5574`

Included skills: `ai-elements`, `better-icons`, `diagnose`, `dogfood`,
`exa-search`, `find-docs`, `frontend-skill`,
`improve-codebase-architecture`, `opensrc`, `tdd`.

### `hqhq1025/skill-optimizer`

Pinned commit: `c48b4b5e22e1298df6c0cc0c412af2d0484f5f27`

Included skills: `skill-optimizer`.

## Redistribution Notes

Keep every imported skill's `LICENSE.txt` file intact when redistributing,
forking, copying, or repackaging this bundle. Do not remove attribution metadata
from `SKILL_SOURCES.json`, `NOTICE.md`, or this file.
