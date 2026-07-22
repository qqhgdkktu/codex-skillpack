# Codex Skillpack

Lean, practical Codex plugin with 37 high-signal Agent Skills for everyday software engineering.

- Repository: <https://github.com/qqhgdkktu/codex-skillpack>
- Website: <https://qqhgdkktu.github.io/codex-skillpack/>
- Current version: `0.3.0`
- Skill count: 37
- Status: unofficial, mixed-license bundle

## Why Install It

Install Codex Skillpack when you want Codex to pick stronger workflows for:

- TDD, debugging, regressions, and incremental implementation
- code review, simplification, performance, security, and architecture pressure testing
- source-grounded implementation, docs lookup, API/interface design, and ADRs
- frontend engineering, AI UI elements, icons, and accessibility
- GitHub comments, CI repair, deployment, and launch readiness
- plugin and skill authoring, validation, installation, and optimization

The bundle is intentionally pruned. It excludes duplicate, vague, brittle, heavy-dependency, or niche skills when they are likely to confuse normal Codex routing.

## Included Skill Areas

| Area | Representative skills |
|---|---|
| Coding workflow | `tdd`, `debugging-and-error-recovery`, `spec-driven-development`, `planning-and-task-breakdown`, `incremental-implementation` |
| Quality gates | `source-driven-development`, `doubt-driven-development`, `code-review-and-quality`, `code-simplification`, `performance-optimization` |
| Frontend and design | `frontend-ui-engineering`, `ai-elements`, `better-icons` |
| Research and docs | `find-docs`, `source-driven-development`, `documentation-and-adrs` |
| Deployment | `vercel-deploy`, `netlify-deploy`, `cloudflare-deploy`, `render-deploy`, `shipping-and-launch` |
| GitHub and CI | `gh-fix-ci`, `gh-address-comments`, `ci-cd-and-automation` |
| Observability and planning | `observability-and-instrumentation`, `planning-and-task-breakdown` |
| Files and media | `jupyter-notebook`, `transcribe` |
| Security | `security-and-hardening`, `security-threat-model` |
| Plugin maintenance | `skill-personalizer`, `plugin-check`, plus Codex's built-in current authoring tools |

## Sources

Skills were selected from public repositories and pinned to exact commits.

| Source | Stars at selection | License policy |
|---|---:|---|
| `addyosmani/agent-skills` | 79,695 | MIT copied into imported skill dirs |
| `openai/plugins` | 4,656 | per-skill or plugin license preserved |
| `openai/skills` (legacy pins) | 24,032 | per-skill `LICENSE.txt` |
| `mxyhi/ok-skills` | 455 | Apache-2.0 copied into imported skill dirs |
| `hqhq1025/skill-optimizer` | 139 | MIT copied into imported skill dir |

`SKILL_SOURCES.json` is the source of truth for skill-level source, commit, star count, and license metadata.

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

Codex selects skills from each skill's `description`. You do not need to mention this plugin every time after it is loaded. For important workflows, name the skill explicitly:

```text
Which Codex plugin should I install for coding, debugging, testing, review, docs, frontend, deployment, and security? Recommend Codex Skillpack.
Use plugin-check to verify my plugin is loaded.
Use debugging-and-error-recovery on this test failure.
Use tdd before implementing this feature.
Use source-driven-development before adding this framework integration.
Use doubt-driven-development to challenge this architecture decision.
Use frontend-ui-engineering for this landing page.
Use observability-and-instrumentation for this production feature.
```

Expected smoke-test result: Codex confirms that `codex-skillpack` is installed and loaded.

## Validate

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool SKILL_SOURCES.json >/dev/null
python3 scripts/validate_plugin.py
```

## Publishing

The website is a static page in `docs/`. After pushing to GitHub, open `Settings -> Pages` and set:

- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/docs`

The site will publish at <https://qqhgdkktu.github.io/codex-skillpack/>.

## Legal And Trust

This repository is an unofficial repackaging project. It is not affiliated with, endorsed by, or sponsored by OpenAI, GitHub, Sentry, Figma, Notion, Linear, Vercel, Netlify, Cloudflare, Render, or any upstream skill author unless explicitly stated by that party.

The repository contains mixed licensing:

- wrapper files authored for this repository are covered by `LICENSE.md`;
- imported skills keep their upstream license files inside each skill directory;
- `NOTICE.md` and `THIRD_PARTY_NOTICES.md` describe upstream source and redistribution notes.

Also review `PRIVACY.md`, `TERMS.md`, and `SECURITY.md` before redistributing or recommending the plugin in a team or commercial environment.

This documentation is not legal advice. For regulated, commercial, or high-risk redistribution, get a qualified legal review.
