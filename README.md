# Codex Skillpack

Personal Codex plugin with a practical skill bundle for day-to-day engineering.

- Repository: <https://github.com/qqhgdkktu/codex-skillpack>
- Website: <https://qqhgdkktu.github.io/codex-skillpack/>
- Skill count: 56

## What It Does

This plugin adds selected, working skills for:

- coding workflows: `tdd`, `diagnose`, `spec-driven-development`, `planning-and-task-breakdown`, `incremental-implementation`
- quality gates: `source-driven-development`, `doubt-driven-development`, `code-review-and-quality`, `code-simplification`, `performance-optimization`
- frontend and design: `frontend-skill`, `ai-elements`, `better-icons`, `playwright`, `dogfood`, `figma`, `figma-use`, `figma-implement-design`
- research and docs: `openai-docs`, `find-docs`, `exa-search`, `opensrc`, `documentation-and-adrs`
- deployment: `vercel-deploy`, `netlify-deploy`, `cloudflare-deploy`, `render-deploy`
- GitHub and CI: `gh-fix-ci`, `gh-address-comments`, `yeet`
- observability and planning: `sentry`, `linear`, `ci-cd-and-automation`, `shipping-and-launch`
- files and media: `doc`, `pdf`, `jupyter-notebook`, `screenshot`, `transcribe`
- security: `security-and-hardening`, `security-threat-model`
- plugin/skill maintenance: `plugin-creator`, `skill-creator`, `skill-installer`, `skill-optimizer`, `plugin-check`
- Notion workflows: `notion-knowledge-capture`, `notion-research-documentation`, `notion-spec-to-implementation`

The bundle is intentionally lean. It excludes duplicate, broad meta, narrow, brittle, or heavy external-tool skills unless they are likely to be broadly useful in normal development.

## Sources

Skills were selected from high-star public repositories:

| Source | Stars at selection | License policy |
|---|---:|---|
| `addyosmani/agent-skills` | 37,183 | MIT copied into imported skill dirs |
| `openai/skills` | 18,688 | per-skill `LICENSE.txt` |
| `mxyhi/ok-skills` | 326 | Apache-2.0 |
| `hqhq1025/skill-optimizer` | 72 | MIT |

See `SKILL_SOURCES.json` and `NOTICE.md` for exact source commits.

## Install Locally

For local development, register a marketplace rooted at your home directory:

```toml
[marketplaces.local-plugins]
source_type = "local"
source = "/Users/mikita"

[plugins."codex-skillpack@local-plugins"]
enabled = true
```

Then make sure `/Users/mikita/.agents/plugins/marketplace.json` includes:

```json
{
  "name": "local-plugins",
  "plugins": [
    {
      "name": "codex-skillpack",
      "source": {
        "source": "local",
        "path": "./plugins/codex-skillpack"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Restart Codex after changing plugin or marketplace configuration.

## Usage

Skills are selected by Codex based on each skill's `description`. You do not need
to mention the plugin every time. For important workflows, explicitly name the
skill to force the behavior:

```text
Use plugin-check to verify my plugin is loaded.
Use diagnose on this test failure.
Use tdd before implementing this feature.
Use source-driven-development before adding this framework integration.
Use doubt-driven-development to challenge this architecture decision.
Use sentry to inspect recent production errors.
Use figma-implement-design for this Figma screen.
Use frontend-skill for this landing page.
```

Expected smoke-test result: Codex confirms that `codex-skillpack` is installed and loaded.

## Validate

```bash
python3 scripts/validate_plugin.py
```

## Publishing

The website is a static page in `docs/`. After pushing to GitHub, open
`Settings -> Pages` and set:

- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/docs`

The site will publish at <https://qqhgdkktu.github.io/codex-skillpack/>.

## Licensing

This repository has mixed upstream licensing. Each imported skill keeps its
`LICENSE.txt`. The wrapper plugin files are provided as-is. Review `NOTICE.md`
before redistributing.
