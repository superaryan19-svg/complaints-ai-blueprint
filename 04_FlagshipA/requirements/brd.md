# Flagship A: AI-Aware Business Requirements Document (BRD)
**Client**: Kestrel Bank | **Project**: AI-Assisted Complaint Operations Copilot | **Week**: 8  
**Document Reference**: BRD-KESTREL-GENAI-001  

---

## 1. Objectives & Project Scope
* **Business Objective**: Deploy an internal AI Copilot for 120 complaint-handling agents across Cards, CASA, Digital, and Branch Escalations to reduce handle time from **25 to 19 minutes**, elevate 30-day resolution rates from **88% to $\ge 95\%$**, and decrease Ombudsman escalations by **15%**.
* **Traceability to Identified Pain Points**:
  * Resolves **P1** (Policy Search) via Policy RAG Q&A.
  * Resolves **P2** (Misrouting) via Intelligent Triage.
  * Resolves **P3** (Drafting Friction) via Assisted Reply Drafting.
  * Resolves **P4** (SLA Drift) via Automated Day-25 alerting rules.
* **Scope Exclusions**: Zero direct autonomous messaging to customers; zero modifications to the core banking ledger in Year 1.

---

## 2. Current vs. Future Operating State
* **As-Is Baseline**: 11 manual human touchpoints, fragmented knowledge across 4 intranets, 20% misrouting, and manual drafting from scratch.
* **To-Be Operating Model**: 7 human touchpoints, 4 automated workflow rules, 3 AI assisted inference points, with strict **Human-in-the-Loop (HITL)** sign-offs.

---

## 3. Detailed Functional Requirements (FR)

### FR-01: Intelligent Triage & Department Routing
* **Trigger**: Ingestion of unstructured complaint text from CRM intake channels.
* **Input**: Customer complaint text, transaction channel, masked customer identifier.
* **Processing**: Model (`Claude Haiku 5.5`) predicts target team (Cards, CASA, Digital, Branch) with an associated confidence probability score ($0.0 - 1.0$).
* **Output**: Suggested queue assignment delivered to CRM routing engine. If confidence is $< 0.85$, route to Supervisor Triage Queue.

### FR-02: Policy & Regulatory Knowledge Q&A (RAG)
* **Trigger**: Frontline agent initiates policy lookup query within CRM sidebar widget.
* **Input**: Free-form natural language agent query.
* **Processing**: Vector retrieval across indexed repository of verified bank policies, credit card terms, and RBI circulars. Prompt assembly sent to `Claude Sonnet 5.5`.
* **Output**: Concise procedural guidance explicitly citing the governing circular number, section heading, and publication date.

### FR-03: Guided Reply Drafting (HITL)
* **Trigger**: Agent clicks "Generate Response Draft" after reviewing case records.
* **Input**: Complaint narrative, verified policy citations, approved refund decision.
* **Processing**: Model synthesizes empathetic, professional response incorporating mandatory statutory disclosures and Ombudsman redress rights.
* **Output**: Editable draft pre-filled in CRM email/letter composer. Outgoing dispatch button disabled until agent reviews text.

---

## 4. AI Quality & Guardrail Requirements

| Metric / Guardrail | Minimum Acceptance Threshold | Operational Fallback & Verification |
| :--- | :---: | :--- |
| **Triage Accuracy** | **$\ge 90.0\%$** on 200-complaint test set | Agent can re-route in 1 click; all manual overrides logged. |
| **Policy Retrieval Accuracy** | **$\ge 85.0\%$** rated correct by 2 reviewers | System must output: *"Procedure not found in verified repository"* rather than guessing. |
| **Strict Citation Requirement** | **100% of policy answers** must cite section | Answers lacking document citation are automatically blocked by output regex guardrails. |
| **Hallucination Ceiling** | **$< 1.0\%$** factual error rate | High-temperature generation prohibited (Temperature set to $0.0 - 0.2$). |

---

## 5. Human Oversight & Governance Controls
1. **Zero Unreviewed Dispatches**: Outgoing dispatch pipeline technically blocks message transmission unless signed off by an authorized agent.
2. **Override Logging**: If an agent rejects an AI draft or changes suggested routing, the CRM captures:
   * Original AI recommendation vs. final human action.
   * Categorical reason for override (Inaccurate, Irrelevant tone, Outdated policy).
   * Agent employee ID and timestamp.
3. **Threshold Intervention**: Sustained override rates $>15\%$ for two consecutive weeks trigger immediate MLOps audit.

---

## 6. Data Privacy & Architecture Requirements
* **PII Redaction Pipeline**: Customer Name, Account Number, Primary Account Number (PAN), Aadhaar, Phone, and Email must be scrubbed using local regex/NER before sending prompts to the model API.
* **Data Residency**: Cloud hosting, vector databases, and logging endpoints must reside in India regions (e.g., AWS Mumbai / Azure Central India).
* **Zero Model Training**: Contracts must prohibit vendors from using bank prompts or completions for foundational model re-training.
* **Log Retention**: Interaction logs retained for 180 days in encrypted S3/Blob storage, adhering to DPDP compliance limits.

---

## 7. Non-Functional Requirements (NFR)

| NFR Category | Requirement Specification |
| :--- | :--- |
| **Response Latency** | P95 latency $< 1,000\text{ ms}$ for Triage (`Haiku 5.5`); P95 latency $< 4,500\text{ ms}$ for Policy RAG (`Sonnet 5.5`). |
| **System Availability** | 99.9% uptime during standard banking operating hours (08:00 to 20:00 IST). |
| **Unit Cost Ceiling** | Blended model inference cost must not exceed **₹3.00 ($0.034)** per complaint handled. |
| **Auditability** | 100% of prompts, completions, latency, and guardrail alerts stored with cryptographic hash. |

---

## 8. Monitoring & Acceptance Criteria
* **Go-Live Sign-Off**: Requires joint sign-off from Head of Customer Service, Principal Nodal Officer, and Chief Risk Officer.
* **Pilot Gate Performance**: Formal evaluation against the **A3 Dashboard** KPIs after 90 days.
