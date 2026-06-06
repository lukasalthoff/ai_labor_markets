#!/usr/bin/env python3
"""Build alternative-specification CSVs for Qwen × {baseline, slow, rapid}.

Mirrors the canonical Qwen-moderate build but writes outputs under
  ai_capabilities/alternative_specifications/qwen2.5-72b-awq/<scenario>/
  model_predictions/alternative_specifications/qwen2.5-72b-awq/<scenario>/

Schema matches the canonical files (genAI-only; no smart-robots columns).

Run from the repo root:
    python3 scripts/build_alternative_specifications.py
"""
from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

# Reuse the canonical build helpers
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_canonical_qwen_moderate import (  # noqa: E402
    CLUSTER_MAP, build_skill_requirements_5d,
)

PROJ = Path("/Users/lalthoff/US Inequality Dropbox/Lukas Althoff/writing/2024_ai_labormarket")
REPO = Path(__file__).resolve().parent.parent

SCENARIOS = ["baseline", "slow", "rapid"]   # moderate is the canonical headline


def build_task_ai_capabilities_for_scen(scen: str) -> pd.DataFrame:
    meta = pd.read_csv(
        REPO / "ai_capabilities" / "alternative_specifications" / "gpt4o" / "task_ai_capabilities.csv",
        usecols=["soc_code", "soc_code_onet", "occ_title", "task_id", "task_description",
                 "task_weight", "job_zone", "physical", "management"],
    )

    auto = pd.read_csv(
        PROJ / f"data/task_skill_validation/full_qwen/task_skill_qwen_automation_{scen}_full.csv",
        usecols=["soc_code_onet", "taskid", "response_numeric"],
    ).rename(columns={"taskid": "task_id"})
    auto["automatable_genai"] = (auto["response_numeric"] >= 0.75).astype(int)

    aug = pd.read_csv(
        PROJ / f"data/task_skill_validation/full_qwen/task_skill_qwen_augmentation_{scen}_full.csv",
        usecols=["soc_code_onet", "taskid", "response"],
    ).rename(columns={"taskid": "task_id"})
    aug["augmentation_genai"] = 1 + aug["response"].astype(float) / 100.0

    out = (
        meta
        .merge(auto[["soc_code_onet", "task_id", "automatable_genai"]],
               on=["soc_code_onet", "task_id"], how="left")
        .merge(aug[["soc_code_onet", "task_id", "augmentation_genai"]],
               on=["soc_code_onet", "task_id"], how="left")
    )
    return out


def build_skill_requirements_35d_for_scen(scen: str) -> pd.DataFrame:
    sim = pd.read_csv(
        PROJ / f"data/task_skill_validation/full_qwen/task_skill_qwen_simplification_{scen}_full.csv",
        usecols=["soc_code_onet", "taskid", "skill", "response_before", "response_after"],
    ).rename(columns={
        "taskid": "task_id",
        "response_before": "skill_requirement_pre",
        "response_after": "skill_requirement_post_genai",
    })

    meta = (
        pd.read_csv(REPO / "ai_capabilities" / "alternative_specifications" / "gpt4o" /
                    "task_ai_capabilities.csv",
                    usecols=["soc_code", "soc_code_onet", "occ_title", "task_id"])
        .drop_duplicates(["soc_code_onet", "task_id"])
    )
    sim = sim.merge(meta, on=["soc_code_onet", "task_id"], how="left")

    sim["skill_cluster"] = sim["skill"].map(CLUSTER_MAP).fillna("")
    cap_map = {"math": "Math", "social": "Social", "manual": "Manual",
               "technical": "Technical", "verbal": "Verbal", "": ""}
    sim["skill_cluster"] = sim["skill_cluster"].map(cap_map)

    return sim[["soc_code", "soc_code_onet", "occ_title", "task_id", "skill",
                "skill_cluster", "skill_requirement_pre", "skill_requirement_post_genai"]]


def build_occupation_ai_effects_for_scen(scen: str, task_ai: pd.DataFrame, sk_5d: pd.DataFrame) -> pd.DataFrame:
    existing = pd.read_csv(
        REPO / "model_predictions" / "alternative_specifications" / "gpt4o" / "occupation_ai_effects.csv",
        usecols=["soc_code", "occ_title", "occ_group", "tot_employment"],
    )

    def to_5char(s: pd.Series) -> pd.Series:
        return s.str.slice(0, 5)

    pre = pd.read_csv(
        PROJ / "model_moments" / "moments_occ_preai_standardces.csv",
        usecols=["soc_code", "share", "meanwage", "p"],
    ).rename(columns={"share": "emp_share_pre", "meanwage": "mean_wage_pre", "p": "price_pre"})
    pre["soc_code"] = to_5char(pre["soc_code"])
    pre["wage_bill_pre"] = pre["emp_share_pre"] * pre["mean_wage_pre"]

    post = pd.read_csv(
        PROJ / f"model_moments/moments_occ_genai_qwen_{scen}_standardces.csv",
        usecols=["soc_code", "share", "meanwage", "p"],
    ).rename(columns={"share": "emp_share_post_genai", "meanwage": "mean_wage_post_genai",
                      "p": "price_post_genai"})
    post["soc_code"] = to_5char(post["soc_code"])
    post["wage_bill_post_genai"] = post["emp_share_post_genai"] * post["mean_wage_post_genai"]

    occ = existing.merge(pre, on="soc_code", how="inner").merge(post, on="soc_code", how="inner")

    occ["pct_ch_mean_wage_genai"] = (occ["mean_wage_post_genai"] - occ["mean_wage_pre"]) / occ["mean_wage_pre"]
    occ["pct_ch_emp_share_genai"] = (occ["emp_share_post_genai"] - occ["emp_share_pre"]) / occ["emp_share_pre"]
    occ["pct_ch_wage_bill_genai"] = (occ["wage_bill_post_genai"] - occ["wage_bill_pre"]) / occ["wage_bill_pre"]

    # Occupation-level skill intensities from scenario's pre-AI requirements.
    # sk_5d's `skill` column is already the lowercase cluster name.
    task_w = task_ai[["soc_code", "soc_code_onet", "task_id", "task_weight"]]
    intens_src = sk_5d.merge(task_w, on=["soc_code", "soc_code_onet", "task_id"], how="left").dropna(subset=["task_weight"])
    intens_src["weighted"] = intens_src["skill_requirement_pre"] * intens_src["task_weight"]
    grp = intens_src.groupby(["soc_code", "skill"]).agg(
        num=("weighted", "sum"), den=("task_weight", "sum"),
    )
    grp["intensity"] = grp["num"] / grp["den"]
    intens = grp[["intensity"]].unstack("skill")
    intens.columns = [f"skill_{c}" for _, c in intens.columns]
    intens = intens.reset_index()

    occ = occ.merge(intens, on="soc_code", how="left")

    col_order = [
        "soc_code", "occ_title", "occ_group", "tot_employment",
        "emp_share_pre", "mean_wage_pre", "wage_bill_pre", "price_pre",
        "emp_share_post_genai", "mean_wage_post_genai", "wage_bill_post_genai", "price_post_genai",
        "pct_ch_mean_wage_genai", "pct_ch_emp_share_genai", "pct_ch_wage_bill_genai",
        "skill_math", "skill_social", "skill_technical", "skill_verbal", "skill_manual",
    ]
    return occ[[c for c in col_order if c in occ.columns]]


def main() -> None:
    print(f"[alt-spec] source project: {PROJ}")
    print(f"[alt-spec] repo root:      {REPO}")

    for scen in SCENARIOS:
        print(f"\n[alt-spec] === {scen} ===")
        cap_dir = REPO / "ai_capabilities" / "alternative_specifications" / "qwen2.5-72b-awq" / scen
        pred_dir = REPO / "model_predictions" / "alternative_specifications" / "qwen2.5-72b-awq" / scen
        cap_dir.mkdir(parents=True, exist_ok=True)
        pred_dir.mkdir(parents=True, exist_ok=True)

        print(f"  task_ai_capabilities.csv ...", flush=True)
        task_ai = build_task_ai_capabilities_for_scen(scen)
        task_ai.to_csv(cap_dir / "task_ai_capabilities.csv", index=False)
        print(f"    -> {cap_dir / 'task_ai_capabilities.csv'}  ({len(task_ai):,} rows)")

        print(f"  task_skill_requirements_35d.csv ...", flush=True)
        sk_35d = build_skill_requirements_35d_for_scen(scen)
        sk_35d.to_csv(cap_dir / "task_skill_requirements_35d.csv", index=False)
        print(f"    -> {cap_dir / 'task_skill_requirements_35d.csv'}  ({len(sk_35d):,} rows)")

        print(f"  task_skill_requirements_5d.csv ...", flush=True)
        sk_5d = build_skill_requirements_5d(sk_35d)
        sk_5d.to_csv(cap_dir / "task_skill_requirements_5d.csv", index=False)
        print(f"    -> {cap_dir / 'task_skill_requirements_5d.csv'}  ({len(sk_5d):,} rows)")

        print(f"  occupation_ai_effects.csv ...", flush=True)
        occ = build_occupation_ai_effects_for_scen(scen, task_ai, sk_5d)
        occ.to_csv(pred_dir / "occupation_ai_effects.csv", index=False)
        print(f"    -> {pred_dir / 'occupation_ai_effects.csv'}  ({len(occ):,} rows)")

    print("\n[alt-spec] done.")


if __name__ == "__main__":
    main()
