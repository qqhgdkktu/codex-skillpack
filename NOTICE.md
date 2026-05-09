# Notice

This plugin bundles selected third-party Agent Skills for local and shared Codex
use.

The selection favors practical, working skills for software engineering:
debugging, TDD, planning, frontend work, documentation, deployment, GitHub/CI,
security, file handling, production launch workflows, source-grounded work,
observability, focused Figma-to-code workflows, performance, and skill/plugin
maintenance. On 2026-05-09 the bundle was pruned from 83 to 56 skills to reduce
trigger ambiguity.

This project is an unofficial redistribution bundle. It is not affiliated with,
endorsed by, or sponsored by OpenAI, GitHub, Sentry, Figma, Notion, Linear,
Vercel, Netlify, Cloudflare, Render, or any upstream skill author unless that
party states otherwise.

## Sources

| Repository | Commit | Stars at selection | License policy |
|---|---|---:|---|
| `addyosmani/agent-skills` | `4c585c3721a3da180f760a91142d704c9b97c80c` | 37,183 | MIT copied into imported skill dirs |
| `openai/skills` | `4c4058ebf44f6734e62c70ab4a81246d4d093fc8` | 18,688 | per-skill `LICENSE.txt` |
| `mxyhi/ok-skills` | `0cab7e8a7cddc187e627604e6ce384077c7f5574` | 326 | Apache-2.0 copied into imported skill dirs |
| `hqhq1025/skill-optimizer` | `c48b4b5e22e1298df6c0cc0c412af2d0484f5f27` | 72 | MIT copied into imported skill dirs |

`SKILL_SOURCES.json` is the source of truth for skill-level source, commit, star
count, and license metadata. `THIRD_PARTY_NOTICES.md` summarizes the same
information in a human-readable redistribution format.

## 2026-05-09 Refresh

I checked every upstream source in `SKILL_SOURCES.json` against GitHub. Three
sources were already current: `addyosmani/agent-skills`,
`zhu1090093659/spec_driven_develop`, and `hqhq1025/skill-optimizer`.

`openai/skills` had 6 newer commits. Existing OpenAI skills were refreshed
where still present upstream, and 14 practical OpenAI skills were added:
Figma workflows, Linear, Notion meeting intelligence, Playwright interactive,
Security Ownership Map, Sentry, and Speech.

`mxyhi/ok-skills` had 3 newer commits. Existing imported ok-skills were
refreshed, 7 practical skills were added (`autoresearch`, `browser-trace`,
`diagnose`, `get-api-docs`, `grill-me`, `grill-with-docs`,
`karpathy-guidelines`), and stale `brainstorming` was removed because upstream
replaced it with more focused skills.

## 2026-05-09 Lean Prune

I reviewed the 83-skill set for practical value and routing clarity. The bundle
now keeps 56 high-signal skills and removes 27 noisy candidates:

- duplicate workflows: extra debugging, TDD, planning, and meta skill-routing
  skills that overlapped with stronger retained skills;
- narrow Figma write workflows: Code Connect, new-file creation, full design
  generation, and design-system-library generation;
- heavy or brittle workflows: broad autonomous loops, browser tracing,
  Playwright js-repl interactivity, ownership graph analysis, and speech TTS;
- interactive stress-test modes and broad behavioral guidelines that could
  over-trigger in normal coding chats.

Retained skills prioritize day-to-day engineering: TDD, diagnosis, API design,
source-grounded implementation, code review, frontend polish, Figma-to-code,
docs, deployment, Sentry, security, performance, and plugin maintenance.

The `zhu1090093659/spec_driven_develop` skill was removed in this pass because
it overlapped with the retained `spec-driven-development` workflow.

## Added from `addyosmani/agent-skills`

I evaluated the full current skill tree. It forms a cohesive engineering
lifecycle pack rather than a mixed grab bag: idea/spec, planning, incremental
build, browser verification, source-grounded development, review, security,
performance, migration, CI/CD, and launch. The lean bundle keeps the strongest,
least-duplicative subset.

Shared reference files from the upstream `references/` directory were copied
inside each imported skill so Codex can resolve them relative to `SKILL.md`.
The `idea-refine` skill was lightly adapted to replace an upstream absolute
script path with a local `scripts/idea-refine.sh` path.

## Exclusions

I intentionally did not keep every imported skill. Excluded skills include
no-license repositories, duplicate workflows, broad meta skills, very narrow
domain packs, and skills that depend on heavy or brittle external tools unless
they are likely to be useful in normal Codex work.

## License Policy

This repository contains two kinds of material:

- wrapper files created for Codex Skillpack, covered by `LICENSE.md`;
- imported third-party skills, each governed by the `LICENSE.txt` preserved
  inside that skill directory.

Do not treat the root wrapper license as replacing upstream skill licenses.
Keep upstream `LICENSE.txt` files and attribution metadata when redistributing
the bundle or copying skills into another project.

## No Warranty

The skills are workflow instructions, not guarantees. They may suggest commands,
tool use, external service calls, or code changes that are inappropriate for a
specific repository. Users remain responsible for reviewing actions, protecting
secrets, checking third-party terms, and verifying generated code before use.

## No Legal Advice

This notice, the wrapper license, and the repository documentation are practical
project documentation, not legal advice. Consult a qualified professional before
using or redistributing this bundle in a regulated, commercial, or high-risk
environment.

## Redistribution

Review `LICENSE.md`, `PRIVACY.md`, `TERMS.md`, `SECURITY.md`, and the license
file inside each skill directory before publishing, redistributing, or using
this bundle in a team or commercial environment.
