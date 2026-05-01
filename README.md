# My Codex Plugin

Personal Codex plugin for reusable local skills.

- Repository: <https://github.com/qqhgdkktu/my-codex-plugin>
- Website: <https://qqhgdkktu.github.io/my-codex-plugin/>

## Contents

- `.codex-plugin/plugin.json` - plugin manifest
- `skills/plugin-check/SKILL.md` - smoke-test skill confirming the plugin is loaded
- `docs/` - static GitHub Pages website
- `.github/workflows/pages.yml` - GitHub Pages deployment workflow

## Install

For local development, register a marketplace rooted at your home directory:

```toml
[marketplaces.local-plugins]
source_type = "local"
source = "/Users/mikita"

[plugins."my-codex-plugin@local-plugins"]
enabled = true
```

Then make sure `/Users/mikita/.agents/plugins/marketplace.json` includes:

```json
{
  "name": "local-plugins",
  "plugins": [
    {
      "name": "my-codex-plugin",
      "source": {
        "source": "local",
        "path": "./plugins/my-codex-plugin"
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

## Smoke test

After installing and restarting Codex, ask:

```text
Use plugin-check to verify my plugin is loaded.
```

Expected result: Codex confirms that `my-codex-plugin` is installed and loaded.

## Publishing

This repository includes a GitHub Pages workflow. After pushing to GitHub, open
the repository settings and make sure Pages is configured to deploy from GitHub
Actions if it is not enabled automatically.
