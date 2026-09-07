<?php
// auth/dashboard_redirect.php
session_start();

if (!isset($_SESSION['login_id']) || !isset($_SESSION['role'])) {
    // Session not initialized, redirect to login
    header("Location: ../login.php");
    exit();
}

$role = $_SESSION['role'];

switch ($role) {
    case 'admin':
        header("Location: ../admin/dashboard.php");
        break;
    case 'ngo':
        header("Location: ../ngo/dashboard.php");
        break;
    case 'donor':
        header("Location: ../donor/dashboard.php");
        break;
    case 'patient':
        header("Location: ../patient/dashboard.php");
        break;
    default:
        // Undefined role, clear session and login
        session_unset();
        session_destroy();
        header("Location: ../login.php");
        break;
}
exit();
?>
