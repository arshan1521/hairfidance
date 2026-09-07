# CHAPTER 13: SYSTEM DESIGN

## 13.1 HIGH-LEVEL ARCHITECTURAL PATTERN: 3-TIER MVC
		HairFidence is architected according to the classical **3-Tier Model-View-Controller (MVC)** software architectural pattern. The MVC design pattern enforces strict separation of concerns, decoupling the presentation layer (Views) from domain data models (Models) and routing logic (Controllers). This separation guarantees maintainability, modular testability, and enterprise-grade code organization.

```
+-----------------------------------------------------------------------------------------+
|                                TIER 1: PRESENTATION (VIEWS)                             |
|                                                                                         |
|  * Admin Console (admin/dashboard.php)      * NGO Operational Hub (ngo/dashboard.php)   |
|  * Donor Dashboard (donor/dashboard.php)    * Patient Catalog & Portal (patient/...)    |
|  * Public Landing & Auth (index.php, login.php, register.php)                           |
+-----------------------------------------------------------------------------------------+
                                             ^
                                             |  HTTP Requests / HTML Response Rendering
                                             v
+-----------------------------------------------------------------------------------------+
|                               TIER 2: BUSINESS LOGIC (CONTROLLERS)                      |
|                                                                                         |
|  * AuthController & Session Router (auth/dashboard_redirect.php)                        |
|  * ConcurrencyLockController (PDO Atomic Transaction Manager)                           |
|  * MedicalReportAuditController (Document Verification & Validation)                    |
|  * CatalogFilterController (Dynamic Attribute Query Engine)                             |
|  * GrievanceTicketingController (Complaint Lifecycle Handler)                           |
|  * RBAC Security Middleware Guard (includes/auth_check.php)                             |
+-----------------------------------------------------------------------------------------+
                                             ^
                                             |  PDO Prepared Statements / SQL Data Binding
                                             v
+-----------------------------------------------------------------------------------------+
|                             TIER 3: DATA PERSISTENCE (MODELS)                           |
|                                                                                         |
|  * MariaDB / MySQL Relational Database Engine (InnoDB Storage Engine)                   |
|  * 8 Normalized Relational Tables:                                                      |
|    - `login`                 - `donors`             - `patients`                        |
|    - `ngos`                  - `hair_donation_posts`- `hair_requests`                   |
|    - `campaigns`             - `complaints`                                             |
|  * ACID Transaction Concurrency Locks (SELECT ... FOR UPDATE)                           |
|  * Referential Integrity Enforced via Foreign Key Cascades                              |
+-----------------------------------------------------------------------------------------+
```

1. **Tier 1: Presentation Layer (Views):** Responsible exclusively for user interface rendering. Views are authored using semantic HTML5, modern ECMAScript 6+ (ES6), and Vanilla CSS3 custom properties. The views consume structured associative data arrays emitted by controllers and render responsive, accessible interfaces. Crucially, views contain zero raw database access or business logic.
2. **Tier 2: Application / Controller Layer (Controllers):** Implemented via modular PHP 8.x scripts. Controllers intercept HTTP `GET` and `POST` payloads, validate input types, enforce authentication boundaries via `check_access()`, coordinate file upload security, execute domain business logic (e.g., verifying that hair length $\ge 8.0\text{ inches}$), and manage atomic database transactions.
3. **Tier 3: Data Persistence Layer (Models):** Governed by the MariaDB/MySQL relational database engine configured with the **InnoDB storage engine**. The persistence layer guarantees full ACID compliance (Atomicity, Consistency, Isolation, Durability), enforces referential integrity through foreign key cascades, and executes row-level pessimistic locks (`FOR UPDATE`) to manage concurrent asset allocation.

---

## 13.2 DATA FLOW DIAGRAMS (DFD)

### 13.2.1 DFD Level 0: System Context Diagram
		The Level 0 Context Diagram establishes the global boundary of the system, illustrating how external entities (Administrator, Healthcare NGO, Hair Donor, Cancer Patient) interact with the centralized HairFidence process.

```
                           +----------------------------------------------+
                           |                  HAIR DONOR                  |
                           +----------------------------------------------+
                              | Hair Specs, Photographs     ^ Live Pipeline
                              | & Contact Profile           | Status Updates
                              v                             |
+----------------------+   +------------------------------------+   +----------------------+
|        SYSTEM        |-->|                                    |<--|      HEALTHCARE      |
|    ADMINISTRATOR     |<--|            HAIRFIDENCE             |-->|         NGO          |
+----------------------+   |        CENTRALIZED SYSTEM          |   +----------------------+
  Accreditation,           |            (PROCESS 0)             |    Physical Audits,
  Complaint Resolution     +------------------------------------+    Clinical Reviews,
  & Global Metrics            |                              ^       Camps & Verifications
                              | Verified Available Catalog   | Diagnostic Records
                              v                              | & Hair Requests
                           +----------------------------------------------+
                           |                CANCER PATIENT                |
                           +----------------------------------------------+
```

### 13.2.2 DFD Level 1: Macro Subsystem Decomposition
		The Level 1 Diagram decomposes the central system into seven distinct operational processes, mapping data flows across physical database tables:

```
[User Input] ----> ( Process 1.0: Authentication & Role Router )
                                |
        +-----------------------+-----------------------+
        |                       |                       |
        v                       v                       v
( Process 2.0: NGO )   ( Process 3.0: Hair )   ( Process 4.0: Patient )
( Accreditation &  )   ( Cataloging & Post )   ( Clinical Upload &    )
( Governance       )   ( Insertion         )   ( Report Verification  )
        |                       |                       |
        | [login, ngos]         | [hair_donation_posts] | [patients]
        v                       v                       v
+-----------------------------------------------------------------+
|   Process 5.0: Concurrency-Locked Request & Matching Engine     |
|   (Atomic PDO Transaction with SELECT ... FOR UPDATE Lock)      |
+-----------------------------------------------------------------+
                                |
                                | [hair_requests, hair_donation_posts]
                                v
        +-----------------------+-----------------------+
        |                                               |
        v                                               v
( Process 6.0: Community )             ( Process 7.0: Grievance Redressal )
( Campaign Publishing    )             ( Support Ticketing Console        )
  [campaigns]                            [complaints]
```

### 13.2.3 DFD Level 2: Transactional Request & Locking Workflow
		Decomposes Sub-Process 5.0 (Request Handling), demonstrating the exact sequence where a patient requests a hair asset and the system executes row-level locking:

```
[Patient UI]
     |  1. Submits Hair Request (post_id, ngo_id)
     v
( Process 5.1: Initialize Atomic PDO Transaction via $pdo->beginTransaction() )
     |
     v
( Process 5.2: Query `hair_donation_posts` WHERE post_id=? FOR UPDATE )
     |
     +---> Evaluate Current Status:
              |
              |-- [Status != 'Available'] --> ( Process 5.3: Execute Rollback & Return Conflict Error )
              |
              +-- [Status == 'Available'] --> ( Process 5.4: Insert Tuple into `hair_requests` [Pending] )
                                                    |
                                                    v
                                              ( Process 5.5: UPDATE `hair_donation_posts` SET status='Processing' )
                                                    |
                                                    v
                                              ( Process 5.6: Commit Transaction via $pdo->commit() )
                                                    |
                                                    v
                                              ( Process 5.7: Emit Dispatch Notice to Assigned NGO )
```

---

## 13.3 UML MODELING

### 13.3.1 Use Case Specifications & Actor-Action Matrix
		The system defines four principal human actors interacting with fifteen formal use cases:

```
========================================================================================
USE CASE IDENTIFIER AND ACTOR-ACTION MAPPING MATRIX
========================================================================================
Actors:
  * Admin   : System Administrator (Regulatory Governance)
  * NGO     : Healthcare Non-Governmental Organization (Verification Intermediary)
  * Donor   : Hair Donor (Civic Contributor)
  * Patient : Cancer Patient / Patient Caregiver (Medical Beneficiary)

Use Case Mapping:
+--------+---------------------------------------+---------------------+-------------------+
| UC ID  | Use Case Name                         | Primary Actor(s)    | Associated Tables |
+--------+---------------------------------------+---------------------+-------------------+
| UC-01  | User Authentication & Session Login   | All Roles           | login             |
| UC-02  | Multi-Role Profile Registration       | Donor, Patient, NGO | login, profiles   |
| UC-03  | Vetting & Accredit NGO Accounts       | Admin               | ngos              |
| UC-04  | Create Hair Donation Post             | Donor               | hair_donation_posts|
| UC-05  | View Multi-Stage Pipeline Status      | Donor, Patient, NGO | hair_donation_posts|
| UC-06  | Upload Clinical Oncology Certificate  | Patient             | patients          |
| UC-07  | Search & Filter Hair Catalog          | Patient             | hair_donation_posts|
| UC-08  | Submit Hair Request (Pessimistic Lock)| Patient             | hair_requests     |
| UC-09  | Audit Patient Diagnostic Summary      | NGO                 | patients          |
| UC-10  | Approve / Reject Hair Request         | NGO                 | hair_requests     |
| UC-11  | Verify Physical Parcel Arrival        | NGO                 | hair_donation_posts|
| UC-12  | Publish Community Donation Campaign   | NGO                 | campaigns         |
| UC-13  | Submit Grievance / Support Ticket     | Donor, Patient, NGO | complaints        |
| UC-14  | Investigate & Resolve Complaint Ticket| Admin               | complaints        |
| UC-15  | Aggregate System Analytics & Metrics  | Admin               | All Tables        |
+--------+---------------------------------------+---------------------+-------------------+
```

### 13.3.2 Class Diagram (Entities, Attributes, Methods & Relationships)
		The object-oriented structural design of HairFidence is modeled below, illustrating entity attributes, visibility, method signatures, and multiplicity relationships:

```
+-----------------------------------------------------------------------------+
|                                 <<Entity>>                                  |
|                                    User                                     |
+-----------------------------------------------------------------------------+
| - login_id: Integer {PK}                                                    |
| - email: String                                                             |
| - password_hash: String                                                     |
| - role: Enum['admin', 'ngo', 'donor', 'patient']                            |
| - created_at: Timestamp                                                     |
+-----------------------------------------------------------------------------+
| + authenticate(email: String, plainPassword: String): Boolean               |
| + hashPassword(plainPassword: String): String                               |
| + logout(): Void                                                            |
+-----------------------------------------------------------------------------+
                                       ^
         +-----------------------------+-----------------------------+
         |                             |                             |
+------------------------+  +------------------------+  +------------------------+
|       <<Entity>>       |  |       <<Entity>>       |  |       <<Entity>>       |
|         Donor          |  |        Patient         |  |          NGO           |
+------------------------+  +------------------------+  +------------------------+
| - donor_id: Int {PK}   |  | - patient_id: Int {PK} |  | - ngo_id: Int {PK}     |
| - login_id: Int {FK}   |  | - login_id: Int {FK}   |  | - login_id: Int {FK}   |
| - full_name: String    |  | - full_name: String    |  | - org_name: String     |
| - phone: String        |  | - phone: String        |  | - reg_number: String   |
| - address: Text        |  | - address: Text        |  | - is_approved: Boolean |
+------------------------+  | - report_url: String   |  +------------------------+
| + addDonation(): Post  |  +------------------------+  | + auditReport(): Bool  |
| + trackHistory(): List |  | + uploadReport(): Bool |  | + approveReq(): Bool   |
+------------------------+  | + browseCatalog(): List|  | + createDrive(): Camp  |
         |                  | + requestHair(): Bool  |  +------------------------+
         | 1                +------------------------+               | 1
         |                              | 1                          |
         v 0..*                         v 0..*                       v 0..*
+------------------------+  +------------------------+  +------------------------+
|       <<Entity>>       |  |       <<Entity>>       |  |       <<Entity>>       |
|    HairDonationPost    |  |      HairRequest       |  |        Campaign        |
+------------------------+  +------------------------+  +------------------------+
| - post_id: Int {PK}    |  | - request_id: Int {PK} |  | - campaign_id: Int{PK} |
| - donor_id: Int {FK}   |  | - patient_id: Int {FK} |  | - ngo_id: Int {FK}     |
| - hair_length: Decimal |  | - post_id: Int {FK}    |  | - title: String        |
| - hair_type: String    |  | - ngo_id: Int {FK}     |  | - description: Text    |
| - image_url: String    |  | - request_date: Time   |  | - event_date: Date     |
| - status: Enum         |  | - status: Enum         |  | - location: String     |
+------------------------+  +------------------------+  +------------------------+
```

### 13.3.3 Sequence Diagram: Concurrency-Safe Hair Allocation Path
		Details the chronological message interchange during patient request execution:

```
Patient Client               Web Controller                      Database Engine (InnoDB)
      |                             |                                       |
      | 1. POST request_hair        |                                       |
      |---------------------------->|                                       |
      |    (post_id, ngo_id)        | 2. beginTransaction()                 |
      |                             |-------------------------------------->|
      |                             |                                       |
      |                             | 3. SELECT status FROM hair_posts      |
      |                             |    WHERE post_id=? FOR UPDATE         |
      |                             |-------------------------------------->| [Acquires Row Lock]
      |                             | 4. Return status = 'Available'        |
      |                             |<--------------------------------------|
      |                             |                                       |
      |                             | 5. INSERT INTO hair_requests          |
      |                             |    (patient_id, post_id, ngo_id)      |
      |                             |-------------------------------------->|
      |                             |                                       |
      |                             | 6. UPDATE hair_donation_posts         |
      |                             |    SET status = 'Processing'          |
      |                             |-------------------------------------->| [Asset Locked]
      |                             |                                       |
      |                             | 7. commit()                           |
      |                             |-------------------------------------->| [Releases Lock]
      | 8. HTTP 302 Redirect        |                                       |
      |    (Success Confirmation)   |                                       |
      |<----------------------------|                                       |
```

### 13.3.4 Activity Diagram: End-to-End Hair Donation & Verification Lifecycle
```
(*) --> [Donor Registers Profile]
        |
        v
    [Donor Authors Hair Post (Length, Texture, Photo)]
        |
        v
    [Post Enters Database: Status = 'Available']
        |
        v
    [Patient Uploads Oncology Report & Browses Catalog]
        |
        v
    [Patient Submits Hair Request via Partner NGO]
        |
        v
    [System Initiates Atomic Transaction with Row Lock]
        |
        v
    {Is Post Still Available?}
        |
        |-- [No: Conflict Detected] --> [Rollback Transaction] --> [Show Error to Patient] --> (*)
        |
        +-- [Yes: Lock Acquired] ----> [Insert Request: Status = 'Pending']
                                            |
                                            v
                                       [Update Post: Status = 'Processing']
                                            |
                                            v
                                       [Commit Transaction]
                                            |
                                            v
                                       [NGO Inspects Clinical Records & Physical Hair]
                                            |
                                            v
                                       {Clinical Audit Result?}
                                            |
                                            |-- [Rejected] --> [Reset Post Status to 'Available']
                                            |                  [Set Request Status to 'Rejected'] --> (*)
                                            |
                                            +-- [Approved] --> [Set Post Status to 'Donated']
                                                               [Set Request Status to 'Approved']
                                                                    |
                                                                    v
                                                               [Coordinate Free Wig Handover] --> (*)
```

---

## 13.4 DATABASE DESIGN & RELATIONAL SCHEMA TABLES
		The `hairfidence` database consists of 8 optimized relational tables engineered under the InnoDB storage engine with `utf8mb4` encoding:

### Table 1: `login` (Central Authentication & Identity Relation)
```sql
CREATE TABLE IF NOT EXISTS `login` (
    `login_id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(150) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `role` ENUM('admin', 'ngo', 'donor', 'patient') NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `login_id`
* **Unique Key:** `email`
* **Functional Dependencies:** $\text{login\_id} \rightarrow \text{email, password, role, created\_at}$

### Table 2: `donors` (Philanthropic Donor Profiles)
```sql
CREATE TABLE IF NOT EXISTS `donors` (
    `donor_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL,
    `address` TEXT NOT NULL,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `donor_id`
* **Foreign Key:** `login_id` references `login(login_id)` with cascading deletion.
* **Functional Dependencies:** $\text{donor\_id} \rightarrow \text{login\_id, full\_name, phone, address}$

### Table 3: `patients` (Cancer Survivor Clinical Profiles)
```sql
CREATE TABLE IF NOT EXISTS `patients` (
    `patient_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL,
    `address` TEXT NOT NULL,
    `medical_report_url` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `patient_id`
* **Foreign Key:** `login_id` references `login(login_id)` with cascading deletion.
* **Functional Dependencies:** $\text{patient\_id} \rightarrow \text{login\_id, full\_name, phone, address, medical\_report\_url}$

### Table 4: `ngos` (Accredited Healthcare Non-Profit Intermediaries)
```sql
CREATE TABLE IF NOT EXISTS `ngos` (
    `ngo_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `organization_name` VARCHAR(150) NOT NULL,
    `registration_number` VARCHAR(100) NOT NULL,
    `is_approved` TINYINT(1) DEFAULT 0,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `ngo_id`
* **Foreign Key:** `login_id` references `login(login_id)` with cascading deletion.
* **Functional Dependencies:** $\text{ngo\_id} \rightarrow \text{login\_id, organization\_name, registration\_number, is\_approved}$

### Table 5: `hair_donation_posts` (Physical Hair Inventory Catalog)
```sql
CREATE TABLE IF NOT EXISTS `hair_donation_posts` (
    `post_id` INT AUTO_INCREMENT PRIMARY KEY,
    `donor_id` INT NOT NULL,
    `hair_length` DECIMAL(5,2) NOT NULL,
    `hair_type` VARCHAR(50) NOT NULL,
    `image_url` VARCHAR(255) NOT NULL,
    `status` ENUM('Available', 'Processing', 'Donated') DEFAULT 'Available',
    FOREIGN KEY (`donor_id`) REFERENCES `donors`(`donor_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `post_id`
* **Foreign Key:** `donor_id` references `donors(donor_id)` with cascading deletion.
* **Functional Dependencies:** $\text{post\_id} \rightarrow \text{donor\_id, hair\_length, hair\_type, image\_url, status}$

### Table 6: `hair_requests` (Formal Allocation Transaction Records)
```sql
CREATE TABLE IF NOT EXISTS `hair_requests` (
    `request_id` INT AUTO_INCREMENT PRIMARY KEY,
    `patient_id` INT NOT NULL,
    `post_id` INT NOT NULL,
    `ngo_id` INT NOT NULL,
    `request_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `status` ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending',
    FOREIGN KEY (`patient_id`) REFERENCES `patients`(`patient_id`) ON DELETE CASCADE,
    FOREIGN KEY (`post_id`) REFERENCES `hair_donation_posts`(`post_id`) ON DELETE CASCADE,
    FOREIGN KEY (`ngo_id`) REFERENCES `ngos`(`ngo_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `request_id`
* **Foreign Keys:** 
  * `patient_id` references `patients(patient_id)` ON DELETE CASCADE
  * `post_id` references `hair_donation_posts(post_id)` ON DELETE CASCADE
  * `ngo_id` references `ngos(ngo_id)` ON DELETE CASCADE
* **Functional Dependencies:** $\text{request\_id} \rightarrow \text{patient\_id, post\_id, ngo\_id, request\_date, status}$

### Table 7: `campaigns` (Community Donation Drives & Outreach Events)
```sql
CREATE TABLE IF NOT EXISTS `campaigns` (
    `campaign_id` INT AUTO_INCREMENT PRIMARY KEY,
    `ngo_id` INT NOT NULL,
    `title` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `event_date` DATE NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`ngo_id`) REFERENCES `ngos`(`ngo_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `campaign_id`
* **Foreign Key:** `ngo_id` references `ngos(ngo_id)` ON DELETE CASCADE
* **Functional Dependencies:** $\text{campaign\_id} \rightarrow \text{ngo\_id, title, description, event\_date, location}$

### Table 8: `complaints` (Grievance Redressal & Support Tickets)
```sql
CREATE TABLE IF NOT EXISTS `complaints` (
    `complaint_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `subject` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `status` ENUM('Pending', 'Resolved') DEFAULT 'Pending',
    `date_submitted` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
* **Primary Key:** `complaint_id`
* **Foreign Key:** `login_id` references `login(login_id)` ON DELETE CASCADE
* **Functional Dependencies:** $\text{complaint\_id} \rightarrow \text{login\_id, subject, description, status, date\_submitted}$

---

## 13.5 NORMALIZATION PROOFS (1NF, 2NF, 3NF)

### 1. First Normal Form (1NF) Justification
		*Mathematical Condition:* A relation $R$ is in 1NF if and only if every attribute domain contains only atomic, indivisible values, and there are no repeating groups or composite columns.
		*Application:*
		In `hair_donation_posts`, `hair_length` contains single scalar decimal values, `hair_type` stores unitary strings (`Straight`, `Wavy`, `Curly`), and `image_url` stores single file system path strings. There are no comma-delimited arrays or nested repeating records. Similarly, `address` in `donors` and `patients` stores atomic text blocks. Hence, all eight tables rigorously satisfy **1NF**.

### 2. Second Normal Form (2NF) Justification
		*Mathematical Condition:* A relation $R$ is in 2NF if it is in 1NF and no non-prime attribute is partially dependent on any candidate key of $R$. (i.e., all non-prime attributes must be fully functionally dependent on the entire primary key).
		*Application:*
		Every table in the HairFidence schema uses a single-column, surrogate primary key generated via `AUTO_INCREMENT` (`login_id`, `donor_id`, `patient_id`, `ngo_id`, `post_id`, `request_id`, `campaign_id`, `complaint_id`).
		Since the cardinality of every primary key is exactly one, no proper subset of any candidate key exists:
		$$\forall \text{ PK }, |\text{PK}| = 1 \implies \text{No proper subset } X \subset \text{PK exists such that } X \rightarrow Y$$
		Thus, partial functional dependencies are mathematically impossible in this schema. All relations strictly conform to **2NF**.

### 3. Third Normal Form (3NF) Justification
		*Mathematical Condition:* A relation $R$ is in 3NF if it is in 2NF and there exists no non-prime attribute that is transitively dependent on the primary key. Formally, for every non-trivial functional dependency $X \rightarrow A$:
		1. $X$ is a superkey, OR
		2. $A$ is a prime attribute (part of a candidate key).
		*Application:*
		Examine user credentials and role-specific profile data: If donor contact details were stored inside the `login` relation, an update anomaly would emerge where non-key attributes transitively depend on other non-key attributes:
		$$\text{login\_id} \rightarrow \text{donor\_id} \rightarrow \text{full\_name}$$
		HairFidence strictly eliminates transitive dependencies by isolating authentication data (`login`) from entity profiles (`donors`, `patients`, `ngos`). Each profile relation depends directly on its primary key and references `login` via an indexed foreign key.
		
		In `hair_requests`, the relation links `(patient_id, post_id, ngo_id)`. The status of the request depends directly on the transaction key `request_id`, not transitively on `patient_id` or `ngo_id`.
		Because every non-trivial functional dependency $X \rightarrow A$ has a superkey as its determinant $X$, transitive dependencies are completely eliminated. Therefore, the entire schema strictly achieves **Third Normal Form (3NF)**.
