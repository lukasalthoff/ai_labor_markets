# College Major-Level AI Effects

[Back to main README](../../README.md)

## Overview

This dataset contains model-predicted AI effects on the returns to college majors. The data underlies Figure A20 in the paper, which ranks fields of study by their predicted AI-induced change in wage returns. The mapping from majors to AI effects uses a direct major-task-skill mapping based on course-level skill requirements from the [Course-Skill Atlas](https://www.nature.com/articles/s41597-024-03931-8) (Javadian Sabet et al., 2024), combined with the model's predicted changes in returns to skills.

## File

- [`major_ai_effects.csv`](major_ai_effects.csv) -- 62 fields of study

## Variables

| Variable | Description |
|---|---|
| `field_name` | Name of the field of study (following the taxonomy in Javadian Sabet et al., 2024) |
| `rel_ch_meanwage` | AI-induced change in mean wage return to the major (weighted average of skill-level wage changes, weighted by the major's skill intensity) |
| `rel_ch_meanwage_centered` | Standardized version: `(rel_ch_meanwage - mean) / sd` across all majors, then multiplied by 100 for the figure |
| `rank` | Rank from highest (1 = most positive effect) to lowest |

## Methodology

1. **Major-to-skill mapping:** Each major's skill intensity is scored across 5 broad skill dimensions (math, social, technical, verbal, manual) using course-level data from the [Course-Skill Atlas](https://www.nature.com/articles/s41597-024-03931-8), averaged across all universities and all available years.

2. **Skill-to-wage-change mapping:** The model predicts AI-induced changes in the return to each skill dimension (coefficients from a regression of AI-induced welfare gains on skill levels, without controlling for learning ability). For the canonical Qwen-2.5-72B-Instruct-AWQ × moderate 2030 scenario, the skill-level wage changes (per 1-unit increase on the 1–7 O*NET scale) are:
   - Manual: -0.249%
   - Math: -0.244%
   - Social: -0.316%
   - Technical: -0.427%
   - Verbal: -0.822%

3. **Major-level effect:** The AI-induced wage change for each major is the weighted average of skill-level wage changes, weighted by the major's skill intensity scores.

## Crosswalking to CIP Codes

The field names follow the taxonomy from Javadian Sabet et al. (2024) and can be crosswalked to CIP (Classification of Instructional Programs) codes for use with data sources such as the National Student Clearinghouse.

## Source

Althoff, Lukas and Hugo Reichardt. "Task-Specific Technical Change and Comparative Advantage." Working Paper, 2026.
