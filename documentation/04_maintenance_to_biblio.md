# CHAPTER 16: SYSTEM MAINTENANCE

## 16.1 CORRECTIVE MAINTENANCE PLAN
		Corrective maintenance encompasses the systematic identification, isolation, and rectification of software defects, runtime errors, or unexpected behaviors discovered during active production use. In HairFidence, corrective maintenance protocols focus on:
		* **Error Logging & Exception Monitoring:** PHP error logging is directed to dedicated, secure server log files (`error.log`) with display errors disabled (`display_errors = Off`) to prevent internal system path disclosure to end-users.
		* **Input Formatting Edge Cases:** Managing rare input anomalies, such as non-standard characters in donor names or addresses, by enforcing UTF-8 multibyte normalization (`mb_convert_encoding`) and enhanced input trimming.
		* **Mobile Viewport Anomalies:** Resolving minor CSS rendering discrepancies that manifest across newly released mobile browser versions, specifically regarding viewport orientation adjustments and modal dialog positioning.

## 16.2 ADAPTIVE MAINTENANCE PLAN
		Adaptive maintenance involves modifying the software platform to remain fully operational across evolving external computing environments, updated operating systems, and newer third-party software releases:
		* **PHP Engine Evolution:** Routine code auditing to maintain forward compatibility with upcoming PHP interpreter minor and major releases (e.g., transitions from PHP 8.2 to PHP 8.3 and 8.4), ensuring that deprecated syntax or standard library changes do not degrade runtime stability.
		* **DBMS Engine Updates:** Adjusting SQL syntax and indexing strategies to leverage newer optimization features in MySQL 8.0+ and MariaDB 10.5+, such as improved JSON querying capabilities or enhanced index compression algorithms.
		* **Web Standards & Browser Engine Compliance:** Periodic review of CSS and JavaScript APIs against updated W3C standards and modern browser security policies (such as evolving SameSite cookie attributes and Content Security Policies).

## 16.3 PERFECTIVE MAINTENANCE PLAN
		Perfective maintenance encompasses proactive enhancements, performance optimizations, and user experience refinements driven by user feedback and operational analytics:
		* **Catalog Search Performance:** Integrating client-side AJAX debounced search algorithms, enabling patients to filter hair donations by length, texture, and location instantly without triggering full page reloads.
		* **Interactive Data Visualizations:** Enhancing the Administrator and NGO dashboards with dynamic SVG and canvas charting libraries to graphically represent monthly hair donation growth and patient allocation trends.
		* **Multi-Lingual Support:** Introducing internationalization (i18n) localization layers to support Malayalam and Hindi, ensuring that patients and donors across diverse linguistic demographics can comfortably navigate the platform.

## 16.4 PREVENTIVE MAINTENANCE PLAN & DISASTER RECOVERY
		Preventive maintenance focuses on preemptive optimizations to prevent potential future failures, maintain high availability, and protect organizational data:
		* **Database Index Optimization:** Scheduling weekly automated maintenance scripts executing `OPTIMIZE TABLE` and `ANALYZE TABLE` across high-churn tables (`hair_donation_posts`, `hair_requests`, `complaints`) to defragment storage and recalculate query execution plans.
		* **Log Rotation & File Pruning:** Implementing automated cron scripts to compress and rotate server access logs and purge temporary upload artifacts older than 30 days.
		* **Automated Backup & Disaster Recovery (DR) Strategy:** 
		  1. *Daily Logical Dumps:* Executing daily automated `mysqldump` snapshots of the `hairfidence` database, encrypted via AES-256 and transferred to an off-site cloud storage bucket.
		  2. *Static Storage Synchronization:* Performing incremental daily backups of the `uploads/` directory to preserve patient medical summaries and donor photographs.
		  3. *Recovery Time Objective (RTO) & Recovery Point Objective (RPO):* The architecture guarantees an RTO of $< 2\text{ hours}$ and an RPO of $< 24\text{ hours}$ in the event of catastrophic server hardware failure.

---

# CHAPTER 17: FUTURE ENHANCEMENT

## 17.1 CROSS-PLATFORM MOBILE APPLICATIONS
		While the current web interface is fully responsive, future development will encompass dedicated native cross-platform mobile applications for Android and iOS engineered using **Flutter** or **React Native**. Native applications will provide direct access to smartphone camera hardware, allowing donors to capture calibrated hair specimen photos with automated length estimation markers and enabling cancer patients to scan medical documents with automated edge detection.

## 17.2 AUTOMATED POSTAL & LOGISTICS API INTEGRATION
		To fully eliminate donor tracking opacity, future releases will integrate third-party logistics APIs (such as India Post Speed Post API, DTDC, and Delhivery). Upon submitting a hair donation post, the system will automatically generate a prepaid shipping label with a scannable barcode. Real-time courier webhook events will dynamically update the donor's tracking dashboard as the physical parcel transitions from local post office dispatch to NGO facility arrival.

## 17.3 AI-POWERED VIRTUAL WIG AR SIMULATOR
		An Augmented Reality (AR) facial mapping module will be incorporated into the patient portal using WebGL, WebAssembly, and lightweight TensorFlow.js computer vision models. Patients will be able to preview how various medical wig styles, colors, cuts, and hair volumes look on their own face in real-time through their device camera before submitting a request. This will provide emotional reassurance and personalization.

## 17.4 PHILANTHROPIC MICRO-SPONSORSHIP GATEWAY
		While donated natural hair is free, the specialized chemical cleaning, hygiene sanitization, and artisanal hand-knotting of medical wigs incur costs ranging from ₹2,500 to ₹5,000 per prosthesis. Future enhancements will integrate secure payment gateways (e.g., Razorpay, Stripe) allowing civic donors and corporate social responsibility (CSR) bodies to financially sponsor the crafting costs of specific wigs for underprivileged oncology patients.

## 17.5 MULTI-CHANNEL NOTIFICATION WEBHOOKS
		Integrating cloud messaging gateways (such as Twilio and Gupshup) will enable automated milestone SMS and WhatsApp alerts. Donors will receive instant notifications when their physical hair parcel is received by the NGO, when it passes clinical inspection, and the moment it is dispatched to a cancer survivor, strengthening community trust.

---

# CHAPTER 18: CONCLUSION

## 18.1 SUMMARY OF PROJECT ACHIEVEMENTS
		The development and operational validation of **HairFidence: Cancer Patient Hair Donation Management System** represent a meaningful technological achievement in modernizing humanitarian healthcare logistics. By replacing informal, untracked, and error-prone manual donation practices with a secure, role-governed 3-Tier MVC web platform, this project establishes a transparent, accountable bridge connecting altruistic donors, verified healthcare NGOs, and cancer patients recovering from chemotherapy.
		
		The system successfully digitizes the end-to-end hair donation lifecycle. It empowers donors with real-time multi-stage pipeline tracking, equips healthcare NGOs with auditable verification and campaign tools, and provides cancer survivors with an accessible, dignified portal to receive customized cranial medical prostheses at zero financial cost.

## 18.2 VALIDATION OF CORE OBJECTIVES
		All foundational technical and architectural objectives established during system inception were verified through comprehensive testing:
		* **Concurrency Safety:** The implementation of **Pessimistic Concurrency Locking (`SELECT ... FOR UPDATE`)** inside atomic PDO transactions completely eliminates race conditions and resource double-booking.
		* **Data Security & Privacy:** Cryptographic BCrypt password hashing, zero-trust RBAC middleware, and strict document path isolation ensure that sensitive patient oncology summaries remain protected against unauthorized access.
		* **Database Integrity:** The relational schema rigorously satisfies **Third Normal Form (3NF)**, guaranteeing zero insertion, update, or deletion anomalies across all eight entity relations.
		* **Operational Usability:** Intuitive responsive design guarantees flawless rendering across desktop, tablet, and mobile environments.

## 18.3 ACADEMIC & ENGINEERING CONCLUSION
		Ultimately, HairFidence stands as a testament to how sound software engineering principles, robust relational database design, and human-centered empathy can unite to solve poignant societal challenges. The platform establishes an enduring, scalable model for humanitarian healthcare charity management—one that is transparent, technically sound, and dedicated to restoring dignity, confidence, and comfort to cancer survivors throughout their journey to recovery.

---

# CHAPTER 19: APPENDIX

## APPENDIX A: COMPLETE DATABASE DDL SQL SCRIPT (`database.sql`)
```sql
-- Database Schema for HairFidence Management System
CREATE DATABASE IF NOT EXISTS `hairfidence`;
USE `hairfidence`;

-- Drop existing tables to guarantee clean rebuild
DROP TABLE IF EXISTS `complaints`;
DROP TABLE IF EXISTS `campaigns`;
DROP TABLE IF EXISTS `hair_requests`;
DROP TABLE IF EXISTS `hair_donation_posts`;
DROP TABLE IF EXISTS `ngos`;
DROP TABLE IF EXISTS `patients`;
DROP TABLE IF EXISTS `donors`;
DROP TABLE IF EXISTS `login`;

-- 1. Login Table (Authentication & Identity)
CREATE TABLE IF NOT EXISTS `login` (
    `login_id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(150) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `role` ENUM('admin', 'ngo', 'donor', 'patient') NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Donors Table (Donor Profiles)
CREATE TABLE IF NOT EXISTS `donors` (
    `donor_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL,
    `address` TEXT NOT NULL,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Patients Table (Cancer Patient Clinical Profiles)
CREATE TABLE IF NOT EXISTS `patients` (
    `patient_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL,
    `address` TEXT NOT NULL,
    `medical_report_url` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. NGOs Table (Accredited Healthcare Non-Profits)
CREATE TABLE IF NOT EXISTS `ngos` (
    `ngo_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `organization_name` VARCHAR(150) NOT NULL,
    `registration_number` VARCHAR(100) NOT NULL,
    `is_approved` TINYINT(1) DEFAULT 0,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Hair Donation Posts Table (Inventory Catalog)
CREATE TABLE IF NOT EXISTS `hair_donation_posts` (
    `post_id` INT AUTO_INCREMENT PRIMARY KEY,
    `donor_id` INT NOT NULL,
    `hair_length` DECIMAL(5,2) NOT NULL,
    `hair_type` VARCHAR(50) NOT NULL,
    `image_url` VARCHAR(255) NOT NULL,
    `status` ENUM('Available', 'Processing', 'Donated') DEFAULT 'Available',
    FOREIGN KEY (`donor_id`) REFERENCES `donors`(`donor_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. Hair Requests Table (Allocation Transactions)
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

-- 7. Campaigns Table (Community Donation Drives)
CREATE TABLE IF NOT EXISTS `campaigns` (
    `campaign_id` INT AUTO_INCREMENT PRIMARY KEY,
    `ngo_id` INT NOT NULL,
    `title` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `event_date` DATE NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`ngo_id`) REFERENCES `ngos`(`ngo_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8. Complaints Table (Grievance Redressal Tickets)
CREATE TABLE IF NOT EXISTS `complaints` (
    `complaint_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `subject` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `status` ENUM('Pending', 'Resolved') DEFAULT 'Pending',
    `date_submitted` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed Default Administrator Account
INSERT INTO `login` (`login_id`, `email`, `password`, `role`)
VALUES (1, 'admin@hairfidence.com', '$2y$10$fSVaG3kV8s//9BkYqmTF/OvKFvnjj/pNYbm4TOikDewu876fnrile', 'admin')
ON DUPLICATE KEY UPDATE `email` = `email`;
```

---

## APPENDIX B: CORE ARCHITECTURAL CODE FILES

### Database Connection Handler (`config/db.php`)
```php
<?php
// config/db.php - Centralized PDO Database Connection
$host    = 'localhost';
$db      = 'hairfidence';
$user    = 'root';
$pass    = ''; // Local development password
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    error_log("Database connection failure: " . $e->getMessage());
    die("Database connection failed. Please ensure MariaDB is running in XAMPP.");
}
?>
```

### Role-Based Access Control Middleware (`includes/auth_check.php`)
```php
<?php
// includes/auth_check.php - RBAC Guard Middleware
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

function check_access($allowed_roles) {
    if (!isset($_SESSION['login_id']) || !isset($_SESSION['role'])) {
        header("Location: ../login.php?error=Session+Expired");
        exit();
    }
    
    $role = $_SESSION['role'];
    $allowed = is_array($allowed_roles) ? in_array($role, $allowed_roles, true) : ($role === $allowed_roles);
    
    if (!$allowed) {
        header("Location: ../login.php?error=Unauthorized+Access+Forbidden");
        exit();
    }
}
?>
```

---

## APPENDIX C: SYSTEM DATA DICTIONARY

| Table Name | Field Name | Data Type | Nullable | Key | Default Value | Description |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `login` | `login_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique identifier for authentication credentials. |
| `login` | `email` | `VARCHAR(150)` | No | UNI | None | Unique electronic mail address. |
| `login` | `password` | `VARCHAR(255)` | No | | None | BCrypt cryptographic password hash. |
| `login` | `role` | `ENUM` | No | | None | User classification: `'admin'/'ngo'/'donor'/'patient'`. |
| `login` | `created_at` | `TIMESTAMP` | Yes | | `CURRENT_TIMESTAMP` | Account creation timestamp. |
| `donors` | `donor_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique donor profile key. |
| `donors` | `login_id` | `INT` | No | FK | None | References `login(login_id)` ON DELETE CASCADE. |
| `donors` | `full_name` | `VARCHAR(100)` | No | | None | Legal name of donor. |
| `donors` | `phone` | `VARCHAR(15)` | No | | None | Contact telephone number. |
| `donors` | `address` | `TEXT` | No | | None | Postal dispatch address. |
| `patients` | `patient_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique patient profile key. |
| `patients` | `login_id` | `INT` | No | FK | None | References `login(login_id)` ON DELETE CASCADE. |
| `patients` | `full_name` | `VARCHAR(100)` | No | | None | Legal name of patient. |
| `patients` | `phone` | `VARCHAR(15)` | No | | None | Contact telephone number. |
| `patients` | `address` | `TEXT` | No | | None | Delivery residential address. |
| `patients` | `medical_report_url` | `VARCHAR(255)` | No | | None | Relative server path to diagnostic report file. |
| `ngos` | `ngo_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique NGO profile key. |
| `ngos` | `login_id` | `INT` | No | FK | None | References `login(login_id)` ON DELETE CASCADE. |
| `ngos` | `organization_name`| `VARCHAR(150)` | No | | None | Registered name of healthcare charity. |
| `ngos` | `registration_number`| `VARCHAR(100)` | No | | None | Statutory registration number. |
| `ngos` | `is_approved` | `TINYINT(1)` | Yes | | `0` | Administrative accreditation status (0/1). |
| `hair_donation_posts`| `post_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique hair post inventory key. |
| `hair_donation_posts`| `donor_id` | `INT` | No | FK | None | References `donors(donor_id)` ON DELETE CASCADE. |
| `hair_donation_posts`| `hair_length` | `DECIMAL(5,2)`| No | | None | Hair measurement in inches. |
| `hair_donation_posts`| `hair_type` | `VARCHAR(50)` | No | | None | Hair texture (Straight/Wavy/Curly). |
| `hair_donation_posts`| `image_url` | `VARCHAR(255)` | No | | None | Server path to specimen photograph. |
| `hair_donation_posts`| `status` | `ENUM` | Yes | | `'Available'` | Status: `'Available'/'Processing'/'Donated'`. |
| `hair_requests` | `request_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique request transaction key. |
| `hair_requests` | `patient_id` | `INT` | No | FK | None | References `patients(patient_id)` ON DELETE CASCADE. |
| `hair_requests` | `post_id` | `INT` | No | FK | None | References `hair_donation_posts(post_id)` ON DELETE CASCADE. |
| `hair_requests` | `ngo_id` | `INT` | No | FK | None | References `ngos(ngo_id)` ON DELETE CASCADE. |
| `hair_requests` | `request_date`| `TIMESTAMP` | Yes | | `CURRENT_TIMESTAMP` | Date and time request was initiated. |
| `hair_requests` | `status` | `ENUM` | Yes | | `'Pending'` | Status: `'Pending'/'Approved'/'Rejected'`. |
| `campaigns` | `campaign_id` | `INT` | No | PK | `AUTO_INCREMENT` | Unique campaign event key. |
| `campaigns` | `ngo_id` | `INT` | No | FK | None | References `ngos(ngo_id)` ON DELETE CASCADE. |
| `campaigns` | `title` | `VARCHAR(150)` | No | | None | Title of donation drive. |
| `campaigns` | `description`| `TEXT` | No | | None | Guidelines and event details. |
| `campaigns` | `event_date` | `DATE` | No | | None | Scheduled calendar date of drive. |
| `campaigns` | `location` | `VARCHAR(255)` | No | | None | Physical venue address. |
| `complaints` | `complaint_id`| `INT` | No | PK | `AUTO_INCREMENT` | Unique support ticket key. |
| `complaints` | `login_id` | `INT` | No | FK | None | References `login(login_id)` ON DELETE CASCADE. |
| `complaints` | `subject` | `VARCHAR(150)` | No | | None | Grievance subject summary. |
| `complaints` | `description`| `TEXT` | No | | None | Detailed grievance description. |
| `complaints` | `status` | `ENUM` | Yes | | `'Pending'` | Ticket status: `'Pending'/'Resolved'`. |
| `complaints` | `date_submitted`| `TIMESTAMP`| Yes | | `CURRENT_TIMESTAMP` | Timestamp of ticket submission. |

---

# CHAPTER 20: BIBLIOGRAPHY

## TECHNICAL REFERENCE BOOKS
[1] *Software Engineering: A Practitioner's Approach*, Roger S. Pressman and Bruce R. Maxim, 8th Edition, McGraw-Hill Education, 2015.  
[2] *Fundamentals of Database Systems*, Ramez Elmasri and Shamkant B. Navathe, 7th Edition, Pearson Education, 2016.  
[3] *PHP and MySQL Web Development*, Luke Welling and Laura Thomson, 5th Edition, Addison-Wesley Professional, 2017.  
[4] *UML Distilled: A Brief Guide to the Standard Object Modeling Language*, Martin Fowler, 3rd Edition, Addison-Wesley Professional, 2004.  
[5] *Design Patterns: Elements of Reusable Object-Oriented Software*, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, 1st Edition, Addison-Wesley Professional, 1994.  
[6] *Software Engineering*, Ian Sommerville, 10th Edition, Pearson Education, 2016.  

## AUTHORITATIVE DOCUMENTATION & WEB REFERENCES
[1] PHP Documentation Group, *PHP: Hypertext Preprocessor Official Reference Manual*, Available online: https://www.php.net/manual/en/ (Accessed: June 2026).  
[2] Oracle Corporation, *MySQL 8.0 Reference Manual: InnoDB Storage Engine & Locking Models*, Available online: https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html (Accessed: June 2026).  
[3] Mozilla Developer Network (MDN), *Web Technology for Developers: Semantic HTML5 and CSS Flexible Box Layout*, Available online: https://developer.mozilla.org/en-US/docs/Web (Accessed: May 2026).  
[4] Open Web Application Security Project (OWASP), *OWASP Top 10: The Ten Most Critical Web Application Security Risks*, Available online: https://owasp.org/Top10/ (Accessed: May 2026).  
[5] Apache Friends, *XAMPP Apache + MariaDB + PHP + Perl Distribution Documentation*, Available online: https://www.apachefriends.org/ (Accessed: April 2026).  
[6] APJ Abdul Kalam Technological University, *Master of Computer Applications Curriculum, Scheme and Syllabi (2020 Scheme)*, Government of Kerala, Available online: https://ktu.edu.in/ (Accessed: July 2026).  
