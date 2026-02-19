# Task-Level AI Capabilities

[Back to main README](../../../README.md)

## Overview

This folder contains task-level measures of AI capabilities that feed into the model: **automation** (can AI perform the task?), **augmentation** (productivity multiplier when AI assists), and **simplification** (how skill requirements change after AI). The occupation-level AI effects in [model_predictions/occupations/](../occupations/) are built from these task-level data.

Two AI scenarios are reported, consistent with the occupation data:

- **Generative AI:** Automation, augmentation, and simplification from generative AI (e.g., large language models).
- **Generative + physical AI:** Generative AI plus **smart robots**. Smart robots add task-level automation and augmentation beyond generative AI but do **not** further simplify skill requirements (no additional simplification beyond generative AI).

## Files

| File | Description | Rows |
|------|-------------|------|
| [task_ai_capabilities.csv](task_ai_capabilities.csv) | One row per occupation–task: automation and augmentation (genAI and smart robots) | ~19,500 |
| [task_skill_requirements_5d.csv](task_skill_requirements_5d.csv) | Task × 5 skill dimensions: pre- and post-genAI skill requirements | ~97,500 |
| [task_skill_requirements_35d.csv](task_skill_requirements_35d.csv) | Task × 35 O*NET skills: pre- and post-genAI skill requirements | ~684,000 |
| [skill_anchors.csv](skill_anchors.csv) | O*NET skill definitions and rating anchors (levels 2, 4, 6) | 35 |

## Variables

### task_ai_capabilities.csv

| Variable | Description |
|----------|-------------|
| `soc_code` | 3-digit SOC code (e.g., `11-10`), for joining to [occupation_ai_effects.csv](../occupations/occupation_ai_effects.csv) |
| `soc_code_onet` | Full O*NET-SOC code (e.g., `11-1011.00`) |
| `occ_title` | Occupation title |
| `task_id` | O*NET task identifier |
| `task_description` | Task statement text (O*NET) |
| `task_weight` | Task importance weight (theta) used in the model |
| `job_zone` | O*NET Job Zone (1–5, education/experience level) |
| `physical` | Physical task indicator (0/1) |
| `management` | Management task indicator (0/1) |
| `automatable_genai` | Generative AI can automate this task (0/1) |
| `automatable_smart_robots` | Smart robots can automate this task (0/1) |
| `augmentation_genai` | Generative AI productivity multiplier (1 = no gain) |
| `augmentation_smart_robots` | Smart robots productivity multiplier (1 = no gain) |

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

These anchors were used to prompt GPT-4o to rate task–skill requirements on a consistent 1–7 scale.

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

## Rating methodology

Task–skill requirements (pre- and post-genAI) were obtained by prompting GPT-4o to rate each O*NET task on each skill using the 1–7 scale and the anchor examples in [skill_anchors.csv](skill_anchors.csv). Automation and augmentation were obtained from separate GPT-based exercises (see paper for details).

## Crosswalking

The `soc_code` field (3-digit SOC, first 5 characters of the O*NET code) matches the occupation-level file [occupation_ai_effects.csv](../occupations/occupation_ai_effects.csv), so you can join task-level capabilities to occupation-level AI effects.

## Source

Althoff, Lukas and Hugo Reichardt. "Task-Specific Technical Change and Comparative Advantage." Working Paper, 2026.
