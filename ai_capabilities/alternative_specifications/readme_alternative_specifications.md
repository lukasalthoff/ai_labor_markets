# AI Capabilities — Alternative Specifications

[Back to ai_capabilities README](../readme_ai_capabilities.md)

This folder holds alternative AI-scenario × model variants of the task-level AI capability data. The headline (canonical) data at the parent folder uses **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** 2030 AI scenario (Karger, Atanasov, Tetlock, *et al.*, 2024 — see Forecasting Research Institute).

Each variant ships the same three files in the same schema as the canonical:

- `task_ai_capabilities.csv`
- `task_skill_requirements_5d.csv`
- `task_skill_requirements_35d.csv`

## Layout (AI scenario first, then model)

```
no_explicit_scenario/        # Model rated without any 2030 AI-scenario system message
  gpt4o/
  qwen2.5-72b-awq/
  gpt-oss/
slow/                        # Slow 2030 AI-progress trajectory
  qwen2.5-72b-awq/
  gpt-oss/
moderate/                    # Moderate 2030 AI-progress trajectory (Qwen is the parent canonical)
  gpt-oss/
rapid/                       # Rapid 2030 AI-progress trajectory
  qwen2.5-72b-awq/
  gpt-oss/
```

## Variants by AI scenario

### No explicit scenario

The model is shown the prompt without any AI-scenario system message. For GPT-4o this is the previous (v1.2) release.

| Model | Notes |
|---|---|
| `gpt4o/` | GPT-4o, OpenAI closed-weight |
| `qwen2.5-72b-awq/` | Qwen-2.5-72B-Instruct-AWQ, Alibaba open-weight |
| `gpt-oss/` | OpenAI gpt-oss open-weight |

### Slow / Moderate / Rapid 2030

The model is shown a 2030 AI-progress scenario as a system message before each request. Wording is reproduced in [`../readme_ai_capabilities.md`](../readme_ai_capabilities.md).

| Model | Slow | Moderate | Rapid |
|---|---|---|---|
| `qwen2.5-72b-awq/` | ✅ | (parent canonical) | ✅ |
| `gpt-oss/` | ✅ | ✅ | ✅ |

GPT-4o was not run under the 2030 scenarios.
