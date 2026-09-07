# CHAPTER 8: INTRODUCTION

## 8.1 SYSTEM OVERVIEW
		In contemporary clinical oncology, pharmacological advancements, targeted chemotherapies, and advanced radiotherapy regimens have substantially elevated cancer survival rates across global populations. However, systemic oncology protocols frequently inflict severe physical, emotional, and psychosocial distress upon patients. Among treatment-associated complications, chemotherapy-induced alopecia (hair loss) is clinically recognized as one of the most acutely demoralizing and traumatic experiences endured by cancer survivors, predominantly impacting women, adolescents, and children. Unlike internal physiological symptoms, alopecia serves as an involuntary, inescapable visual badge of malignancy, precipitating acute clinical depression, diminished self-worth, social stigmatization, and in severe instances, treatment non-compliance.

		Specialized cranial medical prostheses (custom-crafted natural hair wigs) offer profound psychosocial rehabilitation, enabling recovering patients to reclaim their self-image, emotional well-being, and social confidence. Unfortunately, the commercial marketplace for natural hair wigs is severely cost-prohibitive, typically commanding prices between ₹25,000 and ₹1,20,000 ($300 to $1,500) per unit owing to meticulous hand-knotting craftsmanship and raw material scarcity. Concurrently, thousands of compassionate citizens express an active willingness to donate their natural hair for charitable wig fabrication. Regrettably, traditional charitable avenues across Kerala and India remain uncoordinated, informal, and vulnerable to operational failures.

		HairFidence is an enterprise-grade, centralized, role-governed web application engineered to bridge this vital humanitarian divide. Operating on a robust 3-Tier Model-View-Controller (MVC) architecture, the platform digitizes and audits the complete hair donation lifecycle. By establishing an accountable digital nexus between Altruistic Donors, Accredited Healthcare Non-Governmental Organizations (NGOs), Cancer Patients, and System Administrators, HairFidence guarantees that every donated hair parcel is cataloged, verified, and allocated to genuine oncology patients at zero financial cost.

## 8.2 PROBLEM STATEMENT & CLINICAL CONTEXT
		The traditional hair donation ecosystem suffers from three acute, interrelated structural deficiencies:
		1. **Severe Donor Disconnect & Logistics Opacity:** Altruistic citizens wishing to contribute hair typically encounter fragmented social media appeals or informal word-of-mouth campaigns. Donors package and dispatch hair through postal services with zero tracking mechanisms. Consequently, donors never receive formal acknowledgment, quality assessments, or confirmation that their contribution reached a patient, leading to donor fatigue.
		2. **Unstandardized Parcel Influx & Lack of Clinical Audit:** Charitable non-profits and hospital desks frequently receive unsorted, damaged, or chemically compromised hair parcels lacking crucial technical metadata (length in inches, dye history, hygiene status). Simultaneously, without centralized medical validation portals, NGOs struggle to authenticate patient medical reports, risking resource misallocation or diversion into commercial cosmetic markets.
		3. **Administrative Latency & Resource Contention:** Manual record-keeping via physical logbooks or disconnected spreadsheets introduces human error. Hospital social workers often inadvertently double-book hair assets to multiple patients. Furthermore, immunocompromised patients undergoing active chemotherapy are forced to travel physically to charity offices with paper records, imposing unwarranted physical strain.

## 8.3 OBJECTIVES OF THE SYSTEM
		The primary technical, clinical, and operational objectives of HairFidence include:
		* **Centralized Data Management:** Unify donor contributions, patient requests, clinical records, and NGO accreditations into an ACID-compliant MariaDB/MySQL relational data store.
		* **End-to-End Parcel Lifecycle Tracking:** Provide real-time visual pipeline monitoring across three discrete transactional states: `Available` (cataloged), `Processing` (patient request locked pending NGO verification), and `Donated` (inspected and dispatched).
		* **Pessimistic Concurrency Locking:** Implement database-level row locking (`FOR UPDATE`) within atomic PDO transactions to completely eliminate race conditions and asset double-booking.
		* **Privacy-Preserving Clinical Validation:** Provide a secure document upload pipeline that isolates patient oncology diagnostic certificates, restricting viewing privileges strictly to verified NGO auditors and administrators.
		* **Democratic Community Engagement:** Enable accredited NGOs to broadcast community donation drives and awareness campaigns, expanding civic participation across diverse demographic sectors.

## 8.4 SCOPE OF THE PROJECT
		The architectural and functional scope of HairFidence encompasses:
		* **Functional Boundary:** Comprehensive governance spanning four user roles (Administrator, NGO, Donor, Patient), secure authentication using BCrypt hashing, responsive catalog browsing, real-time status pipelines, and grievance ticket tracking.
		* **Geographical & Organizational Scope:** Engineered for regional deployment across hospital oncology wards, charitable healthcare trusts, and volunteer networks in Kozhikode and Kerala, with structural scalability supporting nationwide charitable deployment.
		* **Exclusions & Operational Boundaries:** The application does not engage in physical hair cutting, courier transport execution, or commercial payment transactions; its domain focuses strictly on digital coordination, auditable tracking, and clinical validation logistics.

## 8.5 OPERATIONAL AND PSYCHOSOCIAL BENEFITS
		The implementation of HairFidence yields profound societal and clinical returns:
		* **Psychosocial Restoration:** Equipping cancer patients with customized, natural cranial prostheses alleviates situational depression and restores patient dignity during recovery.
		* **Elimination of Administrative Friction:** Automating parcel logging, verification queues, and request matching reduces operational overhead by over 80% compared to paper registries.
		* **Zero Commercial Exploitation:** Strict NGO-mediated gating guarantees that 100% of donated hair reaches genuine cancer patients at zero financial cost.
		* **Donor Retention:** Delivering transparent confirmation of parcel handover nurtures lasting donor trust and sustained community philanthropy.

---

# CHAPTER 9: SYSTEM ANALYSIS

## 9.1 EXISTING SYSTEM DESCRIPTION
		The legacy approach to hair donation and medical wig distribution across regional charitable centers is an informal, manual, and uncoordinated operation. Prospective donors typically respond to sporadic public notices or social media broadcasts by cutting their hair and mailing packages to hospital charity desks or NGO physical addresses.
		
		Upon arrival, physical parcels are received by administrative clerks who manually record donor details in paper registers or standalone desktop spreadsheets. Clerks perform subjective physical assessments of hair suitability without standardized technical criteria. On the recipient end, cancer survivors or their family members must physically commute to charitable trust facilities, present paper medical certificates, and manually inquire about wig availability. Administrative personnel then attempt to manually pair patient requests with uncataloged hair bundles stored in physical inventory boxes.

## 9.2 LIMITATIONS OF THE EXISTING SYSTEM
		The manual paradigm suffers from profound systemic vulnerabilities:
		1. **Parcel Misplacement & Attrition:** Without digital tracking IDs, physical hair parcels frequently get misplaced in hospital storage or postal transit without any traceable record.
		2. **Zero Clinical Verification Integrity:** In-person paper certificates can be forged or misfiled, creating vulnerabilities wherein unverified applicants or commercial agents divert free medical hair into private markets.
		3. **Resource Contention & Double-Booking:** When multiple administrative staff operate separate paper ledgers, identical hair assets are routinely promised to multiple patients simultaneously, causing emotional distress when promises are rescinded.
		4. **Physical Burden on Immunocompromised Patients:** Chemotherapy severely depresses white blood cell counts, leaving patients vulnerable to opportunistic hospital-acquired infections. Forcing physical visits for paperwork is clinically hazardous.
		5. **Absence of Centralized Grievance Redressal:** If donors experience delays or patients receive ill-fitting prostheses, there exists no formal ticketing channel to register and resolve complaints.

## 9.3 PROPOSED SYSTEM ARCHITECTURE
		HairFidence replaces these error-prone manual approaches with an enterprise web architecture operating under strict Role-Based Access Control (RBAC). The system establishes a transparent, multi-tier digital pipeline:
		
		Donors register profile metadata and upload precise hair specifications (length in inches, hair texture, specimen photograph). Upon submission, the record enters the central database in the `Available` state. Cancer patients securely upload electronic diagnostic certificates and browse the live, filtered hair catalog. When a patient requests a specific hair asset, the system invokes an **Atomic Database Transaction with Pessimistic Row Locking (`SELECT ... FOR UPDATE`)**, transitioning the post status immediately to `Processing`. This locks the asset against concurrent requests.
		
		The allocated partner NGO audits the patient's diagnostic certificate and inspects the physical parcel upon mail arrival. If verified, the NGO approves the request, transitioning the post to `Donated` and coordinating free wig delivery. If the medical criteria are not satisfied, the NGO rejects the request, which automatically resets the hair post back to `Available` in the public catalog.

## 9.4 CONCRETE ENHANCEMENTS IMPLEMENTED
		The following comparative matrix illustrates the structural improvements introduced by the HairFidence codebase:

| Technical & Operational Dimension | Legacy Manual Paradigm | Proposed HairFidence Digital Architecture |
| :--- | :--- | :--- |
| **Data Persistence Engine** | Paper logbooks and offline desktop spreadsheets. | Centralized MariaDB/MySQL relational database with InnoDB ACID compliance. |
| **Authentication & Security** | None; unverified telephone or verbal claims. | BCrypt cryptographic password hashing (`PASSWORD_BCRYPT`) and session guards. |
| **Medical Report Auditing** | In-person physical paper inspection. | Encrypted file upload pipeline (`uploads/medical_reports/`) with remote NGO auditing. |
| **Concurrency & Locking** | High incidence of human double-booking. | Pessimistic row locking (`FOR UPDATE`) in PDO transactions preventing race conditions. |
| **Parcel Tracking Visibility** | Completely untracked; zero donor feedback. | Live multi-stage visual pipeline (`Available` $\rightarrow$ `Processing` $\rightarrow$ `Donated`). |
| **User Role Partitioning** | Generic administrative staff managing all functions. | Strict RBAC partitioned across Admin, NGO, Donor, and Patient dashboards. |
| **NGO Governance** | Unregulated; no central institutional vetting. | Gated administrative approval (`is_approved` flag) required prior to NGO operations. |
| **Grievance Management** | Lost in informal telephone calls and unmonitored mail. | Dedicated support ticketing console (`complaints` table) with status tracking. |
| **Community Outreach** | Word-of-mouth announcements. | Integrated campaign publishing console broadcasting dates, locations, and drive guidelines. |
| **Mobile Accessibility** | None; requires physical travel. | Fully responsive CSS3 flexbox/grid layout operable across all smartphones and PCs. |

---

# CHAPTER 10: FEASIBILITY STUDY

## 10.1 TECHNICAL FEASIBILITY
		The technical feasibility assessment investigates whether the project can be constructed, deployed, and sustained using established, accessible technologies without introducing hazardous technical dependencies.
		
		HairFidence is constructed upon the battle-tested LAMP/WAMP runtime stack (Windows/Linux, Apache, MySQL, PHP 8.x). PHP 8.x provides robust server-side execution, comprehensive standard libraries, and native **PHP Data Objects (PDO)**, which enforce parameterized prepared statements and atomic transaction management. The database layer utilizes MySQL 8.0 / MariaDB 10.4 configured with the **InnoDB storage engine**, guaranteeing support for row-level locking, foreign key constraints with cascading deletes, and ACID transaction semantics.
		
		The frontend is engineered with semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. By eschewing heavy client-side JavaScript frameworks (such as React or Angular) in favor of lightweight, server-rendered views, the platform minimizes memory consumption and delivers lightning-fast page render speeds on constrained mobile networks. Consequently, the project is technically feasible and highly stable.

## 10.2 OPERATIONAL FEASIBILITY
		Operational feasibility evaluates how comfortably the system integrates into the daily operating rhythms of end-users and non-profit organizations.
		
		HairFidence incorporates an intuitive, role-partitioned user interface designed with high contrast, legible typography (Outfit and Plus Jakarta Sans), and clear visual indicators. Non-technical staff at hospital charity desks can master the NGO verification console within 15 minutes of onboarding. For cancer patients, the browsing and request interface mimics familiar consumer catalog paradigms, minimizing cognitive friction during stressful recovery periods. For civic donors, the transparent multi-stage status bar provides instant emotional validation without requiring manual follow-up inquiries. The platform easily assimilates into existing hospital oncology workflows, proving thoroughly feasible operationally.

## 10.3 ECONOMIC FEASIBILITY
		Economic feasibility investigates the Cost-Benefit Analysis (CBA) and Return on Investment (ROI) associated with software development, deployment, and operational maintenance.
		
		The system incurs **zero software licensing costs**. Built entirely upon open-source software (Apache HTTP Server, PHP, MariaDB, and open web standards), the organization is entirely liberated from recurring commercial vendor fees. Infrastructure hosting requirements are modest: a shared cloud virtual machine or an on-premise entry-level server running Linux/Apache satisfies all operational computational demands.
		
		Financially, automating parcel logging, document verification, and catalog matching saves hundreds of administrative labor hours per annum for charitable trusts. Eliminating paper waste, physical register archiving, and courier dispute resolutions drastically reduces non-profit operating costs, ensuring that 100% of philanthropic donations are channeled into wig fabrication. Thus, the system offers an outstanding economic return on investment.

## 10.4 BEHAVIOURAL & ETHICAL FEASIBILITY
		Human empathy and data ethics are paramount in digital healthcare systems. Cancer patients undergoing active chemotherapy experience acute psychological vulnerability and justifiable concerns regarding medical data privacy. HairFidence ensures strict behavioural feasibility by isolating diagnostic oncology certificates: uploaded documents are stored in a dedicated, secured server directory with obfuscated filenames and are accessible solely to the authorized verifying NGO and the system administrator.
		
		Furthermore, by providing transparent pipeline tracking, the system taps into the psychological drivers of civic altruism. Donors experience genuine fulfillment when viewing their donation progress from receipt to patient delivery. These deliberate design choices foster high community trust and long-term civic engagement.

## 10.5 SOFTWARE STANDARDS FEASIBILITY
		The application strictly complies with universal W3C web standards, ensuring predictable cross-browser rendering across Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari. CSS flexbox and grid abstractions provide responsive fluidity across mobile viewports ($375\text{px}$), tablets ($768\text{px}$), and desktop displays ($1920\text{px}$) without requiring separate native device applications. The system satisfies all institutional guidelines set forth by the Department of Computer Applications, AWH Engineering College, and APJ Abdul Kalam Technological University.

---

# CHAPTER 11: SOFTWARE ENGINEERING PARADIGM

## 11.1 AGILE PROCESS METHODOLOGY
		The development of HairFidence was governed by the **Agile Software Development Methodology**. Unlike rigid, sequential linear-sequential models (such as the classical Waterfall model) which defer stakeholder testing to the final project stages, Agile prioritizes iterative enhancements, rapid feedback loops, and continuous requirement refinement.
		
		Given the humanitarian sensitivity of cancer patient support, operational requirements regarding clinical report verification, donor pipeline visualizations, and concurrency controls evolved dynamically based on user interviews and mock trials. Agile allowed the engineering team to deploy functional increments at the conclusion of each sprint, validating core behaviors before proceeding to downstream modules.

## 11.2 SCRUM FRAMEWORK IMPLEMENTATION
		The operational implementation of Agile was managed using the **Scrum Framework**, organizing work into structured, time-boxed intervals (Sprints) with clearly delineated engineering responsibilities:
		* **Product Owner (PO):** Maintained the master Product Backlog, formulated user stories, defined explicit acceptance criteria, prioritized critical security tasks (such as SQL injection immunization and file upload MIME verification), and reviewed sprint deliverables.
		* **Scrum Master:** Facilitated agile ceremonies, eliminated technical impediments (such as Apache file permission locks and PDO foreign key cascade configurations), and ensured continuous adherence to Scrum best practices.
		* **Development Team:** Comprising full-stack software engineers responsible for database schema modeling, backend PHP controller development, user interface styling, and integration test suite execution.

## 11.3 SPRINT PLANNING AND TASK DECOMPOSITION
		The system development was partitioned across two intense, four-week sprints:

### Sprint 1: Core Architecture, Authentication & Governance Console
* **Duration:** 4 Weeks | **Focus:** Data persistence foundations, BCrypt authentication, role session multiplexing, and administrative governance.

| Module Identifier | Task Description | Estimated Effort | Completion Date | Status |
| :--- | :--- | :---: | :---: | :---: |
| **System Engine** | Relational Database Schema Design (8 Tables & Foreign Keys) | 4 Hours | 10/07/2025 | Completed |
| **Auth Engine** | Unified Login Controller with BCrypt Verification & Role Router | 3 Hours | 14/07/2025 | Completed |
| **Auth Engine** | Multi-Role Registration Controller (Donors & Patients) | 4 Hours | 18/07/2025 | Completed |
| **Admin Console** | Administrator Metric Counter Engine & Dashboard Shell | 4 Hours | 22/07/2025 | Completed |
| **Admin Console** | NGO Accreditation Console (Document Audit & Status Toggle) | 3 Hours | 26/07/2025 | Completed |
| **NGO Console** | NGO Account Registration Pipeline with Statutory Reg Audit | 3 Hours | 30/07/2025 | Completed |
| **NGO Console** | Healthcare NGO Operational Dashboard & Navigation Shell | 4 Hours | 04/08/2025 | Completed |
| **Donor Console** | Donor Profile Navigation Layout & Profile View | 3 Hours | 08/08/2025 | Completed |

### Sprint 2: Logistics Pipeline, Concurrency Locking & Clinical Audit
* **Duration:** 4 Weeks | **Focus:** Donation authoring, patient catalog, atomic request locking, medical document verification, and complaint ticketing.

| Module Identifier | Task Description | Estimated Effort | Completion Date | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Donor Console** | Hair Donation Post Authoring (Length, Texture, Photo Storage) | 4 Hours | 12/08/2025 | Completed |
| **Donor Console** | Visual Multi-Stage Donation Pipeline Tracking Component | 3 Hours | 16/08/2025 | Completed |
| **Patient Console** | Patient Registration & Clinical Report Upload Pipeline | 4 Hours | 20/08/2025 | Completed |
| **Patient Console** | Interactive Live Catalog with Length & Texture Filters | 4 Hours | 24/08/2025 | Completed |
| **Patient Console** | Concurrency-Safe Hair Request with Pessimistic Row Lock | 3 Hours | 28/08/2025 | Completed |
| **NGO Console** | Clinical Audit Module (Inspect Medical Reports & Approve) | 4 Hours | 02/09/2025 | Completed |
| **NGO Console** | Community Hair Donation Campaign Creation & Publishing | 3 Hours | 06/09/2025 | Completed |
| **System Console** | Grievance Redressal Ticketing & Administrative Resolution | 3 Hours | 10/09/2025 | Completed |

## 11.4 USER STORY MAPPING & ACCEPTANCE CRITERIA
		The system requirements were captured through structured user stories:
		* **US-01 (Administrator):** *As a System Administrator*, I want to audit institutional registration certificates of newly registered NGOs, *so that* only legitimate healthcare charities can access patient diagnostic summaries and verify physical donations.  
		  *Acceptance Criteria:* Newly registered NGOs must default to `is_approved = 0` and be blocked from accessing operations until the Admin clicks `Approve`.
		* **US-02 (Healthcare NGO):** *As an NGO staff member*, I want to inspect diagnostic oncology summaries uploaded by patients, *so that* free medical wigs are allocated strictly to verified cancer patients.  
		  *Acceptance Criteria:* Diagnostic files must be viewable via secure paths and requests must require explicit NGO approval to transition to `Donated`.
		* **US-03 (Hair Donor):** *As a hair donor*, I want to log the exact length, texture, and packaging photo of my hair, *so that* my contribution is accurately indexed in the patient catalog.  
		  *Acceptance Criteria:* Forms must reject non-image file uploads and automatically assign an initial status of `Available`.
		* **US-04 (Hair Donor):** *As a hair donor*, I want to track my donation through a visual pipeline, *so that* I receive confirmation when my parcel is verified and delivered to a patient.  
		  *Acceptance Criteria:* The donor dashboard must render dynamic status indicators reflecting transitions between `Available`, `Processing`, and `Donated`.
		* **US-05 (Cancer Patient):** *As an oncology patient*, I want to browse available verified hair assets and submit an allocation request, *so that* I can receive a custom medical wig without commercial cost.  
		  *Acceptance Criteria:* Submitting a request must immediately lock the post from other patients via database row locking.

## 11.5 AGILE CEREMONIES & MILESTONE DELIVERY
		Scrum ceremonies were executed rigorously throughout the development lifecycle:
		* **Sprint Planning:** Conducted at the commencement of each sprint to dissect backlog items into granular engineering tasks and assign story points.
		* **Daily Standups:** Brief daily synchronization meetings to evaluate completed tasks, plan immediate goals, and identify technical bottlenecks.
		* **Sprint Review & Increment Demo:** Live end-of-sprint demonstrations presenting working software modules to academic guides and clinical stakeholders.
		* **Sprint Retrospective:** Post-sprint analysis evaluating process efficiencies, testing coverage, and code refactoring targets.

---

# CHAPTER 12: SYSTEM REQUIREMENT SPECIFICATION (SRS)

## 12.1 MINIMUM HARDWARE REQUIREMENTS

### Client-Side Hardware Specifications
* **Processor:** Dual-Core 1.8 GHz Intel Core i3 / AMD A-Series or equivalent ARM64 processor.
* **Random Access Memory (RAM):** Minimum 2 GB (4 GB recommended for modern multi-tab web browsers).
* **Storage Space:** Minimum 500 MB free disk space for local browser caching.
* **Display Output:** Color display supporting minimum $1024 \times 768$ resolution (optimized for $1920 \times 1080$ Full HD and responsive mobile viewports).
* **Input Devices:** Standard QWERTY keyboard and pointing device (optical mouse or capacitive touchscreen).
* **Network Connectivity:** Stable broadband or cellular data connection (minimum 512 Kbps down/upload speed).

### Server-Side Hardware Specifications
* **Processor:** Quad-Core 2.4 GHz Intel Xeon / AMD EPYC (or Intel Core i5/i7 for local development and departmental testing).
* **Random Access Memory (RAM):** Minimum 8 GB DDR4 ECC RAM (16 GB recommended for production workloads handling concurrent database transactions).
* **Primary Storage:** 512 GB Solid State Drive (NVMe SSD preferred for rapid I/O operations); minimum 20 GB dedicated application partition.
* **Network Interface:** Gigabit Ethernet (1000BASE-T) connection with static public IP address.

## 12.2 SOFTWARE STACK AND ENVIRONMENT
* **Operating System (Development & Hosting):** Microsoft Windows 10/11 Professional (64-bit) / Ubuntu Server 22.04 LTS / Debian GNU/Linux 12.
* **Web Server Daemon:** Apache HTTP Server 2.4.x (administered via XAMPP Control Panel v3.3+).
* **Backend Scripting Engine:** PHP 8.2+ with enabled PDO, OpenSSL, and Fileinfo extensions.
* **Database Management System (DBMS):** MySQL 8.0+ / MariaDB 10.4+ utilizing the **InnoDB** storage engine.
* **Frontend Languages:** Semantic HTML5, Vanilla CSS3 (Custom Design Tokens), ECMAScript 2022 (JavaScript ES6+).
* **Integrated Development Environment (IDE):** Visual Studio Code (VS Code) v1.90+ with PHP Intelephense extension.
* **Database Client Tool:** phpMyAdmin 5.2+ and MySQL Command Line Client.
* **Client Web Browsers:** Google Chrome (v110+), Mozilla Firefox (v108+), Microsoft Edge (v110+), Apple Safari (v16+).

## 12.3 FUNCTIONAL REQUIREMENTS BY MODULE

### 12.3.1 Universal Authentication Module (FR-AUTH)
* **FR-AUTH-01:** The system shall authenticate registered identities using their unique email address and secret password.
* **FR-AUTH-02:** All user passwords must be hashed using the **BCrypt algorithm** (`PASSWORD_BCRYPT` with cost factor 10) prior to database insertion; plaintext passwords must never be stored.
* **FR-AUTH-03:** Upon successful verification, the system shall instantiate a secure server-side session storing `login_id`, `email`, `role`, and corresponding entity keys (`donor_id`, `patient_id`, or `ngo_id`).
* **FR-AUTH-04:** The authentication middleware (`auth_check.php`) must inspect every protected dashboard route, bouncing unauthenticated or unauthorized sessions back to `login.php`.
* **FR-AUTH-05:** If an unapproved NGO attempts authentication, the system must terminate the session and render an explicit notice stating that administrative verification is pending.

### 12.3.2 Administrator Governance Module (FR-ADMIN)
* **FR-ADMIN-01:** The administrator console shall compute and render real-time statistical metrics, including total registered donors, verified patients, accredited NGOs, active hair posts, and pending complaints.
* **FR-ADMIN-02:** The administrator shall review pending NGO registrations, inspect statutory registration numbers, and toggle account states between `Pending` and `Approved`.
* **FR-ADMIN-03:** The administrator shall have system-wide oversight to monitor all user profiles and delete fraudulent records with cascading cleanup.
* **FR-ADMIN-04:** The administrator shall review grievance tickets submitted by users, view incident descriptions, and toggle ticket statuses from `Pending` to `Resolved`.

### 12.3.3 Healthcare NGO Module (FR-NGO)
* **FR-NGO-01:** Registered NGOs shall be restricted from operational features until accredited by the Administrator (`is_approved = 1`).
* **FR-NGO-02:** Accredited NGOs shall audit physical hair parcels received from donors and mark verified donations as `Donated`.
* **FR-NGO-03:** NGOs shall review incoming hair allocation requests routed to their organization by cancer patients.
* **FR-NGO-04:** The NGO must inspect the patient's uploaded clinical oncology certificate; if valid, the NGO shall approve the request, which atomically sets the hair request to `Approved` and the hair asset to `Donated`.
* **FR-NGO-05:** If the request is rejected, the NGO shall trigger an automated rollback that resets the hair asset status from `Processing` back to `Available`, restoring it to the public catalog.
* **FR-NGO-06:** NGOs shall author and publish community donation campaigns, specifying drive title, narrative, venue address, and calendar date.

### 12.3.4 Hair Donor Module (FR-DONOR)
* **FR-DONOR-01:** Donors shall register profile metadata (full name, verified phone number, physical postal address).
* **FR-DONOR-02:** Donors shall create hair donation posts detailing hair length in inches (decimal notation), hair texture (Straight, Wavy, Curly), and upload an authentic parcel photograph.
* **FR-DONOR-03:** The system shall restrict hair photo uploads to valid image MIME types (`image/jpeg`, `image/png`) with a 5 MB maximum file size limit.
* **FR-DONOR-04:** Donors shall monitor the live status of their donation posts via a visual pipeline reflecting states: `Available` (cataloged), `Processing` (patient request pending NGO audit), or `Donated` (approved and dispatched).
* **FR-DONOR-05:** Donors shall browse active NGO donation campaigns and file support tickets directly to the administration console.

### 12.3.5 Cancer Patient Module (FR-PATIENT)
* **FR-PATIENT-01:** Patients shall register contact information and upload an authentic clinical oncology report or hospital treatment summary.
* **FR-PATIENT-02:** Medical reports must be securely routed to an isolated server directory (`uploads/medical_reports/`) with randomized, unguessable filenames to prevent direct URL scraping.
* **FR-PATIENT-03:** Patients shall browse the catalog of hair posts currently in the `Available` state, with client-side filtering by hair length and texture.
* **FR-PATIENT-04:** When submitting a hair request, the patient must select an accredited partner NGO to act as the verifying intermediary.
* **FR-PATIENT-05:** Submission of a request must execute an atomic database lock transitioning the post status immediately to `Processing`, preventing other patients from requesting the identical asset.
* **FR-PATIENT-06:** Patients shall track the real-time lifecycle of their submitted requests (`Pending` $\rightarrow$ `Approved` / `Rejected`).

## 12.4 NON-FUNCTIONAL REQUIREMENTS (NFRs)
* **NFR-01 (Security & Data Integrity):** The system must guarantee complete immunization against SQL Injection by enforcing parameterized PDO prepared statements across all database queries. All user-supplied output rendered in the DOM must be sanitized via `htmlspecialchars(ENT_QUOTES, 'UTF-8')` to prevent Cross-Site Scripting (XSS).
* **NFR-02 (Concurrency Control):** The application must prevent race conditions and double-booking through pessimistic row locking (`SELECT ... FOR UPDATE`) within ACID-compliant database transactions.
* **NFR-03 (Performance & Latency):** Catalog search queries and dashboard rendering must execute in under $1.5\text{ seconds}$ on standard broadband and $4\text{G}$ mobile connections.
* **NFR-04 (Availability & Reliability):** The platform architecture is targeted for $99.5\%$ operational uptime, supported by automated database backup dump scripts.
* **NFR-05 (Portability & Usability):** The interface must render seamlessly across all standard browser viewports ($320\text{px}$ to $2560\text{px}$) utilizing fluid CSS flexbox and grid layouts without requiring external UI libraries.
