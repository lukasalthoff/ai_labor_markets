#!/usr/bin/env python3
"""Build canonical top-level data files from Qwen-moderate raw outputs.

Reproduces:
  ai_capabilities/task_ai_capabilities.csv          (genAI only; drops smart_robots)
  ai_capabilities/task_skill_requirements_5d.csv
  ai_capabilities/task_skill_requirements_35d.csv
  model_predictions/occupations/occupation_ai_effects.csv  (genAI only; drops gen+physical)

The canonical headline scenario is Qwen-2.5-72B-Instruct-AWQ scored under the
"moderate" FRI scenario (Karger et al.). GPT-4o-derived variants are preserved
under alternative_specifications/gpt4o/. Smart-robots / gen+physical_AI columns
are dropped from the canonical because Qwen was never run on smart_robots.

Inputs (paths relative to PROJ below):
  data/task_skill_validation/full_qwen/task_skill_qwen_{automation,augmentation,simplification}_moderate_full.csv
  model_moments/moments_occ_{preai,genai_qwen_moderate}_standardces.csv

Plus, for the metadata columns that don't change across model/scenario:
  ai_capabilities/task_ai_capabilities.csv         (existing repo file -> task metadata)
  model_predictions/occupations/occupation_ai_effects.csv  (existing repo file -> occ metadata)

Run from the repo root:
    python3 scripts/build_canonical_qwen_moderate.py
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd


# 35 -> 5 skill cluster mapping (verbatim from code/stata/1a_task_skills.do in the
# project repo; also used in build_qwen_matlab_inputs.R). Skills NOT in this map
# are kept in 35d output but excluded from the 5d aggregation.
CLUSTER_MAP = {
    "Mathematics": "math",
    "Active Listening": "social",
    "Coordination": "social",
    "Instructing": "social",
    "Management of Personnel Resources": "social",
    "Negotiation": "social",
    "Persuasion": "social",
    "Service Orientation": "social",
    "Social Perceptiveness": "social",
    "Equipment Maintenance": "manual",
    "Equipment Selection": "manual",
    "Installation": "manual",
    "Repairing": "manual",
    "Complex Problem Solving": "technical",
    "Programming": "technical",
    "Quality Control Analysis": "technical",
    "Science": "technical",
    "Systems Analysis": "technical",
    "Systems Evaluation": "technical",
    "Technology Design": "technical",
    "Troubleshooting": "technical",
    "Judgment and Decision Making": "technical",
    "Operation and Control": "technical",
    "Operations Analysis": "technical",
    "Operations Monitoring": "technical",
    "Reading Comprehension": "verbal",
    "Speaking": "verbal",
    "Writing": "verbal",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--source-project",
        default="/Users/lalthoff/US Inequality Dropbox/Lukas Althoff/writing/2024_ai_labormarket",
        help="Path to the local project producing the Qwen raw outputs.",
    )
    p.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Path to this repo's root (where outputs will be written).",
    )
    return p.parse_args()


def build_task_ai_capabilities(proj: Path, repo: Path) -> pd.DataFrame:
    """task_ai_capabilities.csv: one row per (occ, task); columns automatable_genai
    and augmentation_genai from Qwen-moderate. Metadata cols come from the
    existing repo file (these are model-independent O*NET task properties)."""

    # Metadata from existing file
    meta = pd.read_csv(repo / "ai_capabilities" / "task_ai_capabilities.csv")
    meta_cols = [
        "soc_code", "soc_code_onet", "occ_title", "task_id", "task_description",
        "task_weight", "job_zone", "physical", "management",
    ]
    meta = meta[meta_cols].copy()

    # Qwen-moderate automation: T3 or T4 -> 1, else 0 (response_numeric >= 0.75)
    auto = pd.read_csv(
        proj / "data/task_skill_validation/full_qwen/task_skill_qwen_automation_moderate_full.csv",
        usecols=["soc_code_onet", "taskid", "response_numeric"],
    )
    auto = auto.rename(columns={"taskid": "task_id"})
    auto["automatable_genai"] = (auto["response_numeric"] >= 0.75).astype(int)
    auto = auto[["soc_code_onet", "task_id", "automatable_genai"]]

    # Qwen-moderate augmentation: 1 + response/100  (matches existing schema)
    aug = pd.read_csv(
        proj / "data/task_skill_validation/full_qwen/task_skill_qwen_augmentation_moderate_full.csv",
        usecols=["soc_code_onet", "taskid", "response"],
    )
    aug = aug.rename(columns={"taskid": "task_id"})
    aug["augmentation_genai"] = 1 + aug["response"].astype(float) / 100.0
    aug = aug[["soc_code_onet", "task_id", "augmentation_genai"]]

    out = (
        meta
        .merge(auto, on=["soc_code_onet", "task_id"], how="left")
        .merge(aug, on=["soc_code_onet", "task_id"], how="left")
    )
    return out


def build_skill_requirements_35d(proj: Path) -> pd.DataFrame:
    """task_skill_requirements_35d.csv: one row per (occ, task, skill); pre and
    post-genAI skill requirements (1-7 scale) from Qwen-moderate."""

    sim = pd.read_csv(
        proj / "data/task_skill_validation/full_qwen/task_skill_qwen_simplification_moderate_full.csv",
        usecols=["soc_code_onet", "taskid", "skill", "response_before", "response_after"],
    )
    sim = sim.rename(columns={
        "taskid": "task_id",
        "response_before": "skill_requirement_pre",
        "response_after": "skill_requirement_post_genai",
    })

    # Bring in occ_title and soc_code (5-char) from existing repo task_ai_capabilities,
    # so the output schema matches the existing 35d file.
    meta = (
        pd.read_csv(Path(__file__).resolve().parent.parent / "ai_capabilities" / "task_ai_capabilities.csv",
                    usecols=["soc_code", "soc_code_onet", "occ_title", "task_id"])
        .drop_duplicates(["soc_code_onet", "task_id"])
    )
    sim = sim.merge(meta, on=["soc_code_onet", "task_id"], how="left")

    # Tag the skill cluster (or blank for 7 skills outside the 5d model)
    sim["skill_cluster"] = sim["skill"].map(CLUSTER_MAP).fillna("")
    # Capitalize for the cluster column to match existing convention
    cap_map = {"math": "Math", "social": "Social", "manual": "Manual",
               "technical": "Technical", "verbal": "Verbal", "": ""}
    sim["skill_cluster"] = sim["skill_cluster"].map(cap_map)

    out = sim[[
        "soc_code", "soc_code_onet", "occ_title", "task_id", "skill",
        "skill_cluster", "skill_requirement_pre", "skill_requirement_post_genai",
    ]].copy()
    return out


def build_skill_requirements_5d(df_35d: pd.DataFrame) -> pd.DataFrame:
    """task_skill_requirements_5d.csv: aggregate the 35 O*NET skills to 5 clusters.
    Within each (occ, task, cluster), take the unweighted mean of the per-skill
    pre/post requirements. The 7 skills with no cluster are dropped."""

    df = df_35d[df_35d["skill_cluster"] != ""].copy()
    cluster_lower = {"Math": "math", "Social": "social", "Manual": "manual",
                     "Technical": "technical", "Verbal": "verbal"}
    df["skill"] = df["skill_cluster"].map(cluster_lower)

    agg = (
        df.groupby(["soc_code", "soc_code_onet", "occ_title", "task_id", "skill"], as_index=False)
          .agg(skill_requirement_pre=("skill_requirement_pre", "mean"),
               skill_requirement_post_genai=("skill_requirement_post_genai", "mean"))
    )
    return agg[["soc_code", "soc_code_onet", "occ_title", "task_id", "skill",
                "skill_requirement_pre", "skill_requirement_post_genai"]]


def build_occupation_ai_effects(proj: Path, repo: Path,
                                 task_ai: pd.DataFrame, sk_5d: pd.DataFrame) -> pd.DataFrame:
    """occupation_ai_effects.csv: one row per 93 occupations (3-digit SOC). Drops
    the gen+physical_AI columns. Skill intensities are recomputed from
    Qwen-moderate's pre-AI skill requirements (weighted by task_weight)."""

    # Existing file -> occupation metadata (occ_group, tot_employment, occ_title)
    existing = pd.read_csv(
        repo / "model_predictions" / "occupations" / "occupation_ai_effects.csv",
        usecols=["soc_code", "occ_title", "occ_group", "tot_employment"],
    )

    # moments_occ_preai -> emp_share_pre, mean_wage_pre, wage_bill_pre, price_pre
    pre = pd.read_csv(
        proj / "model_moments" / "moments_occ_preai_standardces.csv",
        usecols=["soc_code", "share", "meanwage", "p"],
    ).rename(columns={"share": "emp_share_pre", "meanwage": "mean_wage_pre", "p": "price_pre"})
    pre["wage_bill_pre"] = pre["emp_share_pre"] * pre["mean_wage_pre"]

    # moments_occ_genai_qwen_moderate -> post_genai columns
    post = pd.read_csv(
        proj / "model_moments" / "moments_occ_genai_qwen_moderate_standardces.csv",
        usecols=["soc_code", "share", "meanwage", "p"],
    ).rename(columns={"share": "emp_share_post_genai", "meanwage": "mean_wage_post_genai",
                      "p": "price_post_genai"})
    post["wage_bill_post_genai"] = post["emp_share_post_genai"] * post["mean_wage_post_genai"]

    # Trim trailing 0s in soc_code if needed; both should already be 5-char (e.g. "11-10")
    occ_eff = (
        existing
        .merge(pre, on="soc_code", how="inner")
        .merge(post, on="soc_code", how="inner")
    )

    occ_eff["pct_ch_mean_wage_genai"]   = (occ_eff["mean_wage_post_genai"]   - occ_eff["mean_wage_pre"])   / occ_eff["mean_wage_pre"]
    occ_eff["pct_ch_emp_share_genai"]   = (occ_eff["emp_share_post_genai"]   - occ_eff["emp_share_pre"])   / occ_eff["emp_share_pre"]
    occ_eff["pct_ch_wage_bill_genai"]   = (occ_eff["wage_bill_post_genai"]   - occ_eff["wage_bill_pre"])   / occ_eff["wage_bill_pre"]

    # Occupation-level skill intensities from Qwen-moderate pre-AI 5d data,
    # task-weight-weighted means within (soc_code, skill).
    task_w = task_ai[["soc_code", "soc_code_onet", "task_id", "task_weight"]]
    intens_src = sk_5d.merge(task_w, on=["soc_code", "soc_code_onet", "task_id"], how="left")
    intens_src = intens_src.dropna(subset=["task_weight"])
    intens_src["weighted"] = intens_src["skill_requirement_pre"] * intens_src["task_weight"]
    grp = intens_src.groupby(["soc_code", "skill"]).agg(
        num=("weighted", "sum"),
        den=("task_weight", "sum"),
    )
    grp["intensity"] = grp["num"] / grp["den"]
    intens = grp[["intensity"]].unstack("skill")
    intens.columns = [f"skill_{c}" for _, c in intens.columns]
    intens = intens.reset_index()

    occ_eff = occ_eff.merge(intens, on="soc_code", how="left")

    # Final column order (matches existing schema minus the gen+physical cols)
    col_order = [
        "soc_code", "occ_title", "occ_group", "tot_employment",
        "emp_share_pre", "mean_wage_pre", "wage_bill_pre", "price_pre",
        "emp_share_post_genai", "mean_wage_post_genai", "wage_bill_post_genai", "price_post_genai",
        "pct_ch_mean_wage_genai", "pct_ch_emp_share_genai", "pct_ch_wage_bill_genai",
        "skill_math", "skill_social", "skill_technical", "skill_verbal", "skill_manual",
    ]
    return occ_eff[[c for c in col_order if c in occ_eff.columns]]


def main() -> None:
    args = parse_args()
    proj = Path(args.source_project)
    repo = Path(args.repo_root)

    if not proj.exists():
        sys.exit(f"source project not found: {proj}")

    print(f"[build] source project: {proj}")
    print(f"[build] repo root:      {repo}")

    print("[build] task_ai_capabilities.csv ...", flush=True)
    task_ai = build_task_ai_capabilities(proj, repo)
    out = repo / "ai_capabilities" / "task_ai_capabilities.csv"
    task_ai.to_csv(out, index=False)
    print(f"  -> {out}  ({len(task_ai):,} rows)")

    print("[build] task_skill_requirements_35d.csv ...", flush=True)
    sk_35d = build_skill_requirements_35d(proj)
    out = repo / "ai_capabilities" / "task_skill_requirements_35d.csv"
    sk_35d.to_csv(out, index=False)
    print(f"  -> {out}  ({len(sk_35d):,} rows)")

    print("[build] task_skill_requirements_5d.csv ...", flush=True)
    sk_5d = build_skill_requirements_5d(sk_35d)
    out = repo / "ai_capabilities" / "task_skill_requirements_5d.csv"
    sk_5d.to_csv(out, index=False)
    print(f"  -> {out}  ({len(sk_5d):,} rows)")

    print("[build] occupation_ai_effects.csv ...", flush=True)
    occ_eff = build_occupation_ai_effects(proj, repo, task_ai, sk_5d)
    out = repo / "model_predictions" / "occupations" / "occupation_ai_effects.csv"
    occ_eff.to_csv(out, index=False)
    print(f"  -> {out}  ({len(occ_eff):,} rows)")

    print("[build] done.")


if __name__ == "__main__":
    main()
