# DEPARTMENT OF COMPUTER APPLICATIONS
## AWH ENGINEERING COLLEGE, KUTTIKKATTOOR, CALICUT - 673008
### (Affiliated to APJ Abdul Kalam Technological University, Kerala)

---

# HAIRFIDENCE: CANCER PATIENT HAIR DONATION MANAGEMENT SYSTEM

## PROJECT THESIS REPORT
Submitted in partial fulfillment of the requirements for the award of the degree of

### MASTER OF COMPUTER APPLICATIONS (MCA)

**Submitted by:**  
**ARSHAN NIZAR K P**  
**(Register Number: AWH25MCA-2010)**

Under the Guidance of:  
**Mrs. SRUTI SUDEVAN**  
Head of the Department & Associate Professor  
Department of Computer Applications  

**JULY 2026**

---

<div style="page-break-after: always;"></div>

# CERTIFICATE

### DEPARTMENT OF COMPUTER APPLICATIONS  
### AWH ENGINEERING COLLEGE, KUTTIKKATTOOR, CALICUT - 673008

This is to certify that this project thesis entitled **“HAIRFIDENCE: CANCER PATIENT HAIR DONATION MANAGEMENT SYSTEM”** is a bona fide record of the project work carried out by **ARSHAN NIZAR K P (Register Number: AWH25MCA-2010)** in partial fulfillment of the requirements for the award of the Degree of **Master of Computer Applications (MCA)** from **APJ Abdul Kalam Technological University (KTU)** during the academic year **2025 – 2026**.

<br><br><br>

--------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ---------------------------------------------  
**Mrs. SRUTI SUDEVAN** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Mrs. AISWARYA N**  
Head of the Department &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Project Coordinator & Assistant Professor  
Dept. of Computer Applications &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dept. of Computer Applications  
AWH Engineering College, Calicut &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AWH Engineering College, Calicut  

<br><br><br>

Submitted for the Viva-Voce Examination held on: ............................................................

<br><br>

--------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ---------------------------------------------  
**INTERNAL EXAMINER** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **EXTERNAL EXAMINER**

---

<div style="page-break-after: always;"></div>

# COMPANY / INSTITUTIONAL PROJECT COMPLETION CERTIFICATE

### HEALTH-TECH INNOVATIONS & RESEARCH LABS
**Cyberpark SEZ, Nellikkode P.O., Calicut, Kerala – 673016**  
*CIN: U72200KL2021PTC068412 | Email: verification@healthtechlabs.in | Web: www.healthtechlabs.in*

**Ref: HTL/MCA-PROJ/2026/084** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Date: 15th July 2026**

<br>

### TO WHOMSOEVER IT MAY CONCERN

		This is to certify that **Mr. ARSHAN NIZAR K P (Register Number: AWH25MCA-2010)**, a bona fide final year student of **Master of Computer Applications (MCA)** at **AWH Engineering College, Kuttikkattoor, Calicut**, has successfully completed his technical project and software engineering internship entitled **“HAIRFIDENCE: Cancer Patient Hair Donation Management System”** at our research center from **6th January 2026 to 10th July 2026**.

		During his internship tenure, he worked directly under our Healthcare Software Systems Division. He demonstrated outstanding analytical proficiency, software architectural comprehension, and practical dedication in designing, developing, and deploying full-stack web architectures utilizing PHP 8.x, MySQL relational database engines, and responsive user interfaces. He consistently adhered to industry-standard Software Development Life Cycle (SDLC) methodologies, modern cryptographic validation protocols, and relational database normalization principles.

		His conduct, character, and work ethic throughout the period were exemplary. We congratulate him on the successful delivery of the platform and wish him the very best in all his future academic and professional endeavors.

<br><br><br>

For **Health-Tech Innovations & Research Labs**,

<br><br>

-----------------------------------------------------------  
**Dr. SANDEEP MENON, Ph.D.**  
Director & Head of Software Engineering  
Health-Tech Innovations & Research Labs, Calicut  
*(Official Seal / Stamp)*

---

<div style="page-break-after: always;"></div>

# ABOUT THE COMPANY

		Health-Tech Innovations & Research Labs is a premier healthcare software research and development organization situated at the Cyberpark Special Economic Zone (SEZ) in Calicut, Kerala. Founded in 2021, the organization specializes in engineering fault-tolerant, accessible, and high-impact digital health platforms, telemedicine management systems, and humanitarian supply chain logistics solutions for hospital networks and non-governmental charitable organizations throughout South Asia.

		The center operates across four core technical competencies: Cloud-native Healthcare Architectures, Clinical Informatics & Patient Data Privacy, Distributed Logistics Systems, and Human-Centered User Experience Engineering. With a dedicated team of over eighty research engineers, systems architects, and biomedical consultants, the company is committed to transforming paper-based medical and philanthropic records into secure, high-availability digital infrastructures compliant with national and international health data standards.

		Health-Tech Innovations is deeply committed to humanitarian software engineering, maintaining dedicated non-profit initiatives that empower cancer rehabilitation centers, pediatric care societies, and voluntary organ and tissue donation drives. By leveraging modern web technologies, strict role-based access control, and atomic transaction architectures, the laboratory ensures that digital systems protect patient confidentiality while maximizing operational transparency for donors and clinical care teams alike.

		As a recognized industry internship sponsor for premier academic institutions affiliated with APJ Abdul Kalam Technological University, Health-Tech Innovations actively collaborates with postgraduate researchers to bridge the gap between theoretical software paradigms and robust, real-world community deployments.

---

<div style="page-break-after: always;"></div>

# ACKNOWLEDGEMENT

		I express my profound sense of gratitude and sincere indebtedness to our respected Principal, **Dr. Sabeena M V**, for providing all necessary academic facilities, computational infrastructure, and institutional encouragement that made the completion of this thesis work possible.

		I convey my deepest and heartfelt thanks to **Mrs. Sruti Sudevan**, Head of the Department of Computer Applications, for her constant inspiration, academic leadership, and continuous encouragement throughout the duration of the MCA curriculum and during this project endeavor.

		I take immense privilege in expressing my sincere gratitude to my Project Guide and Coordinator, **Mrs. Aiswarya N**, Assistant Professor, Department of Computer Applications, and **Mrs. Sruti Sudevan**, for their indispensable guidance, technical mentorship, and patient supervision. Their constructive criticisms, insightful suggestions, and thorough evaluations at every phase of system modeling, design, and testing helped shape this project into an academically rigorous and socially impactful system.

		I also extend my sincere gratitude to all the teaching and non-teaching faculty members of the Department of Computer Applications for their invaluable support, timely suggestions, and generous academic assistance throughout the project development cycle.

		I express my loving thanks to my parents and family members whose unwavering moral support, sacrifices, and continuous prayers have been the bedrock of my life and education. I also express my warm appreciation to my batchmates and friends for their collaborative discussions, constructive feedback during user experience reviews, and camaraderie throughout our post-graduate journey.

		Above all, I surrender myself in eternal gratitude before the Almighty for granting me the wisdom, health, strength, and perseverance to complete this project thesis successfully.

<br><br>

**ARSHAN NIZAR K P**  
(Reg No: AWH25MCA-2010)

---

<div style="page-break-after: always;"></div>

# ABSTRACT

		Chemotherapy-induced alopecia (hair loss) is widely recognized in oncological care as one of the most psychologically distressing side effects for cancer patients, precipitating profound loss of personal dignity, clinical anxiety, and social alienation. While thousands of citizens across society wish to donate their natural hair for medical wig-making initiatives, traditional donation approaches in Kerala and nationally remain unorganized. Existing initiatives rely on informal WhatsApp groups, sporadic in-person drop-offs, and unlinked paper spreadsheets. This absence of centralized logistics creates acute operational bottlenecks: generous donors have zero visibility into parcel arrivals; non-governmental organizations (NGOs) receive unsorted specimens lacking vital metadata; and immunocompromised cancer patients are forced to physically travel to offices with paper diagnostic reports to prove their condition.

		To decisively resolve these failures, this thesis presents **HairFidence: Cancer Patient Hair Donation Management System**, an end-to-end, secure, 3-Tier Model-View-Controller (MVC) web application. The platform digitizes, automates, and audits the entire hair donation, clinical verification, and prosthesis distribution lifecycle. Engineered using an interactive HTML5/Vanilla CSS3/ES6+ JavaScript frontend paired with a modular PHP 8.x backend engine, all transactional states are anchored in an optimized 8-table relational MySQL schema running in an Apache XAMPP environment. 

		HairFidence partitions governance across four discrete role modules: System Administrator (platform vetting and grievance resolution), Healthcare NGOs (physical parcel audits, clinical diagnostic report verification, and community drives), Donors (specification authoring and multi-stage pipeline tracking), and Patients (secure medical report uploading and catalog browsing). A critical technical contribution is the implementation of **Pessimistic Concurrency Locking** via `SELECT ... FOR UPDATE` wrapped within atomic PDO database transactions, strictly preventing double-booking race conditions during simultaneous patient requests. Rigorous unit, integration, and black-box test suites validate that the system delivers robust data security, zero-cost wig access for cancer survivors, and total transparency for civic donors.

---

<div style="page-break-after: always;"></div>

# TABLE OF CONTENTS

| Chapter No. | Chapter Title | Page Number |
| :---: | :--- | :---: |
| | **CERTIFICATE** | ii |
| | **COMPANY CERTIFICATE** | iii |
| | **ABOUT THE COMPANY** | iv |
| | **ACKNOWLEDGEMENT** | v |
| | **ABSTRACT** | vi |
| | **LIST OF TABLES** | ix |
| | **LIST OF FIGURES** | x |
| **8** | **INTRODUCTION** | **1** |
| | 8.1 System Overview | 1 |
| | 8.2 Problem Statement & Clinical Context | 3 |
| | 8.3 Objectives of the System | 5 |
| | 8.4 Scope of the Project | 7 |
| | 8.5 Operational and Psychosocial Benefits | 9 |
| **9** | **SYSTEM ANALYSIS** | **11** |
| | 9.1 Existing System Description | 11 |
| | 9.2 Limitations of the Existing System | 13 |
| | 9.3 Proposed System Architecture | 15 |
| | 9.4 Concrete Enhancements Implemented | 17 |
| **10** | **FEASIBILITY STUDY** | **20** |
| | 10.1 Technical Feasibility | 20 |
| | 10.2 Operational Feasibility | 22 |
| | 10.3 Economic Feasibility | 24 |
| | 10.4 Behavioural & Ethical Feasibility | 26 |
| | 10.5 Software Standards Feasibility | 28 |
| **11** | **SOFTWARE ENGINEERING PARADIGM** | **30** |
| | 11.1 Agile Process Methodology | 30 |
| | 11.2 Scrum Framework Implementation | 32 |
| | 11.3 Sprint Planning and Task Decomposition | 34 |
| | 11.4 User Story Mapping & Acceptance Criteria | 38 |
| | 11.5 Agile Ceremonies & Milestone Delivery | 41 |
| **12** | **SYSTEM REQUIREMENT SPECIFICATION (SRS)** | **43** |
| | 12.1 Minimum Hardware Requirements | 43 |
| | 12.2 Software Stack and Environment | 45 |
| | 12.3 Functional Requirements by Module | 48 |
| | 12.4 Non-Functional Requirements | 54 |
| **13** | **SYSTEM DESIGN** | **58** |
| | 13.1 High-Level MVC Architectural Pattern | 58 |
| | 13.2 Data Flow Diagrams (DFD Level 0, 1, 2) | 62 |
| | 13.3 UML Modeling (Use Case, Class, Sequence) | 68 |
| | 13.4 Database Design & Relational Schema | 76 |
| | 13.5 Normalization Proofs (1NF, 2NF, 3NF) | 83 |
| **14** | **SYSTEM DEVELOPMENT** | **88** |
| | 14.1 Subsystem Modular Breakdown | 88 |
| | 14.2 Core Algorithms & Business Logic | 92 |
| | 14.3 Routing & Endpoints Specification | 99 |
| | 14.4 Input Validation & Security Layers | 102 |
| **15** | **SYSTEM TESTING AND IMPLEMENTATION** | **106** |
| | 15.1 Testing Methodologies Applied | 106 |
| | 15.2 Comprehensive Test Suite Table | 110 |
| | 15.3 Deployment & Build Configuration | 114 |
| | 15.4 Operational Environment Verification | 117 |
| **16** | **SYSTEM MAINTENANCE** | **120** |
| | 16.1 Corrective Maintenance Plan | 120 |
| | 16.2 Adaptive Maintenance Plan | 122 |
| | 16.3 Perfective Maintenance Plan | 124 |
| | 16.4 Preventive Maintenance Plan & DR | 126 |
| **17** | **FUTURE ENHANCEMENT** | **129** |
| | 17.1 Cross-Platform Mobile Applications | 129 |
| | 17.2 Automated Postal & Logistics API Integration | 131 |
| | 17.3 AI-Powered Virtual Wig AR Simulator | 133 |
| | 17.4 Philanthropic Micro-Sponsorship Gateway | 135 |
| | 17.5 Multi-Channel Notification Webhooks | 137 |
| **18** | **CONCLUSION** | **139** |
| | 18.1 Summary of Project Achievements | 139 |
| | 18.2 Validation of Core Objectives | 141 |
| | 18.3 Academic & Engineering Conclusion | 143 |
| **19** | **APPENDIX** | **145** |
| | Appendix A: Complete Database DDL SQL Script | 145 |
| | Appendix B: Core Architectural Code Files | 149 |
| | Appendix C: System Data Dictionary | 153 |
| **20** | **BIBLIOGRAPHY** | **156** |
| | Technical Reference Books | 156 |
| | Authoritative Documentation & Web References | 157 |
