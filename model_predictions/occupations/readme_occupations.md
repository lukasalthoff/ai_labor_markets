# Occupation-Level AI Effects

[Back to main README](../../README.md)

## Overview

This dataset contains model-predicted AI effects at the 3-digit SOC (Standard Occupational Classification) level. The data underlies the headline winners-and-losers figures in the paper (wage bill changes and employment-share changes by occupation).

## Canonical headline scenario

The file [`occupation_ai_effects.csv`](occupation_ai_effects.csv) at the top of this folder is the **canonical** headline data, derived from:

- **AI capabilities:** [Qwen-2.5-72B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-AWQ) (open-weight, Alibaba) scored under the **moderate** 2030 [FRI](https://forecastingresearch.org/) scenario (Karger, Atanasov, Tetlock, *et al.*, 2024)
- **Structural model:** steady-state of the dynamic general-equilibrium model with comparative advantage and switching costs, fed with the Qwen-moderate task-level AI capabilities

Alternative model × scenario variants (GPT-4o + the other three Qwen FRI scenarios), as well as the Shapley-decomposition corners needed to attribute effects to augmentation / automation / simplification, live under [`../alternative_specifications/`](../alternative_specifications/).

## File

- [`occupation_ai_effects.csv`](occupation_ai_effects.csv) — 93 occupations at the 3-digit SOC level

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
| `wage_bill_pre` | Wage bill (= employment share × mean wage) |
| `price_pre` | Output price |

### Model Outputs: Post-AI Steady State (Generative AI)

| Variable | Description |
|---|---|
| `emp_share_post_genai` | Employment share |
| `mean_wage_post_genai` | Mean wage |
| `wage_bill_post_genai` | Wage bill |
| `price_post_genai` | Output price |

### Percentage Changes (Generative AI)

| Variable | Description |
|---|---|
| `pct_ch_mean_wage_genai` | Percent change in mean wage |
| `pct_ch_emp_share_genai` | Percent change in employment share |
| `pct_ch_wage_bill_genai` | Percent change in wage bill |

### Skill Requirements

Occupation-level skill intensities (5-dimensional), task-weight-weighted means within each occupation, on the 1–7 scale (Qwen-moderate pre-AI ratings).

| Variable | Description |
|---|---|
| `skill_math` | Mathematical skill intensity |
| `skill_social` | Social skill intensity |
| `skill_technical` | Technical skill intensity |
| `skill_verbal` | Verbal skill intensity |
| `skill_manual` | Manual skill intensity |

The generative-+-physical-AI (smart robots) columns from the previous release are not included in the canonical file because the Qwen rescore covers generative AI only. The GPT-4o variant in [`../alternative_specifications/gpt4o/`](../alternative_specifications/gpt4o/) retains them.

## Reproduction

The canonical CSV was assembled from the Qwen-moderate steady-state simulation outputs of the structural model. The model itself is documented in the working-paper appendix.

## Crosswalking to Other Classifications

The `soc_code` field uses the 2010 SOC system at the 3-digit (minor group) level. Standard crosswalks from BLS or the Census can be used to map these to other classification systems (e.g., CIP codes for fields of study via the SOC-CIP crosswalk from NCES).

## Source

Althoff, Lukas and Hugo Reichardt. "Task-Specific Technical Change and Comparative Advantage." Working Paper, 2026.
