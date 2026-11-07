# Client Brief: Kestrel Bank (Fictional)

**Date**: November 2026  
**Engagement**: Category A Techno-Consultant Flagship Engagement  
**Document**: Initial Engagement Brief & Context Document  

---

### 1. Client Context
* **Client**: **Kestrel Bank** (Fictional), a mid-size Indian private-sector commercial bank offering retail accounts, credit cards, personal loans, and digital banking services.
* **Scale (Assumed)**:
  * Approximately **40,000 retail complaints per month**.
  * Handled by roughly **120 complaint-handling agents** across 4 dedicated units:
    1. Cards
    2. Savings & Current Accounts
    3. Digital Banking
    4. Branch Escalations

### 2. Business Situation & Complication
Complaint volumes are accelerating rapidly due to digital channel growth. Frontline agents are overwhelmed, spending significant manual time searching disparate knowledge bases and circulars across four isolated systems.

Under the **Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026)**, customers can escalate to the RBI Ombudsman if a complaint is unresolved after 30 days or resolved unsatisfactorily. Unresolved escalations expose the bank to compensatory awards up to ₹30 lakh per case, operational audits, and reputational risk.

### 3. Client Mandate (Ask)
> *"Tell us where AI should and should not be used in complaint handling, what it is worth, and how to roll it out safely."*

### 4. Constraints & Guardrails
* **Data Privacy & Residency**: Compliance with the **Digital Personal Data Protection Act (DPDP Act & Rules)**. Sensitive Personal Data / PII must be redacted before any third-party model inference, and data must remain in India where possible.
* **RBI Regulations**: Adherence to the **RBI FREE-AI Framework (Responsible AI Sutras)** and **RB-IOS 2026**.
* **Systems**: **Zero architectural modifications to the core banking system** in Year 1.
* **Commercial Gate**: Any investment proposal requires an executive **payback period inside 24 months**.

### 5. Data Stand-in & Methodological Note
* Fictional client context uses public **US CFPB (Consumer Financial Protection Bureau)** complaint records as a structural stand-in for issue taxonomy, outcome relief ratios, and complaint text themes.
* All Indian bank volumes, labor costs (₹400/hr loaded), handling times (25 min AHT baseline), and escalation rates (3%) are explicitly cataloged in the [Assumptions Register](assumptions_register.xlsx).
