# Model Predictions — Alternative Specifications

[Back to main README](../../README.md)

This folder holds alternative model × scenario variants of the structural-model occupation-level predictions. The headline (canonical) data at the parent folder uses model inputs from **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** Forecasting Research Institute (FRI) scenario for 2030 (Karger et al.).

## Layout

```
gpt4o/
  occupation_ai_effects.csv             # Original GPT-4o-derived data (incl. gen+physical_AI cols)
  shapley_corners/                      # 6 sub-scenario files for Shapley channel decomposition
qwen2.5-72b-awq/
  baseline/   slow/   rapid/
    occupation_ai_effects.csv
    shapley_corners/
```

The Qwen-moderate variant is the canonical headline at the parent level. Its Shapley corners (for decomposing wage / employment / wage-bill changes into augmentation, automation, and simplification contributions) live under `qwen2.5-72b-awq/moderate/shapley_corners/`.

## Why each variant exists

| Variant | Purpose |
|---|---|
| `gpt4o/` | Cross-vendor robustness vs. Qwen; preserves the version 1.2 dataset including the generative + physical AI columns (smart robots) that Qwen was not run on. |
| `qwen2.5-72b-awq/baseline/` | Qwen without FRI conditioning. |
| `qwen2.5-72b-awq/slow/` | Conservative 2030 AI-capability trajectory. |
| `qwen2.5-72b-awq/moderate/` | Same canonical Qwen-moderate at the parent — Shapley corners surfaced here. |
| `qwen2.5-72b-awq/rapid/` | Aggressive 2030 AI-capability trajectory. |

## Shapley corners

For each variant, `shapley_corners/` contains 6 CSV files that allow exact Shapley decomposition of the post-AI effects into augmentation, automation, and simplification:

- `occupation_ai_effects_woaug.csv` — without augmentation
- `occupation_ai_effects_woaut.csv` — without automation
- `occupation_ai_effects_wosim.csv` — without simplification
- `occupation_ai_effects_onlyaug.csv` — only augmentation
- `occupation_ai_effects_onlyaut.csv` — only automation
- `occupation_ai_effects_onlysim.csv` — only simplification

Combined with the parent-level `occupation_ai_effects.csv` (all channels active) and the pre-AI baseline, these cover the 2³ = 8 Shapley corners.
