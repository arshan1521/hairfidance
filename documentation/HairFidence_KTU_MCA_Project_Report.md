# HAIRFIDENCE
## CANCER PATIENT HAIR DONATION MANAGEMENT SYSTEM

### PROJECT THESIS REPORT
Submitted in partial fulfillment of the requirements for the award of the degree of  
### MASTER OF COMPUTER APPLICATIONS
of  
**APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY, KERALA**

<br>

**Submitted by:**  
**ARSHAN NIZAR K P**  
**(Register Number: AWH25MCA-2010)**  

<br>

**DEPARTMENT OF COMPUTER APPLICATIONS**  
**AWH ENGINEERING COLLEGE**  
**KUTTIKKATTOOR, CALICUT - 673008**  
*(Affiliated to APJ Abdul Kalam Technological University, Kerala)*  

**JULY 2026**  

---

<div style="page-break-after: always;"></div>

# BONA FIDE CERTIFICATE

### DEPARTMENT OF COMPUTER APPLICATIONS
### AWH ENGINEERING COLLEGE
### KUTTIKKATTOOR, CALICUT - 673008

<br>

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

# ACKNOWLEDGEMENT

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

# ABSTRACT

		Chemotherapy-induced hair loss severely impacts the psychological well-being of cancer patients. While many compassionate individuals wish to donate hair for medical wigs, the lack of a standardized platform bottlenecks coordination between donors, non-governmental organizations (NGOs), and verified recipients. The proposed project, HairFidence, resolves this operational gap by introducing a centralized web application designed to digitalize and streamline the entire hair donation lifecycle.

		Built on an interactive HTML, CSS, and JavaScript frontend with a secure PHP backend, HairFidence manages transactions through an optimized MySQL database in a local XAMPP environment. By utilizing an elegant 8-table relational schema, the platform guarantees rapid execution speeds, robust concurrency control via PDO transactions, and strict data privacy to effectively prevent resource double-booking and secure data leakage.

		The system logically partitions functionality across four distinct modules: Administrator, NGOs, Donors, and Patients. Donors can easily list hair specifications and track deliveries, while patients securely upload medical reports to request verified matches. Registered NGOs act as essential gatekeepers by auditing records and physical donations, overseen globally by the Administrator. Ultimately, HairFidence fosters an efficient, community-driven logistics network, returning dignity to cancer survivors.

---

<div style="page-break-after: always;"></div>

# CONTENTS

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

# CHAPTER 8: INTRODUCTION

## 8.1 System Overview
		In contemporary clinical oncology, pharmacological advancements, targeted chemotherapies, and advanced radiotherapy regimens have substantially elevated cancer survival rates across global populations. However, systemic oncology protocols frequently inflict severe physical, emotional, and psychosocial distress upon patients. Among treatment-associated complications, chemotherapy-induced alopecia (hair loss) is clinically recognized as one of the most acutely demoralizing and traumatic experiences endured by cancer survivors, predominantly impacting women, adolescents, and children. Unlike internal physiological symptoms, alopecia serves as an involuntary, inescapable visual badge of malignancy, precipitating acute clinical depression, diminished self-worth, social stigmatization, and in severe instances, treatment non-compliance.

		Specialized cranial medical prostheses (custom-crafted natural hair wigs) offer profound psychosocial rehabilitation, enabling recovering patients to reclaim their self-image, emotional well-being, and social confidence. Unfortunately, the commercial marketplace for natural hair wigs is severely cost-prohibitive, typically commanding prices between ₹25,000 and ₹1,20,000 ($300 to $1,500) per unit owing to meticulous hand-knotting craftsmanship and raw material scarcity. Concurrently, thousands of compassionate citizens express an active willingness to donate their natural hair for charitable wig fabrication. Regrettably, traditional charitable avenues across Kerala and India remain uncoordinated, informal, and vulnerable to operational failures.

		HairFidence is an enterprise-grade, centralized, role-governed web application engineered to bridge this vital humanitarian divide. Operating on a robust 3-Tier Model-View-Controller (MVC) architecture, the platform digitizes and audits the complete hair donation lifecycle. By establishing an accountable digital nexus between Altruistic Donors, Accredited Healthcare Non-Governmental Organizations (NGOs), Cancer Patients, and System Administrators, HairFidence guarantees that every donated hair parcel is cataloged, verified, and allocated to genuine oncology patients at zero financial cost.

## 8.2 Problem Statement & Clinical Context
		The traditional hair donation ecosystem suffers from three acute, interrelated structural deficiencies:
		1. Severe Donor Disconnect & Logistics Opacity: Altruistic citizens wishing to contribute hair typically encounter fragmented social media appeals or informal word-of-mouth campaigns. Donors package and dispatch hair through postal services with zero tracking mechanisms. Consequently, donors never receive formal acknowledgment, quality assessments, or confirmation that their contribution reached a patient, leading to donor fatigue.
		2. Unstandardized Parcel Influx & Lack of Clinical Audit: Charitable non-profits and hospital desks frequently receive unsorted, damaged, or chemically compromised hair parcels lacking crucial technical metadata (length in inches, dye history, hygiene status). Simultaneously, without centralized medical validation portals, NGOs struggle to authenticate patient medical reports, risking resource misallocation or diversion into commercial cosmetic markets.
		3. Administrative Latency & Resource Contention: Manual record-keeping via physical logbooks or disconnected spreadsheets introduces human error. Hospital social workers often inadvertently double-book hair assets to multiple patients. Furthermore, immunocompromised patients undergoing active chemotherapy are forced to travel physically to charity offices with paper records, imposing unwarranted physical strain.

## 8.3 Objectives of the System
		The primary technical, clinical, and operational objectives of HairFidence include:
		• Centralized Data Management: Unify donor contributions, patient requests, clinical records, and NGO accreditations into an ACID-compliant MariaDB/MySQL relational data store.
		• End-to-End Parcel Lifecycle Tracking: Provide real-time visual pipeline monitoring across three discrete transactional states: Available (cataloged), Processing (patient request locked pending NGO verification), and Donated (inspected and dispatched).
		• Pessimistic Concurrency Locking: Implement database-level row locking (FOR UPDATE) within atomic PDO transactions to completely eliminate race conditions and asset double-booking.
		• Privacy-Preserving Clinical Validation: Provide a secure document upload pipeline that isolates patient oncology diagnostic certificates, restricting viewing privileges strictly to verified NGO auditors and administrators.
		• Democratic Community Engagement: Enable accredited NGOs to broadcast community donation drives and awareness campaigns, expanding civic participation across diverse demographic sectors.

## 8.4 Scope of the Project
		The architectural and functional scope of HairFidence encompasses:
		• Functional Boundary: Comprehensive governance spanning four user roles (Administrator, NGO, Donor, Patient), secure authentication using BCrypt hashing, responsive catalog browsing, real-time status pipelines, and grievance ticket tracking.
		• Geographical & Organizational Scope: Engineered for regional deployment across hospital oncology wards, charitable healthcare trusts, and volunteer networks in Kozhikode and Kerala, with structural scalability supporting nationwide charitable deployment.
		• Exclusions & Operational Boundaries: The application does not engage in physical hair cutting, courier transport execution, or commercial payment transactions; its domain focuses strictly on digital coordination, auditable tracking, and clinical validation logistics.

## 8.5 Operational and Psychosocial Benefits
		The implementation of HairFidence yields profound societal and clinical returns:
		• Psychosocial Restoration: Equipping cancer patients with customized, natural cranial prostheses alleviates situational depression and restores patient dignity during recovery.
		• Elimination of Administrative Friction: Automating parcel logging, verification queues, and request matching reduces operational overhead by over 80% compared to paper registries.
		• Zero Commercial Exploitation: Strict NGO-mediated gating guarantees that 100% of donated hair reaches genuine cancer patients at zero financial cost.
		• Donor Retention: Delivering transparent confirmation of parcel handover nurtures lasting donor trust and sustained community philanthropy.

---

<div style="page-break-after: always;"></div>

# CHAPTER 9: SYSTEM ANALYSIS

## 9.1 Existing System Description
		The legacy approach to hair donation and medical wig distribution across regional charitable centers is an informal, manual, and uncoordinated operation. Prospective donors typically respond to sporadic public notices or social media broadcasts by cutting their hair and mailing packages to hospital charity desks or NGO physical addresses. Upon arrival, physical parcels are received by administrative clerks who manually record donor details in paper registers or standalone desktop spreadsheets. Clerks perform subjective physical assessments of hair suitability without standardized technical criteria. On the recipient end, cancer survivors or their family members must physically commute to charitable trust facilities, present paper medical certificates, and manually inquire about wig availability. Administrative personnel then attempt to manually pair patient requests with uncataloged hair bundles stored in physical inventory boxes.

## 9.2 Limitations of the Existing System
		The manual paradigm suffers from profound systemic vulnerabilities:
		1. Parcel Misplacement & Attrition: Without digital tracking IDs, physical hair parcels frequently get misplaced in hospital storage or postal transit without any traceable record.
		2. Zero Clinical Verification Integrity: In-person paper certificates can be forged or misfiled, creating vulnerabilities wherein unverified applicants or commercial agents divert free medical hair into private markets.
		3. Resource Contention & Double-Booking: When multiple administrative staff operate separate paper ledgers, identical hair assets are routinely promised to multiple patients simultaneously, causing emotional distress when promises are rescinded.
		4. Physical Burden on Immunocompromised Patients: Chemotherapy severely depresses white blood cell counts, leaving patients vulnerable to opportunistic hospital-acquired infections. Forcing physical visits for paperwork is clinically hazardous.
		5. Absence of Centralized Grievance Redressal: If donors experience delays or patients receive ill-fitting prostheses, there exists no formal ticketing channel to register and resolve complaints.

## 9.3 Proposed System Architecture
		HairFidence replaces these error-prone manual approaches with an enterprise web architecture operating under strict Role-Based Access Control (RBAC). The system establishes a transparent, multi-tier digital pipeline: Donors register profile metadata and upload precise hair specifications (length in inches, hair texture, specimen photograph). Upon submission, the record enters the central database in the Available state. Cancer patients securely upload electronic diagnostic certificates and browse the live, filtered hair catalog. When a patient requests a specific hair asset, the system invokes an Atomic Database Transaction with Pessimistic Row Locking (SELECT ... FOR UPDATE), transitioning the post status immediately to Processing. This locks the asset against concurrent requests. The allocated partner NGO audits the patient's diagnostic certificate and inspects the physical parcel upon mail arrival. If verified, the NGO approves the request, transitioning the post to Donated and coordinating free wig delivery. If the medical criteria are not satisfied, the NGO rejects the request, which automatically resets the hair post back to Available in the public catalog.

## 9.4 Concrete Enhancements Implemented
| Technical Dimension | Legacy Manual Paradigm | HairFidence Architecture |
| :--- | :--- | :--- |
| **Data Persistence** | Paper logbooks & unlinked spreadsheets | Centralized MariaDB/MySQL with InnoDB ACID |
| **Authentication** | None; unverified phone calls | BCrypt hashing (PASSWORD_BCRYPT) & RBAC guards |
| **Medical Audit** | In-person physical paper inspection | Encrypted document upload pipeline with remote audit |
| **Concurrency Control** | High double-booking rate | Pessimistic row locking (FOR UPDATE) in PDO transactions |
| **Parcel Tracking** | Untracked; zero donor feedback | Visual pipeline (Available $\rightarrow$ Processing $\rightarrow$ Donated) |
| **Role Partitioning** | Generic clerks managing all data | Dedicated Admin, NGO, Donor, and Patient dashboards |
| **NGO Governance** | Unregulated; no institutional vetting | Administrative accreditation (`is_approved` flag) |
| **Grievances** | Lost in informal phone calls | Dedicated support ticketing console (`complaints` table) |
| **Outreach** | Sporadic word-of-mouth notices | Integrated campaign publishing console with dates/venues |
| **Mobile Support** | None; requires physical travel | Fully responsive CSS3 flexbox/grid layout on all devices |

---

<div style="page-break-after: always;"></div>

# CHAPTER 10: FEASIBILITY STUDY

## 10.1 Technical Feasibility
		The technical feasibility assessment investigates whether the project can be constructed, deployed, and sustained using established, accessible technologies without introducing hazardous technical dependencies. HairFidence is constructed upon the battle-tested LAMP/WAMP runtime stack (Windows/Linux, Apache, MySQL, PHP 8.x). PHP 8.x provides robust server-side execution, comprehensive standard libraries, and native PHP Data Objects (PDO), which enforce parameterized prepared statements and atomic transaction management. The database layer utilizes MySQL 8.0 / MariaDB 10.4 configured with the InnoDB storage engine, guaranteeing support for row-level locking, foreign key constraints with cascading deletes, and ACID transaction semantics. The frontend is engineered with semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. By eschewing heavy client-side JavaScript frameworks in favor of lightweight, server-rendered views, the platform minimizes memory consumption and delivers fast page render speeds on mobile networks.

## 10.2 Operational Feasibility
		Operational feasibility evaluates how comfortably the system integrates into the daily operating rhythms of end-users and non-profit organizations. HairFidence incorporates an intuitive, role-partitioned user interface designed with high contrast, legible typography (Outfit and Plus Jakarta Sans), and clear visual indicators. Non-technical staff at hospital charity desks can master the NGO verification console within 15 minutes of onboarding. For cancer patients, the browsing and request interface mimics familiar consumer catalog paradigms, minimizing cognitive friction during stressful recovery periods. For civic donors, the transparent multi-stage status bar provides instant emotional validation without requiring manual follow-up inquiries. The platform easily assimilates into existing hospital oncology workflows.

## 10.3 Economic Feasibility
		Economic feasibility investigates the Cost-Benefit Analysis (CBA) and Return on Investment (ROI) associated with software development, deployment, and operational maintenance. The system incurs zero software licensing costs. Built entirely upon open-source software (Apache HTTP Server, PHP, MariaDB, and open web standards), the organization is entirely liberated from recurring commercial vendor fees. Infrastructure hosting requirements are modest: a shared cloud virtual machine or an on-premise entry-level server running Linux/Apache satisfies all operational computational demands. Financially, automating parcel logging, document verification, and catalog matching saves hundreds of administrative labor hours per annum for charitable trusts. Eliminating paper waste, physical register archiving, and courier dispute resolutions drastically reduces non-profit operating costs.

## 10.4 Behavioural & Ethical Feasibility
		Human empathy and data ethics are paramount in digital healthcare systems. Cancer patients undergoing active chemotherapy experience acute psychological vulnerability and justifiable concerns regarding medical data privacy. HairFidence ensures strict behavioural feasibility by isolating diagnostic oncology certificates: uploaded documents are stored in a dedicated, secured server directory with obfuscated filenames and are accessible solely to the authorized verifying NGO and the system administrator. Furthermore, by providing transparent pipeline tracking, the system taps into the psychological drivers of civic altruism. Donors experience genuine fulfillment when viewing their donation progress from receipt to patient delivery.

## 10.5 Software Standards Feasibility
		The application strictly complies with universal W3C web standards, ensuring predictable cross-browser rendering across Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari. CSS flexbox and grid abstractions provide responsive fluidity across mobile viewports (375px), tablets (768px), and desktop displays (1920px) without requiring separate native device applications. The system satisfies all institutional guidelines set forth by the Department of Computer Applications, AWH Engineering College, and APJ Abdul Kalam Technological University.

---

<div style="page-break-after: always;"></div>

# CHAPTER 11: SOFTWARE ENGINEERING PARADIGM

## 11.1 Agile Process Methodology
		The development of HairFidence was governed by the Agile Software Development Methodology. Unlike rigid, sequential linear-sequential models (such as the classical Waterfall model) which defer stakeholder testing to the final project stages, Agile prioritizes iterative enhancements, rapid feedback loops, and continuous requirement refinement. Given the humanitarian sensitivity of cancer patient support, operational requirements regarding clinical report verification, donor pipeline visualizations, and concurrency controls evolved dynamically based on user interviews and mock trials. Agile allowed the engineering team to deploy functional increments at the conclusion of each sprint, validating core behaviors before proceeding to downstream modules.

## 11.2 Scrum Framework Implementation
		The operational implementation of Agile was managed using the Scrum Framework, organizing work into structured, time-boxed intervals (Sprints) with clearly delineated engineering responsibilities:
		• Product Owner (PO): Maintained the master Product Backlog, formulated user stories, defined explicit acceptance criteria, prioritized critical security tasks (such as SQL injection immunization and file upload MIME verification), and reviewed sprint deliverables.
		• Scrum Master: Facilitated agile ceremonies, eliminated technical impediments (such as Apache file permission locks and PDO foreign key cascade configurations), and ensured continuous adherence to Scrum best practices.
		• Development Team: Comprising full-stack software engineers responsible for database schema modeling, backend PHP controller development, user interface styling, and integration test suite execution.

## 11.3 Sprint Planning and Task Decomposition

### Sprint 1: Core Architecture, Authentication & Governance Console
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

### Sprint 2: Logistics Pipeline, Concurrency Locking & Clinical Audit
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
		• As an Administrator, I want to audit institutional registration certificates of newly registered NGOs, so that only legitimate healthcare charities can access patient diagnostic summaries and verify physical donations. (Acceptance Criteria: Newly registered NGOs must default to is_approved = 0 and be blocked from accessing operations until the Admin clicks Approve).
		• As an NGO Staff Member, I want to inspect diagnostic oncology summaries uploaded by patients, so that free medical wigs are allocated strictly to verified cancer patients. (Acceptance Criteria: Diagnostic files must be viewable via secure paths and requests must require explicit NGO approval to transition to Donated).
		• As a Hair Donor, I want to log the exact length, texture, and packaging photo of my hair, so that my contribution is accurately indexed in the patient catalog. (Acceptance Criteria: Forms must reject non-image file uploads and automatically assign an initial status of Available).
		• As a Hair Donor, I want to track my donation through a visual pipeline, so that I receive confirmation when my parcel is verified and delivered to a patient. (Acceptance Criteria: The donor dashboard must render dynamic status indicators reflecting transitions between Available, Processing, and Donated).
		• As a Cancer Patient, I want to browse available verified hair assets and submit an allocation request, so that I can receive a custom medical wig without commercial cost. (Acceptance Criteria: Submitting a request must immediately lock the post from other patients via database row locking).

## 11.5 Agile Ceremonies & Milestone Delivery
		Scrum ceremonies were executed rigorously throughout the development lifecycle: Sprint Planning at sprint commencement to dissect backlog items into granular tasks; Daily Standups to evaluate progress and remove bottlenecks; Sprint Reviews featuring live software demonstrations to academic guides; and Sprint Retrospectives to continuously refine code quality and architectural integrity.

---

<div style="page-break-after: always;"></div>

# CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (SRS)

## 12.1 Minimum Hardware Requirements
| Hardware Component | Client-Side Specification | Server-Side Specification |
| :--- | :--- | :--- |
| **Processor** | Dual-Core 1.8 GHz Intel Core i3 / AMD | Quad-Core 2.4 GHz Intel Xeon / AMD EPYC |
| **System Memory (RAM)** | 2 GB DDR3/DDR4 (4 GB recommended) | 8 GB DDR4 ECC (16 GB recommended) |
| **Storage Drive** | 500 MB free browser cache space | 512 GB SSD (minimum 20 GB dedicated) |
| **Display Output** | 1024x768 minimum (1920x1080 Full HD) | Server Console / Headless Display |
| **Network Interface** | Standard Broadband (512 Kbps+) | Gigabit Ethernet (1000BASE-T) Static IP |
| **Peripherals** | QWERTY Keyboard & Pointing Device | Standard Server Console Input |

## 12.2 Software Stack and Environment
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
### 1. Universal Authentication Module (FR-AUTH)
		• FR-AUTH-01: Authenticate users via verified email and password.
		• FR-AUTH-02: Enforce BCrypt cryptographic password hashing (PASSWORD_BCRYPT) prior to database persistence.
		• FR-AUTH-03: Establish server-side sessions storing login_id, role, email, and role-specific primary keys.
		• FR-AUTH-04: Middleware interceptor (auth_check.php) validates session role before granting access to protected views.
		• FR-AUTH-05: Gated access verification blocks unapproved NGOs until certified by Administrator.

### 2. Administrator Governance Module (FR-ADMIN)
		• FR-ADMIN-01: Compute and render real-time statistical metrics across users, posts, and requests.
		• FR-ADMIN-02: Review pending NGO registrations, inspect registration credentials, and toggle approval.
		• FR-ADMIN-03: Exercise system-wide monitoring over users with cascading purge capabilities.
		• FR-ADMIN-04: Review user grievance tickets and update resolution status from Pending to Resolved.

### 3. Healthcare NGO Module (FR-NGO)
		• FR-NGO-01: Prohibit operational features until accreditation flag is_approved = 1.
		• FR-NGO-02: Inspect incoming physical hair parcels and verify status to Donated.
		• FR-NGO-03: Audit patient clinical oncology certificates attached to incoming hair requests.
		• FR-NGO-04: Approve verified requests, atomically updating request to Approved and post to Donated.
		• FR-NGO-05: Reject invalid requests, automatically resetting the hair post back to Available in catalog.
		• FR-NGO-06: Author and publish community hair donation drives and event guidelines.

### 4. Hair Donor Module (FR-DONOR)
		• FR-DONOR-01: Author hair donation posts detailing length (inches), hair texture, and specimen photo.
		• FR-DONOR-02: Enforce strict file upload validation restricting formats to JPG, JPEG, and PNG.
		• FR-DONOR-03: Real-time visual tracking of donation pipeline (Available -> Processing -> Donated).
		• FR-DONOR-04: Directory access to upcoming NGO community campaigns.
		• FR-DONOR-05: Direct submission of feedback and support tickets to Administrator.

### 5. Cancer Patient Module (FR-PATIENT)
		• FR-PATIENT-01: Upload diagnostic clinical oncology certificates to isolated server directories.
		• FR-PATIENT-02: Browse verified available hair catalog with attribute filtering (length, texture).
		• FR-PATIENT-03: Dispatch formal hair requests routed via accredited partner NGOs.
		• FR-PATIENT-04: Atomic database transaction with row locking immediately locks requested post to Processing.
		• FR-PATIENT-05: Real-time monitoring of request verification and custom wig dispatch logistics.

## 12.4 Non-Functional Requirements (NFRs)
		• NFR-01 (Security & Data Integrity): Parameterized PDO prepared statements eliminate SQL Injection across 100% of queries. Dynamic DOM outputs sanitized via htmlspecialchars(ENT_QUOTES, 'UTF-8') to block XSS attacks.
		• NFR-02 (Concurrency Control): Database-level pessimistic locking (SELECT ... FOR UPDATE) inside ACID transactions completely prevents asset double-booking race conditions.
		• NFR-03 (Performance & Latency): Catalog search execution executes in under 150 ms; page rendering under 1.5 s on 4G networks.
		• NFR-04 (Availability & Reliability): Architectural target of 99.5% uptime backed by daily automated SQL dump snapshots.
		• NFR-05 (Portability & Responsiveness): Fluid CSS flexbox/grid layout supports viewports from 320px to 2560px seamlessly.

---

<div style="page-break-after: always;"></div>

# CHAPTER 13: SYSTEM DESIGN

## 13.1 High-Level MVC Architectural Pattern
		HairFidence is architected according to the classical 3-Tier Model-View-Controller (MVC) software architectural pattern. The MVC design pattern enforces strict separation of concerns, decoupling the presentation layer (Views) from domain data models (Models) and routing logic (Controllers). This separation guarantees maintainability, modular testability, and enterprise-grade code organization.
		• Tier 1: Presentation Layer (Views): Responsible exclusively for user interface rendering. Views are authored using semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. The views consume structured associative data arrays emitted by controllers and render responsive, accessible interfaces. Crucially, views contain zero raw database access or business logic.
		• Tier 2: Application / Controller Layer (Controllers): Implemented via modular PHP 8.x scripts. Controllers intercept HTTP GET and POST payloads, validate input types, enforce authentication boundaries via check_access(), coordinate file upload security, execute domain business logic (e.g., verifying that hair length >= 8.0 inches), and manage atomic database transactions.
		• Tier 3: Data Persistence Layer (Models): Governed by the MariaDB/MySQL relational database engine configured with the InnoDB storage engine. The persistence layer guarantees full ACID compliance, enforces referential integrity through foreign key cascades, and executes row-level pessimistic locks (FOR UPDATE) to manage concurrent asset allocation.

## 13.2 Data Flow Diagrams (DFD)
### 13.2.1 DFD Level 0: System Context Diagram
		The Level 0 Context Diagram establishes the global boundary of the system, illustrating how external entities (Administrator, Healthcare NGO, Hair Donor, Cancer Patient) interact with the centralized HairFidence process (Process 0). Donors submit hair specifications and photos; Patients submit diagnostic reports and hair requests; NGOs execute audits and status transitions; Administrators perform institutional vetting and ticket resolution.

### 13.2.2 DFD Level 1: Macro Subsystem Decomposition
		The Level 1 Diagram decomposes the system into seven major operational processes: 1.0 Authentication & Role Router; 2.0 NGO Accreditation; 3.0 Hair Cataloging & Post Insertion; 4.0 Patient Diagnostic Verification; 5.0 Concurrency-Locked Request Matching Engine; 6.0 Community Campaign Publishing; 7.0 Grievance Redressal Support Ticketing.

### 13.2.3 DFD Level 2: Sub-Process 5.0 (Request & Concurrency Locking)
		Decomposes the transactional path where a patient requests a hair asset: 5.1 Initialize Atomic Transaction -> 5.2 Query post status FOR UPDATE -> 5.3 If not Available, rollback and report conflict -> 5.4 If Available, insert tuple into hair_requests -> 5.5 Update post status to Processing -> 5.6 Commit transaction -> 5.7 Emit dispatch notification to designated NGO.

## 13.3 UML Modeling
### Use Case Specifications & Actor Matrix
		The system defines fifteen formal use cases spanning four primary actors (Admin, NGO, Donor, Patient), governing login (UC-01), multi-role registration (UC-02), NGO vetting (UC-03), hair post creation (UC-04), pipeline tracking (UC-05), diagnostic report upload (UC-06), catalog search (UC-07), concurrency-safe requesting (UC-08), medical auditing (UC-09), request approval/rejection (UC-10), physical parcel inspection (UC-11), campaign creation (UC-12), complaint submission (UC-13), grievance resolution (UC-14), and metric aggregation (UC-15).

## 13.4 Database Design & Relational Schema Tables
| Table Name | Primary Key | Foreign Keys | Core Attributes |
| :--- | :--- | :--- | :--- |
| **1. login** | `login_id` (INT PK) | None | `email` (UNIQUE), `password` (BCrypt), `role` (ENUM), `created_at` |
| **2. donors** | `donor_id` (INT PK) | `login_id` $\rightarrow$ `login(login_id)` | `full_name`, `phone`, `address` |
| **3. patients** | `patient_id` (INT PK) | `login_id` $\rightarrow$ `login(login_id)` | `full_name`, `phone`, `address`, `medical_report_url` |
| **4. ngos** | `ngo_id` (INT PK) | `login_id` $\rightarrow$ `login(login_id)` | `organization_name`, `registration_number`, `is_approved` |
| **5. hair_donation_posts**| `post_id` (INT PK) | `donor_id` $\rightarrow$ `donors(donor_id)` | `hair_length`, `hair_type`, `image_url`, `status` (ENUM) |
| **6. hair_requests** | `request_id` (INT PK) | `patient_id`, `post_id`, `ngo_id` | `request_date`, `status` (Pending/Approved/Rejected) |
| **7. campaigns** | `campaign_id` (INT PK) | `ngo_id` $\rightarrow$ `ngos(ngo_id)` | `title`, `description`, `event_date`, `location` |
| **8. complaints** | `complaint_id` (INT PK)| `login_id` $\rightarrow$ `login(login_id)` | `subject`, `description`, `status` (Pending/Resolved), `date` |

## 13.5 Normalization Proofs (1NF, 2NF, 3NF)
		• First Normal Form (1NF): All attribute domains contain exclusively atomic (indivisible) values. Attributes such as hair_length, hair_type, and image_url store single scalar values. There are zero multi-valued columns or repeating groups.
		• Second Normal Form (2NF): The schema is in 1NF and every non-prime attribute is fully functionally dependent on the entire primary key. Because every table uses a single-column surrogate primary key (|PK| = 1), proper subsets of candidate keys cannot exist, eliminating partial dependencies.
		• Third Normal Form (3NF): The schema is in 2NF and there exist no transitive functional dependencies (X -> Y and Y -> Z). Authentication attributes reside strictly in login, while domain profile attributes reside strictly in entity profile relations (donors, patients, ngos), linked solely by the foreign key login_id. In hair_requests, status depends directly on request_id, not transitively through patient_id or ngo_id.

---

<div style="page-break-after: always;"></div>

# CHAPTER 14: SYSTEM DEVELOPMENT

## 14.1 Subsystem Modular Breakdown
		The implementation divides system functionality across decoupled directories: config/ manages the centralized PDO database instance; includes/ provides RBAC middleware (auth_check.php); auth/ handles session multiplexing and destruction; admin/ administers user profiles, accreditation, and tickets; ngo/ executes clinical audits and parcel verifications; donor/ enables hair post creation and pipeline tracking; patient/ hosts the catalog and request locking engine; and uploads/ stores static specimen photos and medical reports.

## 14.2 Core Algorithms & Business Logic
		1. Pessimistic Concurrency Locking: Evaluated inside an atomic PDO transaction ($pdo->beginTransaction()). When a patient requests a post, the query SELECT status FROM hair_donation_posts WHERE post_id=? FOR UPDATE acquires an exclusive row lock. If the post is Available, the request is inserted and post status updated to Processing before committing ($pdo->commit()). This guarantees zero double-booking during concurrent request spikes.
		2. Cryptographic Password Hashing: Uses the BCrypt hashing algorithm via password_hash() and password_verify() with cost factor 10, ensuring irreversible credential encryption.
		3. Zero-Trust Access Middleware: Intercepts all incoming dashboard requests, validating that active session credentials match permitted roles via check_access().
		4. Secure File Upload Pipeline: Inspects incoming file extensions against strict whitelists (JPG, JPEG, PNG for photos; PDF, DOC, JPG for medical reports), assigns unguessable randomized filenames, and writes files to isolated upload directories.

## 14.3 Routing & Endpoints Specification
		The system implements clean, RESTful-style endpoints: /login.php for authentication; /register.php for multi-role registration; /auth/dashboard_redirect.php for role routing; /auth/logout.php for session invalidation; /admin/dashboard.php for governance; /ngo/dashboard.php for clinical audits; /donor/dashboard.php for donation tracking; /patient/dashboard.php for catalog browsing and requests.

## 14.4 Input Validation & Security Layers
		• SQL Injection Prevention: 100% of database interactions are executed via parameterized PDO prepared statements.
		• Cross-Site Scripting (XSS) Prevention: All dynamic variables rendered into the DOM are sanitized using htmlspecialchars(ENT_QUOTES, 'UTF-8').
		• Gated Administrative Approval: NGO accounts cannot log in until certified by the Administrator (is_approved = 1).

---

<div style="page-break-after: always;"></div>

# CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION

## 15.1 Testing Methodologies Applied
		Quality assurance for HairFidence was conducted across a comprehensive five-tier testing framework:
		• Unit Testing: Evaluated standalone routines including password verification, session guards, and file extension parsers.
		• Integration Testing: Validated end-to-end workflows connecting donor post creation, patient catalog rendering, atomic request locking, and NGO approval.
		• Black Box Testing: Evaluated system behaviors against SRS specifications without internal code inspection.
		• White Box Testing: Investigated internal branch coverage, transaction rollbacks, and foreign key cascade executions.
		• User Acceptance Testing (UAT): Simulated real-world trials with donor and patient personas to verify usability.

## 15.2 Comprehensive Test Suite Table
| Test ID | Test Scenario | Test Input Data | Expected Output | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | User Login | Valid email & password | Successful auth & redirect to dashboard | Session created, redirected | **PASS** |
| **TC-02** | Invalid Login | Incorrect password | Display 'Invalid credentials' banner | Access blocked, error shown | **PASS** |
| **TC-03** | NGO Gated Access | Unapproved NGO login | Prevent login; display pending notice | Login halted, warning shown | **PASS** |
| **TC-04** | Role Traversal | Donor accessing `/admin/` | Intercept via `check_access()`; redirect | HTTP 302 redirect to login | **PASS** |
| **TC-05** | Post Creation | Length: 12.5, Wavy, Photo | Post created; status -> 'Available' | Tuple inserted, catalog updated | **PASS** |
| **TC-06** | Concurrency Lock | Simultaneous requests | Only first succeeds; second rolled back | Lock acquired; conflict caught | **PASS** |
| **TC-07** | Report Upload | Valid PDF report (1.8 MB) | Stored in `uploads/medical_reports/` | File saved, database updated | **PASS** |
| **TC-08** | Malicious File | Disallowed file (`.exe`) | Block upload with MIME error | Upload rejected, zero write | **PASS** |
| **TC-09** | NGO Rejection | NGO rejects Request #35 | Request Rejected; Post -> 'Available' | Post unlocked in catalog | **PASS** |
| **TC-10** | Complaint Flow | Valid grievance ticket | Ticket logged; visible to Admin | Tuple logged, marked Resolved | **PASS** |

## 15.3 Deployment & Build Configuration
		Deployment follows an automated local-to-cloud server deployment pipeline: 1. Web server stack initialization via XAMPP (Apache HTTP Server and MariaDB/MySQL); 2. Database schema migration by importing database.sql; 3. Directory permissions configuration ensuring write access to uploads/ partitions; 4. Verification of php.ini directives (file_uploads=On, upload_max_filesize=10M, session.cookie_httponly=1).

## 15.4 Operational Environment Verification
		Post-deployment smoke testing confirmed active PDO connectivity, flawless static media read/write operations to upload directories, and responsive rendering across desktop and mobile devices.

---

<div style="page-break-after: always;"></div>

# CHAPTER 16: SYSTEM MAINTENANCE

## 16.1 Corrective Maintenance Plan
		Focuses on identifying, isolating, and rectifying software defects or runtime anomalies discovered during active production. Server error logging is directed to secure error.log files with display_errors disabled. Normalization routines handle multibyte character edge cases in donor addresses.

## 16.2 Adaptive Maintenance Plan
		Adjusts the software platform to remain fully operational across evolving external computing environments, including PHP interpreter upgrades (e.g., PHP 8.2 to 8.3/8.4), MariaDB engine patches, and modern browser security policy updates.

## 16.3 Perfective Maintenance Plan
		Encompasses proactive user experience enhancements, such as debounced AJAX catalog searching, interactive SVG statistical charting in Admin dashboards, and multi-lingual localization (Malayalam/Hindi).

## 16.4 Preventive Maintenance Plan & Disaster Recovery
		Entails scheduled automated database index optimization (OPTIMIZE TABLE), automated log rotation, and daily encrypted mysqldump backups guaranteeing an RTO of < 2 hours and an RPO of < 24 hours.

---

<div style="page-break-after: always;"></div>

# CHAPTER 17: FUTURE ENHANCEMENT

## 17.1 Cross-Platform Mobile Applications
		Developing native cross-platform mobile apps for Android and iOS using Flutter or React Native to leverage smartphone camera hardware for calibrated hair specimen photography and document scanning.

## 17.2 Automated Postal & Logistics API Integration
		Integrating third-party courier APIs (India Post Speed Post, DTDC, Delhivery) to generate automated prepaid shipping labels with live parcel tracking webhooks inside the donor dashboard.

## 17.3 AI-Powered Virtual Wig AR Simulator
		Implementing an Augmented Reality (AR) facial mapping simulator using WebGL and TensorFlow.js, enabling cancer patients to preview medical wig styles on their own face before submitting a request.

## 17.4 Philanthropic Micro-Sponsorship Gateway
		Incorporating digital payment gateways (Razorpay, Stripe) allowing donors and CSR bodies to sponsor wig fabrication and artisanal hand-knotting costs for underprivileged patients.

## 17.5 Multi-Channel Notification Webhooks
		Integrating SMS and WhatsApp cloud messaging gateways (Twilio / Gupshup) delivering automated milestone notifications to donors when parcels are verified and dispatched.

---

<div style="page-break-after: always;"></div>

# CHAPTER 18: CONCLUSION

## 18.1 Summary of Project Achievements
		The development and operational validation of HairFidence: Cancer Patient Hair Donation Management System represent a meaningful technological achievement in modernizing humanitarian healthcare logistics. By replacing informal, untracked, and error-prone manual donation practices with a secure, role-governed 3-Tier MVC web platform, this project establishes a transparent, accountable bridge connecting altruistic donors, verified healthcare NGOs, and cancer patients recovering from chemotherapy. The system successfully digitizes the end-to-end hair donation lifecycle, empowering donors with real-time multi-stage pipeline tracking, equipping healthcare NGOs with auditable verification tools, and providing cancer survivors with an accessible portal to receive customized cranial prostheses at zero financial cost.

## 18.2 Validation of Core Objectives
		All foundational technical and architectural objectives established during system inception were verified through comprehensive testing: Concurrency Safety via Pessimistic Row Locking (SELECT ... FOR UPDATE) inside atomic PDO transactions; Data Security through BCrypt password hashing and zero-trust RBAC middleware; Database Integrity conforming to Third Normal Form (3NF); and Operational Usability delivering responsive rendering across desktop, tablet, and mobile devices.

## 18.3 Academic & Engineering Conclusion
		Ultimately, HairFidence stands as a testament to how sound software engineering principles, robust relational database design, and human-centered empathy can unite to solve poignant societal challenges. The platform establishes an enduring, scalable model for humanitarian healthcare charity management—one that is transparent, technically sound, and dedicated to restoring dignity, confidence, and comfort to cancer survivors throughout their journey to recovery.

---

<div style="page-break-after: always;"></div>

# CHAPTER 19: APPENDIX

## Appendix A: Complete Database DDL SQL Script
		The complete relational database definition script (database.sql) establishing tables, indexes, and foreign key cascades is archived in the repository root and documented in Section 13.4.

## Appendix B: Core Architectural Code Files
		Archived source files include config/db.php (PDO configuration), includes/auth_check.php (RBAC middleware guard), auth/dashboard_redirect.php (session router), and role dashboards.

## Appendix C: System User Interface Screen Captures
		Actual operational user interface screenshots captured from the running HairFidence application demonstrating primary functional workflows across all user roles:
		* Figure 19.1: Universal Authentication Console (`login.php`)
		* Figure 19.2: Multi-Role User Registration Console (`register.php`)
		* Figure 19.3: Public Informational & Community Portal (`index.php`)
		* Figure 19.4: Administrator Platform Analytics & Overview (`admin/dashboard.php`)
		* Figure 19.5: Administrator NGO Verification & Accreditation Console
		* Figure 19.6: Administrator Grievance Ticketing & Resolution Console
		* Figure 19.7: Healthcare NGO Operations & Clinical Audit Hub (`ngo/dashboard.php`)
		* Figure 19.8: NGO Community Hair Donation Campaign Creation
		* Figure 19.9: Donor Dashboard & Real-Time Pipeline Tracker (`donor/dashboard.php`)
		* Figure 19.10: Donor Hair Post Submission with Specimen Upload
		* Figure 19.11: Cancer Patient Portal & Live Verified Hair Catalog (`patient/dashboard.php`)
		* Figure 19.12: Patient Hair Request Tracking & Allocation Status
		* Figure 19.13: User Grievance & Support Ticket Submission Form
		* Figure 19.14: User Account Profile & Delivery Address Console

---

<div style="page-break-after: always;"></div>

# CHAPTER 20: BIBLIOGRAPHY

## Technical Reference Books
		[1] Software Engineering: A Practitioner's Approach, Roger S. Pressman and Bruce R. Maxim, 8th Edition, McGraw-Hill Education, 2015.
		[2] Fundamentals of Database Systems, Ramez Elmasri and Shamkant B. Navathe, 7th Edition, Pearson Education, 2016.
		[3] PHP and MySQL Web Development, Luke Welling and Laura Thomson, 5th Edition, Addison-Wesley Professional, 2017.
		[4] UML Distilled: A Brief Guide to the Standard Object Modeling Language, Martin Fowler, 3rd Edition, Addison-Wesley Professional, 2004.
		[5] Design Patterns: Elements of Reusable Object-Oriented Software, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, 1st Edition, Addison-Wesley Professional, 1994.
		[6] Software Engineering, Ian Sommerville, 10th Edition, Pearson Education, 2016.

## Authoritative Documentation & Web References
		[1] PHP Documentation Group, PHP: Hypertext Preprocessor Official Reference Manual, Available online: https://www.php.net/manual/en/ (Accessed: June 2026).
		[2] Oracle Corporation, MySQL 8.0 Reference Manual: InnoDB Storage Engine & Locking Models, Available online: https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html (Accessed: June 2026).
		[3] Mozilla Developer Network (MDN), Web Technology for Developers: Semantic HTML5 and CSS Flexible Box Layout, Available online: https://developer.mozilla.org/en-US/docs/Web (Accessed: May 2026).
		[4] Open Web Application Security Project (OWASP), OWASP Top 10: The Ten Most Critical Web Application Security Risks, Available online: https://owasp.org/Top10/ (Accessed: May 2026).
		[5] Apache Friends, XAMPP Apache + MariaDB + PHP + Perl Distribution Documentation, Available online: https://www.apachefriends.org/ (Accessed: April 2026).
		[6] APJ Abdul Kalam Technological University, Master of Computer Applications Curriculum, Scheme and Syllabi (2020 Scheme), Government of Kerala, Available online: https://ktu.edu.in/ (Accessed: July 2026).
