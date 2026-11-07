import numpy as np
import pandas as pd
import os

def simulate_events():
    rng = np.random.default_rng(7)
    N_DAYS, START = 90, "2026-01-05" # a 90-day pilot

    PRICE = { # USD per 1M tokens: input, cached input, output
        "Claude Sonnet 5.5": (2.00, 0.10, 10.00),
        "Claude Haiku 5.5": (0.10, 0.01, 0.50),
    }

    # use case: (model, share of events, avg input tokens, avg output tokens, minutes saved)
    USE_CASES = {
        "Triage & routing": ("Claude Haiku 5.5", 0.45, 1_200, 60, 2.5),
        "Draft reply": ("Claude Sonnet 5.5", 0.35, 6_000, 450, 6.0),
        "Policy knowledge Q&A": ("Claude Sonnet 5.5", 0.20, 8_500, 500, 4.0),
    }

    TEAMS = ["Cards", "Savings & Current", "Digital Banking", "Branch Escalations"]
    AGENTS = 120 # complaint-handling agents in the pilot

    rows = []
    event_id = 0

    for day in pd.date_range(START, periods=N_DAYS, freq="D"):
        # adoption ramps up over the first weeks
        ramp = min(1.0, 0.25 + day.dayofyear / 60)
        active = int(AGENTS * ramp) # agents using the copilot so far
        n = int(rng.poisson(900 * ramp) * (0.55 if day.dayofweek == 6 else 1)) # quiet Sundays

        for _ in range(n):
            uc = rng.choice(list(USE_CASES), p=[v[1] for v in USE_CASES.values()])
            model, _, inp, out, mins = USE_CASES[uc]
            tin = int(rng.normal(inp, inp * 0.15))
            tcache = int(tin * 0.35 * (rng.random() < 0.9)) # ~90% cache hit on shared prompt
            tout = max(20, int(rng.normal(out, out * 0.2)))
            p_in, p_cache, p_out = PRICE[model]
            cost = ((tin - tcache) * p_in + tcache * p_cache + tout * p_out) / 1e6
            outcome = rng.choice(
                ["Accepted", "Edited", "Rejected"],
                p=[0.55 + 0.15 * ramp, 0.30 - 0.10 * ramp, 0.15 - 0.05 * ramp]
            )
            saved = {"Accepted": mins, "Edited": mins * 0.5, "Rejected": -0.5}[outcome]
            event_id += 1
            agent = int(rng.integers(1, active + 1))
            rows.append({
                "event_id": event_id,
                "timestamp": day + pd.Timedelta(minutes=int(rng.integers(8 * 60, 20 * 60))),
                "date": day.date(),
                "agent_id": f"AG{agent:03d}",
                "team": TEAMS[agent % 4],
                "use_case": uc,
                "model": model,
                "input_tokens": tin,
                "cached_tokens": tcache,
                "output_tokens": tout,
                "cost_usd": round(cost, 6),
                "latency_ms": int(rng.lognormal(np.log(1800 if "Sonnet" in model else 600), 0.35)),
                "agent_outcome": outcome,
                "minutes_saved": saved,
                "guardrail_flag": rng.choice(
                    ["No flag", "PII blocked", "Low confidence", "Off-policy"],
                    p=[0.965, 0.015, 0.015, 0.005]
                ),
                "escalated_to_human": "Yes" if rng.random() < 0.06 else "No",
            })

    log = pd.DataFrame(rows)
    out_dir = "03_A3_dashboard"
    os.makedirs(out_dir, exist_ok=True)
    
    log_path = os.path.join(out_dir, "ai_event_log.csv")
    log.to_csv(log_path, index=False)

    # Baseline (pre-AI) values from A1 + assumptions
    targets_df = pd.DataFrame({
        "metric": [
            "Avg handle time (min)",
            "Complaints per month",
            "Loaded agent cost (INR/hr)",
            "Resolved within 30 days (%)",
            "Escalated to Ombudsman (%)"
        ],
        "baseline": [25, 40_000, 400, 88.0, 3.0],
        "target": [19, 40_000, 400, 95.0, 2.55],
        "source": [
            "Assumption (interviews)",
            "Assumption (A2 input)",
            "Assumption (A2 input)",
            "Assumption (A1 timely rate as proxy)",
            "Assumption (A2 input)"
        ],
    })
    targets_path = os.path.join(out_dir, "baseline_targets.csv")
    targets_df.to_csv(targets_path, index=False)

    print(f"Generated {len(log)} AI events successfully.")
    print(f"Total AI pilot cost: ${log['cost_usd'].sum():.2f}")
    print(f"Total Hours saved: {round(log['minutes_saved'].sum() / 60):,}")
    print("\nOutcome distribution:")
    print(log["agent_outcome"].value_counts(normalize=True).round(3) * 100)
    print("\nGuardrail flag distribution:")
    print(log["guardrail_flag"].value_counts(normalize=True).round(3) * 100)

if __name__ == "__main__":
    simulate_events()
