import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.cluster import KMeans
import os

IN_PATH = "01_A1_diagnostic/data/clean/complaints_clean.csv"
OUT_SAMPLE = "01_A1_diagnostic/outputs/narrative_sample_to_tag.csv"
OUT_TAGGED = "01_A1_diagnostic/outputs/narrative_sample_tagged.csv"

os.makedirs("01_A1_diagnostic/outputs", exist_ok=True)

df = pd.read_csv(IN_PATH, dtype=str)
text = df["Consumer complaint narrative"].fillna("").str.strip()
narr = df[text.ne("")].copy()

print(f"Total complaints with narratives: {len(narr)}")

# A. Sample 100 complaints for manual review & tagging
sample = narr.sample(n=min(100, len(narr)), random_state=42).copy()

# Add empty tagging columns for manual audit
sample_to_tag = sample[["Complaint ID", "Product", "Issue", "Consumer complaint narrative"]].assign(
    root_cause="",
    ai_could_help=""
)
sample_to_tag.to_csv(OUT_SAMPLE, index=False)
print(f"Exported blank 100-narrative review sample to {OUT_SAMPLE}")

# Apply automated tagging rules for baseline benchmarking
def infer_tags(row):
    t = str(row["Consumer complaint narrative"]).lower()
    issue = str(row["Issue"]).lower()
    
    # Root cause classification
    if "fee" in t or "interest" in t or "charge" in t:
        rc = "Policy"
        ai = "Knowledge"
    elif "transferred" in t or "branch told me" in t or "dispute" in t or "delayed" in t:
        rc = "Process"
        ai = "Triage"
    elif "circular" in t or "unable to explain" in t or "conflicting" in t:
        rc = "Information"
        ai = "Knowledge"
    elif "statement" in t or "unauthorized" in t:
        rc = "System"
        ai = "Draft"
    else:
        rc = "Customer understanding"
        ai = "None"
    return pd.Series([rc, ai], index=["root_cause", "ai_could_help"])

sample[["root_cause", "ai_could_help"]] = sample.apply(infer_tags, axis=1)
sample[["Complaint ID", "Product", "Issue", "Consumer complaint narrative", "root_cause", "ai_could_help"]].to_csv(OUT_TAGGED, index=False)
print(f"Exported benchmark-tagged sample to {OUT_TAGGED}")

print("\n--- SAMPLE ROOT CAUSE BREAKDOWN (N=100) ---")
print(sample["root_cause"].value_counts(normalize=True).round(3) * 100)

print("\n--- SAMPLE AI OPPORTUNITY BREAKDOWN (N=100) ---")
print(sample["ai_could_help"].value_counts(normalize=True).round(3) * 100)

# B. TF-IDF + K-Means Theme Clustering
print("\n--- TF-IDF & K-MEANS THEME EXTRACTION (k=6) ---")
stops = list(ENGLISH_STOP_WORDS | {"xxxx", "xx", "inr", "bank"})
vec = TfidfVectorizer(stop_words=stops, max_features=5000, min_df=3, token_pattern=r"(?u)\b[a-zA-Z]{3,}\b")
X = vec.fit_transform(narr["Consumer complaint narrative"])

k = 6
km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
narr["theme"] = km.labels_
terms = vec.get_feature_names_out()

for i, centre in enumerate(km.cluster_centers_):
    top_words = [terms[j] for j in centre.argsort()[-7:][::-1]]
    cluster_count = (narr["theme"] == i).sum()
    print(f"Theme {i + 1} ({cluster_count} complaints): {', '.join(top_words)}")
