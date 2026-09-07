# CHAPTER 14: SYSTEM DEVELOPMENT

## 14.1 SUBSYSTEM MODULAR BREAKDOWN
		The codebase of HairFidence is logically partitioned into discrete, decoupled directory subsystems. Each subsystem encapsulates specific operational responsibilities, guaranteeing high cohesion and loose coupling:

```
MINI_PROJECT/
|-- config/
|   `-- db.php                         # Core Database Engine (PDO DSN, Connection Options)
|-- includes/
|   `-- auth_check.php                 # Role-Based Access Control (RBAC) Middleware Guard
|-- auth/
|   |-- dashboard_redirect.php         # Session Router (Directs user to role dashboard)
|   `-- logout.php                     # Secure Session Invalidation & Destruction
|-- admin/
|   `-- dashboard.php                  # System Governance, NGO Vetting, Complaint Redressal
|-- ngo/
|   `-- dashboard.php                  # NGO Operations, Hair Verification, Medical Report Audits
|-- donor/
|   `-- dashboard.php                  # Donation Post Authoring, Live Pipeline Tracker
|-- patient/
|   `-- dashboard.php                  # Hair Catalog, Medical Report Upload, Atomic Request Lock
|-- uploads/
|   |-- hair_photos/                   # File system partition for Donor Specimen Photos
|   `-- medical_reports/               # Isolated storage partition for Diagnostic Records
|-- index.php                          # Public Landing & Informational Healthcare Portal
|-- login.php                          # Unified Authentication Console
|-- register.php                       # Multi-Role Account Creation Interface
`-- database.sql                       # DDL Schema, Foreign Key Constraints & Seed Records
```

* **`config/` (System Configuration):** Contains `db.php`, which instantiates a centralized `PDO` database handle using strict error handling options (`PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`) and disabled prepared statement emulation (`PDO::ATTR_EMULATE_PREPARES => false`).
* **`includes/` (Reusable Middleware):** Contains `auth_check.php`, providing the `check_access($allowed_roles)` function to enforce Role-Based Access Control (RBAC) prior to rendering protected consoles.
* **`auth/` (Session Management):** Houses `dashboard_redirect.php` for multiplexing users to their role-specific consoles post-authentication, and `logout.php` for destroying session variables and flushing cookies.
* **`admin/` (Governance Subsystem):** Contains `dashboard.php`, providing global platform statistics, NGO registration vetting consoles, user monitoring, and grievance ticket resolution mechanisms.
* **`ngo/` (Intermediary Subsystem):** Houses `dashboard.php`, enabling accredited healthcare NGOs to inspect physical hair parcels, audit patient diagnostic oncology summaries, approve/reject requests, and publish community donation campaigns.
* **`donor/` (Donor Subsystem):** Contains `dashboard.php`, providing hair contribution authoring forms (with photo upload), multi-stage pipeline status visualizations, and support ticket filing.
* **`patient/` (Beneficiary Subsystem):** Houses `dashboard.php`, enabling cancer patients to securely upload medical certificates, browse available hair donations with attribute filters, and submit concurrency-safe allocation requests.
* **`uploads/` (Static Media Storage):** An isolated file system repository partitioned into `hair_photos/` and `medical_reports/` with restricted script execution policies.

---

## 14.2 CORE ALGORITHMS & BUSINESS LOGIC IMPLEMENTATION

### Algorithm 1: Pessimistic Concurrency Locking on Hair Requests
		When multiple cancer patients browse the public catalog simultaneously, there exists an acute risk of a race condition where two patients submit requests for the identical hair post at the exact same millisecond. To prevent resource contention and double-booking, the system executes an **Atomic Database Transaction with Pessimistic Row Locking (`SELECT ... FOR UPDATE`)**:

```php
// Business Logic Extract from patient/dashboard.php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['request_hair'])) {
    $post_id = intval($_POST['post_id']);
    $ngo_id  = intval($_POST['ngo_id']);

    if (empty($post_id) || empty($ngo_id)) {
        $error_msg = "Please select an accredited NGO to verify your request.";
    } else {
        try {
            // Step 1: Initiate Atomic Database Transaction
            $pdo->beginTransaction();

            // Step 2: Acquire Exclusive Pessimistic Write Lock on the Target Tuple
            $check_stmt = $pdo->prepare("SELECT status FROM hair_donation_posts WHERE post_id = ? FOR UPDATE");
            $check_stmt->execute([$post_id]);
            $current_status = $check_stmt->fetchColumn();

            // Step 3: Validate State Precondition
            if ($current_status !== 'Available') {
                throw new Exception("Conflict: This hair specimen has already been requested by another patient.");
            }

            // Step 4: Insert Transaction Record into `hair_requests`
            $stmt = $pdo->prepare("INSERT INTO hair_requests (patient_id, post_id, ngo_id, status) VALUES (?, ?, ?, 'Pending')");
            $stmt->execute([$patient_id, $post_id, $ngo_id]);

            // Step 5: Transition Post State to 'Processing' (Locking out other patients)
            $lock_stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Processing' WHERE post_id = ?");
            $lock_stmt->execute([$post_id]);

            // Step 6: Commit Transaction & Release Lock
            $pdo->commit();
            $success_msg = "Request submitted successfully. The hair post has been locked for NGO verification.";
        } catch (Exception $e) {
            // Rollback on any failure to preserve ACID consistency
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            $error_msg = $e->getMessage();
        }
    }
}
```

### Algorithm 2: Cryptographic Password Verification & Role Session Multiplexing
		User authentication is executed against the `login` relation. Passwords are encrypted via the industry-standard **BCrypt algorithm**. In addition, the system enforces gated access control for NGO accounts:

```php
// Business Logic Extract from login.php
$stmt = $pdo->prepare("SELECT * FROM login WHERE email = ?");
$stmt->execute([$email]);
$user = $stmt->fetch();

if ($user && password_verify($password, $user['password'])) {
    $role = $user['role'];
    $is_approved_ngo = true;
    $profile_data = [];

    // Role-specific identity retrieval
    if ($role === 'donor') {
        $stmt = $pdo->prepare("SELECT donor_id, full_name FROM donors WHERE login_id = ?");
        $stmt->execute([$user['login_id']]);
        $profile_data = $stmt->fetch();
    } elseif ($role === 'patient') {
        $stmt = $pdo->prepare("SELECT patient_id, full_name FROM patients WHERE login_id = ?");
        $stmt->execute([$user['login_id']]);
        $profile_data = $stmt->fetch();
    } elseif ($role === 'ngo') {
        $stmt = $pdo->prepare("SELECT ngo_id, organization_name, is_approved FROM ngos WHERE login_id = ?");
        $stmt->execute([$user['login_id']]);
        $profile_data = $stmt->fetch();
        
        // Enforce administrative gatekeeping
        if ($profile_data && (int)$profile_data['is_approved'] !== 1) {
            $is_approved_ngo = false;
        }
    }

    if (!$is_approved_ngo) {
        $error = "Access Denied: Your NGO registration is pending administrative approval.";
    } else {
        // Instantiate authenticated session
        $_SESSION['login_id'] = $user['login_id'];
        $_SESSION['email']    = $user['email'];
        $_SESSION['role']     = $role;
        $_SESSION['name']     = $profile_data['full_name'] ?? $profile_data['organization_name'] ?? 'Admin';
        if ($role === 'donor')   $_SESSION['donor_id']   = $profile_data['donor_id'];
        if ($role === 'patient') $_SESSION['patient_id'] = $profile_data['patient_id'];
        if ($role === 'ngo')     $_SESSION['ngo_id']     = $profile_data['ngo_id'];

        header("Location: auth/dashboard_redirect.php");
        exit();
    }
} else {
    $error = "Invalid electronic mail or password credentials.";
}
```

### Algorithm 3: Zero-Trust Access Middleware (`includes/auth_check.php`)
		Enforces role boundaries across protected endpoints, preventing unauthorized horizontal or vertical privilege escalation:

```php
// Middleware implementation in includes/auth_check.php
function check_access($allowed_roles) {
    if (!isset($_SESSION['login_id']) || !isset($_SESSION['role'])) {
        header("Location: ../login.php?error=Please+Login+First");
        exit();
    }
    
    $role = $_SESSION['role'];
    $allowed = is_array($allowed_roles) ? in_array($role, $allowed_roles, true) : ($role === $allowed_roles);
    
    if (!$allowed) {
        header("Location: ../login.php?error=Unauthorized+Access+Forbidden");
        exit();
    }
}
```

### Algorithm 4: Secure File Upload & Extension Verification Pipeline
		Protects against remote script execution vulnerabilities by validating file extensions, sanitizing file names, and generating unguessable timestamps:

```php
// File Upload Logic from donor/dashboard.php
$file_name = $_FILES['hair_photo']['name'];
$file_tmp  = $_FILES['hair_photo']['tmp_name'];
$file_ext  = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
$allowed_exts = ['jpg', 'jpeg', 'png'];

if (!in_array($file_ext, $allowed_exts, true)) {
    throw new Exception("Security Alert: Invalid image file format. Only JPG, JPEG, and PNG are permitted.");
}

$upload_dir = '../uploads/hair_photos/';
if (!is_dir($upload_dir)) {
    mkdir($upload_dir, 0777, true);
}

// Generate collision-resistant unique file identifier
$new_file_name = 'hair_' . $donor_id . '_' . time() . '.' . $file_ext;
$dest_path     = $upload_dir . $new_file_name;
$db_path       = 'uploads/hair_photos/' . $new_file_name;

if (!move_uploaded_file($file_tmp, $dest_path)) {
    throw new Exception("File System Error: Failed to write uploaded photograph to disk.");
}
```

---

## 14.3 ROUTING & ENDPOINTS SPECIFICATION
		HairFidence implements structured, modular routing based on HTTP methods and clean endpoint paths:

| Endpoint Route | HTTP Method | Permitted Role | Functional Controller Responsibility |
| :--- | :---: | :---: | :--- |
| `/index.php` | `GET` | Public | Renders public landing portal, mission statements, and NGO drive notices. |
| `/login.php` | `GET` / `POST` | Public | Authenticates credentials, validates BCrypt hash, sets session markers. |
| `/register.php` | `GET` / `POST` | Public | Registers Donor, Patient, or NGO accounts within an atomic transaction. |
| `/auth/dashboard_redirect.php`| `GET` | Authenticated | Evaluates `$_SESSION['role']` and dispatches browser to correct dashboard. |
| `/auth/logout.php` | `GET` | Authenticated | Clears `$_SESSION` array, invalidates cookie, bounces to `/login.php`. |
| `/admin/dashboard.php` | `GET` / `POST` | Admin | Aggregates stats, approves/rejects NGOs, resolves complaint tickets. |
| `/ngo/dashboard.php` | `GET` / `POST` | Approved NGO | Audits clinical reports, verifies hair donations, publishes campaigns. |
| `/donor/dashboard.php` | `GET` / `POST` | Donor | Authors hair donation posts, tracks multi-stage pipeline, logs complaints. |
| `/patient/dashboard.php`| `GET` / `POST` | Patient | Uploads oncology report, searches catalog, submits concurrency-locked requests. |

---

## 14.4 INPUT VALIDATION & SECURITY LAYERS

### 1. SQL Injection Prevention via Parameterized Queries
		All interactions with MariaDB/MySQL are mediated through `PDO::prepare()` statements. No user input is ever concatenated directly into SQL query strings:
```php
// Strictly immunized against SQL Injection
$stmt = $pdo->prepare("SELECT * FROM hair_donation_posts WHERE hair_length >= ? AND hair_type = ?");
$stmt->execute([$min_length, $selected_type]);
```

### 2. Cross-Site Scripting (XSS) Prevention
		All dynamic variables interpolated into HTML elements are escaped using `htmlspecialchars()` with strict flags:
```php
// Escaping HTML entities prior to DOM insertion
echo htmlspecialchars($donor['full_name'], ENT_QUOTES, 'UTF-8');
```

---

# CHAPTER 15: SYSTEM TESTING AND IMPLEMENTATION

## 15.1 TESTING METHODOLOGIES APPLIED
		Quality assurance for HairFidence was executed across a structured five-tier testing framework:
		1. **Unit Testing:** Evaluated individual algorithmic functions in isolation, including BCrypt hashing correctness, session authentication guards, mathematical hair length validators, and file upload extension parsers.
		2. **Integration Testing:** Verified seamless data interchange between distinct modules (e.g., verifying that creating a donor post immediately displays in the patient catalog, and requesting the post immediately updates the donor's pipeline tracking view).
		3. **Black Box Functional Testing:** Systematically tested user interfaces against functional requirements without inspecting internal source code routines.
		4. **White Box Structural Testing:** Conducted statement and branch coverage testing on PHP scripts, verifying that database failure exceptions trigger rollbacks and that foreign key cascades maintain referential integrity upon tuple deletions.
		5. **User Acceptance Testing (UAT):** Simulated operational trials involving test users representing donors, hospital NGO personnel, and oncology patients to evaluate usability and workflow clarity.

---

## 15.2 COMPREHENSIVE TEST SUITE TABLE

| Test ID | Test Scenario | Test Input Data | Expected Output | Actual Result Observed | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | User Authentication with Valid Credentials | Email: `admin@hairfidence.com`<br>Pass: `adminpassword` | Successful authentication; session instantiated; redirected to `admin/dashboard.php`. | Authenticated successfully; redirected to Administrator console. | **PASS** |
| **TC-02** | User Authentication with Invalid Password | Email: `admin@hairfidence.com`<br>Pass: `incorrect123` | Rejection; zero session variables created; display "Invalid credentials" error banner. | Access denied; error message displayed; returned to login form. | **PASS** |
| **TC-03** | NGO Authentication Prior to Admin Approval | Email: `contact@hopecharity.org`<br>Status: `is_approved = 0` | Intercept login; refuse dashboard access; display "Pending administrative verification". | Login halted; explicit verification warning banner displayed. | **PASS** |
| **TC-04** | Role-Based Access Traversal Protection | Direct URL access to `admin/dashboard.php` with an active Donor session | Intercept request via `check_access()`; redirect to login with "Unauthorized Access". | HTTP 302 redirect triggered; bounced to login; incident logged. | **PASS** |
| **TC-05** | Hair Donation Post Authoring | Length: `12.50`, Type: `Wavy`, Photo: `specimen.jpg` | Record inserted into `hair_donation_posts`; post status automatically set to `'Available'`. | Tuple inserted into database; post visible in catalog. | **PASS** |
| **TC-06** | Concurrency Lock & Double-Booking Prevention | Two concurrent sessions submit request for Post ID `#104` simultaneously | First request succeeds and acquires row lock; second request caught by exception and rolled back. | Session A receives success confirmation; Session B receives "Conflict: Already requested". | **PASS** |
| **TC-07** | Diagnostic Medical Report File Upload | File: `oncology_summary.pdf`<br>Size: `1.8 MB` | File validated, stored in `uploads/medical_reports/`, URL saved in `patients` table. | File written to disk; database record updated; viewable by NGO. | **PASS** |
| **TC-08** | Disallowed File Extension Rejection | File: `malicious_script.exe`<br>MIME: `application/x-msdownload` | Validation failure; upload blocked; throw "Invalid file type" exception. | Upload rejected; zero disk write; error alert rendered. | **PASS** |
| **TC-09** | NGO Request Rejection Asset Unlock | NGO clicks `Reject Request` on Request ID `#35` | `hair_requests` status becomes `'Rejected'`; associated hair post status resets to `'Available'`. | Request marked rejected; post reappears as Available in catalog. | **PASS** |
| **TC-10** | Grievance Ticket Submission & Resolution | Subject: "Address Update", Desc: "Relocated to ward 5" | Complaint logged with status `'Pending'`; Admin toggles status to `'Resolved'`. | Ticket logged; visible in Admin console; successfully marked Resolved. | **PASS** |

---

## 15.3 DEPLOYMENT & BUILD CONFIGURATION
		The implementation and deployment of HairFidence follows an automated local-to-cloud server deployment pipeline:

### Step 1: Web Server Stack Initialization
		The Apache HTTP Server 2.4 and MariaDB/MySQL database engines are initialized via the XAMPP Control Panel (or native systemd daemons on Ubuntu Linux).

### Step 2: Database Schema Migration
		The schema is imported by executing the DDL script `database.sql` through phpMyAdmin or the MySQL command line client:
```bash
mysql -u root -p hairfidence < database.sql
```

### Step 3: Directory Permissions & Storage Configuration
		File system permissions are configured to allow Apache write access to upload partitions while restricting executable script execution:
```bash
# Set directory permissions for secure upload partitions
chmod 755 c:/xampp/htdocs/MINI_PROJECT/
chmod 775 c:/xampp/htdocs/MINI_PROJECT/uploads/hair_photos/
chmod 775 c:/xampp/htdocs/MINI_PROJECT/uploads/medical_reports/
```

### Step 4: PHP Runtime Configuration Directives
		The server configuration (`php.ini`) is verified for the following directives:
```ini
file_uploads = On
upload_max_filesize = 10M
post_max_size = 12M
max_execution_time = 60
session.cookie_httponly = 1
session.use_only_cookies = 1
```

---

## 15.4 OPERATIONAL ENVIRONMENT VERIFICATION
		Following deployment, the system is subjected to operational verification:
		* **Database Connectivity Verification:** Invoking `config/db.php` confirms that PDO connects to MariaDB without error or credential leakage.
		* **Media Storage Verification:** Test file uploads confirm that image files are written to `uploads/hair_photos/` and PDF records to `uploads/medical_reports/`.
		* **Cross-Browser Smoke Testing:** The public portal and all four role dashboards are rendered across Google Chrome, Mozilla Firefox, and mobile viewports to verify visual fidelity and responsiveness.
