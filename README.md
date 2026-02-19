# Task-Specific Technical Change and Comparative Advantage

**Data release v1.2**

## Overview

Despite large estimated productivity gains from AI across a wide range of tasks, the labor market effects are not well understood. This paper develops a methodology to estimate workers' comparative advantage across tasks and the labor market effects of task-biased technical change. We propose and estimate a dynamic general equilibrium model in which workers build multi-dimensional skills and can switch occupations based on their evolving comparative advantage. The model is informed by existing detailed data on tasks in the US labor market and new data on their skill requirements.

The paper is available [here](https://hugoreichardt.com/pdf/tstc_compadvantage.pdf).


Authors: [Lukas Althoff](https://lukasalthoff.com) (Stanford University) & [Hugo Reichardt](https://hugoreichardt.com) (CREI)


## Datasets

### Model-predicted effects of AI

  - **[By occupation](model_predictions/occupations/)**: Model-predicted AI effects at the 3-digit SOC level (93 occupations), including pre- and post-AI employment shares, mean wages, and wage bills for two scenarios (generative AI only; generative + physical AI). ([Documentation](model_predictions/occupations/readme_occupations.md))

  - **[By college major](model_predictions/college_majors/)**: AI-induced changes in returns to 62 college majors, constructed via a direct major-task-skill mapping using the [Course-Skill Atlas](https://www.nature.com/articles/s41597-024-03931-8). ([Documentation](model_predictions/college_majors/readme_college_majors.md))

### AI capabilities at the task level

  - **[Automation, augmentation, and simplification](ai_capabilities/)**: Task-level measures (O*NET) for generative AI and smart robots; 5- and 35-dimensional skill requirements and skill anchors. ([Documentation](ai_capabilities/readme_ai_capabilities.md))

## Version history

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