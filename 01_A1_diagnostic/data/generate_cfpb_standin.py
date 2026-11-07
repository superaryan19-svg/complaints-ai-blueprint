import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_complaints_data(filename="01_A1_diagnostic/data/raw/complaints.csv", n_rows=25000):
    rng = np.random.default_rng(42)
    random.seed(42)

    start_date = datetime(2024, 9, 1)
    end_date = datetime(2026, 8, 31)
    date_range_days = (end_date - start_date).days

    products = [
        "Credit card",
        "Checking or savings account",
        "Credit card or prepaid card",
        "Mortgage",             # will be filtered out by step1
        "Vehicle loan or lease" # will be filtered out by step1
    ]
    p_weights = [0.42, 0.40, 0.10, 0.05, 0.03]

    issues_card = [
        "Problem with a purchase shown on your statement",
        "Fees or interest",
        "Getting a credit card",
        "Problem when making a payment",
        "Closing an account",
        "Trouble using your card",
        "Advertising and marketing"
    ]
    w_card = [0.32, 0.26, 0.16, 0.11, 0.08, 0.05, 0.02]

    issues_bank = [
        "Managing an account",
        "Deposits and withdrawals",
        "Fees or interest",
        "Opening an account",
        "Problem with a lender or other company charging your account",
        "Closing an account"
    ]
    w_bank = [0.28, 0.25, 0.22, 0.12, 0.08, 0.05]

    responses = [
        "Closed with explanation",
        "Closed with monetary relief",
        "Closed with non-monetary relief",
        "Untimely response"
    ]
    w_resp = [0.65, 0.22, 0.09, 0.04]

    channels = ["Web", "Phone", "Referral", "Postal mail"]
    w_chan = [0.72, 0.18, 0.06, 0.04]

    narrative_templates = [
        "I was charged an unexpected fee of INR XXXX against stated terms. When I contacted customer support, the representative was unable to explain the policy.",
        "A transaction of XXXX appeared on my statement that I did not authorize. I raised a dispute three weeks ago and have received no resolution or acknowledgement.",
        "I submitted a request to close my card account over a month ago. The branch told me to call the helpline, but the phone agent asked me to visit the branch.",
        "My deposit of XXXX was delayed by several days causing a payment bounce. I have been transferred between five different teams without any clear answer.",
        "The bank revised annual fee terms without prior SMS or email notification. I have been following up repeatedly for the last 25 days.",
        "I requested a waiver of interest charged during a technical outage when UPI was down. The agent quoted conflicting rules from past circulars.",
        "My account was temporarily frozen without clear reasoning. Branch staff could not locate the compliance circular governing this hold.",
        "Rewards points were not credited for festival campaign purchases despite meeting all eligibility criteria."
    ]

    rows = []
    base_id = 9000000

    for i in range(n_rows):
        cid = str(base_id + i)
        prod = rng.choice(products, p=p_weights)
        
        # Pick issue based on product
        if "card" in prod.lower():
            issue = rng.choice(issues_card, p=w_card)
            sub_prod = "General-purpose credit card"
        elif "checking" in prod.lower() or "savings" in prod.lower():
            issue = rng.choice(issues_bank, p=w_bank)
            sub_prod = "Checking account"
        else:
            issue = "Other loan problem"
            sub_prod = "Other loan"

        rec_days = int(rng.integers(0, date_range_days))
        dt_rec = start_date + timedelta(days=rec_days)

        # Routing lag (0 to 3 days)
        lag = int(rng.choice([0, 1, 2, 3, 5], p=[0.55, 0.30, 0.10, 0.04, 0.01]))
        dt_sent = dt_rec + timedelta(days=lag)

        resp = rng.choice(responses, p=w_resp)
        timely = "Yes" if resp != "Untimely response" and rng.random() > 0.02 else "No"
        chan = rng.choice(channels, p=w_chan)

        # 35% have narrative
        if rng.random() < 0.35:
            narr = rng.choice(narrative_templates)
        else:
            narr = ""

        rows.append({
            "Date received": dt_rec.strftime("%Y-%m-%d"),
            "Product": prod,
            "Sub-product": sub_prod,
            "Issue": issue,
            "Sub-issue": "General",
            "Consumer complaint narrative": narr,
            "Company response to consumer": resp,
            "Timely response?": timely,
            "Submitted via": chan,
            "Date sent to company": dt_sent.strftime("%Y-%m-%d"),
            "Complaint ID": cid
        })

    # Add 5 duplicates to test deduplication step
    for j in range(5):
        rows.append(rows[j].copy())

    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"Generated {len(df)} complaint records in {filename}")

if __name__ == "__main__":
    generate_complaints_data()
