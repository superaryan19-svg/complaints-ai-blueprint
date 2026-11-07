import pandas as pd
import os

RAW = "01_A1_diagnostic/data/raw/complaints.csv"
OUT = "01_A1_diagnostic/data/clean/bank_complaints_24m.csv"
PRODUCTS = r"Checking or savings account|Credit card" # bank products only
START, END = "2024-09-01", "2026-08-31"             # a 24-month window

print(f"Loading and filtering raw complaints from {RAW}...")

keep = []
for chunk in pd.read_csv(RAW, chunksize=50_000, dtype=str):
    chunk["Date received"] = pd.to_datetime(chunk["Date received"], format="mixed", errors="coerce")
    mask = (
        chunk["Product"].str.contains(PRODUCTS, case=False, na=False)
        & chunk["Date received"].between(START, END)
    )
    keep.append(chunk[mask])

df = pd.concat(keep, ignore_index=True)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
df.to_csv(OUT, index=False)

print(f"Filtered dataset shape: {df.shape}")
print("\nProduct Breakdown:")
print(df["Product"].value_counts())
print(f"\nSaved filtered data to {OUT}")
