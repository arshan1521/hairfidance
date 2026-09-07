<?php
// register.php
require_once 'config/db.php';

$error = '';
$success = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email']);
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];
    $role = $_POST['role'];

    // Donor Specific Fields
    $donor_full_name = trim($_POST['donor_full_name'] ?? '');
    $donor_phone = trim($_POST['donor_phone'] ?? '');
    $donor_address = trim($_POST['donor_address'] ?? '');

    // Patient Specific Fields
    $patient_full_name = trim($_POST['patient_full_name'] ?? '');
    $patient_phone = trim($_POST['patient_phone'] ?? '');
    $patient_address = trim($_POST['patient_address'] ?? '');

    // NGO Specific Fields
    $org_name = trim($_POST['org_name'] ?? '');
    $reg_number = trim($_POST['reg_number'] ?? '');

    // Basic Validations
    if (empty($email) || empty($password) || empty($role)) {
        $error = "Please fill in all credentials.";
    } elseif ($password !== $confirm_password) {
        $error = "Passwords do not match.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        try {
            // Check if user already exists in Login table
            $stmt = $pdo->prepare("SELECT login_id FROM login WHERE email = ?");
            $stmt->execute([$email]);
            if ($stmt->fetch()) {
                $error = "Email is already registered.";
            } else {
                // Begin transaction to ensure database integrity
                $pdo->beginTransaction();

                // Hash password
                $password_hash = password_hash($password, PASSWORD_DEFAULT);

                // Insert into login table
                $stmt = $pdo->prepare("INSERT INTO login (email, password, role) VALUES (?, ?, ?)");
                $stmt->execute([$email, $password_hash, $role]);
                $login_id = $pdo->lastInsertId();

                // Role-specific inserts and file handling
                if ($role === 'donor') {
                    if (empty($donor_full_name) || empty($donor_phone) || empty($donor_address)) {
                        throw new Exception("Please fill all Donor profile fields.");
                    }
                    $stmt = $pdo->prepare("INSERT INTO donors (login_id, full_name, phone, address) VALUES (?, ?, ?, ?)");
                    $stmt->execute([$login_id, $donor_full_name, $donor_phone, $donor_address]);

                } elseif ($role === 'patient') {
                    if (empty($patient_full_name) || empty($patient_phone) || empty($patient_address) || empty($_FILES['medical_report']['name'])) {
                        throw new Exception("Please fill all Patient profile fields and upload medical report.");
                    }

                    // Handle File Upload
                    $file_name = $_FILES['medical_report']['name'];
                    $file_tmp = $_FILES['medical_report']['tmp_name'];
                    $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
                    $allowed_exts = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'];

                    if (!in_array($file_ext, $allowed_exts)) {
                        throw new Exception("Invalid medical report file type. Allowed: PDF, DOC, DOCX, JPG, PNG.");
                    }

                    // Create directory if not exists
                    $upload_dir = 'uploads/medical_reports/';
                    if (!is_dir($upload_dir)) {
                        mkdir($upload_dir, 0777, true);
                    }

                    // Generate unique file path
                    $new_file_name = 'report_' . $login_id . '_' . time() . '.' . $file_ext;
                    $dest_path = $upload_dir . $new_file_name;

                    if (!move_uploaded_file($file_tmp, $dest_path)) {
                        throw new Exception("Failed to upload medical report. Try again.");
                    }

                    // Insert into patients table (with medical_report_url)
                    $stmt = $pdo->prepare("INSERT INTO patients (login_id, full_name, phone, address, medical_report_url) VALUES (?, ?, ?, ?, ?)");
                    $stmt->execute([$login_id, $patient_full_name, $patient_phone, $patient_address, $dest_path]);

                } elseif ($role === 'ngo') {
                    if (empty($org_name) || empty($reg_number) || empty($_FILES['ngo_certificate']['name'])) {
                        throw new Exception("Please fill all NGO profile fields and upload your registration certificate.");
                    }

                    // Handle Certificate Upload
                    $file_name = $_FILES['ngo_certificate']['name'];
                    $file_tmp = $_FILES['ngo_certificate']['tmp_name'];
                    $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
                    $allowed_exts = ['pdf', 'jpg', 'jpeg', 'png'];

                    if (!in_array($file_ext, $allowed_exts)) {
                        throw new Exception("Invalid certificate type. Allowed: PDF, JPG, JPEG, PNG.");
                    }

                    // Create directory if not exists
                    $upload_dir = 'uploads/ngo_certificates/';
                    if (!is_dir($upload_dir)) {
                        mkdir($upload_dir, 0777, true);
                    }

                    $new_file_name = 'certificate_' . $login_id . '_' . time() . '.' . $file_ext;
                    $dest_path = $upload_dir . $new_file_name;

                    if (!move_uploaded_file($file_tmp, $dest_path)) {
                        throw new Exception("Failed to upload NGO certificate. Try again.");
                    }

                    // Insert NGO record (Pending approval is_approved = 0)
                    $stmt = $pdo->prepare("INSERT INTO ngos (login_id, organization_name, registration_number, is_approved) VALUES (?, ?, ?, 0)");
                    $stmt->execute([$login_id, $org_name, $reg_number]);
                }

                // Commit transaction if all inserts succeed
                $pdo->commit();
                $success = "Registration successful! You can now log in.";
            }
        } catch (Exception $e) {
            // Roll back changes if any query or file upload fails
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            $error = $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - HairFidence</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<header>
    <div class="nav-container">
        <a href="index.php" class="logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: var(--secondary)">
                <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/>
                <path d="M12 6v12M6 12h12"/>
            </svg>
            HairFidence
        </a>
        <ul class="nav-links">
            <li><a href="index.php" class="nav-item">Home</a></li>
            <li><a href="login.php" class="nav-item">Login</a></li>
            <li><a href="register.php" class="nav-item active btn btn-primary" style="color: white; padding: 0.5rem 1rem;">Register</a></li>
        </ul>
    </div>
</header>

<main class="container">
    <div class="auth-container glass-card animate-fade-in">
        <div class="auth-header">
            <h2>Join HairFidence</h2>
            <p>Create your account and make a difference today</p>
        </div>

        <?php if (!empty($error)): ?>
            <div class="alert alert-danger">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
                <?php echo htmlspecialchars($error); ?>
            </div>
        <?php endif; ?>

        <?php if (!empty($success)): ?>
            <div class="alert alert-success">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                <?php echo htmlspecialchars($success); ?>
            </div>
        <?php endif; ?>

        <form id="register_form" action="register.php" method="POST" enctype="multipart/form-data">
            <!-- Account Credentials -->
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email" required value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" class="form-control" placeholder="Create a password" required>
            </div>

            <div class="form-group">
                <label for="confirm_password">Confirm Password</label>
                <input type="password" id="confirm_password" name="confirm_password" class="form-control" placeholder="Repeat password" required>
            </div>

            <div class="form-group">
                <label for="register_role">Select Your Role</label>
                <select id="register_role" name="role" class="form-control form-select" required>
                    <option value="" disabled selected>-- Choose your role --</option>
                    <option value="donor" <?php echo (isset($_POST['role']) && $_POST['role'] === 'donor') ? 'selected' : ''; ?>>Hair Donor</option>
                    <option value="patient" <?php echo (isset($_POST['role']) && $_POST['role'] === 'patient') ? 'selected' : ''; ?>>Cancer Patient / Wig Requestor</option>
                    <option value="ngo" <?php echo (isset($_POST['role']) && $_POST['role'] === 'ngo') ? 'selected' : ''; ?>>Non-Governmental Org (NGO)</option>
                </select>
            </div>

            <!-- Donor Specific Fields -->
            <div id="donor_fields" style="display: none;">
                <h3 style="font-size: 1.2rem; margin: 1.5rem 0 1rem 0; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Donor Details</h3>
                <div class="form-group">
                    <label for="donor_name">Full Name</label>
                    <input type="text" id="donor_name" name="donor_full_name" class="form-control" placeholder="John Doe" value="<?php echo htmlspecialchars($_POST['donor_full_name'] ?? ''); ?>">
                </div>
                <div class="form-group">
                    <label for="donor_phone">Phone Number</label>
                    <input type="tel" id="donor_phone" name="donor_phone" class="form-control" placeholder="9876543210" value="<?php echo htmlspecialchars($_POST['donor_phone'] ?? ''); ?>">
                </div>
                <div class="form-group">
                    <label for="donor_address">Address</label>
                    <textarea id="donor_address" name="donor_address" class="form-control" placeholder="Your residential address"><?php echo htmlspecialchars($_POST['donor_address'] ?? ''); ?></textarea>
                </div>
            </div>

            <!-- Patient Specific Fields -->
            <div id="patient_fields" style="display: none;">
                <h3 style="font-size: 1.2rem; margin: 1.5rem 0 1rem 0; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Patient Details</h3>
                <div class="form-group">
                    <label for="patient_name">Full Name</label>
                    <input type="text" id="patient_name" name="patient_full_name" class="form-control" placeholder="Jane Doe" value="<?php echo htmlspecialchars($_POST['patient_full_name'] ?? ''); ?>">
                </div>
                <div class="form-group">
                    <label for="patient_phone">Phone Number</label>
                    <input type="tel" id="patient_phone" name="patient_phone" class="form-control" placeholder="9876543210" value="<?php echo htmlspecialchars($_POST['patient_phone'] ?? ''); ?>">
                </div>
                <div class="form-group">
                    <label for="patient_address">Address</label>
                    <textarea id="patient_address" name="patient_address" class="form-control" placeholder="Your delivery address"><?php echo htmlspecialchars($_POST['patient_address'] ?? ''); ?></textarea>
                </div>
                <div class="form-group">
                    <label for="medical_report">Upload Medical/Chemotherapy Report (Required)</label>
                    <input type="file" id="medical_report" name="medical_report" class="form-control">
                    <span style="font-size: 0.8rem; color: var(--dark-muted)">Accepted formats: PDF, DOC, DOCX, JPG, PNG (Max 5MB). Strictly confidential.</span>
                </div>
            </div>

            <!-- NGO Specific Fields -->
            <div id="ngo_fields" style="display: none;">
                <h3 style="font-size: 1.2rem; margin: 1.5rem 0 1rem 0; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">NGO Details</h3>
                <div class="form-group">
                    <label for="org_name">Organization Name</label>
                    <input type="text" id="org_name" name="org_name" class="form-control" placeholder="Hope Foundation" value="<?php echo htmlspecialchars($_POST['org_name'] ?? ''); ?>">
                </div>
                <div class="form-group">
                    <label for="reg_number">Registration / License Number</label>
                    <input type="text" id="reg_number" name="reg_number" class="form-control" placeholder="NGO-12345-IN" value="<?php echo htmlspecialchars($_POST['reg_number'] ?? ''); ?>">
                </div>
                <div class="form-group">
                    <label for="ngo_certificate">Upload Registration Certificate (Required)</label>
                    <input type="file" id="ngo_certificate" name="ngo_certificate" class="form-control">
                    <span style="font-size: 0.8rem; color: var(--dark-muted)">Accepted formats: PDF, JPG, PNG (Max 5MB). Admin will verify before account activation.</span>
                </div>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1.5rem;">Create Account</button>
            <p style="text-align: center; margin-top: 1.5rem; font-size: 0.9rem;">
                Already have an account? <a href="login.php" style="font-weight: 600;">Log In here</a>
            </p>
        </form>
    </div>
</main>

<footer>
    <p>&copy; <?php echo date('Y'); ?> HairFidence. Connecting Donors, NGOs, and Cancer Survivors.</p>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
