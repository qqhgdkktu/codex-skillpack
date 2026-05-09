# Security Policy

## Supported Versions

Only the latest `main` branch and the latest published plugin version are
actively maintained.

## Reporting A Vulnerability

For non-sensitive security issues, open a GitHub issue:

<https://github.com/qqhgdkktu/codex-skillpack/issues>

Do not post secrets, private tokens, exploit payloads, customer data, or
unredacted logs in public issues. If the repository has GitHub private
vulnerability reporting enabled, use that flow for sensitive reports.

## Scope

In scope:

- unsafe skill instructions that could leak secrets, damage repositories, or
  trigger dangerous commands;
- broken plugin packaging that loads unexpected files;
- license or attribution mistakes that affect redistribution.

Out of scope:

- vulnerabilities in Codex, OpenAI services, GitHub, Sentry, Figma, Notion,
  Linear, Vercel, Netlify, Cloudflare, Render, or any other third-party service;
- issues caused by local credentials, workspace permissions, or user-approved
  commands outside this repository.

## Safe Use

Review generated commands before running them, keep secrets out of prompts and
logs, use least-privilege credentials, and run repository tests before merging
or deploying generated changes.
