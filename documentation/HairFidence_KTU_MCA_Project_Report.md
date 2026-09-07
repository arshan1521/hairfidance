# HAIRFIDENCE: A CENTRALIZED ROLE-BASED WEB APPLICATION FOR HAIR DONATION LIFECYCLE MANAGEMENT

## PROJECT THESIS REPORT
Submitted to  
**AWH ENGINEERING COLLEGE, KUTTIKKATTOOR, CALICUT - 673008**  
in partial fulfillment of the requirements for the award of the degree of  

### MASTER OF COMPUTER APPLICATIONS (MCA)
of  
**APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY (KTU), KERALA**

<br>

**Submitted by:**  
**ARSHAN NIZAR K P**  
**(Register Number: AWH25MCA-2010)**

<br>

**Under the Guidance of:**  
**Ms. AMEENA AFSAR**  
Assistant Professor, Department of Computer Applications  

<br>

**DEPARTMENT OF COMPUTER APPLICATIONS**  
**AWH ENGINEERING COLLEGE, KUTTIKKATTOOR, KOZHIKODE, KERALA – 673008**  
**ACADEMIC YEAR: 2025–2026**

---

<div style="page-break-after: always;"></div>

# CERTIFICATE

### DEPARTMENT OF COMPUTER APPLICATIONS  
### AWH ENGINEERING COLLEGE, KUTTIKKATTOOR, CALICUT - 673008

<br>

This is to certify that this project thesis entitled **“HAIRFIDENCE: A CENTRALIZED ROLE-BASED WEB APPLICATION FOR HAIR DONATION LIFECYCLE MANAGEMENT”** is a bona fide record of the project work carried out by **ARSHAN NIZAR K P (Register Number: AWH25MCA-2010)** in partial fulfillment of the requirements for the award of the Degree of **Master of Computer Applications (MCA)** from **APJ Abdul Kalam Technological University (KTU)** during the academic year **2025 – 2026**.

<br><br><br>

---------------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----------------------------------------------------  
**Ms. AMEENA AFSAR** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Mrs. SRUTI SUDEVAN**  
Project Guide & Assistant Professor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Head of the Department & Associate Professor  
Dept. of Computer Applications &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dept. of Computer Applications  
AWH Engineering College, Calicut &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AWH Engineering College, Calicut  

<br><br><br>

Submitted for the Viva-Voce Examination held on: ............................................................

<br><br>

---------------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----------------------------------------------------  
**EXTERNAL EXAMINER** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **INTERNAL EXAMINER**

---

<div style="page-break-after: always;"></div>

# ACKNOWLEDGEMENT

		I express my profound sense of gratitude and sincere indebtedness to our respected Principal, **Dr. Sabeena MV**, for providing all necessary institutional facilities, computational infrastructure, and academic encouragement that made the completion of this project thesis possible.

		I convey my deepest and heartfelt thanks to **Mrs. Sruti Sudevan**, Head of the Department of Computer Applications, for her continuous inspiration, academic leadership, and vital encouragement throughout the duration of the MCA program and during this project endeavor.

		I take immense privilege in expressing my sincere gratitude to my Project Guide, **Ms. Ameena Afsar**, Assistant Professor, Department of Computer Applications, for her technical mentorship, invaluable suggestions, and patient supervision. Her constructive critiques, insightful suggestions, and thorough evaluations at every phase of system modeling, design, and testing helped shape this project into an academically rigorous and socially impactful system.

		I also extend my sincere gratitude to all the teaching and technical staff members of the Department of Computer Applications for their invaluable support, timely suggestions, and generous academic assistance throughout the project development cycle.

		I express my loving thanks to my family members and batchmates whose unwavering moral support, sacrifices, and continuous encouragement have been the bedrock of my life and education. Their feedback during user experience reviews and software testing has been deeply appreciated.

		Above all, I surrender myself in eternal gratitude before the Almighty for granting me the wisdom, health, strength, and perseverance to complete this project thesis successfully.

<br><br>

**ARSHAN NIZAR K P**  
(Reg No: AWH25MCA-2010)

---

<div style="page-break-after: always;"></div>

# ABSTRACT

		Chemotherapy-induced alopecia (hair loss) is widely recognized in oncological medicine as one of the most psychologically distressing and traumatic side effects for cancer patients, precipitating profound erosion of self-esteem, clinical anxiety, and acute social alienation. While thousands of empathetic citizens wish to donate natural hair for medical wig fabrication, traditional donation mechanisms across Kerala and India remain uncoordinated, fragmented, and heavily vulnerable to logistics failures. Existing approaches rely on informal WhatsApp groups, untracked courier drop-offs, and open social media appeals. This absence of centralized coordination creates acute bottlenecks: donors receive zero visibility into parcel arrivals; non-governmental organizations (NGOs) receive unsorted specimens lacking vital technical metadata; and immunocompromised cancer patients are forced to physically travel with paper diagnostic reports to prove their condition.

		To decisively resolve these failures, this thesis presents **HairFidence: A Centralized Role-Based Web Application for Hair Donation Lifecycle Management**, an end-to-end, secure, 3-Tier Model-View-Controller (MVC) web architecture. The platform digitizes, automates, and audits the entire hair donation, clinical verification, and prosthesis allocation lifecycle. Engineered using semantic HTML5, Vanilla CSS3 custom properties, and JavaScript (ES6+) on the client side, paired with a modular PHP 8.x backend engine, all transactional states are anchored in an optimized 8-table relational MySQL schema running in an Apache XAMPP environment. 

		HairFidence partitions governance across four discrete role modules: System Administrator (institutional NGO accreditation and grievance resolution), Healthcare NGOs (physical parcel audits, clinical diagnostic report verification, and community donation drives), Donors (specification authoring and multi-stage visual pipeline tracking), and Patients (secure medical report uploading and catalog browsing). A critical technical contribution is the implementation of **Pessimistic Concurrency Locking** via `SELECT ... FOR UPDATE` wrapped within atomic PDO database transactions, strictly preventing double-booking race conditions during simultaneous patient requests. Rigorous unit, integration, and black-box test suites validate that the system delivers robust data security, zero-cost wig access for cancer survivors, and total transparency for civic donors.

---

<div style="page-break-after: always;"></div>

# TABLE OF CONTENTS

| Chapter No. | Chapter Title | Page Number |
| :---: | :--- | :---: |
| | **CERTIFICATE** | ii |
| | **ACKNOWLEDGEMENT** | iii |
| | **ABSTRACT** | iv |
| | **LIST OF TABLES** | vii |
| | **LIST OF FIGURES** | viii |
| **1** | **INTRODUCTION** | **1** |
| | 1.1 Domain Overview & Background | 1 |
| | 1.2 Motivation | 3 |
| | 1.3 Problem Statement | 5 |
| | 1.4 Objectives | 6 |
| | 1.5 Organization of the Report | 7 |
| **2** | **SYSTEM ANALYSIS** | **8** |
| | 2.1 Existing System | 8 |
| | 2.2 Proposed System | 10 |
| | 2.3 Module Description | 12 |
| | 2.4 Sprint Planning | 15 |
| | 2.5 User Stories | 18 |
| **3** | **FEASIBILITY STUDY** | **21** |
| | 3.1 Economic Feasibility | 21 |
| | 3.2 Technical Feasibility | 23 |
| | 3.3 Operational Feasibility | 24 |
| | 3.4 Behavioral Feasibility | 25 |
| | 3.5 Software Feasibility | 26 |
| **4** | **SOFTWARE ENGINEERING PARADIGM** | **28** |
| | 4.1 Agile Development Methodology | 28 |
| | 4.2 Scrum Framework | 30 |
| **5** | **SYSTEM REQUIREMENT SPECIFICATION (SRS)** | **33** |
| | 5.1 Software Requirements | 33 |
| | 5.2 Hardware Requirements | 35 |
| **6** | **SYSTEM DESIGN** | **37** |
| | 6.1 Database Design & Normalization (1NF, 2NF, 3NF) | 37 |
| | 6.2 Data Dictionary (Tables) | 41 |
| | 6.3 UML Architecture (Class & Sequence Diagrams) | 46 |
| | 6.4 Use Case Diagram & Actor Mapping | 50 |
| | 6.5 System Scenarios | 52 |
| **7** | **SYSTEM DEVELOPMENT** | **55** |
| | 7.1 Development Lifecycle Activities | 55 |
| | 7.2 Implementation Technologies | 57 |
| | 7.3 Core Code Implementations | 59 |
| **8** | **SYSTEM TESTING AND IMPLEMENTATION** | **66** |
| | 8.1 Types of Testing | 66 |
| | 8.2 Test Case Matrix | 69 |
| | 8.3 Deployment & Cutover Strategy | 72 |
| **9** | **SYSTEM MAINTENANCE** | **75** |
| | 9.1 Corrective Maintenance | 75 |
| | 9.2 Adaptive Maintenance | 76 |
| | 9.3 Perfective Maintenance | 77 |
| **10** | **FUTURE ENHANCEMENTS** | **79** |
| **11** | **CONCLUSION** | **82** |
| **12** | **APPENDIX** | **84** |
| **13** | **BIBLIOGRAPHY** | **94** |

---

<div style="page-break-after: always;"></div>

# CHAPTER 1: INTRODUCTION

## 1.1 DOMAIN OVERVIEW & BACKGROUND
		In modern healthcare management, chemotherapy and radiation regimens continue to elevate cancer survival rates worldwide. However, cytotoxic chemotherapy protocols frequently inflict severe physical and emotional trauma upon patients. Among treatment-associated complications, chemotherapy-induced alopecia (hair loss) is clinically recognized as one of the most demoralizing experiences endured by cancer survivors, predominantly impacting women and children. Unlike internal physiological distress, alopecia serves as an inescapable, visible badge of disease, precipitating acute clinical depression, loss of self-worth, and social alienation.

		Specialized cranial medical prostheses (custom natural hair wigs) provide immense psychosocial rehabilitation, enabling recovering patients to reclaim their self-image and confidence. Unfortunately, the commercial marketplace for natural hair wigs is severely cost-prohibitive, typically commanding prices between ₹25,000 and ₹1,20,000 per unit due to meticulous hand-knotting craftsmanship and raw material scarcity. Concurrently, thousands of compassionate citizens express an active willingness to donate their natural hair. Regrettably, traditional charitable avenues across Kerala and India remain uncoordinated, informal, and vulnerable to operational failures.

## 1.2 MOTIVATION
		Traditional hair donation initiatives rely heavily on sporadic social media campaigns, unmonitored postal mail, and manual registers. These informal avenues suffer from profound breakdowns in trust:
		1. Donors package and dispatch hair parcels with zero tracking mechanisms, never receiving formal acknowledgment or confirmation that their contribution reached a genuine patient.
		2. Non-governmental organizations (NGOs) and hospital charity desks receive unsorted, damaged, or contaminated specimens lacking vital technical metadata (length, texture, dye history).
		3. Open social media appeals compromise patient dignity, exposing private diagnostic reports to the public web without verification safeguards.
		4. Commercial intermediaries frequently exploit unregulated donation streams, diverting free hair bundles into private cosmetic markets.

		These systemic failures motivated the development of **HairFidence**, a platform designed to provide institutional governance, clinical validation, and transparent multi-stage parcel tracking.

## 1.3 PROBLEM STATEMENT
		There is an urgent societal need for a verifiable, confidential, role-governed web application that streamlines the entire hair donation lifecycle. The platform must centralize donor cataloging, empower accredited NGOs as clinical gatekeepers, protect patient medical privacy through isolated document storage, and eliminate asset double-booking through robust database concurrency controls.

## 1.4 OBJECTIVES
		The primary technical and operational objectives of HairFidence include:
		* **Centralized Data Management:** Unify donor contributions, patient requests, clinical records, and NGO accreditations into an ACID-compliant MariaDB/MySQL relational data store.
		* **End-to-End Parcel Lifecycle Tracking:** Provide real-time visual pipeline monitoring across three discrete transactional states: `Available` (cataloged), `Processing` (patient request locked pending NGO verification), and `Donated` (inspected and dispatched).
		* **Pessimistic Concurrency Locking:** Implement database-level row locking (`FOR UPDATE`) within atomic PDO transactions to completely eliminate race conditions and asset double-booking.
		* **Privacy-Preserving Clinical Validation:** Provide a secure document upload pipeline that isolates patient oncology diagnostic certificates, restricting viewing privileges strictly to verified NGO auditors and administrators.
		* **Democratic Community Engagement:** Enable accredited NGOs to broadcast community donation drives and awareness campaigns, expanding civic participation across diverse demographic sectors.

## 1.5 ORGANIZATION OF THE REPORT
		This thesis report is organized into thirteen structured chapters: Chapter 2 examines system analysis and sprint breakdowns; Chapter 3 evaluates technical, operational, and economic feasibility; Chapter 4 presents the Agile Scrum engineering paradigm; Chapter 5 defines system requirement specifications; Chapter 6 details system design, 3NF normalization, and UML models; Chapter 7 covers modular development and core code implementations; Chapter 8 outlines testing suites and cutover strategies; Chapter 9 outlines maintenance plans; Chapter 10 projects future enhancements; Chapter 11 concludes the study; Chapter 12 provides appendix screen layouts; and Chapter 13 lists authoritative references.

---

<div style="page-break-after: always;"></div>

# CHAPTER 2: SYSTEM ANALYSIS

## 2.1 EXISTING SYSTEM
		The legacy approach to hair donation and medical wig distribution across regional charitable centers is an informal, manual, and uncoordinated operation. Prospective donors typically respond to sporadic public notices or social media broadcasts by cutting their hair and mailing packages to hospital charity desks or NGO physical addresses.
		
		Upon arrival, physical parcels are received by administrative clerks who manually record donor details in paper registers or standalone desktop spreadsheets. Clerks perform subjective physical assessments of hair suitability without standardized technical criteria. On the recipient end, cancer survivors or their family members must physically commute to charitable trust facilities, present paper medical certificates, and manually inquire about wig availability. Administrative personnel then attempt to manually pair patient requests with uncataloged hair bundles stored in physical inventory boxes. This leads to lost parcels, clinical record falsification, duplicate promises, and severe emotional distress.

## 2.2 PROPOSED SYSTEM
		HairFidence replaces these error-prone manual approaches with an enterprise web architecture operating under strict Role-Based Access Control (RBAC). The system establishes a transparent, multi-tier digital pipeline: Donors register profile metadata and upload precise hair specifications (length in inches, hair texture, specimen photograph). Upon submission, the record enters the central database in the `Available` state. Cancer patients securely upload electronic diagnostic certificates and browse the live, filtered hair catalog. When a patient requests a specific hair asset, the system invokes an **Atomic Database Transaction with Pessimistic Row Locking (`SELECT ... FOR UPDATE`)**, transitioning the post status immediately to `Processing`. This locks the asset against concurrent requests. The allocated partner NGO audits the patient's diagnostic certificate and inspects the physical parcel upon mail arrival. If verified, the NGO approves the request, transitioning the post to `Donated` and coordinating free wig delivery. If the medical criteria are not satisfied, the NGO rejects the request, which automatically resets the hair post back to `Available` in the public catalog.

## 2.3 MODULE DESCRIPTION
		HairFidence is partitioned into four independent yet interconnected functional modules:

### 2.3.1 Administrator Module
		The overarching governance layer for the application:
		* **Approve NGOs:** Reviews statutory registration credentials and activates NGO accounts (`is_approved = 1`).
		* **Manage Users & Platform:** Monitors Donor and Patient profiles and exercises root data sanitization.
		* **Resolve Complaints:** Centralized ticketing console to view user-submitted issues and toggle their status to `Resolved`.
		* **System Statistics:** High-level analytical dashboard tracking donation metrics and community drive statistics.

### 2.3.2 Healthcare NGO Module
		The intermediary layer responsible for medical verification and physical asset logistics:
		* **Create Campaign:** Deploys local hair donation drives with details (venue, date, description).
		* **Verify Hair Donations:** Validates incoming physical hair parcels and updates status to `Donated`.
		* **Audit Medical Reports:** Reviews patient diagnostic summaries to verify genuine oncological need.
		* **Manage Hair Requests:** Audits patient requests and approves or rejects them with automated catalog state transitions.

### 2.3.3 Hair Donor Module
		The philanthropic interface optimized for rapid data entry and tracking:
		* **Add Hair Donation:** Uploads details of hair (length in inches, texture, specimen photograph).
		* **View Donation Status:** Real-time visual tracking of donation pipeline (`Available` $\rightarrow$ `Processing` $\rightarrow$ `Donated`).
		* **View Campaigns:** Accesses directory of upcoming NGO-led donation events.
		* **Submit Grievances:** Direct ticketing channel to administrator for technical or logistics support.

### 2.3.4 Cancer Patient Module
		A highly secure, privacy-focused interface for cancer survivors to request cranial prostheses:
		* **Upload Medical Report:** Securely attaches institutional diagnostic reports for NGO validation.
		* **Browse Available Hair:** Interactive directory to browse and filter verified, available hair donations.
		* **Send Hair Request:** Dispatches a formal request for a specific hair asset routing it via an approved NGO with atomic locking.
		* **View Request Status:** Monitors the status of requested hair (`Pending` $\rightarrow$ `Approved` / `Rejected`).

## 2.4 SPRINT PLANNING
		The development of HairFidence was organized using Agile Scrum across two focused sprints:

### Sprint 1: Core Architecture, Authentication & Governance Console
| Module | Task Description | Hours | Expected Date | Actual Date | Remarks |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **System** | Database Schema Design & Tables Setup | 4 | 10/07/2025 | 10/07/2025 | 8 Normalized Tables |
| **Auth** | User Login & Role-Based Redirection | 3 | 14/07/2025 | 14/07/2025 | BCrypt Authentication |
| **Auth** | Donor & Patient Registration Workflow | 4 | 18/07/2025 | 18/07/2025 | Multi-role registration |
| **Admin** | Admin Dashboard & Statistical Counters | 4 | 22/07/2025 | 22/07/2025 | Metric counter engine |
| **Admin** | NGO Approval & Verification Console | 3 | 26/07/2025 | 26/07/2025 | Gated access control |
| **NGO** | NGO Registration & Document Attachments | 3 | 30/07/2025 | 30/07/2025 | Verification queue |
| **NGO** | NGO Operational Dashboard Interface | 4 | 04/08/2025 | 04/08/2025 | Operational views |
| **Donor** | Donor Dashboard & Navigation Layout | 3 | 08/08/2025 | 08/08/2025 | Responsive shell |

### Sprint 2: Logistics Pipeline, Concurrency Locking & Clinical Audit
| Module | Task Description | Hours | Expected Date | Actual Date | Remarks |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Donor** | Add Hair Donation Post & Specs Upload | 4 | 12/08/2025 | 12/08/2025 | Photo upload pipeline |
| **Donor** | Donation Status Pipeline Tracking UI | 3 | 16/08/2025 | 16/08/2025 | Multi-state visual bar |
| **Patient** | Patient Registration & Medical Report Upload | 4 | 20/08/2025 | 20/08/2025 | Encrypted report storage |
| **Patient** | Interactive Hair Catalog with Filter Bar | 4 | 24/08/2025 | 24/08/2025 | Length & texture search |
| **Patient** | Submit Hair Request & Concurrency Lock | 3 | 28/08/2025 | 28/08/2025 | Pessimistic row locking |
| **NGO** | Audit Medical Reports & Approve Requests | 4 | 02/09/2025 | 02/09/2025 | State machine logic |
| **NGO** | Create & Publish Community Campaigns | 3 | 06/09/2025 | 06/09/2025 | Public drive publisher |
| **System** | Complaint Redressal Ticketing & Profile | 3 | 10/09/2025 | 10/09/2025 | Ticketing lifecycle |

## 2.5 USER STORIES
		* **As an Administrator:** I want to review and accredit newly registered NGOs so that only legitimate medical charities can access patient diagnostic summaries and verify physical donations.
		* **As an Administrator:** I want to track system-wide donation metrics and resolve grievance tickets so that the platform maintains high transparency and rapid operational support.
		* **As an NGO Staff Member:** I want to inspect and audit clinical oncology reports submitted by patients so that medical wigs are provided exclusively to genuine cancer survivors.
		* **As an NGO Staff Member:** I want to publish community hair donation campaigns and dates so that civic volunteers can attend local collection drives.
		* **As a Hair Donor:** I want to log the exact attributes of my hair (length, texture, photo) so that my contribution can be cataloged accurately for cancer patients in need.
		* **As a Hair Donor:** I want to track my donation through a transparent multi-stage pipeline so that I have certainty regarding the arrival, audit, and final delivery of my hair.
		* **As a Cancer Patient:** I want to securely upload my institutional diagnostic reports without public exposure so that my medical need can be validated respectfully.
		* **As a Cancer Patient:** I want to browse a live catalog of clean, verified hair donations and request a matching wig so that I can regain my confidence and emotional comfort.

---

<div style="page-break-after: always;"></div>

# CHAPTER 3: FEASIBILITY STUDY

## 3.1 ECONOMIC FEASIBILITY
		HairFidence is constructed entirely upon Free and Open-Source Software (FOSS) technologies: PHP 8.x, Apache HTTP Server, MariaDB/MySQL, and open web standards. By eliminating proprietary operating system and database licensing costs, the system incurs zero recurring software acquisition fees. Server hosting requirements are minimal: a shared virtual private server (VPS) or an on-premise local server running Linux/Apache satisfies all operational demands. By automating parcel logging, document verification, and catalog matching, the platform saves hundreds of administrative labor hours for non-profit organizations, yielding a high return on investment (ROI).

## 3.2 TECHNICAL FEASIBILITY
		The platform is technically feasible and highly stable. It utilizes proven web engineering standards: PHP 8.x executing on an Apache HTTP server and backed by an optimized MySQL relational database engine. Concurrency safety is maintained through native PDO atomic transactions, ensuring that simultaneous requests for the same hair asset are handled without race conditions. Client-side interactions are lightweight, requiring no heavy external libraries, guaranteeing fast execution across varied desktop and mobile hardware.

## 3.3 OPERATIONAL FEASIBILITY
		HairFidence seamlessly integrates into the operational workflows of healthcare non-profits and hospital charity desks. Its intuitive, role-partitioned user interfaces allow staff, donors, and cancer patients to navigate features with minimal orientation. Automated pipeline tracking eliminates manual follow-up inquiries, while digitized medical document verification substantially accelerates the wig allocation timeline.

## 3.4 BEHAVIORAL FEASIBILITY
		Human-centered empathy is central to HairFidence. For cancer patients, privacy is paramount; the system isolates diagnostic certificates so they are visible solely to the verifying NGO and system administrator. For donors, the emotional satisfaction of charitable giving is reinforced through visual stage-by-stage pipeline tracking. These user-centric considerations ensure widespread community acceptance and sustained engagement.

## 3.5 SOFTWARE FEASIBILITY
		The web application conforms strictly to universal W3C web standards, ensuring full cross-browser compatibility across Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari. Responsive CSS grid and flexbox layouts ensure seamless rendering on smartphones, tablets, and widescreen desktop monitors without requiring separate native device installations.

---

<div style="page-break-after: always;"></div>

# CHAPTER 4: SOFTWARE ENGINEERING PARADIGM

## 4.1 AGILE DEVELOPMENT METHODOLOGY
		The development of HairFidence was guided by the Agile methodology. In contrast to rigid, sequential waterfall models, Agile prioritizes iterative enhancements, flexibility, and continuous stakeholder feedback. The project was broken down into focused development iterations where functional modules were built, validated, and refined incrementally. This iterative approach allowed rapid adaptation to real-world requirements, such as optimizing document upload security and refining the multi-state donation tracking pipeline.

## 4.2 SCRUM FRAMEWORK
		Scrum was adopted as the operational framework to govern sprint execution. The Scrum framework established structured work intervals (Sprints) combined with distinct organizational responsibilities:
		* **Product Owner:** Defined core functional objectives, user stories, and prioritized backlog items such as concurrency control and medical report auditing.
		* **Scrum Master:** Ensured adherence to Scrum principles, resolved technical impediments, and streamlined sprint transitions.
		* **Development Team:** Implemented frontend components, PHP backend services, database migrations, and integration test suites.
		Through regular Sprint Planning, Daily Standups, Sprint Reviews, and Retrospectives, the team delivered fully functional increments at the conclusion of each sprint cycle.

---

<div style="page-break-after: always;"></div>

# CHAPTER 5: SYSTEM REQUIREMENT SPECIFICATION (SRS)

## 5.1 SOFTWARE REQUIREMENTS
| Software Component | Specification |
| :--- | :--- |
| **Operating System** | Microsoft Windows 10 / 11 (64-bit) / Ubuntu Server 22.04 LTS / Linux |
| **Web Server Environment** | Apache HTTP Server 2.4.x (via XAMPP Control Panel v3.3+) |
| **Backend Scripting Engine** | PHP 8.2+ with PDO, OpenSSL, and Fileinfo extensions |
| **Database Management System** | MySQL 8.0+ / MariaDB 10.4+ with InnoDB Storage Engine |
| **Frontend Architecture** | HTML5, Vanilla CSS3 (Custom Properties), JavaScript (ES6+) |
| **Development Environment (IDE)**| Visual Studio Code (VS Code) with PHP Intelephense |
| **Database Client Tools** | phpMyAdmin 5.2+ and MySQL Command Line Client |
| **Client Web Browsers** | Google Chrome (v110+), Mozilla Firefox, Microsoft Edge, Safari |

## 5.2 HARDWARE REQUIREMENTS
| Hardware Component | Client-Side Minimum Specification | Server-Side Minimum Specification |
| :--- | :--- | :--- |
| **Processor (CPU)** | Dual-Core 1.8 GHz Intel Core i3 / AMD | Quad-Core 2.4 GHz Intel Xeon / AMD EPYC |
| **Memory (RAM)** | 2.0 GB DDR3 / DDR4 (4 GB recommended) | 8.0 GB DDR4 ECC (16 GB recommended) |
| **Storage Drive** | 500 MB free browser cache space | 512 GB SSD (minimum 20 GB free partition)|
| **Display Output** | Minimum 1024x768 (1920x1080 Full HD) | Server Console / Headless Display |
| **Network Interface** | Standard Broadband / 4G (512 Kbps+) | Gigabit Ethernet (1000BASE-T) Static IP |

---

<div style="page-break-after: always;"></div>

# CHAPTER 6: SYSTEM DESIGN

## 6.1 DATABASE DESIGN & NORMALIZATION (1NF, 2NF, 3NF)
		The database design of HairFidence is engineered to eliminate data redundancy, avoid insertion/update/deletion anomalies, and guarantee referential integrity across all transactional entities:
		* **First Normal Form (1NF):** A relation is in 1NF if and only if all attribute domains contain atomic (indivisible) values. Attributes such as `hair_length`, `hair_type`, and `image_url` store single scalar values without multi-valued arrays or repeating groups.
		* **Second Normal Form (2NF):** A relation is in 2NF if it is in 1NF and no non-prime attribute is partially dependent on any candidate key. Because every table uses a single-attribute surrogate primary key generated via `AUTO_INCREMENT` ($|\text{PK}| = 1$), partial dependencies are mathematically impossible.
		* **Third Normal Form (3NF):** A relation is in 3NF if it is in 2NF and there exist no transitive dependencies ($X \rightarrow Y$ and $Y \rightarrow Z$). Authentication data resides strictly in `login`, while domain profile attributes reside in `donors`, `patients`, and `ngos`. In `hair_requests`, the request status depends directly on `request_id`, not transitively on `patient_id` or `ngo_id`. Thus, 3NF is strictly achieved.

## 6.2 DATA DICTIONARY (TABLES)

### Table 1: `login` (Authentication Store)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `login_id` | `INT` | Unique authentication key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `email` | `VARCHAR(150)` | User electronic mail address | `NOT NULL`, `UNIQUE` |
| `password` | `VARCHAR(255)` | BCrypt cryptographic hash | `NOT NULL` |
| `role` | `ENUM` | Access role (`admin`, `ngo`, `donor`, `patient`) | `NOT NULL` |
| `created_at`| `TIMESTAMP` | Account creation timestamp | `DEFAULT CURRENT_TIMESTAMP` |

### Table 2: `donors` (Hair Donor Profiles)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `donor_id` | `INT` | Unique donor profile key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `login_id` | `INT` | Foreign key referencing credentials | `FOREIGN KEY` $\rightarrow$ `login(login_id)` `ON DELETE CASCADE` |
| `full_name` | `VARCHAR(100)` | Legal name of donor | `NOT NULL` |
| `phone` | `VARCHAR(15)` | Contact telephone number | `NOT NULL` |
| `address` | `TEXT` | Postal address of donor | `NOT NULL` |

### Table 3: `patients` (Cancer Survivor Profiles)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `patient_id` | `INT` | Unique patient profile key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `login_id` | `INT` | Foreign key referencing credentials | `FOREIGN KEY` $\rightarrow$ `login(login_id)` `ON DELETE CASCADE` |
| `full_name` | `VARCHAR(100)` | Legal name of patient | `NOT NULL` |
| `phone` | `VARCHAR(15)` | Emergency telephone number | `NOT NULL` |
| `address` | `TEXT` | Delivery residential address | `NOT NULL` |
| `medical_report_url` | `VARCHAR(255)` | Path to diagnostic oncology report | `NOT NULL` |

### Table 4: `ngos` (Accredited Healthcare Non-Profits)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `ngo_id` | `INT` | Unique NGO profile key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `login_id` | `INT` | Foreign key referencing credentials | `FOREIGN KEY` $\rightarrow$ `login(login_id)` `ON DELETE CASCADE` |
| `organization_name` | `VARCHAR(150)` | Legal trust / society name | `NOT NULL` |
| `registration_number` | `VARCHAR(100)` | Statutory registration certificate | `NOT NULL` |
| `is_approved` | `TINYINT(1)` | Administrative accreditation flag | `DEFAULT 0` (0=Pending, 1=Approved) |

### Table 5: `hair_donation_posts` (Hair Inventory Catalog)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `post_id` | `INT` | Unique hair post key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `donor_id` | `INT` | Foreign key identifying donor | `FOREIGN KEY` $\rightarrow$ `donors(donor_id)` `ON DELETE CASCADE` |
| `hair_length` | `DECIMAL(5,2)` | Length in inches | `NOT NULL` |
| `hair_type` | `VARCHAR(50)` | Texture (`Straight`, `Wavy`, `Curly`)| `NOT NULL` |
| `image_url` | `VARCHAR(255)` | Relative path to specimen photo | `NOT NULL` |
| `status` | `ENUM` | State machine flag | `DEFAULT 'Available'` (`Available`, `Processing`, `Donated`) |

### Table 6: `hair_requests` (Allocation Transactions)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `request_id` | `INT` | Unique allocation transaction key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `patient_id` | `INT` | Beneficiary patient key | `FOREIGN KEY` $\rightarrow$ `patients(patient_id)` `ON DELETE CASCADE` |
| `post_id` | `INT` | Allocated hair post key | `FOREIGN KEY` $\rightarrow$ `hair_donation_posts(post_id)` `ON DELETE CASCADE` |
| `ngo_id` | `INT` | Verifying partner NGO key | `FOREIGN KEY` $\rightarrow$ `ngos(ngo_id)` `ON DELETE CASCADE` |
| `request_date` | `TIMESTAMP` | Timestamp request was initiated | `DEFAULT CURRENT_TIMESTAMP` |
| `status` | `ENUM` | Verification state | `DEFAULT 'Pending'` (`Pending`, `Approved`, `Rejected`) |

### Table 7: `campaigns` (Community Donation Drives)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `campaign_id` | `INT` | Unique campaign key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `ngo_id` | `INT` | Hosting NGO key | `FOREIGN KEY` $\rightarrow$ `ngos(ngo_id)` `ON DELETE CASCADE` |
| `title` | `VARCHAR(150)` | Event promotional title | `NOT NULL` |
| `description` | `TEXT` | Guidelines and instructions | `NOT NULL` |
| `event_date` | `DATE` | Scheduled calendar date | `NOT NULL` |
| `location` | `VARCHAR(255)` | Physical venue address | `NOT NULL` |

### Table 8: `complaints` (Grievance Redressal Tickets)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `complaint_id` | `INT` | Unique complaint ticket key | `AUTO_INCREMENT`, `PRIMARY KEY` |
| `login_id` | `INT` | Filing user credential key | `FOREIGN KEY` $\rightarrow$ `login(login_id)` `ON DELETE CASCADE` |
| `subject` | `VARCHAR(150)` | Grievance subject line | `NOT NULL` |
| `description` | `TEXT` | Detailed incident narrative | `NOT NULL` |
| `status` | `ENUM` | Resolution status | `DEFAULT 'Pending'` (`Pending`, `Resolved`) |
| `date_submitted`| `TIMESTAMP` | Ticket submission timestamp | `DEFAULT CURRENT_TIMESTAMP` |

## 6.3 UML ARCHITECTURE

### Class Diagram Description
		The object-oriented design defines a central `User` identity class with specialized subclasses `Donor`, `Patient`, and `NGO`. A `Donor` encapsulates a one-to-many relationship with `HairDonationPost`. A `Patient` and `HairDonationPost` participate in a formal transaction contract managed by `HairRequest`, which is audited by an `NGO`. The `NGO` class also maintains a one-to-many relationship with `Campaign`.

### Sequence Diagram: Patient Hair Request & Concurrency Lock
		1. Patient Client submits `POST /patient/dashboard.php` with `post_id` and `ngo_id`.
		2. The controller invokes `$pdo->beginTransaction()`.
		3. The controller executes `SELECT status FROM hair_donation_posts WHERE post_id=? FOR UPDATE` acquiring an exclusive row lock.
		4. The database returns `status = 'Available'`.
		5. The controller executes `INSERT INTO hair_requests (patient_id, post_id, ngo_id, status) VALUES (?, ?, ?, 'Pending')`.
		6. The controller executes `UPDATE hair_donation_posts SET status='Processing' WHERE post_id=?`.
		7. The controller calls `$pdo->commit()`, releasing the row lock.
		8. The controller redirects the patient with a success alert; concurrent requests attempting step 3 are queued or rejected with conflict exceptions.

## 6.4 USE CASE DIAGRAM & ACTOR MAPPING
		* **Administrator:** Authenticates, vets and approves registered NGOs, monitors system metrics, resolves complaint tickets.
		* **Healthcare NGO:** Registers profile, creates donation campaigns, reviews patient diagnostic reports, inspects physical hair parcels, issues request approvals or rejections.
		* **Hair Donor:** Registers profile, logs hair donation post (length, texture, photo), views real-time multi-stage pipeline status, views upcoming drives, submits support tickets.
		* **Cancer Patient:** Registers profile, uploads medical report, searches available hair catalog, dispatches formal hair requests, tracks allocation status.

## 6.5 SYSTEM SCENARIOS
		* **Scenario 1 (Donation Logging):** Donor logs in $\rightarrow$ fills length and texture $\rightarrow$ uploads parcel photo $\rightarrow$ system validates MIME $\rightarrow$ post enters database as `Available`.
		* **Scenario 2 (Request & Locking):** Patient browses catalog $\rightarrow$ selects specimen $\rightarrow$ chooses partner NGO $\rightarrow$ transaction locks post to `Processing` $\rightarrow$ notification dispatched to NGO.
		* **Scenario 3 (Clinical Audit & Approval):** NGO accesses console $\rightarrow$ views patient report $\rightarrow$ inspects physical hair bundle $\rightarrow$ clicks `Approve` $\rightarrow$ post status updates to `Donated` and request to `Approved` $\rightarrow$ wig hand-crafted and delivered.
		* **Scenario 4 (Request Rejection):** NGO determines report is invalid $\rightarrow$ clicks `Reject` $\rightarrow$ request marked `Rejected` $\rightarrow$ hair post automatically unlocked back to `Available` in catalog.

---

<div style="page-break-after: always;"></div>

# CHAPTER 7: SYSTEM DEVELOPMENT

## 7.1 DEVELOPMENT LIFECYCLE ACTIVITIES
		System development transformed architectural models into operational software through iterative phases: database schema migration via DDL scripts; backend controller implementation with PDO data access objects; frontend responsive styling; security hardening against OWASP vulnerabilities; and comprehensive integration testing.

## 7.2 IMPLEMENTATION TECHNOLOGIES
		* **PHP Data Objects (PDO):** Enforces parameterized SQL compilation, completely neutralizing SQL Injection attacks.
		* **BCrypt Hashing:** Uses `password_hash()` with `PASSWORD_BCRYPT` ensuring irreversible credential security.
		* **Role-Based Access Control (RBAC):** Middleware interceptor `check_access()` prevents unauthorized horizontal or vertical privilege escalation.
		* **Isolated File System Partitions:** Patient medical reports are stored in dedicated directories with restricted script execution permissions.

## 7.3 CORE CODE IMPLEMENTATIONS

### 1. PDO Database Configuration (`config/db.php`)
```php
<?php
// config/db.php - Centralized PDO Database Connection
$host    = 'localhost';
$db      = 'hairfidence';
$user    = 'root';
$pass    = ''; // Local development environment password
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false, // Forces native prepared statements
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    error_log("Database Connection Failure: " . $e->getMessage());
    die("Database connection failed. Please ensure MariaDB is running in XAMPP.");
}
?>
```

### 2. Secure Login & RBAC Session Router (`login.php`)
```php
<?php
// login.php - Secure Authentication & Role Router
require_once 'config/db.php';
session_start();

$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email    = trim($_POST['email']);
    $password = $_POST['password'];

    if (!empty($email) && !empty($password)) {
        $stmt = $pdo->prepare("SELECT * FROM login WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();

        if ($user && password_verify($password, $user['password'])) {
            $role = $user['role'];
            $is_approved_ngo = true;
            $profile = [];

            if ($role === 'donor') {
                $stmt = $pdo->prepare("SELECT donor_id, full_name FROM donors WHERE login_id = ?");
                $stmt->execute([$user['login_id']]);
                $profile = $stmt->fetch();
            } elseif ($role === 'patient') {
                $stmt = $pdo->prepare("SELECT patient_id, full_name FROM patients WHERE login_id = ?");
                $stmt->execute([$user['login_id']]);
                $profile = $stmt->fetch();
            } elseif ($role === 'ngo') {
                $stmt = $pdo->prepare("SELECT ngo_id, organization_name, is_approved FROM ngos WHERE login_id = ?");
                $stmt->execute([$user['login_id']]);
                $profile = $stmt->fetch();
                if ($profile && (int)$profile['is_approved'] !== 1) {
                    $is_approved_ngo = false;
                }
            }

            if (!$is_approved_ngo) {
                $error = "Access Restricted: NGO registration is pending Administrator approval.";
            } else {
                $_SESSION['login_id'] = $user['login_id'];
                $_SESSION['email']    = $user['email'];
                $_SESSION['role']     = $role;
                $_SESSION['name']     = $profile['full_name'] ?? $profile['organization_name'] ?? 'Admin';
                if ($role === 'donor')   $_SESSION['donor_id']   = $profile['donor_id'];
                if ($role === 'patient') $_SESSION['patient_id'] = $profile['patient_id'];
                if ($role === 'ngo')     $_SESSION['ngo_id']     = $profile['ngo_id'];

                header("Location: auth/dashboard_redirect.php");
                exit();
            }
        } else {
            $error = "Invalid electronic mail or password credentials.";
        }
    } else {
        $error = "Please fill in all authentication fields.";
    }
}
?>
```

### 3. Hair Donation Post Submission with File Validation (`donor/dashboard.php`)
```php
<?php
// Extract from donor/dashboard.php: Post Submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_donation'])) {
    $hair_length = trim($_POST['hair_length']);
    $hair_type   = $_POST['hair_type'];

    if (empty($hair_length) || empty($hair_type) || empty($_FILES['hair_photo']['name'])) {
        $error_msg = "Please fill in all donation attributes and upload a photo.";
    } else {
        try {
            $file_name = $_FILES['hair_photo']['name'];
            $file_tmp  = $_FILES['hair_photo']['tmp_name'];
            $file_ext  = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
            $allowed   = ['jpg', 'jpeg', 'png'];

            if (!in_array($file_ext, $allowed, true)) {
                throw new Exception("Invalid image type. Only JPG, JPEG, and PNG are accepted.");
            }

            $upload_dir = '../uploads/hair_photos/';
            if (!is_dir($upload_dir)) {
                mkdir($upload_dir, 0777, true);
            }

            $new_file_name = 'hair_' . $donor_id . '_' . time() . '.' . $file_ext;
            $dest_path     = $upload_dir . $new_file_name;
            $db_path       = 'uploads/hair_photos/' . $new_file_name;

            if (!move_uploaded_file($file_tmp, $dest_path)) {
                throw new Exception("Failed to persist specimen image to disk.");
            }

            $stmt = $pdo->prepare("INSERT INTO hair_donation_posts (donor_id, hair_length, hair_type, image_url, status) VALUES (?, ?, ?, ?, 'Available')");
            $stmt->execute([$donor_id, $hair_length, $hair_type, $db_path]);
            $success_msg = "Donation post created successfully and cataloged as Available.";
        } catch (Exception $e) {
            $error_msg = $e->getMessage();
        }
    }
}
?>
```

### 4. NGO Medical Verification & Hair Request State Machine (`ngo/dashboard.php`)
```php
<?php
// Extract from ngo/dashboard.php: Request Approval & Rejection Logic
// 1. Handle Approval
if (isset($_GET['approve_request'])) {
    $request_id = intval($_GET['approve_request']);
    try {
        $pdo->beginTransaction();

        $stmt = $pdo->prepare("UPDATE hair_requests SET status = 'Approved' WHERE request_id = ? AND ngo_id = ?");
        $stmt->execute([$request_id, $ngo_id]);

        $stmt = $pdo->prepare("SELECT post_id FROM hair_requests WHERE request_id = ?");
        $stmt->execute([$request_id]);
        $post_id = $stmt->fetchColumn();

        if ($post_id) {
            $stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Donated' WHERE post_id = ?");
            $stmt->execute([$post_id]);
        }

        $pdo->commit();
        $success_msg = "Request approved and marked as Donated.";
    } catch (PDOException $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        $error_msg = "Approval failed: " . $e->getMessage();
    }
}

// 2. Handle Rejection (Automatic Unlock back to Available)
if (isset($_GET['reject_request'])) {
    $request_id = intval($_GET['reject_request']);
    try {
        $pdo->beginTransaction();

        $stmt = $pdo->prepare("UPDATE hair_requests SET status = 'Rejected' WHERE request_id = ? AND ngo_id = ?");
        $stmt->execute([$request_id, $ngo_id]);

        $stmt = $pdo->prepare("SELECT post_id FROM hair_requests WHERE request_id = ?");
        $stmt->execute([$request_id]);
        $post_id = $stmt->fetchColumn();

        if ($post_id) {
            $stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Available' WHERE post_id = ?");
            $stmt->execute([$post_id]);
        }

        $pdo->commit();
        $success_msg = "Request rejected. Specimen returned to Available status in catalog.";
    } catch (PDOException $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        $error_msg = "Rejection failed: " . $e->getMessage();
    }
}
?>
```

---

<div style="page-break-after: always;"></div>

# CHAPTER 8: SYSTEM TESTING AND IMPLEMENTATION

## 8.1 TYPES OF TESTING
		* **Unit Testing:** Verified isolated routines including password hashing, session role guards, mathematical hair length validators, and file upload extension parsers.
		* **Integration Testing:** Validated cross-module operational sequences: Donor Post Upload $\rightarrow$ Catalog Display $\rightarrow$ Patient Concurrency Lock $\rightarrow$ State Transition to `Processing` $\rightarrow$ NGO Clinical Audit $\rightarrow$ Final Handover (`Donated`).
		* **Black Box Testing:** Evaluated UI inputs against functional specifications without referencing source code internals.
		* **White Box Testing:** Verified statement and branch coverage, exception handling, transaction rollback consistency, and foreign key cascading constraints.

## 8.2 TEST CASE MATRIX
| Test ID | Test Scenario | Input Data | Expected Output | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | User Authentication | Email: `admin@hairfidence.com`<br>Pass: `adminpassword` | Authenticate and redirect to Admin console | Session initialized, redirected | **PASS** |
| **TC-02** | Invalid Authentication | Email: `admin@hairfidence.com`<br>Pass: `wrongpass` | Display "Invalid credentials" banner | Access denied, error banner rendered | **PASS** |
| **TC-03** | NGO Gated Login | Unapproved NGO credentials | Prevent dashboard access; display warning | Access blocked, warning shown | **PASS** |
| **TC-04** | Role Traversal Guard | Donor navigating to `/admin/` | Intercept via `check_access()`; redirect | HTTP 302 redirect to login | **PASS** |
| **TC-05** | Hair Post Authoring | Length: `12.5`, Texture: `Wavy` | Post created; status -> `Available` | Tuple inserted, catalog rendered | **PASS** |
| **TC-06** | Concurrency Lock | Concurrent requests for Post #104 | First succeeds; second caught by rollback | Conflict caught; zero double-booking | **PASS** |
| **TC-07** | Medical Upload | PDF report file (1.8 MB) | Validated, saved in `/uploads/medical_reports/` | Stored on disk, database updated | **PASS** |
| **TC-08** | Malicious File Block | Executable file (`test.exe`) | Block upload; throw file type exception | Upload blocked, error alert shown | **PASS** |
| **TC-09** | NGO Request Rejection | NGO rejects Request #35 | Post status unlocks back to `Available` | Specimen restored to catalog | **PASS** |
| **TC-10** | Grievance Ticketing | Valid subject & description | Ticket logged as `Pending`; resolved by Admin | Ticket resolved in console | **PASS** |

## 8.3 DEPLOYMENT & CUTOVER STRATEGY
		Deployment followed a local-to-cloud operational pipeline:
		1. Apache HTTP Server 2.4 and MariaDB initialized via XAMPP Control Panel.
		2. Execution of `database.sql` to instantiate the schema and seed default Administrator credentials.
		3. Configuration of file system permissions (`chmod 775` on `uploads/hair_photos/` and `uploads/medical_reports/`).
		4. Configuration of `php.ini` directives (`file_uploads = On`, `upload_max_filesize = 10M`, `session.cookie_httponly = 1`).

---

<div style="page-break-after: always;"></div>

# CHAPTER 9: SYSTEM MAINTENANCE

## 9.1 CORRECTIVE MAINTENANCE
		Focuses on defect triage and runtime error resolution. Server error logging is directed to secure `error.log` files with `display_errors = Off` to prevent system path disclosure. Input sanitization routines handle multibyte UTF-8 characters and address encoding variations.

## 9.2 ADAPTIVE MAINTENANCE
		Ensures operational continuity across evolving external software environments: upgrading code syntax for upcoming PHP interpreter releases (PHP 8.3/8.4), applying MariaDB engine patches, and maintaining compliance with modern browser security policies (SameSite cookies).

## 9.3 PERFECTIVE MAINTENANCE
		Proactive enhancements to optimize performance and usability: implementing client-side debounced AJAX catalog search filters, enhancing analytical dashboard charting with dynamic SVG graphics, and preparing multi-lingual localization support (Malayalam/Hindi).

---

<div style="page-break-after: always;"></div>

# CHAPTER 10: FUTURE ENHANCEMENTS

		* **Automated Courier Logistics API Integration:** Integration with India Post Speed Post, DTDC, or Delhivery APIs to automatically generate prepaid shipping labels with live parcel tracking webhooks.
		* **Cross-Platform Mobile Applications:** Native mobile applications built on **Flutter** for Android and iOS, leveraging smartphone cameras for calibrated hair strand measurement and automated document scanning.
		* **AI-Powered Virtual Wig Simulator (AR):** An Augmented Reality computer vision module using WebGL and TensorFlow.js enabling cancer patients to preview medical wig styles virtually on their own face before submitting requests.
		* **Certified Wig Workshop Integration:** Establishing direct digital dispatch channels to certified medical wig manufacturing workshops and integrating philanthropic micro-sponsorship payment gateways (Razorpay/Stripe).

---

<div style="page-break-after: always;"></div>

# CHAPTER 11: CONCLUSION

		The development and operational validation of **HairFidence: A Centralized Role-Based Web Application for Hair Donation Lifecycle Management** represent a meaningful technological milestone in humanitarian healthcare logistics. By replacing informal, untracked, and error-prone manual donation practices with a secure, role-governed 3-Tier MVC web platform, this project establishes a transparent, accountable bridge connecting altruistic donors, verified healthcare NGOs, and cancer patients recovering from chemotherapy.

		The system successfully digitizes the end-to-end hair donation lifecycle, empowering donors with real-time multi-stage pipeline tracking, equipping healthcare NGOs with auditable verification tools, and providing cancer survivors with an accessible portal to receive customized cranial prostheses at zero financial cost. The implementation of Pessimistic Concurrency Locking inside atomic PDO transactions completely eliminates race conditions and resource double-booking, while strict 3NF database normalization guarantees data integrity. Ultimately, HairFidence establishes an enduring standard for healthcare charity management—one that unites robust software engineering with deep human empathy to restore dignity, confidence, and comfort to cancer survivors.

---

<div style="page-break-after: always;"></div>

# CHAPTER 12: APPENDIX

## APPENDIX: UI SCREEN LAYOUTS AND WORKFLOW DESCRIPTIONS
		1. **Universal Authentication Console (`login.php`):** Clean login interface providing secure email and password entry, with automatic role-based dispatching to Admin, NGO, Donor, or Patient consoles.
		2. **Multi-Role Registration Portal (`register.php`):** Interactive tabbed registration enabling Donors, Patients, and NGOs to submit profile details and mandatory certifications within atomic transactions.
		3. **Public Landing Portal (`index.php`):** High-contrast healthcare information portal presenting the mission, donation criteria, and upcoming NGO community hair drives.
		4. **Administrator Governance Portal (`admin/dashboard.php`):** Metric counters, NGO accreditation review queue, user account management, and grievance ticket resolution console.
		5. **Healthcare NGO Verification Desk (`ngo/dashboard.php`):** Verification desk allowing NGO personnel to review patient oncology summaries, inspect physical hair parcels, and issue approvals or rejections.
		6. **Donor Philanthropy Dashboard (`donor/dashboard.php`):** Hair post authoring form with specimen photo upload and real-time visual multi-stage pipeline tracking (`Available` $\rightarrow$ `Processing` $\rightarrow$ `Donated`).
		7. **Patient Medical Portal & Hair Catalog (`patient/dashboard.php`):** Secure diagnostic report upload interface and interactive catalog with attribute filters (length, texture) and atomic request locking.
		8. **Grievance Redressal View (`complaints`):** Universal ticket submission console enabling stakeholders to file inquiries directly to system administrators.

---

<div style="page-break-after: always;"></div>

# CHAPTER 13: BIBLIOGRAPHY

## WEB RESOURCES & AUTHORITATIVE DOCUMENTATION
[1] PHP Documentation Group, *PHP: Hypertext Preprocessor Official Reference Manual*, Available online: https://www.php.net/manual/en/ (Accessed: June 2026).  
[2] Oracle Corporation, *MySQL 8.0 Reference Manual: InnoDB Storage Engine & Locking Models*, Available online: https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html (Accessed: June 2026).  
[3] Mozilla Developer Network (MDN), *Web Technology for Developers: Semantic HTML5 and CSS Flexible Box Layout*, Available online: https://developer.mozilla.org/en-US/docs/Web (Accessed: May 2026).  
[4] Open Web Application Security Project (OWASP), *OWASP Top 10: The Ten Most Critical Web Application Security Risks*, Available online: https://owasp.org/Top10/ (Accessed: May 2026).  
[5] MariaDB Foundation, *MariaDB Server Documentation: Transactions and Concurrency Control*, Available online: https://mariadb.com/kb/en/documentation/ (Accessed: April 2026).  
[6] APJ Abdul Kalam Technological University, *Master of Computer Applications Curriculum, Scheme and Syllabi (2020 Scheme)*, Government of Kerala, Available online: https://ktu.edu.in/ (Accessed: July 2026).  

## TECHNICAL REFERENCE TEXTBOOKS
[1] *Software Engineering: A Practitioner's Approach*, Roger S. Pressman and Bruce R. Maxim, 8th Edition, McGraw-Hill Education, 2015.  
[2] *Fundamentals of Database Systems*, Ramez Elmasri and Shamkant B. Navathe, 7th Edition, Pearson Education, 2016.  
[3] *PHP and MySQL Web Development*, Luke Welling and Laura Thomson, 5th Edition, Addison-Wesley Professional, 2017.  
[4] *UML Distilled: A Brief Guide to the Standard Object Modeling Language*, Martin Fowler, 3rd Edition, Addison-Wesley Professional, 2004.  
[5] *Design Patterns: Elements of Reusable Object-Oriented Software*, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, 1st Edition, Addison-Wesley Professional, 1994.  
[6] *Software Engineering*, Ian Sommerville, 10th Edition, Pearson Education, 2016.  
