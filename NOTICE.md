# Notice

This plugin bundles selected third-party Agent Skills for personal Codex use.

The selection favors practical, working skills for software engineering:
debugging, TDD, planning, frontend work, documentation, deployment, GitHub/CI,
security, file handling, and skill/plugin maintenance.

## Sources

| Repository | Commit | Stars at selection | License policy |
|---|---|---:|---|
| `openai/skills` | `fb7b56dff09cb2a44dd390cde69c717e8a319eb7` | 17,934 | per-skill `LICENSE.txt` |
| `mxyhi/ok-skills` | `8d7d14520705941254754e908bda0230f3ed9b64` | 311 | Apache-2.0 copied into imported skill dirs |
| `zhu1090093659/spec_driven_develop` | `9f19aa74306ac379868b09677e8e3b3550be04d7` | 706 | MIT copied into imported skill dirs |
| `hqhq1025/skill-optimizer` | `c48b4b5e22e1298df6c0cc0c412af2d0484f5f27` | 67 | MIT copied into imported skill dirs |

## Exclusions

I intentionally did not import every skill from every repository. Excluded
skills include no-license repositories, very narrow domain packs, and skills
that depend on heavy or brittle external tools unless they are likely to be
useful in normal Codex work.

## Redistribution

This is not an official OpenAI plugin. Review the license file inside each
skill directory before publishing or redistributing this bundle.

