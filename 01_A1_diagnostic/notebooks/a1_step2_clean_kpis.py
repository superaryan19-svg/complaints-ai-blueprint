import pandas as pd
import os

IN_PATH = "01_A1_diagnostic/data/clean/bank_complaints_24m.csv"
OUT_CLEAN = "01_A1_diagnostic/data/clean/complaints_clean.csv"
OUT_KPIS = "01_A1_diagnostic/outputs/baseline_kpis.csv"
OUT_RELIEF = "01_A1_diagnostic/outputs/relief_by_issue.csv"

os.makedirs("01_A1_diagnostic/outputs", exist_ok=True)

df = pd.read_csv(IN_PATH, dtype=str)
print(f"Loaded {len(df)} records for cleaning.")

# 1. Types
for col in ["Date received", "Date sent to company"]:
    df[col] = pd.to_datetime(df[col], format="mixed", errors="coerce")

# 2. Duplicates: one row per Complaint ID
before = len(df)
df = df.drop_duplicates(subset="Complaint ID", keep="last")
print("Duplicates removed:", before - len(df))

# 3. Derived fields (flags, never silent fixes)
df["month"] = df["Date received"].dt.to_period("M").astype(str)
df["routing_lag_days"] = (df["Date sent to company"] - df["Date received"]).dt.days
df["flag_bad_dates"] = df["routing_lag_days"].isna() | (df["routing_lag_days"] < 0)
df["timely"] = df["Timely response?"].eq("Yes")
df["relief"] = df["Company response to consumer"].isin(
    ["Closed with monetary relief", "Closed with non-monetary relief"]
)
df["has_narrative"] = df["Consumer complaint narrative"].fillna("").str.strip().ne("")

# 4. Baseline KPI table
months = df["month"].nunique()
kpis = {
    "Complaints in window": len(df),
    "Average complaints per month": round(len(df) / months),
    "Timely response rate (%)": round(100 * df["timely"].mean(), 1),
    "Median routing lag (days)": df.loc[~df["flag_bad_dates"], "routing_lag_days"].median(),
    "Share closed with relief (%)": round(100 * df["relief"].mean(), 1),
    "Share submitted via web (%)": round(100 * df["Submitted via"].eq("Web").mean(), 1),
    "Share with a narrative (%)": round(100 * df["has_narrative"].mean(), 1),
    "Rows with bad dates (flagged)": int(df["flag_bad_dates"].sum()),
}

baseline = pd.Series(kpis, name="Baseline")
print("\n--- BASELINE KPIS ---")
print(baseline)

baseline.to_csv(OUT_KPIS)
df.to_csv(OUT_CLEAN, index=False)
print(f"\nSaved clean complaints to {OUT_CLEAN}")
print(f"Saved baseline KPIs to {OUT_KPIS}")

# 5. Outcome mix and relief rate by issue
relief_by_issue = (
    df.groupby("Issue")
    .agg(complaints=("Complaint ID", "count"), relief_rate=("relief", "mean"))
    .sort_values("complaints", ascending=False)
)
relief_by_issue["relief_rate"] = (100 * relief_by_issue["relief_rate"]).round(1)

print("\n--- TOP ISSUES BY RELIEF RATE ---")
print(relief_by_issue.head(10))

relief_by_issue.to_csv(OUT_RELIEF)
print(f"Saved relief by issue analysis to {OUT_RELIEF}")
