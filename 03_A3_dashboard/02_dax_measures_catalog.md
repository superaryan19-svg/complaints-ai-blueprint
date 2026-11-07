# A3 DAX Measures Catalog & KPI Dictionary
**Project**: Kestrel Bank AI Value Dashboard | **Module**: A3 Power BI Analytics  

---

## 1. Setup Instructions
1. In Power BI Desktop, click **Home** $\rightarrow$ **Enter Data**.
2. Name the table `_Measures` and click **Load**.
3. Create each DAX measure below by selecting `_Measures` $\rightarrow$ **New Measure**.

---

## 2. Complete DAX Measure Code

```dax
-- ====================================================================
-- SECTION 1: FINANCIAL & OPERATIONAL PARAMETERS (ALIGNED WITH A2 MODEL)
-- ====================================================================

FX INR per USD = 88

Agent Cost per Hour = 400

Realisation = 0.5

Pilot Agents = 120


-- ====================================================================
-- SECTION 2: COST AND BUSINESS VALUE MEASURES
-- ====================================================================

AI Runs = COUNTROWS ( FactAIEvents )

AI Cost INR = SUM ( FactAIEvents[cost_usd] ) * [FX INR per USD]

Cost per Run INR = DIVIDE ( [AI Cost INR], [AI Runs] )

Hours Saved = SUM ( FactAIEvents[minutes_saved] ) / 60

Realised Value INR = [Hours Saved] * [Agent Cost per Hour] * [Realisation]

Net Value INR = [Realised Value INR] - [AI Cost INR]

Cumulative Net Value INR = 
VAR LastDay = MAX ( DimDate[Date] )
RETURN
    CALCULATE (
        [Net Value INR],
        FILTER ( ALL ( DimDate ), DimDate[Date] <= LastDay )
    )


-- ====================================================================
-- SECTION 3: QUALITY, RISK & GOVERNANCE MEASURES
-- ====================================================================

Acceptance Rate = 
DIVIDE (
    CALCULATE (
        [AI Runs],
        FactAIEvents[agent_outcome] IN { "Accepted", "Edited" }
    ),
    [AI Runs]
)

Override Rate = 
DIVIDE (
    CALCULATE (
        [AI Runs],
        FactAIEvents[agent_outcome] = "Rejected"
    ),
    [AI Runs]
)

Guardrail Flag Rate = 
DIVIDE (
    CALCULATE (
        [AI Runs],
        FactAIEvents[guardrail_flag] <> "No flag"
    ),
    [AI Runs]
)

PII Blocks = 
CALCULATE (
    [AI Runs],
    FactAIEvents[guardrail_flag] = "PII blocked"
)

Human Escalation Rate = 
DIVIDE (
    CALCULATE (
        [AI Runs],
        FactAIEvents[escalated_to_human] = "Yes"
    ),
    [AI Runs]
)

P95 Latency (s) = 
PERCENTILE.INC ( FactAIEvents[latency_ms], 0.95 ) / 1000


-- ====================================================================
-- SECTION 4: USER ADOPTION & SCALE MEASURES
-- ====================================================================

Active Agents = DISTINCTCOUNT ( FactAIEvents[agent_id] )

Adoption % = DIVIDE ( [Active Agents], [Pilot Agents] )

Runs per Agent = DIVIDE ( [AI Runs], [Active Agents] )

Runs per Day = DIVIDE ( [AI Runs], DISTINCTCOUNT ( FactAIEvents[date] ) )

Teams Live = DISTINCTCOUNT ( FactAIEvents[team] )
```

---

## 3. Verified Benchmark Check Table (Full 90-Day Pilot)

Every measure calculated across the unfiltered 90-day pilot dataset matches the build guide benchmarks:

| Measure Name | Expected Value | Display Format | Consulting Interpretation |
| :--- | :---: | :---: | :--- |
| **AI Runs** | **64,588** | `#,##0` | Total inferences across 90 days. |
| **AI Cost INR** | **₹45,017** | `₹#,##0` | Total token API expenditure ($511.56 @ ₹88/USD). |
| **Cost per Run INR** | **₹0.70** | `₹0.00` | Sub-rupee marginal cost per AI interaction. |
| **Hours Saved** | **3,370 hrs** | `#,##0 hrs` | Net operational hours reclaimed. |
| **Realised Value INR**| **₹6.74 lakh** | `₹#,##0.0 lakh` | Gross savings discounted at 50% cash conversion. |
| **Net Value INR** | **₹6.29 lakh** | `₹#,##0.0 lakh` | Realised value minus token costs. |
| **Acceptance Rate** | **89.7%** | `0.0%` | Well exceeds Phase 2 gate threshold ($\ge 80\%$). |
| **Override Rate** | **10.3%** | `0.0%` | Within acceptable risk ceiling ($\le 15\%$). |
| **Guardrail Flag Rate**| **3.4%** | `0.0%` | Combined PII, low confidence & policy alerts. |
| **PII Blocks** | **944** | `#,##0` | Demonstrates DPDP automated redaction in action. |
| **Human Escalation** | **6.0%** | `0.0%` | Edge cases requiring senior supervisor review. |
| **P95 Latency (s)** | **2.89 s** | `0.00 s` | Meets SLA (<5s requirement for RAG). |
| **Active Agents** | **120** | `#,##0` | 100% of pilot cohort active by Day 90. |
| **Teams Live** | **4** | `0` | All 4 business units active (Cards, CASA, Digital, Branch). |
| **Runs / Day / Agent**| **718 / 538** | `#,##0` | Strong daily workflow stickiness. |

---

## 4. Key Architectural Explanations (Interview-Ready)

* **Why `FILTER(ALL(DimDate), ...)` in Cumulative Measure?**:  
  Standard time-intelligence functions break when an axis is grouped by `Week Start` or sliced by custom ranges. `FILTER(ALL(DimDate), DimDate[Date] <= LastDay)` explicitly resets visual date filters and aggregates all historical values up to the latest visible date.
* **Why `DIVIDE()` instead of `/`?**:  
  Prevents `#DIV/0!` errors when evaluating new pilot teams or quiet weekend dates with zero runs, returning clean blanks instead of broken UI cards.
* **CFO Disclosure on Net Value**:  
  Net Value in this dashboard tracks **direct model token usage against realized labor value**. It intentionally excludes fixed annual run teams and upfront build capex, which are modeled in the A2 Business Case. Adding an explicit footnote regarding this builds trust with finance executives.
