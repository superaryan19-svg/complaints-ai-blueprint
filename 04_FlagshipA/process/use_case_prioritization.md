# Flagship A: Use-Case Prioritization & The Decision Ladder
**Client**: Kestrel Bank | **Module**: 04_FlagshipA/process/use_case_prioritization.md | **Week**: 9  

---

## 1. The Consultant's Decision Ladder

The foundational principle of technology consulting is to stop at the **cheapest, simplest rung that reliably solves the root cause**:

```
[Level 5] Autonomous Agent (Highest Cost, Highest Autonomous Risk)
    ▲
[Level 4] LLM + RAG / Generative Writing
    ▲
[Level 3] Classical Machine Learning (Supervised Classifier, Clustering)
    ▲
[Level 2] Deterministic Rule / Automated Workflow
    ▲
[Level 1] Process, Policy, or Ownership Fix (Cheapest, Lowest Risk)
```

### Application Across Candidate Use Cases

| Candidate Use Case | Lowest Rung That Works | Technical & Commercial Justification |
| :--- | :--- | :--- |
| **1. Triage & Routing** | **Small LLM (Now) $\rightarrow$ Classical ML (Later)** | The CRM lacks structured categories today. A lightweight LLM (`Haiku 5.5`) handles raw zero-shot triage now; after 6 months of logged labels, train an ultra-cheap classical classifier. |
| **2. Policy Knowledge Q&A** | **LLM + RAG** | Policies and circulars change constantly. Static rules fail. RAG retrieves dynamic excerpts with precise clause citations. |
| **3. Draft Reply (HITL)** | **LLM + Human Approval** | Complex natural language generation; risks are fully controlled by requiring agent sign-off before dispatch. |
| **4. Escalation Summary** | **LLM Summarization** | Condensing multi-week thread histories into concise bulleted briefings for supervisors. |
| **5. Vulnerable Customer Flag**| **Rules + Classical ML + Human** | High ethical and regulatory sensitivity; requires explicit socio-demographic fairness testing before LLM inference. |
| **6. Theme & Root-Cause Mining**| **Classical ML (Batch)** | Monthly offline batch processing using TF-IDF + K-Means (as built in A1); lightweight LLM applied only to label clusters. |
| **7. Auto-Send Customer Replies**| **NOT RECOMMENDED (Rejected)** | Customer-facing regulatory communications; failure or hallucination cost is unacceptable under RBI regulations. |
| **8. AI Decides Compensation** | **Rules + Human (Rejected)** | Discretionary refund limits are an accounting policy governance issue; keep final monetary disbursement human. |
| **9. Post-Resolution Sentiment**| **Prebuilt Workflow / AI Builder** | Standard sentiment tagging on post-closure feedback surveys; quick win using existing platform connectors. |

---

## 2. Six-Criteria Scoring Framework

Each use case is scored **1 to 5** across six dimensions:
* **Value Dimension (Average of 1 & 2)**:
  1. *Financial Value*: Direct cost avoidance and efficiency yield.
  2. *Customer / Regulatory Impact*: RBI SLA compliance and customer experience.
* **Feasibility Dimension (Average of 3, 4, 5 & 6)**:
  3. *Data Readiness*: Cleanliness and availability of inputs.
  4. *Technical Feasibility*: Architectural simplicity and integration friction.
  5. *Risk Profile*: Low downside risk (5 = Lowest risk, 1 = Highest risk).
  6. *Adoption Readiness*: Willingness of frontline teams to embrace.

> **Evaluation Rule**: A use case **passes** if **Total Score $\ge 20 / 30$** AND **No individual criterion scores 1**.

### Use-Case Scorecard

| # | Candidate Use Case | Financial Value | Reg. Impact | Data Ready | Tech Feas. | Risk (5=Low) | Adoption | Total Score | Outcome |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Triage & Routing** | 4 | 4 | 5 | 5 | 4 | 4 | **26 / 30** | **PASS (Do First - Phase 1)** |
| **2** | **Policy Knowledge Q&A (RAG)** | 4 | 4 | 4 | 4 | 4 | 4 | **24 / 30** | **PASS (Do First - Phase 1)** |
| **3** | **Draft Reply (Agent Approval)**| 5 | 4 | 4 | 3 | 3 | 3 | **22 / 30** | **PASS (Plan Carefully - Phase 2)** |
| **4** | **Escalation Case Summary** | 3 | 3 | 5 | 5 | 4 | 4 | **24 / 30** | **PASS (Quick Win - Phase 1/2)** |
| **5** | **Vulnerable-Customer Flagging** | 3 | 5 | 3 | 3 | 2 | 3 | **19 / 30** | **DEFER (Score < 20; Needs audit)** |
| **6** | **Root-Cause Theme Mining** | 3 | 3 | 4 | 4 | 5 | 4 | **23 / 30** | **PASS (Quick Win - Offline Batch)**|
| **7** | **Auto-Send Replies (No Review)**| 5 | 2 | 4 | 3 | **1** | 2 | **17 / 30** | **REJECT (Risk = 1; Regulatory hazard)**|
| **8** | **AI Decides Compensation** | 4 | 2 | 3 | 2 | **1** | 2 | **14 / 30** | **REJECT (Risk = 1; Governance violation)**|
| **9** | **Feedback Sentiment Flow** | 2 | 3 | 4 | 5 | 5 | 4 | **23 / 30** | **PASS (Phase 0 Quick Win)** |

---

## 3. Value vs. Feasibility Matrix

```
High Value (5.0) │
                 │              [3. Draft Reply]
                 │                                        [1. Triage & Routing]
                 │   [5. Vulnerable Flag]                 [2. Policy Q&A (RAG)]
                 │
                 │   [7. REJECT: Auto-Send]
                 │                                        [4. Case Summary]
                 │                                        [6. Theme Mining]
                 │   [8. REJECT: Auto-Comp]               [9. Feedback Flow]
Low Value (1.0)  │
                 └─────────────────────────────────────────────────────────────
                  Low Feasibility (1.0)                 High Feasibility (5.0)
```

### Strategic Rollout Quadrants:
* **Quadrant I: Do First (High Value, High Feasibility)**: Use Cases **#1 (Triage)** and **#2 (Policy RAG)**. Forms the foundation of Phase 1.
* **Quadrant II: Plan Carefully (High Value, Moderate Feasibility)**: Use Case **#3 (Draft Reply)**. High financial yield (6.0 min saved), but requires rigorous prompt hardening and agent review controls (Phase 2).
* **Quadrant III: Quick Wins (Moderate Value, High Feasibility)**: Use Cases **#4 (Summary)**, **#6 (Batch Mining)**, and **#9 (Feedback Flow)**.
* **Quadrant IV: Do Not Do (High Risk / Low Feasibility)**: Use Cases **#7 (Auto-Send)** and **#8 (Auto-Comp)**. Rejected to safeguard bank reputation and regulatory compliance.
