# Contributing

Contributions should keep Codex Skillpack lean, practical, and legally
redistributable.

## Skill Selection Rules

Add a skill only when it is broadly useful for normal software engineering and
has clear instructions, a compatible license, and a low risk of confusing Codex
routing.

Prefer skills for:

- coding workflow, TDD, debugging, and review;
- frontend implementation and verification;
- documentation, API design, and source-grounded work;
- CI/CD, deployment, observability, security, and performance;
- plugin and skill maintenance.

Avoid skills that are duplicate, vague, unlicensed, overly domain-specific,
heavy on brittle external dependencies, or likely to over-trigger in unrelated
coding chats.

## Legal Requirements

Every imported skill must keep its upstream `LICENSE.txt` in the skill
directory. Update `SKILL_SOURCES.json`, `NOTICE.md`, and
`THIRD_PARTY_NOTICES.md` when changing sources, commits, or included skills.

Do not add secrets, private customer data, generated logs with tokens, or
branded assets that are not licensed for redistribution.

## Validation

Run:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool SKILL_SOURCES.json >/dev/null
python3 scripts/validate_plugin.py
```
