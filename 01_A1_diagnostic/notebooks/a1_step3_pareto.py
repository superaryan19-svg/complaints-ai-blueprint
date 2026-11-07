import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

IN_PATH = "01_A1_diagnostic/data/clean/complaints_clean.csv"
OUT_IMG = "01_A1_diagnostic/outputs/pareto_issues.png"

os.makedirs("01_A1_diagnostic/outputs", exist_ok=True)

df = pd.read_csv(IN_PATH, dtype=str)
counts = df["Issue"].value_counts()
top = counts.head(10)
cum_pct = 100 * top.cumsum() / counts.sum()

fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)

# Bar chart of top issues
sns.barplot(x=top.values, y=top.index, ax=ax, color="#2b5c8f")
ax.set_xlabel("Number of Complaints", fontsize=11, fontweight="bold", labelpad=8)
ax.set_ylabel("")
ax.set_title("Top Complaint Issues (Pareto Analysis) — Kestrel Bank Diagnostic", fontsize=13, fontweight="bold", pad=12)

for i, (v, c) in enumerate(zip(top.values, cum_pct.values)):
    ax.text(v + (top.values.max() * 0.015), i, f"{v:,} ({c:.0f}% cum.)", va="center", fontsize=9, fontweight="bold")

# Determine how many issues make up 80%
all_cum = 100 * counts.cumsum() / counts.sum()
n80 = int((all_cum < 80).sum()) + 1

print(f"\nIssues needed to reach 80% of complaints: {n80} of {len(counts)}")
summary_text = f"Consultant Finding:\n• {n80} of {len(counts)} issues drive 80% of complaints.\n• Top 3 issues: '{top.index[0]}', '{top.index[1]}', '{top.index[2]}'."

ax.text(0.55, 0.15, summary_text, transform=ax.transAxes, fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.6", facecolor="#f8f9fa", edgecolor="#ced4da"))

plt.tight_layout()
plt.savefig(OUT_IMG)
plt.close()

print(f"Saved Pareto chart to {OUT_IMG}")
