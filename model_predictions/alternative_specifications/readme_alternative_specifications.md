# Model Predictions — Alternative Specifications

[Back to main README](../../README.md)

This folder holds alternative model × scenario variants of the structural-model occupation-level predictions. The headline (canonical) data at the parent folder ([`../occupations/occupation_ai_effects.csv`](../occupations/occupation_ai_effects.csv)) uses model inputs from **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** Forecasting Research Institute (FRI) scenario for 2030 (Karger, Atanasov, Tetlock, *et al.*, 2024).

Each variant ships `occupation_ai_effects.csv` in the same schema as the canonical.

## Layout

```
gpt4o/
  occupation_ai_effects.csv              # also keeps the generative + physical-AI (smart robots) columns
qwen2.5-72b-awq/
  baseline/  slow/  rapid/
    occupation_ai_effects.csv
```

The Qwen-moderate variant is the canonical headline at the parent level and is not duplicated here.

## Why each variant exists

| Variant | Purpose |
|---|---|
| `gpt4o/` | The previous v1.2 release. Cross-vendor robustness vs. Qwen. Retains the `emp_share_post_gen_plus_physical_ai` / `mean_wage_post_gen_plus_physical_ai` / `wage_bill_post_gen_plus_physical_ai` columns that the Qwen rescore did not cover. |
| `qwen2.5-72b-awq/baseline/` | Qwen without FRI conditioning — anchors the FRI sensitivity range. |
| `qwen2.5-72b-awq/slow/` | Conservative 2030 AI-capability trajectory. |
| `qwen2.5-72b-awq/rapid/` | Aggressive 2030 AI-capability trajectory. |
