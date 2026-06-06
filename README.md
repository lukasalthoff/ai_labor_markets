# Task-Specific Technical Change and Comparative Advantage

**Data release v1.3**

## Overview

Despite large estimated productivity gains from AI across a wide range of tasks, the labor market effects are not well understood. This paper develops a methodology to estimate workers' comparative advantage across tasks and the labor market effects of task-biased technical change. We propose and estimate a dynamic general equilibrium model in which workers build multi-dimensional skills and can switch occupations based on their evolving comparative advantage. The model is informed by existing detailed data on tasks in the US labor market and new data on their skill requirements.

The paper is available [here](https://hugoreichardt.com/pdf/tstc_compadvantage.pdf).


Authors: [Lukas Althoff](https://lukasalthoff.com) (Stanford University) & [Hugo Reichardt](https://hugoreichardt.com) (CREI)


## Datasets

The canonical headline data are derived from **Qwen-2.5-72B-Instruct-AWQ** scored under the **moderate** 2030 [Forecasting Research Institute](https://forecastingresearch.org/) (FRI) scenario (Karger, Atanasov, Tetlock, *et al.*, 2024). Alternative model × scenario variants — including the previous GPT-4o release and three other Qwen FRI scenarios — live under `alternative_specifications/` inside each dataset folder.

### Model-predicted effects of AI

  - **[By occupation](model_predictions/occupations/)**: Model-predicted AI effects at the 3-digit SOC level (93 occupations), including pre- and post-AI employment shares, mean wages, and wage bills. ([Documentation](model_predictions/occupations/readme_occupations.md))

  - **[By college major](model_predictions/college_majors/)**: AI-induced changes in returns to 62 college majors, constructed via a direct major-task-skill mapping using the [Course-Skill Atlas](https://www.nature.com/articles/s41597-024-03931-8). ([Documentation](model_predictions/college_majors/readme_college_majors.md))

  - **[Alternative specifications](model_predictions/alternative_specifications/)**: GPT-4o (including the generative + physical-AI / smart-robots columns from the previous release) and Qwen × three other FRI scenarios; Shapley-decomposition corners. ([Documentation](model_predictions/alternative_specifications/readme_alternative_specifications.md))

### AI capabilities at the task level

  - **[Automation, augmentation, and simplification](ai_capabilities/)**: Task-level measures (O*NET) for generative AI; 5- and 35-dimensional skill requirements and skill anchors. The [verbatim LLM prompts](ai_capabilities/prompts/) used to elicit the ratings and [cross-model agreement figures](ai_capabilities/figures/) are included. ([Documentation](ai_capabilities/readme_ai_capabilities.md))

  - **[Alternative specifications](ai_capabilities/alternative_specifications/)**: GPT-4o (with smart-robots columns) and Qwen × three other FRI scenarios. ([Documentation](ai_capabilities/alternative_specifications/readme_alternative_specifications.md))

## Version history

### Version 1.3
June 6, 2026

- Re-derived the canonical task-level AI capabilities and occupation-level AI effects from Qwen-2.5-72B-Instruct-AWQ scored under the FRI moderate 2030 scenario.
- Added [`ai_capabilities/prompts/`](ai_capabilities/prompts/) with the verbatim LLM prompt templates.
- Added [`ai_capabilities/figures/`](ai_capabilities/figures/) with cross-model agreement visualisations.
- Moved the previous v1.2 GPT-4o data and the generative + physical-AI variant to `alternative_specifications/gpt4o/`.
- Added Qwen × {baseline, slow, rapid} variants and Shapley-decomposition corners under `alternative_specifications/qwen2.5-72b-awq/`.

### Version 1.2
February 19, 2025

- Added task-level AI capabilities dataset, including automation, augmentation, and simplification.

### Version 1.1
February 18, 2025

- Corrected estimates of AI-induced changes in returns by college major.

### Version 1.0
February 15, 2025

- Added occupation-level AI effects dataset (93 occupations at 3-digit SOC level) with documentation
- Added college major-level AI effects dataset (62 fields of study) with documentation


## Citation

```bibtex
@unpublished{tstc2026,
  title   = {Task-Specific Technical Change and Comparative Advantage},
  author  = {Althoff, Lukas and Reichardt, Hugo},
  year    = {2026},
  note    = {Working paper}
}
```