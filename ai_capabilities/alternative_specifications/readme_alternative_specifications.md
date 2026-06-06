# AI Capabilities — Alternative Specifications

[Back to ai_capabilities README](../readme_ai_capabilities.md)

This folder holds alternative model × scenario variants of the task-level AI capability data. The headline (canonical) data at the parent folder uses **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** Forecasting Research Institute (FRI) scenario for 2030 (Karger, Atanasov, Tetlock, *et al.*, 2024).

Each variant ships the same three files in the same schema as the canonical:

- `task_ai_capabilities.csv`
- `task_skill_requirements_5d.csv`
- `task_skill_requirements_35d.csv`

## Layout

```
gpt4o/
  task_ai_capabilities.csv           # also keeps automatable/augmentation_smart_robots cols
  task_skill_requirements_5d.csv
  task_skill_requirements_35d.csv
qwen2.5-72b-awq/
  baseline/   # Qwen rated without an FRI scenario system message
  slow/       # FRI slow 2030 scenario
  rapid/      # FRI rapid 2030 scenario
    task_ai_capabilities.csv
    task_skill_requirements_5d.csv
    task_skill_requirements_35d.csv
```

The Qwen-moderate variant is the canonical headline at the parent level and is not duplicated here.

## Why each variant exists

| Variant | Purpose |
|---|---|
| `gpt4o/` | The previous v1.2 release. Cross-vendor robustness vs. Qwen. Retains the smart-robots / generative + physical AI columns that the Qwen rescore did not cover. |
| `qwen2.5-72b-awq/baseline/` | Qwen without FRI conditioning — anchors the FRI sensitivity range. |
| `qwen2.5-72b-awq/slow/` | Conservative 2030 AI-capability trajectory. |
| `qwen2.5-72b-awq/rapid/` | Aggressive 2030 AI-capability trajectory. |

See [`../readme_ai_capabilities.md`](../readme_ai_capabilities.md) for the full FRI scenario system messages and the rating methodology.
