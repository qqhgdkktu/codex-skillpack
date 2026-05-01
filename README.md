# Codex Skillpack

Personal Codex plugin with a practical skill bundle for day-to-day engineering.

- Repository: <https://github.com/qqhgdkktu/codex-skillpack>
- Website: <https://qqhgdkktu.github.io/codex-skillpack/>
- Skill count: 41

## What It Does

This plugin adds selected, working skills for:

- coding workflows: `tdd`, `systematic-debugging`, `spec-driven-develop`, `planning-with-files`
- frontend work: `frontend-skill`, `ai-elements`, `better-icons`, `playwright`, `dogfood`
- research and docs: `openai-docs`, `find-docs`, `find-skills`, `exa-search`, `opensrc`
- deployment: `vercel-deploy`, `netlify-deploy`, `cloudflare-deploy`, `render-deploy`
- GitHub and CI: `gh-fix-ci`, `gh-address-comments`, `yeet`
- files and media: `doc`, `pdf`, `jupyter-notebook`, `screenshot`, `transcribe`
- security: `security-best-practices`, `security-threat-model`
- plugin/skill maintenance: `plugin-creator`, `skill-creator`, `skill-installer`, `skill-optimizer`, `plugin-check`
- Notion workflows: `notion-knowledge-capture`, `notion-research-documentation`, `notion-spec-to-implementation`

The bundle is intentionally not every skill found online. It excludes no-license, narrow, brittle, or heavy external-tool skills unless they are likely to be broadly useful.

## Sources

Skills were selected from high-star public repositories:

| Source | Stars at selection | License policy |
|---|---:|---|
| `openai/skills` | 17,934 | per-skill `LICENSE.txt` |
| `zhu1090093659/spec_driven_develop` | 706 | MIT |
| `mxyhi/ok-skills` | 311 | Apache-2.0 |
| `hqhq1025/skill-optimizer` | 67 | MIT |

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
Use systematic-debugging on this test failure.
Use tdd before implementing this feature.
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
