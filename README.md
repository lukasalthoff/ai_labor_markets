# Task-Specific Technical Change and Comparative Advantage

## Overview

Despite large estimated productivity gains from AI across a wide range of tasks, the labor market effects are not well understood. This paper develops a methodology to estimate workers' comparative advantage across tasks and the labor market impact of task-biased technical change. We propose and estimate a dynamic general equilibrium model in which workers build multi-dimensional skills and can switch occupations based on their evolving comparative advantage. The model is informed by existing detailed data on tasks in the US labor market and new data on their skill requirements.

The paper is available [here](https://hugoreichardt.com/pdf/tstc_compadvantage.pdf).


Authors: [Lukas Althoff](https://lukasalthoff.com) (Stanford University) & [Hugo Reichardt](https://hugoreichardt.com) (CREI)


## Data

**Model-predicted effects of AI**

  - **[By occupation](data/occupation_impacts/)**: Model-predicted AI effects at the 3-digit SOC level (93 occupations), including pre- and post-AI employment shares, mean wages, and wage bills for two scenarios (generative AI only; generative + physical AI). ([Documentation](data/occupation_impacts/readme_occupation_impacts.md))

  - **[By college major](data/major_impacts/)**: AI-induced changes in returns to 62 college majors, constructed via a direct major-task-skill mapping using the [Course-Skill Atlas](https://www.nature.com/articles/s41597-024-03931-8). ([Documentation](data/major_impacts/readme_major_impacts.md))


## Version history

### Version 1.0

- Added occupation-level AI impacts dataset (93 occupations at 3-digit SOC level) with documentation
- Added major-level AI impacts dataset (62 fields of study) with documentation


## Citation

```bibtex
@unpublished{tstc2026,
  title   = {Task-Specific Technical Change and Comparative Advantage},
  author  = {Althoff, Lukas and Reichardt, Hugo},
  year    = {2026},
  note    = {Working paper}
}
```