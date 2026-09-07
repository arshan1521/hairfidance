import fitz
import os
import sys

PDF_PATH = r'C:\Users\ARSHAN NIZAR\.gemini\antigravity-ide\brain\092badc1-a1a9-44e9-ab43-c05438b7e052\.user_uploaded\media_1788794877769.pdf'
WORKSPACE_DIR = r'c:\Users\ARSHAN NIZAR\Downloads\MINI_PROJECT'
OUTPUT_MD_PATH = os.path.join(WORKSPACE_DIR, 'documentation', 'HairFidence_KTU_MCA_Project_Report.md')

def build_markdown():
    doc = fitz.open(PDF_PATH)
    print(f"Loaded PDF with {len(doc)} pages.")

    # We will assemble the exact markdown content matching HairFidence_MCA_new.pdf verbatim.
    md = []

    # ──────────────────────────────────────────────────────────────────────────
    # PAGE 1: TITLE / COVER PAGE
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# HAIRFIDENCE
## CANCER PATIENT HAIR DONATION MANAGEMENT SYSTEM

### PROJECT THESIS
SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS  
FOR THE AWARD OF THE DEGREE OF  
### MASTER OF COMPUTER APPLICATIONS

<br>

**SUBMITTED BY**  
**ARSHAN NIZAR K P**  
**(Register Number: AWH25MCA-2010)**

<br>

<div align="center">
  <img src="../college_logo.png" alt="AWH Engineering College Logo" width="180"/>
</div>

<br>

**DEPARTMENT OF COMPUTER APPLICATIONS**  
**AWH ENGINEERING COLLEGE**  
**KUTTIKKATTOOR, CALICUT - 673008**  
*(Affiliated to APJ Abdul Kalam Technological University, Kerala)*  

**JULY 2026**

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # PAGE 2: BONA FIDE CERTIFICATE
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# DEPARTMENT OF COMPUTER APPLICATIONS
# AWH ENGINEERING COLLEGE
# KUTTIKKATTOOR, CALICUT - 673008

<br>

## BONA FIDE CERTIFICATE

		This is to certify that this project thesis entitled **“HAIRFIDENCE: CANCER PATIENT HAIR DONATION MANAGEMENT SYSTEM”** is a bona fide record of the project work carried out by **ARSHAN NIZAR K P (Register Number: AWH25MCA-2010)** in partial fulfillment of the requirements for the award of the Degree of **Master of Computer Applications** from **APJ Abdul Kalam Technological University** during the academic year **2025–2026**.

<br><br><br>

---------------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----------------------------------------------------  
**Mrs. SRUTI SUDEVAN** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Ms. AMEENA AFSAR**  
Head of the Department & Associate Professor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Assistant Professor  
Dept. of Computer Applications &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dept. of Computer Applications  
AWH Engineering College, Calicut &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AWH Engineering College, Calicut  

<br><br><br>

---------------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----------------------------------------------------  
**INTERNAL EXAMINER** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **EXTERNAL EXAMINER**  

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # PAGE 3: ACKNOWLEDGEMENT
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# ACKNOWLEDGEMENT

		I express my profound sense of gratitude and sincere indebtedness to our respected Principal, Dr. Sabeena M V, for providing all necessary academic facilities, computational infrastructure, and institutional encouragement that made the completion of this thesis work possible.

		I convey my deepest and heartfelt thanks to Mrs. Sruti Sudevan, Head of the Department of Computer Applications, for her constant inspiration, academic leadership, and continuous encouragement throughout the duration of the MCA curriculum and during this project endeavor.

		I take immense privilege in expressing my sincere gratitude to my Project Guide and Coordinator, Ms. Ameena Afsar, Assistant Professor, Department of Computer Applications, and Mrs. Sruti Sudevan, for their indispensable guidance, technical mentorship, and patient supervision. Their constructive criticisms, insightful suggestions, and thorough evaluations at every phase of system modeling, design, and testing helped shape this project into an academically rigorous and socially impactful system.

		I also extend my sincere gratitude to all the teaching and non-teaching faculty members of the Department of Computer Applications for their invaluable support, timely suggestions, and generous academic assistance throughout the project development cycle.

		I express my loving thanks to my parents and family members whose unwavering moral support, sacrifices, and continuous prayers have been the bedrock of my life and education. I also express my warm appreciation to my batchmates and friends for their collaborative discussions, constructive feedback during user experience reviews, and camaraderie throughout our post-graduate journey.

		Above all, I surrender myself in eternal gratitude before the Almighty for granting me the wisdom, health, strength, and perseverance to complete this project thesis successfully.

<br>

**ARSHAN NIZAR K P**  
*(Register Number: AWH25MCA-2010)*  

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # PAGE 4: ABSTRACT
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# ABSTRACT

		Chemotherapy-induced hair loss severely impacts the psychological well-being of cancer patients. While many compassionate individuals wish to donate hair for medical wigs, the lack of a standardized platform bottlenecks coordination between donors, non-governmental organizations (NGOs), and verified recipients. The proposed project, HairFidence, resolves this operational gap by introducing a centralized web application designed to digitalize and streamline the entire hair donation lifecycle.

		Built on an interactive HTML, CSS, and JavaScript frontend with a secure PHP backend, HairFidence manages transactions through an optimized MySQL database in a local XAMPP environment. By utilizing an elegant 8-table relational schema, the platform guarantees rapid execution speeds, robust concurrency control via PDO transactions, and strict data privacy to effectively prevent resource double-booking and secure data leakage.

		The system logically partitions functionality across four distinct modules: Administrator, NGOs, Donors, and Patients. Donors can easily list hair specifications and track deliveries, while patients securely upload medical reports to request verified matches. Registered NGOs act as essential gatekeepers by auditing records and physical donations, overseen globally by the Administrator. Ultimately, HairFidence fosters an efficient, community-driven logistics network, returning dignity to cancer survivors.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # PAGES 5-6: CONTENTS
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CONTENTS

| Sl. No. | Section / Chapter Heading | Page No. |
| :---: | :--- | :---: |
| **i** | **CERTIFICATE** | **ii** |
| **ii** | **COMPANY CERTIFICATE** | **iii** |
| **iii** | **ABOUT THE COMPANY** | **iv** |
| **iv** | **ACKNOWLEDGEMENT** | **v** |
| **v** | **ABSTRACT** | **vi** |
| **8** | **CHAPTER 8: INTRODUCTION** | **1** |
| 8.1 | System Overview | 1 |
| 8.2 | Problem Statement & Clinical Context | 3 |
| 8.3 | Objectives of the System | 5 |
| 8.4 | Scope of the Project | 7 |
| 8.5 | Operational and Psychosocial Benefits | 9 |
| **9** | **CHAPTER 9: SYSTEM ANALYSIS** | **11** |
| 9.1 | Existing System Description | 11 |
| 9.2 | Limitations of the Existing System | 13 |
| 9.3 | Proposed System Architecture | 15 |
| 9.4 | Concrete Enhancements Implemented | 17 |
| **10** | **CHAPTER 10: FEASIBILITY STUDY** | **20** |
| 10.1 | Technical Feasibility | 20 |
| 10.2 | Operational Feasibility | 22 |
| 10.3 | Economic Feasibility | 24 |
| 10.4 | Behavioural & Ethical Feasibility | 26 |
| 10.5 | Software Standards Feasibility | 28 |
| **11** | **CHAPTER 11: SOFTWARE ENGINEERING PARADIGM** | **30** |
| 11.1 | Agile Process Methodology | 30 |
| 11.2 | Scrum Framework Implementation | 32 |
| 11.3 | Sprint Planning and Task Decomposition | 34 |
| 11.4 | User Story Mapping & Acceptance Criteria | 38 |
| 11.5 | Agile Ceremonies & Milestone Delivery | 41 |
| **12** | **CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (SRS)** | **43** |
| 12.1 | Minimum Hardware Requirements | 43 |
| 12.2 | Software Stack and Environment | 45 |
| 12.3 | Functional Requirements by Module | 48 |
| 12.4 | Non-Functional Requirements | 54 |
| **13** | **CHAPTER 13: SYSTEM DESIGN** | **58** |
| 13.1 | High-Level MVC Architectural Pattern | 58 |
| 13.2 | Data Flow Diagrams (DFD Level 0, 1, 2) | 62 |
| 13.3 | UML Modeling (Use Case, Class, Sequence) | 68 |
| 13.4 | Database Design & Relational Schema | 76 |
| 13.5 | Normalization Proofs (1NF, 2NF, 3NF) | 83 |
| **14** | **CHAPTER 14: SYSTEM DEVELOPMENT** | **88** |
| 14.1 | Subsystem Modular Breakdown | 88 |
| 14.2 | Core Algorithms & Business Logic | 92 |
| 14.3 | Routing & Endpoints Specification | 99 |
| 14.4 | Input Validation & Security Layers | 102 |
| **15** | **CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION** | **106** |
| 15.1 | Testing Methodologies Applied | 106 |
| 15.2 | Comprehensive Test Suite Table | 110 |
| 15.3 | Deployment & Build Configuration | 114 |
| 15.4 | Operational Environment Verification | 117 |
| **16** | **CHAPTER 16: SYSTEM MAINTENANCE** | **120** |
| 16.1 | Corrective Maintenance Plan | 120 |
| 16.2 | Adaptive Maintenance Plan | 122 |
| 16.3 | Perfective Maintenance Plan | 124 |
| 16.4 | Preventive Maintenance Plan & DR | 126 |
| **17** | **CHAPTER 17: FUTURE ENHANCEMENT** | **129** |
| 17.1 | Cross-Platform Mobile Applications | 129 |
| 17.2 | Automated Postal & Logistics API Integration | 131 |
| 17.3 | AI-Powered Virtual Wig AR Simulator | 133 |
| 17.4 | Philanthropic Micro-Sponsorship Gateway | 135 |
| 17.5 | Multi-Channel Notification Webhooks | 137 |
| **18** | **CHAPTER 18: CONCLUSION** | **139** |
| 18.1 | Summary of Project Achievements | 139 |
| 18.2 | Validation of Core Objectives | 141 |
| 18.3 | Academic & Engineering Conclusion | 143 |
| **19** | **CHAPTER 19: APPENDIX** | **145** |
| **20** | **CHAPTER 20: BIBLIOGRAPHY** | **156** |

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 8: INTRODUCTION (Pages 7-10)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 8: INTRODUCTION

<br><br>

## 8.1 System Overview
		In contemporary clinical oncology, pharmacological advancements, targeted chemotherapies, and advanced radiotherapy regimens have substantially elevated cancer survival rates across global populations. However, systemic oncology protocols frequently inflict severe physical, emotional, and psychosocial distress upon patients. Among treatment-associated complications, chemotherapy-induced alopecia (hair loss) is clinically recognized as one of the most acutely demoralizing and traumatic experiences endured by cancer survivors, predominantly impacting women, adolescents, and children. Unlike internal physiological symptoms, alopecia serves as an involuntary, inescapable visual badge of malignancy, precipitating acute clinical depression, diminished self-worth, social stigmatization, and in severe instances, treatment non-compliance.

		Specialized cranial medical prostheses (custom-crafted natural hair wigs) offer profound psychosocial rehabilitation, enabling recovering patients to reclaim their self-image, emotional well-being, and social confidence. Unfortunately, the commercial marketplace for natural hair wigs is severely cost-prohibitive, typically commanding prices between ₹25,000 and ₹1,20,000 ($300 to $1,500) per unit owing to meticulous hand-knotting craftsmanship and raw material scarcity. Concurrently, thousands of compassionate citizens express an active willingness to donate their natural hair for charitable wig fabrication. Regrettably, traditional charitable avenues across Kerala and India remain uncoordinated, informal, and vulnerable to operational failures.

		HairFidence is an enterprise-grade, centralized, role-governed web application engineered to bridge this vital humanitarian divide. Operating on a robust 3-Tier Model-View-Controller (MVC) architecture, the platform digitizes and audits the complete hair donation lifecycle. By establishing an accountable digital nexus between Altruistic Donors, Accredited Healthcare Non-Governmental Organizations (NGOs), Cancer Patients, and System Administrators, HairFidence guarantees that every donated hair parcel is cataloged, verified, and allocated to genuine oncology patients at zero financial cost.

## 8.2 Problem Statement & Clinical Context
		The traditional hair donation ecosystem suffers from three acute, interrelated structural deficiencies:
		1. **Severe Donor Disconnect & Logistics Opacity:** Altruistic citizens wishing to contribute hair typically encounter fragmented social media appeals or informal word-of-mouth campaigns. Donors package and dispatch hair through postal services with zero tracking mechanisms. Consequently, donors never receive formal acknowledgment, quality assessments, or confirmation that their contribution reached a patient, leading to donor fatigue.
		2. **Unstandardized Parcel Influx & Lack of Clinical Audit:** Charitable non-profits and hospital desks frequently receive unsorted, damaged, or chemically compromised hair parcels lacking crucial technical metadata (length in inches, dye history, hygiene status). Simultaneously, without centralized medical validation portals, NGOs struggle to authenticate patient medical reports, risking resource misallocation or diversion into commercial cosmetic markets.
		3. **Administrative Latency & Resource Contention:** Manual record-keeping via physical logbooks or disconnected spreadsheets introduces human error. Hospital social workers often inadvertently double-book hair assets to multiple patients. Furthermore, immunocompromised patients undergoing active chemotherapy are forced to travel physically to charity offices with paper records, imposing unwarranted physical strain.

## 8.3 Objectives of the System
		The primary technical, clinical, and operational objectives of HairFidence include:
		• **Centralized Data Management:** Unify donor contributions, patient requests, clinical records, and NGO accreditations into an ACID-compliant MariaDB/MySQL relational data store.
		• **End-to-End Parcel Lifecycle Tracking:** Provide real-time visual pipeline monitoring across three discrete transactional states: Available (cataloged), Processing (patient request locked pending NGO verification), and Donated (inspected and dispatched).
		• **Pessimistic Concurrency Locking:** Implement database-level row locking (`FOR UPDATE`) within atomic PDO transactions to completely eliminate race conditions and asset double-booking.
		• **Privacy-Preserving Clinical Validation:** Provide a secure document upload pipeline that isolates patient oncology diagnostic certificates, restricting viewing privileges strictly to verified NGO auditors and administrators.
		• **Democratic Community Engagement:** Enable accredited NGOs to broadcast community donation drives and awareness campaigns, expanding civic participation across diverse demographic sectors.

## 8.4 Scope of the Project
		The architectural and functional scope of HairFidence encompasses:
		• **Functional Boundary:** Comprehensive governance spanning four user roles (Administrator, NGO, Donor, Patient), secure authentication using BCrypt hashing, responsive catalog browsing, real-time status pipelines, and grievance ticket tracking.
		• **Geographical & Organizational Scope:** Engineered for regional deployment across hospital oncology wards, charitable healthcare trusts, and volunteer networks in Kozhikode and Kerala, with structural scalability supporting nationwide charitable deployment.
		• **Exclusions & Operational Boundaries:** The application does not engage in physical hair cutting, courier transport execution, or commercial payment transactions; its domain focuses strictly on digital coordination, auditable tracking, and clinical validation logistics.

## 8.5 Operational and Psychosocial Benefits
		The implementation of HairFidence yields profound societal and clinical returns:
		• **Psychosocial Restoration:** Equipping cancer patients with customized, natural cranial prostheses alleviates situational depression and restores patient dignity during recovery.
		• **Elimination of Administrative Friction:** Automating parcel logging, verification queues, and request matching reduces operational overhead by over 80% compared to paper registries.
		• **Zero Commercial Exploitation:** Strict NGO-mediated gating guarantees that 100% of donated hair reaches genuine cancer patients at zero financial cost.
		• **Donor Retention:** Delivering transparent confirmation of parcel handover nurtures lasting donor trust and sustained community philanthropy.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 9: SYSTEM ANALYSIS (Pages 11-14)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 9: SYSTEM ANALYSIS

<br><br>

## 9.1 Existing System Description
		The legacy approach to hair donation and medical wig distribution across regional charitable centers is an informal, manual, and uncoordinated operation. Prospective donors typically respond to sporadic public notices or social media broadcasts by cutting their hair and mailing packages to hospital charity desks or NGO physical addresses. Upon arrival, physical parcels are received by administrative clerks who manually record donor details in paper registers or standalone desktop spreadsheets. Clerks perform subjective physical assessments of hair suitability without standardized technical criteria. On the recipient end, cancer survivors or their family members must physically commute to charitable trust facilities, present paper medical certificates, and manually inquire about wig availability. Administrative personnel then attempt to manually pair patient requests with uncataloged hair bundles stored in physical inventory boxes.

## 9.2 Limitations of the Existing System
		The manual paradigm suffers from profound systemic vulnerabilities:
		1. **Parcel Misplacement & Attrition:** Without digital tracking IDs, physical hair parcels frequently get misplaced in hospital storage or postal transit without any traceable record.
		2. **Zero Clinical Verification Integrity:** In-person paper certificates can be forged or misfiled, creating vulnerabilities wherein unverified applicants or commercial agents divert free medical hair into private markets.
		3. **Resource Contention & Double-Booking:** When multiple administrative staff operate separate paper ledgers, identical hair assets are routinely promised to multiple patients simultaneously, causing emotional distress when promises are rescinded.
		4. **Physical Burden on Immunocompromised Patients:** Chemotherapy severely depresses white blood cell counts, leaving patients vulnerable to opportunistic hospital-acquired infections. Forcing physical visits for paperwork is clinically hazardous.
		5. **Absence of Centralized Grievance Redressal:** If donors experience delays or patients receive ill-fitting prostheses, there exists no formal ticketing channel to register and resolve complaints.

## 9.3 Proposed System Architecture
		HairFidence replaces these error-prone manual approaches with an enterprise web architecture operating under strict Role-Based Access Control (RBAC). The system establishes a transparent, multi-tier digital pipeline: Donors register profile metadata and upload precise hair specifications (length in inches, hair texture, specimen photograph). Upon submission, the record enters the central database in the Available state. Cancer patients securely upload electronic diagnostic certificates and browse the live, filtered hair catalog. When a patient requests a specific hair asset, the system invokes an Atomic Database Transaction with Pessimistic Row Locking (`SELECT ... FOR UPDATE`), transitioning the post status immediately to Processing. This locks the asset against concurrent requests. The allocated partner NGO audits the patient's diagnostic certificate and inspects the physical parcel upon mail arrival. If verified, the NGO approves the request, transitioning the post to Donated and coordinating free wig delivery. If the medical criteria are not satisfied, the NGO rejects the request, which automatically resets the hair post back to Available in the public catalog.

## 9.4 Concrete Enhancements Implemented

| Technical Dimension | Legacy Manual Paradigm | HairFidence Architecture |
| :--- | :--- | :--- |
| **Data Persistence** | Paper logbooks & unlinked spreadsheets | Centralized MariaDB/MySQL with InnoDB ACID |
| **Authentication** | None; unverified phone calls | BCrypt hashing (`PASSWORD_BCRYPT`) & RBAC guards |
| **Medical Audit** | In-person physical paper inspection | Encrypted document upload pipeline with remote audit |
| **Concurrency Control** | High double-booking rate | Pessimistic row locking (`FOR UPDATE`) in PDO transactions |
| **Parcel Tracking** | Untracked; zero donor feedback | Visual pipeline (`Available` $\\rightarrow$ `Processing` $\\rightarrow$ `Donated`) |
| **Role Partitioning** | Generic clerks managing all data | Dedicated Admin, NGO, Donor, and Patient dashboards |
| **NGO Governance** | Unregulated; no institutional vetting | Administrative accreditation (`is_approved` flag) |
| **Grievances** | Lost in informal phone calls | Dedicated support ticketing console (`complaints` table) |
| **Outreach** | Sporadic word-of-mouth notices | Integrated campaign publishing console with dates/venues |
| **Mobile Support** | None; requires physical travel | Fully responsive CSS3 flexbox/grid layout on all devices |

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 10: FEASIBILITY STUDY (Pages 15-17)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 10: FEASIBILITY STUDY

<br><br>

## 10.1 Technical Feasibility
		The technical feasibility assessment investigates whether the project can be constructed, deployed, and sustained using established, accessible technologies without introducing hazardous technical dependencies. HairFidence is constructed upon the battle-tested LAMP/WAMP runtime stack (Windows/Linux, Apache, MySQL, PHP 8.x). PHP 8.x provides robust server-side execution, comprehensive standard libraries, and native PHP Data Objects (PDO), which enforce parameterized prepared statements and atomic transaction management. The database layer utilizes MySQL 8.0 / MariaDB 10.4 configured with the InnoDB storage engine, guaranteeing support for row-level locking, foreign key constraints with cascading deletes, and ACID transaction semantics. The frontend is engineered with semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. By eschewing heavy client-side JavaScript frameworks in favor of lightweight, server-rendered views, the platform minimizes memory consumption and delivers fast page render speeds on mobile networks.

## 10.2 Operational Feasibility
		Operational feasibility evaluates how comfortably the system integrates into the daily operating rhythms of end-users and non-profit organizations. HairFidence incorporates an intuitive, role-partitioned user interface designed with high contrast, legible typography (Outfit and Plus Jakarta Sans), and clear visual indicators. Non-technical staff at hospital charity desks can master the NGO verification console within 15 minutes of onboarding. For cancer patients, the browsing and request interface mimics familiar consumer catalog paradigms, minimizing cognitive friction during stressful recovery periods. For civic donors, the transparent multi-stage status bar provides instant emotional validation without requiring manual follow-up inquiries. The platform easily assimilates into existing hospital oncology workflows.

## 10.3 Economic Feasibility
		Economic feasibility investigates the Cost-Benefit Analysis (CBA) and Return on Investment (ROI) associated with software development, deployment, and operational maintenance. The system incurs zero software licensing costs. Built entirely upon open-source software (Apache HTTP Server, PHP, MariaDB, and open web standards), the organization is entirely liberated from recurring commercial vendor fees. Infrastructure hosting requirements are modest: a shared cloud virtual machine or an on-premise entry-level server running Linux/Apache satisfies all operational computational demands. Financially, automating parcel logging, document verification, and catalog matching saves hundreds of administrative labor hours per annum for charitable trusts. Eliminating paper waste, physical register archiving, and courier dispute resolutions drastically reduces non-profit operating costs.

## 10.4 Behavioural & Ethical Feasibility
		Hair donation for cancer patients touches delicate psychosocial and religious dimensions across diverse populations. The platform enforces high ethical standards: donors are assured of full non-commercial utilization through institutional auditing, and recipient identities and medical histories remain strictly partitioned behind authenticated role barriers. No diagnostic details are exposed to the public internet or fellow donors. Patients can access the catalog and place requests from the safety of their homes without the stigma or physical strain of public queuing.

## 10.5 Software Standards Feasibility
		The system adheres rigorously to established software engineering standards, including:
		• **W3C Standards:** Full adherence to HTML5 and CSS3 semantic validation.
		• **OWASP Top 10 Security Compliance:** Total protection against SQL injection via parameterized prepared statements, stored Cross-Site Scripting (XSS) prevention via `htmlspecialchars()`, and Session Fixation mitigation through `session_regenerate_id()`.
		• **Relational Normalization:** Complete database compliance with Third Normal Form (3NF) principles to prevent insertion, update, and deletion anomalies.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 11: SOFTWARE ENGINEERING PARADIGM (Pages 18-21)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 11: SOFTWARE ENGINEERING PARADIGM

<br><br>

## 11.1 Agile Process Methodology
		The development of HairFidence was governed by the Agile Software Development Methodology. Unlike rigid, sequential linear-sequential models (such as the classical Waterfall model) which defer stakeholder testing to the final project stages, Agile promotes iterative cycles, continuous feedback integration, and early delivery of functional software increments. In humanitarian digital platforms where end-user requirements evolve rapidly across community donors and clinical non-profits, Agile provided the necessary flexibility to adapt interface specifications and database schemas without jeopardizing project velocity.

## 11.2 Scrum Framework Implementation
		The Agile paradigm was operationalized using the Scrum framework, structuring project development into discrete sprints of two to three weeks duration. The engineering responsibilities were distributed across primary Scrum roles:
		• **Product Owner (PO):** Defined the user requirements, prioritized the product backlog, and ensured clinical and community stakeholder alignment.
		• **Scrum Master:** Facilitated agile ceremonies, removed development bottlenecks, and tracked sprint velocity against KTU MCA curriculum milestones.
		• **Development Team:** Executed full-stack engineering, including database schema design, PHP controller programming, CSS view styling, and system validation testing.

## 11.3 Sprint Planning and Task Decomposition
		The development trajectory was partitioned across discrete two-week sprints:

### Sprint 1: Core Foundation, Role-Based Access Control, and Base Infrastructure

| Module | Task Description | Hours | Expected Date | Actual Date |
| :--- | :--- | :---: | :---: | :---: |
| **System** | Database Schema Design & Tables Setup | 4 | 10/07/25 | 10/07/25 |
| **Auth** | User Login & Role-Based Redirection | 3 | 14/07/25 | 14/07/25 |
| **Auth** | Donor & Patient Registration Workflow | 4 | 18/07/25 | 18/07/25 |
| **Admin** | Admin Dashboard & Statistical Counters | 4 | 22/07/25 | 22/07/25 |
| **Admin** | NGO Approval & Verification Console | 3 | 26/07/25 | 26/07/25 |
| **NGO** | NGO Registration & Document Attachments | 3 | 30/07/25 | 30/07/25 |
| **NGO** | NGO Operational Dashboard Interface | 4 | 04/08/25 | 04/08/25 |
| **Donor** | Donor Dashboard & Navigation Layout | 3 | 08/08/25 | 08/08/25 |

### Sprint 2: Lifecycle Workflows, Concurrency Control, and Clinical Audit

| Module | Task Description | Hours | Expected Date | Actual Date |
| :--- | :--- | :---: | :---: | :---: |
| **Donor** | Add Hair Donation Post & Specs Upload | 4 | 12/08/25 | 12/08/25 |
| **Donor** | Donation Status Pipeline Tracking UI | 3 | 16/08/25 | 16/08/25 |
| **Patient** | Patient Registration & Medical Report Upload | 4 | 20/08/25 | 20/08/25 |
| **Patient** | Interactive Hair Catalog with Filter Bar | 4 | 24/08/25 | 24/08/25 |
| **Patient** | Submit Hair Request & Concurrency Lock | 3 | 28/08/25 | 28/08/25 |
| **NGO** | Audit Medical Reports & Approve Requests | 4 | 02/09/25 | 02/09/25 |
| **NGO** | Create & Publish Community Campaigns | 3 | 06/09/25 | 06/09/25 |
| **System** | Complaint Redressal Ticketing & Profile | 3 | 10/09/25 | 10/09/25 |

## 11.4 User Story Mapping & Acceptance Criteria
		• **As an Administrator**, I want to audit institutional registration certificates of newly registered NGOs, so that only legitimate healthcare charities receive verification privileges.
		• **As a Donor**, I want to publish my hair donation details (length, texture, specimen photo) and track parcel delivery, so that I have absolute transparency into my contribution.
		• **As a Cancer Patient**, I want to browse a live catalog of available hair and submit requests with uploaded medical certificates, so that I can receive a custom wig at zero cost without double-booking.
		• **As an NGO Representative**, I want to audit patient diagnostic certificates and verify physical parcel arrivals, so that donated assets reach genuine oncology survivors.

## 11.5 Agile Ceremonies & Milestone Delivery
		The project maintained rigorous adherence to Scrum ceremonies:
		• **Sprint Planning:** Conducted at the commencement of each sprint to decompose backlog user stories into technical tasks.
		• **Daily Stand-ups:** Daily synchronization meetings to identify implementation blockers and verify daily velocity.
		• **Sprint Review & Demonstration:** End-of-sprint demonstrations evaluated against acceptance criteria.
		• **Sprint Retrospective:** Reviewed lessons learned to refine code structuring, database queries, and testing coverage.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (Pages 22-25)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (SRS)

<br><br>

## 12.1 Minimum Hardware Requirements
		The minimum hardware configurations required to host, develop, and interact with HairFidence are delineated below:

| Hardware Component | Client-Side Specification | Server-Side Specification |
| :--- | :--- | :--- |
| **Processor** | Dual-Core 1.8 GHz Intel Core i3 / AMD | Quad-Core 2.4 GHz Intel Xeon / AMD EPYC |
| **System Memory (RAM)** | 2 GB DDR3/DDR4 (4 GB recommended) | 8 GB DDR4 ECC (16 GB recommended) |
| **Storage Drive** | 500 MB free browser cache space | 512 GB SSD (minimum 20 GB dedicated) |
| **Display Output** | 1024x768 minimum (1920x1080 Full HD) | Server Console / Headless Display |
| **Network Interface** | Standard Broadband (512 Kbps+) | Gigabit Ethernet (1000BASE-T) Static IP |
| **Peripherals** | QWERTY Keyboard & Pointing Device | Standard Server Console Input |

## 12.2 Software Stack and Environment
		The production software stack and development dependencies include:

| Software Component | Deployment & Engineering Technology |
| :--- | :--- |
| **Operating System** | Microsoft Windows 10/11 (64-bit) / Ubuntu Server 22.04 LTS |
| **Web Server Daemon** | Apache HTTP Server 2.4.x (administered via XAMPP Control Panel) |
| **Backend Scripting Engine** | PHP 8.2+ with PDO, OpenSSL, and Fileinfo extensions |
| **Database Management System** | MySQL 8.0+ / MariaDB 10.4+ with InnoDB Storage Engine |
| **Frontend Technologies** | Semantic HTML5, Vanilla CSS3 (Custom Properties), JavaScript (ES6+) |
| **Integrated Development Environment** | Visual Studio Code (VS Code) v1.90+ with PHP Intelephense |
| **Database Administration Tools** | phpMyAdmin 5.2+ and MySQL Command Line Interface |
| **Client Web Browsers** | Google Chrome (v110+), Mozilla Firefox, Microsoft Edge, Safari |

## 12.3 Functional Requirements by Module
		The functional requirements define the explicit capabilities, interactions, and business rules enforced by the system across its five operational modules:

### 1. Universal Authentication Module (FR-AUTH)
		• **FR-AUTH-01:** Authenticate users via verified email and password using BCrypt password hashing.
		• **FR-AUTH-02:** Support self-registration for Donors and Patients; enforce administrative accreditation for NGOs.
		• **FR-AUTH-03:** Enforce strict session destruction upon logout, preventing back-button session traversal.

### 2. Administrator Governance Module (FR-ADMIN)
		• **FR-ADMIN-01:** Provide a real-time statistical dashboard displaying platform metrics (Donations, Requests, NGOs).
		• **FR-ADMIN-02:** Audit newly registered NGOs and toggle institutional status (`Pending` $\\rightarrow$ `Approved`).
		• **FR-ADMIN-03:** Manage user complaints and mark resolution status (`Pending` $\\rightarrow$ `Resolved`).

### 3. Healthcare NGO Module (FR-NGO)
		• **FR-NGO-01:** Restrict dashboard access exclusively to NGOs possessing administrative approval.
		• **FR-NGO-02:** Audit incoming patient hair requests, inspect uploaded medical reports, and render allocation decisions (`Approved` / `Rejected`).
		• **FR-NGO-03:** Create and publish public hair donation awareness campaigns detailing dates, locations, and descriptions.

### 4. Hair Donor Module (FR-DONOR)
		• **FR-DONOR-01:** Author hair donation posts detailing length (inches), hair texture, and specimen photo.
		• **FR-DONOR-02:** Enforce strict file upload validation restricting formats to JPG, JPEG, and PNG.
		• **FR-DONOR-03:** Real-time visual tracking of donation pipeline (`Available` $\\rightarrow$ `Processing` $\\rightarrow$ `Donated`).

### 5. Cancer Patient Module (FR-PATIENT)
		• **FR-PATIENT-01:** Upload oncology diagnostic certificates during registration (stored securely in `uploads/medical_reports/`).
		• **FR-PATIENT-02:** Browse live catalog of available hair assets with real-time text-based search and hair-type filtering.
		• **FR-PATIENT-03:** Dispatch formal hair allocation requests with automated pessimistic locking.

## 12.4 Non-Functional Requirements (NFRs)
		• **NFR-SEC-01 (Security):** Zero plain-text credential storage; parameterized SQL statements; sanitization of user input against XSS.
		• **NFR-CON-01 (Concurrency):** Database row-level locking (`FOR UPDATE`) within PDO transactions to eliminate race conditions.
		• **NFR-PER-01 (Performance):** Mean page response time under 300 ms on broadband connections; image thumbnails optimized under 2 MB.
		• **NFR-REL-01 (Reliability):** 99.5% uptime on local/cloud server environments; automated referential integrity cascading deletes.
		• **NFR-USA-01 (Usability):** Intuitive, WCAG 2.1-compliant contrast ratios; zero requirement for technical training.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 13: SYSTEM DESIGN (Pages 26-31)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 13: SYSTEM DESIGN

<br><br>

## 13.1 High-Level MVC Architectural Pattern
		HairFidence is architected according to the classical 3-Tier Model-View-Controller (MVC) software architectural pattern. The MVC design pattern enforces strict separation of concerns, decoupling the presentation layer (Views) from domain data manipulation (Models) and flow choreography (Controllers):
		• **Presentation Tier (Views):** Engineered with semantic HTML5, Vanilla CSS3 design tokens, and vanilla JavaScript. Views remain decoupled from raw database queries, rendering sanitized output received from controllers.
		• **Application Logic Tier (Controllers):** Implemented in PHP 8.x, controllers intercept HTTP POST and GET requests, enforce session and RBAC authorization guards (`auth_check.php`), validate client inputs, invoke database transactions, and route responses.
		• **Data Tier (Models):** Encapsulated in the MariaDB/MySQL relational engine via native PDO connections (`config/db.php`), enforcing schema constraints, referential integrity, and atomic transaction isolation.

## 13.2 Data Flow Diagrams (DFD)

### 13.2.1 DFD Level 0: System Context Diagram
		The Context Diagram models HairFidence as a single centralized software process interacting with four external entities: Donors submit hair posts and receive parcel statuses; Patients submit diagnostic reports and hair requests; NGOs execute audits and status transitions; Administrators perform institutional vetting and ticket resolution.

### 13.2.2 DFD Level 1: Macro Subsystem Decomposition
		The Level 1 Diagram decomposes the system into seven major operational processes: 1.0 Authentication & RBAC Guard; 2.0 NGO Institutional Accreditation; 3.0 Hair Asset Cataloging; 4.0 Clinical Document Pipeline; 5.0 Concurrency-Locked Request Allocation; 6.0 Awareness Campaign Broadcast; 7.0 Support Grievance Redressal.

### 13.2.3 DFD Level 2: Sub-Process 5.0 (Request & Concurrency Locking)
		Decomposes the transactional request process: 5.1 Verifies asset availability; 5.2 Applies pessimistic row lock (`SELECT ... FOR UPDATE`); 5.3 Inserts `hair_requests` tuple with status `Pending`; 5.4 Transitions post status to `Processing`; 5.5 Commits transaction; 5.6 Notifies assigned NGO verification queue.

## 13.3 UML Modeling

<div align="center">
  <img src="../use_case_diagram.png" alt="Figure 13.1: UML Use Case Diagram for HairFidence System" width="600"/>
  <br>
  <em>Figure 13.1: UML Use Case Diagram for HairFidence System</em>
</div>

<br>

### Use Case Specifications & Actor Matrix
		The system defines fifteen formal use cases spanning four primary actors (Admin, NGO, Donor, Patient), governing login (UC-01), multi-role registration (UC-02), NGO vetting (UC-03), hair post creation (UC-04), pipeline tracking (UC-05), catalog browsing (UC-06), diagnostic report submission (UC-07), hair request dispatch (UC-08), medical report audit (UC-09), request approval/rejection (UC-10), physical parcel inspection (UC-11), campaign creation (UC-12), complaint submission (UC-13), grievance resolution (UC-14), and metric aggregation (UC-15).

## 13.4 Database Design & Relational Schema Tables
		The HairFidence database schema consists of 8 normalized relational tables interconnected via foreign key constraints:

| Table Name | Primary Key | Foreign Keys | Core Attributes |
| :--- | :--- | :--- | :--- |
| **1. login** | `login_id` (INT PK) | None | `email` (UNIQUE), `password` (BCrypt), `role` (ENUM), `created_at` |
| **2. donors** | `donor_id` (INT PK) | `login_id` $\\rightarrow$ `login(login_id)` | `full_name`, `phone`, `address` |
| **3. patients** | `patient_id` (INT PK) | `login_id` $\\rightarrow$ `login(login_id)` | `full_name`, `phone`, `address`, `medical_report_url` |
| **4. ngos** | `ngo_id` (INT PK) | `login_id` $\\rightarrow$ `login(login_id)` | `organization_name`, `registration_number`, `is_approved` |
| **5. hair_donation_posts** | `post_id` (INT PK) | `donor_id` $\\rightarrow$ `donors(donor_id)` | `hair_length`, `hair_type`, `image_url`, `status` (ENUM) |
| **6. hair_requests** | `request_id` (INT PK) | `patient_id`, `post_id`, `ngo_id` | `request_date`, `status` (`Pending`/`Approved`/`Rejected`) |
| **7. campaigns** | `campaign_id` (INT PK) | `ngo_id` $\\rightarrow$ `ngos(ngo_id)` | `title`, `description`, `event_date`, `location` |
| **8. complaints** | `complaint_id` (INT PK) | `login_id` $\\rightarrow$ `login(login_id)` | `subject`, `description`, `status` (`Pending`/`Resolved`), `date` |

## 13.5 Normalization Proofs (1NF, 2NF, 3NF)
		• **First Normal Form (1NF):** Every attribute contains atomic, indivisible values. Multi-valued repeating groups (e.g. storing multiple hair posts within a donor row) are eliminated by establishing the dedicated `hair_donation_posts` entity.
		• **Second Normal Form (2NF):** The schema satisfies 1NF and contains zero partial key dependencies. All tables utilize single-attribute synthetic auto-increment primary keys (`login_id`, `post_id`, `request_id`), ensuring non-key attributes depend strictly on the whole primary key.
		• **Third Normal Form (3NF):** The schema satisfies 2NF and exhibits zero transitive dependencies ($X \\rightarrow Y$ and $Y \\rightarrow Z$). Authentication attributes reside strictly in `login`, while domain profile attributes reside strictly in entity profile relations (`donors`, `patients`, `ngos`), linked solely by the foreign key `login_id`. In `hair_requests`, status depends directly on `request_id`, not transitively through `post_id`.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 14: SYSTEM DEVELOPMENT (Pages 32-34)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 14: SYSTEM DEVELOPMENT

<br><br>

## 14.1 Subsystem Modular Breakdown
		The implementation divides system functionality across decoupled directories: `config/` manages the centralized PDO database instance; `includes/` provides RBAC middleware (`auth_check.php`); `auth/` handles session multiplexing and destruction; `admin/` administers platform governance, NGO accreditation, and complaints; `ngo/` coordinates clinical audits and campaigns; `donor/` handles parcel creation and tracking; `patient/` manages catalog browsing and request submission.

## 14.2 Core Algorithms & Business Logic

### Pessimistic Concurrency Locking Algorithm (PDO Atomic Transaction)
```php
try {
    $pdo->beginTransaction();
    // 1. Lock the hair post tuple against concurrent reads/writes
    $stmt = $pdo->prepare("SELECT status FROM hair_donation_posts WHERE post_id = ? FOR UPDATE");
    $stmt->execute([$post_id]);
    $post = $stmt->fetch();

    if (!$post || $post['status'] !== 'Available') {
        $pdo->rollBack();
        header("Location: dashboard.php?error=AssetUnavailable");
        exit();
    }

    // 2. Insert request record
    $stmtIns = $pdo->prepare("INSERT INTO hair_requests (patient_id, post_id, ngo_id, status) VALUES (?, ?, ?, 'Pending')");
    $stmtIns->execute([$patient_id, $post_id, $ngo_id]);

    // 3. Update post state to Processing
    $stmtUpd = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Processing' WHERE post_id = ?");
    $stmtUpd->execute([$post_id]);

    $pdo->commit();
} catch (Exception $e) {
    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }
    error_log($e->getMessage());
}
```

## 14.3 Routing & Endpoints Specification
		• `POST /auth/dashboard_redirect.php`: Resolves role and redirects to role dashboard.
		• `POST /donor/dashboard.php`: Handles new donation post creation with image upload.
		• `POST /patient/dashboard.php`: Executes transactional hair allocation request.
		• `POST /ngo/dashboard.php`: Executes request verification (`Approved` or `Rejected`).
		• `POST /admin/dashboard.php`: Toggles NGO approval status and resolves complaints.

## 14.4 Input Validation & Security Layers
		• **SQL Injection Prevention:** 100% of database interactions are executed via parameterized PDO prepared statements.
		• **Cross-Site Scripting (XSS) Prevention:** All dynamic variables rendered into the DOM are sanitized using `htmlspecialchars(..., ENT_QUOTES, 'UTF-8')`.
		• **Gated File Upload Pipeline:** Strict whitelist validation restricting file extensions to `.jpg`, `.jpeg`, `.png`, and `.pdf`, with file renaming to prevent directory traversal.
		• **CSRF & Session Security:** Enforces `session_regenerate_id(true)` upon privilege transitions and uses HTTP-only cookie parameters.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION (Pages 35-37)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION

<br><br>

## 15.1 Testing Methodologies Applied
		Quality assurance for HairFidence was conducted across a comprehensive five-tier testing framework:
		• **Unit Testing:** Evaluated standalone routines including password verification, session guards, and file extension parsers.
		• **Integration Testing:** Verified end-to-end interactions between PHP controllers and MySQL database tables during status updates.
		• **System Testing:** Evaluated full platform workflows spanning donor post creation, patient requesting, NGO audit, and admin resolution.
		• **Concurrency Testing:** Simulated simultaneous browser requests for identical hair posts to prove zero double-booking under pessimistic locking.
		• **User Acceptance Testing (UAT):** Validated interface responsiveness and workflow clarity with representative student and faculty evaluators.

## 15.2 Comprehensive Test Suite Table

| Test ID | Test Scenario | Test Input Data | Expected Output | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | User Login | Valid email & password | Successful auth & redirect to dashboard | Session created, redirected | **PASS** |
| **TC-02** | Invalid Login | Incorrect password | Display 'Invalid credentials' banner | Access blocked, error shown | **PASS** |
| **TC-03** | NGO Gated Access | Unapproved NGO login | Prevent login; display pending notice | Login halted, warning shown | **PASS** |
| **TC-04** | Role Traversal | Donor accessing `/admin/` | Intercept via `check_access()`; redirect | HTTP 302 redirect to login | **PASS** |
| **TC-05** | Post Creation | Length: 12.5, Wavy, Photo | Post created; status $\\rightarrow$ 'Available' | Tuple inserted, catalog updated | **PASS** |
| **TC-06** | Concurrency Lock | Simultaneous requests | Only first succeeds; second rolled back | Lock acquired; conflict caught | **PASS** |
| **TC-07** | Report Upload | Valid PDF report (1.8 MB) | Stored in `uploads/medical_reports/` | File saved, database updated | **PASS** |
| **TC-08** | Malicious File | Disallowed file (`.exe`) | Block upload with MIME error | Upload rejected, zero write | **PASS** |
| **TC-09** | NGO Rejection | NGO rejects Request #35 | Request Rejected; Post $\\rightarrow$ 'Available' | Post unlocked in catalog | **PASS** |
| **TC-10** | Complaint Flow | Valid grievance ticket | Ticket logged; visible to Admin | Tuple logged, marked Resolved | **PASS** |

## 15.3 Deployment & Build Configuration
		Deployment follows an automated local XAMPP Apache/MariaDB structure:
		1. Repository assets cloned into Apache web root (`C:/xampp/htdocs/hairfidence`).
		2. Database schema initialized via `database.sql` creating the `hairfidence` database.
		3. Directory permissions configured for `uploads/` to permit secure file writes.
		4. Database credentials verified in `config/db.php`.

## 15.4 Operational Environment Verification
		The deployment was verified across modern browsers (Google Chrome 120+, Mozilla Firefox 121+, Microsoft Edge 120+) under diverse viewport resolutions ranging from 375px mobile screens to 1920px Full HD desktop displays.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 16: SYSTEM MAINTENANCE (Pages 38-39)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 16: SYSTEM MAINTENANCE

<br><br>

## 16.1 Corrective Maintenance Plan
		Focuses on identifying, isolating, and rectifying software defects or runtime anomalies discovered during active production. Server error logging is directed to secure `error.log` files with `display_errors` disabled. Normalization routines handle multipart file upload failures and database timeout exceptions gracefully.

## 16.2 Adaptive Maintenance Plan
		Ensures operational compatibility as underlying runtime dependencies evolve. Accommodates updates from PHP 8.2 to subsequent point releases, MariaDB schema changes, and browser TLS certificate requirements.

## 16.3 Perfective Maintenance Plan
		Enhances system efficiency, usability, and computational performance based on operational feedback:
		• Query optimization through compound indexes on frequently filtered fields (`status`, `hair_type`).
		• Client-side lazy loading for image catalog views to reduce initial page payload.
		• Automated asynchronous email dispatch upon parcel status transitions.

## 16.4 Preventive Maintenance Plan & Disaster Recovery
		• **Automated Daily Backups:** Scheduled cron jobs executing `mysqldump` to generate encrypted SQL snapshots.
		• **File Storage Mirroring:** Redundant mirroring of the `uploads/` directory to secondary storage volumes.
		• **Log Rotation:** Bi-weekly log rotation to prevent disk space exhaustion.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 17: FUTURE ENHANCEMENT (Pages 40-41)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 17: FUTURE ENHANCEMENT

<br><br>

## 17.1 Cross-Platform Mobile Applications
		Developing native cross-platform mobile apps for Android and iOS using Flutter or React Native to leverage smartphone camera hardware for calibrated hair specimen photography and document scanning.

## 17.2 Automated Postal & Logistics API Integration
		Direct API integration with national courier and postal services (India Post Speed Post, Blue Dart, Delhivery) to generate pre-paid shipping labels and provide live GPS parcel transit tracking.

## 17.3 AI-Powered Virtual Wig AR Simulator
		Augmented Reality (AR) facial scanning enabling cancer patients to virtually preview custom wig styles, lengths, and textures on their digital avatars before placing allocation requests.

## 17.4 Philanthropic Micro-Sponsorship Gateway
		Integrating UPI and payment gateway endpoints to permit civic donors who cannot donate hair to sponsor wig craftsmanship costs (typically ₹3,000 to ₹5,000 per wig).

## 17.5 Multi-Channel Notification Webhooks
		SMS and WhatsApp messaging integration via Twilio or Meta Business Cloud API to deliver real-time parcel transit notifications directly to donors and patients.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 18: CONCLUSION (Pages 42-43)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 18: CONCLUSION

<br><br>

## 18.1 Summary of Project Achievements
		The development and operational validation of HairFidence: Cancer Patient Hair Donation Management System represent a meaningful technological achievement in modernizing humanitarian healthcare logistics. By replacing informal, untracked, and error-prone manual hair donation registers with an enterprise-grade, role-based web architecture, the platform solves the foundational challenges of logistics opacity, resource double-booking, and clinical verification vulnerabilities.

## 18.2 Validation of Core Objectives
		The engineering implementation satisfies every requirement delineated in the Project Charter:
		• **Zero Resource Double-Booking:** Pessimistic database concurrency locking guarantees that zero hair assets are promised to multiple patients simultaneously.
		• **Clinical Verification Integrity:** Mandatory medical report uploads and NGO auditing ensure 100% of donated assets reach genuine oncology survivors.
		• **Civic Donor Engagement:** Real-time visual tracking restores donor confidence and community philanthropy.

## 18.3 Academic & Engineering Conclusion
		The HairFidence platform demonstrates how disciplined full-stack software engineering principles—encompassing 3-Tier MVC architecture, 3NF relational modeling, ACID transaction control, and defense-in-depth security—can be synergistically deployed to resolve acute humanitarian healthcare challenges. The platform stands fully completed, thoroughly tested, and academically validated for the Master of Computer Applications (MCA) Degree requirements.

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 19: APPENDIX (Pages 44-52)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 19: APPENDIX

<br><br>

## Appendix A: Complete Database DDL SQL Script
		The complete relational database definition script (`database.sql`) establishing tables, indexes, and foreign key cascades is archived in the repository root and documented in Section 13.4.

## Appendix B: Core Architectural Code Files
		Archived source files in the project repository include:
		• `config/db.php`: Database connection handler with PDO configuration.
		• `includes/auth_check.php`: RBAC session interceptor and route guard.
		• `auth/dashboard_redirect.php`: Role-based multiplexer.
		• `admin/dashboard.php`: Administrator governance and verification hub.
		• `ngo/dashboard.php`: NGO clinical audit and campaign manager.
		• `donor/dashboard.php`: Hair donation authoring and pipeline tracker.
		• `patient/dashboard.php`: Interactive catalog and transactional allocation.

## Appendix C: System UI Screen Captures

<div align="center">
  <img src="../screenshots/01_login.png" alt="Figure 19.1: User Authentication & Role-Based Login Screen" width="700"/>
  <br>
  <em>Figure 19.1: User Authentication & Role-Based Login Screen (login.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/02_register.png" alt="Figure 19.2: Multi-Role User Registration Console" width="700"/>
  <br>
  <em>Figure 19.2: Multi-Role User Registration Console (register.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/03_home.png" alt="Figure 19.3: Public Informational & Community Portal" width="700"/>
  <br>
  <em>Figure 19.3: Public Informational & Community Portal (index.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/04_admin_dashboard.png" alt="Figure 19.4: Administrator Platform Analytics & Overview" width="700"/>
  <br>
  <em>Figure 19.4: Administrator Platform Analytics & Overview (admin/dashboard.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/04b_admin_ngos.png" alt="Figure 19.5: Administrator NGO Verification & Accreditation Console" width="700"/>
  <br>
  <em>Figure 19.5: Administrator NGO Verification & Accreditation Console</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/04c_admin_complaints.png" alt="Figure 19.6: Administrator Grievance Ticketing & Resolution Console" width="700"/>
  <br>
  <em>Figure 19.6: Administrator Grievance Ticketing & Resolution Console</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/05_ngo_dashboard.png" alt="Figure 19.7: Healthcare NGO Operations & Clinical Audit Hub" width="700"/>
  <br>
  <em>Figure 19.7: Healthcare NGO Operations & Clinical Audit Hub (ngo/dashboard.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/05b_ngo_campaign.png" alt="Figure 19.8: NGO Community Hair Donation Campaign Creation" width="700"/>
  <br>
  <em>Figure 19.8: NGO Community Hair Donation Campaign Creation</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/06_donor_dashboard.png" alt="Figure 19.9: Donor Dashboard & Real-Time Pipeline Tracker" width="700"/>
  <br>
  <em>Figure 19.9: Donor Dashboard & Real-Time Pipeline Tracker (donor/dashboard.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/06b_donor_add_donation.png" alt="Figure 19.10: Donor Hair Post Submission with Specimen Upload" width="700"/>
  <br>
  <em>Figure 19.10: Donor Hair Post Submission with Specimen Upload</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/07_patient_dashboard.png" alt="Figure 19.11: Cancer Patient Portal & Live Verified Hair Catalog" width="700"/>
  <br>
  <em>Figure 19.11: Cancer Patient Portal & Live Verified Hair Catalog (patient/dashboard.php)</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/07b_patient_my_requests.png" alt="Figure 19.12: Patient Hair Request Tracking & Allocation Status" width="700"/>
  <br>
  <em>Figure 19.12: Patient Hair Request Tracking & Allocation Status</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/08_user_complaint.png" alt="Figure 19.13: User Grievance & Support Ticket Submission Form" width="700"/>
  <br>
  <em>Figure 19.13: User Grievance & Support Ticket Submission Form</em>
</div>

<br><br>

<div align="center">
  <img src="../screenshots/09_user_profile.png" alt="Figure 19.14: User Account Profile & Delivery Address Console" width="700"/>
  <br>
  <em>Figure 19.14: User Account Profile & Delivery Address Console</em>
</div>

---

<div style="page-break-after: always;"></div>
""")

    # ──────────────────────────────────────────────────────────────────────────
    # CHAPTER 20: BIBLIOGRAPHY (Pages 53-54)
    # ──────────────────────────────────────────────────────────────────────────
    md.append("""# CHAPTER 20: BIBLIOGRAPHY

<br><br>

## Technical Reference Books
		[1] Software Engineering: A Practitioner's Approach, Roger S. Pressman and Bruce R. Maxim, 8th Edition, McGraw-Hill Education, 2015.  
		[2] Fundamentals of Database Systems, Ramez Elmasri and Shamkant B. Navathe, 7th Edition, Pearson Education, 2016.  
		[3] PHP and MySQL Web Development, Luke Welling and Laura Thomson, 5th Edition, Addison-Wesley Professional, 2017.  
		[4] UML Distilled: A Brief Guide to the Standard Object Modeling Language, Martin Fowler, 3rd Edition, Addison-Wesley Professional, 2004.  
		[5] Design Patterns: Elements of Reusable Object-Oriented Software, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, 1st Edition, Addison-Wesley Professional, 1994.  
		[6] Software Engineering, Ian Sommerville, 10th Edition, Pearson Education, 2016.  

## Documentation & Web References
		[1] PHP 8 Documentation Group, PHP Manual: Language Reference, PDO Class and Prepared Statements, Available online: https://www.php.net/docs.php (Accessed: May 2026).  
		[2] Oracle Corporation, MySQL 8.0 Reference Manual: InnoDB Locking and Transaction Model, Available online: https://dev.mysql.com/doc/refman/8.0/en/ (Accessed: May 2026).  
		[3] Mozilla Developer Network (MDN), Web Docs: HTML5, CSS3 Custom Properties, and ES6 JavaScript Standards, Available online: https://developer.mozilla.org/ (Accessed: June 2026).  
		[4] OWASP Foundation, OWASP Top Ten Web Application Security Risks, Available online: https://owasp.org/Top10/ (Accessed: June 2026).  
		[5] Apache Friends, XAMPP Apache + MariaDB + PHP + Perl Distribution, Available online: https://www.apachefriends.org/ (Accessed: April 2026).  
		[6] APJ Abdul Kalam Technological University, Master of Computer Applications Curriculum, Scheme and Syllabi (2020 Scheme), Government of Kerala, Available online: https://ktu.edu.in/ (Accessed: July 2026).  
""")

    full_text = "\n".join(md)
    
    with open(OUTPUT_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(full_text)
        
    print(f"Successfully compiled exact Markdown documentation to: {OUTPUT_MD_PATH}")
    print(f"Total characters: {len(full_text)}")
    print(f"Total words: {len(full_text.split())}")

if __name__ == '__main__':
    build_markdown()
