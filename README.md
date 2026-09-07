# hairfidance

## HairFidence: Cancer Patient Hair Donation Management System

HairFidence is a centralized, role-governed web application designed to digitize and streamline the hair donation, clinical verification, and medical wig distribution lifecycle for cancer patients recovering from chemotherapy.

### Key Features
- **Role-Based Access Control (RBAC):** Distinct dashboards and security workflows for Administrator, Healthcare NGOs, Hair Donors, and Cancer Patients.
- **Pessimistic Concurrency Locking:** Enforces atomic database transactions with row-level locks (`SELECT ... FOR UPDATE`) to eliminate double-booking race conditions during hair requests.
- **Clinical Verification Pipeline:** Secure document upload enabling accredited NGOs to audit oncology diagnostic certificates remotely.
- **Real-Time Parcel Tracking:** Multi-stage visual pipeline tracking for donors (`Available` → `Processing` → `Donated`).
- **Normalized Relational Schema:** 8-table relational MySQL schema in Third Normal Form (3NF).

### Technology Stack
- **Backend:** PHP 8.2+ with PDO (PHP Data Objects)
- **Database:** MariaDB / MySQL with InnoDB engine
- **Frontend:** Semantic HTML5, Vanilla CSS3, JavaScript (ES6+)
- **Server:** Apache HTTP Server (XAMPP environment)

### Academic Thesis & Documentation
Full thesis documentation, UML designs, and SRS data are available in the `/documentation` directory.
