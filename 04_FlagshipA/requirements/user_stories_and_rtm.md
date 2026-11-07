# Flagship A: User Stories & Requirements Traceability Matrix (RTM)
**Client**: Kestrel Bank | **Module**: 04_FlagshipA/requirements/user_stories_and_rtm.md | **Week**: 8  

---

## 1. User Stories with Rigorous Evaluation Criteria

### US-01: Intelligent Complaint Triage & Team Routing
> **As a** frontline intake agent,  
> **I want** the CRM to automatically suggest the correct complaint category and specialist department based on narrative text,  
> **So that** tickets do not bounce across multiple desks and routing delays are eliminated.
* **Acceptance Criteria**:
  * Correct department suggested on $\ge 90.0\%$ of an independently curated 200-complaint test set.
  * Agent can override and reassign the ticket to any team with a single click.
  * System latency is $\le 1.2$ seconds for triage inference.
  * Every manual override logs the source team, destination team, and override reason.

---

### US-02: Policy & Regulatory Knowledge Q&A (RAG)
> **As a** complaint-handling specialist,  
> **I want** to ask questions in natural language and receive immediate answers citing specific internal rules and RBI circulars,  
> **So that** I do not waste 15 minutes manually searching across four disconnected intranet repositories.
* **Acceptance Criteria**:
  * Output must explicitly cite the document title, circular number, and exact section heading.
  * If the knowledge store lacks relevant guidance, the model must return: *"Verified procedure not found in repository"* rather than generating speculative answers.
  * P95 response latency must be $< 5.0$ seconds.
  * $\ge 85.0\%$ of responses rated completely accurate by two independent senior compliance officers on a 100-question test set.

---

### US-03: Guided Reply Drafting with Mandatory Human Approval
> **As an** operations supervisor and Principal Nodal Officer,  
> **I want** all AI-drafted customer replies to require explicit human agent review and sign-off before dispatch,  
> **So that** no unverified, inaccurate, or non-compliant text ever reaches a customer.
* **Acceptance Criteria**:
  * **Negative Security Test**: The CRM dispatch API must throw a blocking error if an outgoing transmission request lacks a verified human agent authentication signature.
  * Pre-fills standard regulatory disclosures (including RBI Ombudsman escalation rights).
  * System captures the diff (edit distance) between AI draft and final sent communication for model evaluation.

---

### US-04: Automated PII Masking
> **As the** Chief Information Security Officer and Data Protection Officer,  
> **I want** all customer PII (PAN, Account Number, Phone, Email) automatically redacted before model invocation,  
> **So that** customer personal data is never transmitted to external LLM APIs in compliance with the DPDP Act.
* **Acceptance Criteria**:
  * 100% recall on synthetic PII evaluation test set (50 edge cases containing formatted and unformatted Indian PANs, 16-digit card numbers, and 12-digit Aadhaar formats).
  * Redacted tokens replaced with standard masking tags (e.g., `[MASKED_PAN]`, `[MASKED_ACC]`).

---

## 2. Requirements Traceability Matrix (RTM)

This matrix maps every business requirement through its originating operational pain point, technical design element, verification test set, and ongoing telemetry metric on the **A3 Value Dashboard**:

| Req ID | Pain Point | User Story | Technical Design Element | Test / Verification Method | Target KPI (A3 Dashboard) | Delivery Status |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| **FR-01** | **P2** (Misrouting) | **US-01** | Zero-shot Triage (`Claude Haiku 5.5`) | 200-item historical labelled test set | **Acceptance Rate $\ge 80\%$** | Ready for Pilot |
| **FR-02** | **P1** (Search Delay)| **US-02** | RAG Pipeline with Vector Search | 100-question compliance test set | **Override Rate $\le 15\%$** | Ready for Pilot |
| **FR-03** | **P3** (Drafting) | **US-03** | HITL Response Composer (`Sonnet 5.5`) | Negative dispatch security test | **Human Escalation $\le 6\%$** | Phase 2 Build |
| **NFR-01**| Compliance | **US-04** | Client-Side Regex/NER PII Redactor | 50 synthetic Indian PII test cases | **PII Blocks (Target: 0 Leaks)** | Verified |
| **NFR-02**| SLA / UX | **US-02** | Asynchronous Streaming & Caching | Load test with 50 concurrent queries| **P95 Latency $< 5.0\text{ s}$** | Verified |
| **NFR-03**| Cost Control | Commercial | Model Routing & Prompt Caching | Monthly billing audit vs. token model| **Cost per Run $\le ₹1.50$** | Verified (₹0.70) |
