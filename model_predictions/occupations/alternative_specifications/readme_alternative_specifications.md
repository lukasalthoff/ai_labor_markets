# Model Predictions — Alternative Specifications

[Back to main README](../../../README.md)

This folder holds alternative AI-scenario × model variants of the structural-model occupation-level predictions. The headline (canonical) data at the parent folder ([`../occupation_ai_effects.csv`](../occupation_ai_effects.csv)) uses model inputs from **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** 2030 AI scenario.

Each variant ships `occupation_ai_effects.csv` in the same schema as the canonical.

## Layout (AI scenario first, then model)

```
no_explicit_scenario/        # Model rated without any 2030 AI-scenario system message
  gpt4o/
  qwen2.5-72b-awq/
slow/                        # Slow 2030 AI-progress trajectory
  qwen2.5-72b-awq/
rapid/                       # Rapid 2030 AI-progress trajectory
  qwen2.5-72b-awq/
```

The moderate scenario (Qwen) is the canonical headline at the parent level and is not duplicated here.

## Variants by AI scenario

### No explicit scenario

| Model | Notes |
|---|---|
| `gpt4o/` | GPT-4o, the previous (v1.2) release |
| `qwen2.5-72b-awq/` | Qwen-2.5-72B-Instruct-AWQ baseline (no scenario conditioning) |

### Slow / Rapid 2030

| Model | Slow | Rapid |
|---|---|---|
| `qwen2.5-72b-awq/` | ✅ | ✅ |

The gpt-oss model has not been propagated through the structural model. See [`../../../ai_capabilities/alternative_specifications/`](../../../ai_capabilities/alternative_specifications/) for gpt-oss task-level capabilities.
