# Flagship A: Enterprise AI Governance Plan & Regulatory Control Map
**Client**: Kestrel Bank | **Project**: AI Transformation Blueprint | **Week**: 10  
**Compliance Context**: DPDP Act 2025/2027, RBI FREE-AI Framework (2025), and RB-IOS 2026  

---

## 1. Regulatory Context for Indian Commercial Banking

The deployment of Artificial Intelligence in Kestrel Bank's grievance redress operations is governed by three critical Indian statutory frameworks:

1. **Digital Personal Data Protection Act (DPDP Act & Rules)**:
   * Rules notified November 2025; operational enforcement through May 2027.
   * Mandates strict purpose limitation, data minimization, and local data protection safeguards.
   * Imposes a **strict 72-hour mandatory breach reporting requirement** to the Data Protection Board of India (DPBI).
2. **RBI FREE-AI Framework (Responsible AI in Financial Sector, August 2025)**:
   * Establishes the **7 Sutras** (Fairness, Reliability, Accountability, Transparency, Privacy, Security, Inclusion).
   * Mandates a Board-approved AI Policy, an enterprise-wide Central AI Inventory, clear customer disclosures, and preserved human accountability.
3. **Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026)**:
   * Customers possess the statutory right to escalate complaints unresolved after **30 days**.
   * The Ombudsman can award up to **₹30 lakh** for direct consequential loss plus ₹1 lakh for mental anguish, making turnaround speed and reply quality formal governance priorities.

---

## 2. Statutory Control Map (Framework to Control)

| Regulatory Requirement | Operational Meaning for This System | Implemented Technical & Policy Control | Accountable Owner | Verifiable Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **DPDP**: Purpose Limitation & Minimisation | Transmit only tokens required for reasoning; never send raw customer PII. | Client-side PII scrubbing pipeline masks Account #, Card #, PAN, and Aadhaar prior to API dispatch. | IT Security / DPO | PII Blocks Telemetry on A3 Dashboard; clean test logs. |
| **DPDP**: Security Safeguards & Breach Protocols | Prompts, completions, and logs constitute digital personal data. | AES-256 encryption at rest; TLS 1.3 in transit; 180-day log purge policy; 72-hour DPBI incident runbook. | CISO / DPO | Information Security Policy; tested incident runbook. |
| **DPDP**: Processor Obligations | Third-party cloud/model vendors process data on behalf of the bank. | Commercial BAA agreements prohibiting vendor data retention/training; India cloud regions enforced. | Procurement & Legal | Executed vendor enterprise contract with DPA addendum. |
| **FREE-AI**: AI Policy & Registry | All internal copilots must be centrally logged and risk-tiered. | Copilot registered on Kestrel Bank's Central AI Register (Classified: Tier-2 High-Risk internal system). | Chief Risk Officer | Central AI Registry entry with Model Risk card. |
| **FREE-AI**: Customer Disclosure & Redress | Customers must not be misled into believing they are interacting with unassisted AI. | AI serves as an internal assistant only; every customer response is signed off and issued by a named human agent. | Compliance Lead | CRM dispatch logs storing approving Agent ID. |
| **RB-IOS 2026**: 30-Day Turnaround SLA | Accelerating handle times must not compromise reply factual quality. | Automated Day-25 warning alerts; weekly QA audits of 50 randomly sampled AI-assisted closures. | Principal Nodal Officer | A1 Control Plan KPIs; Ombudsman referral tracking. |
| **Model Risk Management**: Drift & Quality | LLM reasoning or prompt quality may degrade over time or after policy updates. | Automated monthly benchmark regression testing (100 test questions); alert if Override Rate exceeds 15%. | AI Product Owner | A3 Override Rate metric trendline. |

---

## 3. Enterprise AI Risk Register

| Risk ID | Risk Description | Likelihood | Impact | Preventative & Detective Mitigations | Early Warning Signal (A3 Dashboard) |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **R-01** | **Hallucinated or outdated policy leads to incorrect customer rejection** | Medium | **High** | Mandatory clause citation; agent sign-off required; monthly test-set regression run. | **Override Rate $> 15.0\%$** |
| **R-02** | **Customer PII inadvertently leaked to external model API** | Low | **High** | Dual-pass client-side regex + NER redactor; red-team PII evaluation suite. | **PII Blocks Spike or Anomaly** |
| **R-03** | **Frontline agents resist adoption due to fear of replacement or complex UI** | Medium | **High** | Appoint team "AI Champions"; 2-hr training; weekly 15-min feedback huddles; emphasize tool removes typing, not jobs. | **Active Agents Curve Flattening** |
| **R-04** | **Saved agent time fails to translate into bottom-line cash benefits** | Medium | Medium | Agree in advance with Finance on how saved hours are harvested (hiring freezes, reduced overtime, back-office redeployment). | **Hours Saved vs. Financial Plan** |
| **R-05** | **Token usage cost overrun caused by recursive queries or prompt inflation** | Low | Low | Model routing (Haiku for triage); aggressive prompt caching (90% hit rate); hard monthly API cost ceilings. | **Cost per Run $> ₹1.50$** |
| **R-06** | **Model provider updates foundational model, degrading formatting quality** | Medium | Medium | Pin exact model version snapshots; execute end-to-end regression evaluation before any API version upgrade. | **Agent Acceptance Rate Drop** |

---

## 4. RACI Governance Matrix

* **R = Responsible**: The operational role that executes the task.
* **A = Accountable**: The single executive role with final sign-off authority (Only one "A" per row).
* **C = Consulted**: Roles providing critical input, review, and feedback.
* **I = Informed**: Roles updated on progress and outcomes.

| Program Activity | Sponsor (Head CS) | AI Product Owner | IT / Architecture | Compliance & Risk | Team Leads |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Approve AI Use Cases & Budget** | **A** | R | C | C | I |
| **Build, Hardening & Pipeline Integration** | I | **A** | R | C | C |
| **Stage-Gate Go / No-Go Sign-Off** | **A** | R | C | R | C |
| **Daily Telemetry & Quality Monitoring** | I | **A** | R | C | R |
| **Regulatory Audit & Incident Response** | I | R | R | **A** | I |
