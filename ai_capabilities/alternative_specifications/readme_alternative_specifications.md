# AI Capabilities — Alternative Specifications

[Back to ai_capabilities README](../readme_ai_capabilities.md)

This folder holds alternative model × scenario variants of the task-level AI capability data. The headline (canonical) data at the parent folder uses **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** Forecasting Research Institute (FRI) scenario for 2030 (Karger et al.).

Alternatives are useful for sensitivity / robustness analysis.

## Layout

```
gpt4o/
  task_ai_capabilities.csv             # Original GPT-4o-derived data (incl. smart_robots cols)
  task_skill_requirements_5d.csv
  task_skill_requirements_35d.csv
qwen2.5-72b-awq/
  baseline/   # Qwen rated without an FRI scenario system message
  slow/       # FRI slow 2030 scenario
  rapid/      # FRI rapid 2030 scenario
    {augmentation,automation,simplification}.csv
```

The Qwen-moderate variant is the canonical headline at the parent level and is not duplicated here.

## Why each variant exists

| Variant | Purpose |
|---|---|
| `gpt4o/` | Cross-vendor robustness vs. Qwen; preserved as version 1.2 of the dataset. Includes smart-robots columns that Qwen was not run on. |
| `qwen2.5-72b-awq/baseline/` | Qwen without FRI conditioning — anchors the FRI sensitivity range. |
| `qwen2.5-72b-awq/slow/` | Conservative 2030 AI-capability trajectory. |
| `qwen2.5-72b-awq/rapid/` | Aggressive 2030 AI-capability trajectory. |
