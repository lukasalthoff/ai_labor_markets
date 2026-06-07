# LLM Prompts (Verbatim)

[Back to ai_capabilities README](../readme_ai_capabilities.md)

These are the exact prompt templates sent to the LLM (Qwen-2.5-72B-Instruct-AWQ for the canonical estimates; GPT-4o and gpt-oss for alternative specifications) to elicit task-level AI capability ratings.

| File | Dimension measured | Output scale |
|---|---|---|
| [augmentation.txt](augmentation.txt) | Productivity gain (% time saved) when AI assists the task | Integer percentage 0-100 |
| [automation.txt](automation.txt) | Whether AI can fully automate the task (Eloundou et al. T0-T4 rubric) | T0 / T1 / T2 / T3 / T4 |
| [simplification.txt](simplification.txt) | Skill requirement change after AI: rate skill level needed before vs. with AI access | Integers on the 1-7 O*NET scale, one rating each |

Placeholders such as `{title}`, `{task}`, and `{skill_name}` are substituted at request-build time. The 35 O*NET skill anchors used to calibrate the 1-7 scale in `simplification.txt` are listed in [`../skill_anchors.csv`](../skill_anchors.csv).

For the four AI scenarios used in the alternative specifications (slow / moderate / rapid 2030, plus a no-explicit-scenario baseline), the relevant scenario description is prepended as a system message before each user prompt. The verbatim system messages are documented in [`../readme_ai_capabilities.md`](../readme_ai_capabilities.md).
