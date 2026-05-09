# Notice

This plugin bundles selected third-party Agent Skills for personal Codex use.

The selection favors practical, working skills for software engineering:
debugging, TDD, planning, frontend work, documentation, deployment, GitHub/CI,
security, file handling, production launch workflows, source-grounded work,
observability, Figma design workflows, performance, and skill/plugin
maintenance.

## Sources

| Repository | Commit | Stars at selection | License policy |
|---|---|---:|---|
| `addyosmani/agent-skills` | `4c585c3721a3da180f760a91142d704c9b97c80c` | 37,183 | MIT copied into imported skill dirs |
| `openai/skills` | `4c4058ebf44f6734e62c70ab4a81246d4d093fc8` | 18,688 | per-skill `LICENSE.txt` |
| `mxyhi/ok-skills` | `0cab7e8a7cddc187e627604e6ce384077c7f5574` | 326 | Apache-2.0 copied into imported skill dirs |
| `zhu1090093659/spec_driven_develop` | `9f19aa74306ac379868b09677e8e3b3550be04d7` | 714 | MIT copied into imported skill dirs |
| `hqhq1025/skill-optimizer` | `c48b4b5e22e1298df6c0cc0c412af2d0484f5f27` | 72 | MIT copied into imported skill dirs |

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

## Added from `addyosmani/agent-skills`

I evaluated the full current skill tree and imported all 22 skills. They form a
cohesive engineering lifecycle pack rather than a mixed grab bag: idea/spec,
planning, incremental build, TDD, browser verification, source-grounded
development, review, security, performance, migration, CI/CD, and launch.

Shared reference files from the upstream `references/` directory were copied
inside each imported skill so Codex can resolve them relative to `SKILL.md`.
The `idea-refine` skill was lightly adapted to replace an upstream absolute
script path with a local `scripts/idea-refine.sh` path.

## Exclusions

I intentionally did not import every skill from every repository. Excluded
skills include no-license repositories, very narrow domain packs, and skills
that depend on heavy or brittle external tools unless they are likely to be
useful in normal Codex work.

## Redistribution

This is not an official OpenAI plugin. Review the license file inside each
skill directory before publishing or redistributing this bundle.
