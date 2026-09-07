<?php
// login.php
require_once 'config/db.php';
session_start();

$error = '';

// Redirect if already logged in
if (isset($_SESSION['login_id'])) {
    header("Location: auth/dashboard_redirect.php");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email']);
    $password = $_POST['password'];

    if (empty($email) || empty($password)) {
        $error = "Please fill in all fields.";
    } else {
        try {
            // Get credentials from login table
            $stmt = $pdo->prepare("SELECT * FROM login WHERE email = ?");
            $stmt->execute([$email]);
            $user = $stmt->fetch();

            if ($user && password_verify($password, $user['password'])) {
                // Fetch profile specific data depending on role
                $role = $user['role'];
                $is_approved_ngo = true;
                $profile_data = [];

                if ($role === 'donor') {
                    $profile_stmt = $pdo->prepare("SELECT donor_id, full_name FROM donors WHERE login_id = ?");
                    $profile_stmt->execute([$user['login_id']]);
                    $profile_data = $profile_stmt->fetch();
                } elseif ($role === 'patient') {
                    $profile_stmt = $pdo->prepare("SELECT patient_id, full_name FROM patients WHERE login_id = ?");
                    $profile_stmt->execute([$user['login_id']]);
                    $profile_data = $profile_stmt->fetch();
                } elseif ($role === 'ngo') {
                    $profile_stmt = $pdo->prepare("SELECT ngo_id, organization_name, is_approved FROM ngos WHERE login_id = ?");
                    $profile_stmt->execute([$user['login_id']]);
                    $profile_data = $profile_stmt->fetch();
                    
                    if ($profile_data && !$profile_data['is_approved']) {
                        $is_approved_ngo = false;
                    }
                }

                // If it is an NGO and not yet approved, prevent login
                if (!$is_approved_ngo) {
                    $error = "Your NGO account is pending verification and approval by the administrator.";
                } else {
                    // Set Session details (using login_id instead of user_id)
                    $_SESSION['login_id'] = $user['login_id'];
                    $_SESSION['email'] = $user['email'];
                    $_SESSION['role'] = $role;
                    
                    if ($role === 'donor') {
                        $_SESSION['donor_id'] = $profile_data['donor_id'] ?? null;
                        $_SESSION['name'] = $profile_data['full_name'] ?? 'Donor';
                    } elseif ($role === 'patient') {
                        $_SESSION['patient_id'] = $profile_data['patient_id'] ?? null;
                        $_SESSION['name'] = $profile_data['full_name'] ?? 'Patient';
                    } elseif ($role === 'ngo') {
                        $_SESSION['ngo_id'] = $profile_data['ngo_id'] ?? null;
                        $_SESSION['name'] = $profile_data['organization_name'] ?? 'NGO';
                    } else {
                        $_SESSION['name'] = 'Administrator';
                    }

                    // Redirect
                    header("Location: auth/dashboard_redirect.php");
                    exit();
                }
            } else {
                $error = "Invalid email or password.";
            }
        } catch (PDOException $e) {
            $error = "System error: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - HairFidence</title>
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
            <li><a href="login.php" class="nav-item active">Login</a></li>
            <li><a href="register.php" class="btn btn-primary" style="color: white; padding: 0.5rem 1rem;">Register</a></li>
        </ul>
    </div>
</header>

<main class="container">
    <div class="auth-container glass-card animate-fade-in">
        <div class="auth-header">
            <h2>Welcome Back</h2>
            <p>Access your HairFidence portal</p>
        </div>

        <?php if (!empty($error)): ?>
            <div class="alert alert-danger">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
                <?php echo htmlspecialchars($error); ?>
            </div>
        <?php endif; ?>

        <form action="login.php" method="POST">
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email" required value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" class="form-control" placeholder="Enter your password" required>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Log In</button>
            
            <div style="margin-top: 1.5rem; text-align: center; font-size: 0.85rem; color: var(--dark-muted)">
                <p>Default Admin: <strong>admin@hairfidence.com</strong> / <strong>adminpassword</strong></p>
            </div>

            <p style="text-align: center; margin-top: 1.5rem; font-size: 0.9rem;">
                Don't have an account? <a href="register.php" style="font-weight: 600;">Register here</a>
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
