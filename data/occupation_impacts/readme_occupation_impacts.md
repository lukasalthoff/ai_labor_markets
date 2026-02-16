# Occupation-Level AI Impacts

[Back to main README](../../README.md)

## Overview

This dataset contains model-predicted AI impacts at the 3-digit SOC (Standard Occupational Classification) level. The data underlies Figures A15 and A16 in the paper, which show occupation-level winners and losers from AI in terms of wage bill changes and employment share changes.

Two AI scenarios are reported:
- **Generative AI:** Impacts from generative AI only (augmentation, automation, and simplification of tasks)
- **Generative + physical AI:** Impacts from generative AI combined with physical AI (e.g., robotics)

## File

- [`occupation_ai_impacts.csv`](occupation_ai_impacts.csv) -- 93 occupations at the 3-digit SOC level, 26 variables

## Variables

### Identification

| Variable | Description |
|---|---|
| `soc_code` | 3-digit SOC code (e.g., `11-10`), 2010 SOC system |
| `occ_title` | Occupation title at the 3-digit SOC level |
| `occ_group` | Major occupation group (1-digit SOC level) |
| `tot_employment` | Total employment (from BLS Occupational Employment Statistics) |

### Model Outputs: Pre-AI Steady State

| Variable | Description |
|---|---|
| `emp_share_pre` | Employment share |
| `mean_wage_pre` | Mean wage (model units) |
| `wage_bill_pre` | Wage bill (= employment share x mean wage) |
| `price_pre` | Output price |

### Model Outputs: Post-AI Steady State (Generative AI)

| Variable | Description |
|---|---|
| `emp_share_post_genai` | Employment share |
| `mean_wage_post_genai` | Mean wage |
| `wage_bill_post_genai` | Wage bill |
| `price_post_genai` | Output price |

### Model Outputs: Post-AI Steady State (Generative + Physical AI)

| Variable | Description |
|---|---|
| `emp_share_post_gen_plus_physical_ai` | Employment share |
| `mean_wage_post_gen_plus_physical_ai` | Mean wage |
| `wage_bill_post_gen_plus_physical_ai` | Wage bill |

### Percentage Changes (Generative AI)

| Variable | Description |
|---|---|
| `pct_ch_mean_wage_genai` | Percent change in mean wage |
| `pct_ch_emp_share_genai` | Percent change in employment share |
| `pct_ch_wage_bill_genai` | Percent change in wage bill |

### Percentage Changes (Generative + Physical AI)

| Variable | Description |
|---|---|
| `pct_ch_mean_wage_gen_plus_physical_ai` | Percent change in mean wage |
| `pct_ch_emp_share_gen_plus_physical_ai` | Percent change in employment share |
| `pct_ch_wage_bill_gen_plus_physical_ai` | Percent change in wage bill |

### Skill Requirements

Occupation-level skill intensities (5-dimensional), averaged across tasks within each occupation.

| Variable | Description |
|---|---|
| `skill_math` | Mathematical skill intensity |
| `skill_social` | Social skill intensity |
| `skill_technical` | Technical skill intensity |
| `skill_verbal` | Verbal skill intensity |
| `skill_manual` | Manual skill intensity |

## Crosswalking to Other Classifications

The `soc_code` field uses the 2010 SOC system at the 3-digit (minor group) level. Standard crosswalks from BLS or the Census can be used to map these to other classification systems (e.g., CIP codes for fields of study via the SOC-CIP crosswalk from NCES).

## Source

Althoff, Lukas and Hugo Reichardt. "Task-Specific Technical Change and Comparative Advantage." Working Paper, 2024.
