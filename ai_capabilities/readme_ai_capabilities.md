# Task-Level AI Capabilities

[Back to main README](../README.md)

## Overview

This folder contains task-level measures of AI capabilities that feed into the model: **automation** (can AI perform the task?), **augmentation** (productivity multiplier when AI assists), and **simplification** (how skill requirements change after AI). The occupation-level AI effects in [model_predictions/occupations/](../model_predictions/occupations/) are built from these task-level data.

## Canonical headline scenario (top of this folder)

The four CSV files at the top of this folder are the **canonical** headline data, derived from:

- **Model:** [Qwen-2.5-72B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-AWQ) (open-weight, Alibaba)
- **AI scenario:** **moderate** 2030 AI-progress trajectory (Karger, Atanasov, Tetlock, *et al.*, 2024)

Alternative AI-scenario × model variants — GPT-4o and OpenAI gpt-oss without an explicit scenario, plus Qwen and gpt-oss under each of the other 2030 scenarios — live under [`alternative_specifications/`](alternative_specifications/).

## Files

| File | Description | Rows |
|------|-------------|------|
| [task_ai_capabilities.csv](task_ai_capabilities.csv) | One row per occupation–task: automation (0/1) and augmentation (productivity multiplier) | 19,530 |
| [task_skill_requirements_5d.csv](task_skill_requirements_5d.csv) | Task × 5 skill dimensions: pre- and post-genAI skill requirements | 97,650 |
| [task_skill_requirements_35d.csv](task_skill_requirements_35d.csv) | Task × 35 O*NET skills: pre- and post-genAI skill requirements | 683,550 |
| [skill_anchors.csv](skill_anchors.csv) | O*NET skill definitions and rating anchors (levels 2, 4, 6) | 35 |
| [prompts/](prompts/) | Verbatim LLM prompt templates used to elicit the ratings | 3 files |
| [figures/](figures/) | Cross-model agreement figures | 3 files |
| [alternative_specifications/](alternative_specifications/) | Variants grouped by 2030 AI scenario × model (GPT-4o, Qwen, gpt-oss) | — |

## Variables

### task_ai_capabilities.csv

| Variable | Description |
|----------|-------------|
| `soc_code` | 3-digit SOC code (e.g., `11-10`), for joining to [occupation_ai_effects.csv](../model_predictions/occupations/occupation_ai_effects.csv) |
| `soc_code_onet` | Full O*NET-SOC code (e.g., `11-1011.00`) |
| `occ_title` | Occupation title |
| `task_id` | O*NET task identifier |
| `task_description` | Task statement text (O*NET) |
| `task_weight` | Task importance weight (theta) used in the model |
| `job_zone` | O*NET Job Zone (1–5, education/experience level) |
| `physical` | Physical task indicator (0/1) |
| `management` | Management task indicator (0/1) |
| `automatable_genai` | Generative AI can automate this task (0/1, =1 if Qwen rated T3 or T4) |
| `augmentation_genai` | Generative AI productivity multiplier (1 = no gain) |

Smart-robots / generative + physical AI columns from the previous v1.2 release are not included in v1.3.

### task_skill_requirements_5d.csv

| Variable | Description |
|----------|-------------|
| `soc_code`, `soc_code_onet`, `occ_title`, `task_id` | Same as above |
| `skill` | Aggregated skill dimension: `manual`, `math`, `social`, `technical`, `verbal` |
| `skill_requirement_pre` | Pre-AI skill requirement (1–7 scale) |
| `skill_requirement_post_genai` | Post–generative AI skill requirement (1–7 scale) |

The **simplification** effect is `skill_requirement_post_genai - skill_requirement_pre` (negative = skill requirement falls).

### task_skill_requirements_35d.csv

| Variable | Description |
|----------|-------------|
| `soc_code`, `soc_code_onet`, `occ_title`, `task_id` | Same as above |
| `skill` | O*NET skill name (e.g., Reading Comprehension, Mathematics) |
| `skill_cluster` | Aggregate dimension this skill maps to (Math, Social, Manual, Technical, Verbal), or blank for skills not used in the 5d model |
| `skill_requirement_pre` | Pre-AI skill requirement (1–7) |
| `skill_requirement_post_genai` | Post–generative AI skill requirement (1–7) |

### skill_anchors.csv

| Variable | Description |
|----------|-------------|
| `skill` | O*NET skill name |
| `skill_cluster` | Aggregate dimension (or blank) |
| `definition` | O*NET skill definition |
| `anchor_level_2` | Example task at level 2 on the 1–7 scale |
| `anchor_level_4` | Example task at level 4 |
| `anchor_level_6` | Example task at level 6 |

These anchors are referenced inside the simplification prompt to calibrate ratings on a consistent 1–7 scale across both models.

## Skill aggregation: 35 O*NET skills to 5 dimensions

The 5-dimensional skill classification used in the model aggregates 28 of the 35 O*NET skills as follows. The remaining 7 skills are not used in the 5d model (they are still in the 35d file and in [skill_anchors.csv](skill_anchors.csv)).

| Cluster | O*NET skills |
|---------|---------------|
| **Math** | Mathematics |
| **Social** | Active Listening, Coordination, Instructing, Management of Personnel Resources, Negotiation, Persuasion, Service Orientation, Social Perceptiveness |
| **Manual** | Equipment Maintenance, Equipment Selection, Installation, Repairing |
| **Technical** | Complex Problem Solving, Judgment and Decision Making, Operation and Control, Operations Analysis, Operations Monitoring, Programming, Quality Control Analysis, Science, Systems Analysis, Systems Evaluation, Technology Design, Troubleshooting |
| **Verbal** | Reading Comprehension, Speaking, Writing |
| *(not in 5d)* | Active Learning, Critical Thinking, Learning Strategies, Management of Financial Resources, Management of Material Resources, Monitoring, Time Management |

## Models

We score each (occupation, task) — and for simplification each (occupation, task, skill) — through three LLMs:

- **GPT-4o** (closed, OpenAI). Ratings are unconditioned (no explicit AI scenario). The GPT-4o data is the version-1.2 publication baseline; it lives under [`alternative_specifications/no_explicit_scenario/gpt4o/`](alternative_specifications/no_explicit_scenario/gpt4o/).
- **Qwen-2.5-72B-Instruct-AWQ** (open, Alibaba). Ratings are conditioned on each of four AI scenarios (no explicit scenario / slow / moderate / rapid 2030). The Qwen-moderate variant is the canonical headline data at the top of this folder; the other three are under [`alternative_specifications/`](alternative_specifications/).
- **gpt-oss** (open, OpenAI). Same four AI scenarios as Qwen. All variants live under [`alternative_specifications/`](alternative_specifications/).

## AI scenario system messages (verbatim)

These are prepended as system messages to each Qwen and gpt-oss request. They are not used for GPT-4o or for the `no_explicit_scenario` variant of any model.

> **Slow 2030.** AI is a capable assisting technology for humans: writing literature reviews at the level of a capable PhD student, handling half of all freelance software-engineering jobs that would take an experienced human a day to complete, topping up your online grocery cart, and physically being able to unload dishwashers in some homes.

> **Moderate 2030.** AI is an effective collaborator across domains: autonomous lab systems can make rapid advances in solar-cell technology; almost all freelance software-engineering jobs requiring 5 days of effort from an experienced human are automatable; robots can do dishes as quickly as humans; robo-taxis can drive anywhere that humans can.

> **Rapid 2030.** AI systems surpass humans in most cognitive and physical tasks. Autonomous researchers can collapse years-long research timelines into months or even days. AI systems can surpass all freelance software engineers, customer service agents, paralegals, and clerical workers. Models can write 2025-Pulitzer-caliber books—and negotiate the resulting book contract. Robots can assist in an arbitrary home or factory anywhere in the world.

Source: Karger, Atanasov, Tetlock, *et al.*, "Forecasting the Economic Effects of AI," 2024 (Forecasting Research Institute).

## Cross-model agreement

The three figures in [`figures/`](figures/) summarise how the LLM-derived measures agree across models and against external references (O*NET, human raters):

- [`onet_correlation_35skills.pdf`](figures/onet_correlation_35skills.pdf) — for each of the 35 O*NET skills, the bar shows the correlation between LLM-aggregated occupation-level skill requirements and the official O*NET skill levels. GPT-4o and Qwen track O*NET closely and similarly.
- [`multi_llm_heatmap_pre.pdf`](figures/multi_llm_heatmap_pre.pdf) — 6×6 correlation matrix of pre-AI skill ratings across two human raters (Faculty 1 and Faculty 2), the human average, GPT-4o, Qwen, and a pooled mean, on 200 task–skill pairs in the Economists occupation.
- [`multi_llm_heatmap_post.pdf`](figures/multi_llm_heatmap_post.pdf) — same as above for post-AI skill ratings.

## Rating methodology

Each rating dimension is elicited with a dedicated prompt template (see [`prompts/`](prompts/)). At request-build time, the placeholders `{title}`, `{task}`, etc. are substituted, and (for Qwen and gpt-oss) the AI-scenario system message is prepended. Inference uses `temperature=0` and a fixed `seed=42`.

## Reproduction

The canonical CSVs were assembled from the raw Qwen task-skill scoring outputs. The end-to-end scoring pipeline (vLLM, batch inference, JSONL aggregation) is documented in the working-paper repository; the prompts in [`prompts/`](prompts/) are the canonical reference for what the model received.

## Crosswalking

The `soc_code` field (3-digit SOC, first 5 characters of the O*NET code) matches the occupation-level file [occupation_ai_effects.csv](../model_predictions/occupations/occupation_ai_effects.csv), so you can join task-level capabilities to occupation-level AI effects.

## Source

Althoff, Lukas and Hugo Reichardt. "Task-Specific Technical Change and Comparative Advantage." Working Paper, 2026.
