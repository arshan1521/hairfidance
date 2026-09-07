<?php
// includes/auth_check.php
// Middleware helper to enforce role-based access control (RBAC) on dashboards

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

/**
 * Enforces session checks and validates if the user role matches allowed roles.
 * @param array|string $allowed_roles Roles allowed to view this page.
 */
function check_access($allowed_roles) {
    if (!isset($_SESSION['login_id']) || !isset($_SESSION['role'])) {
        header("Location: ../login.php");
        exit();
    }
    
    $role = $_SESSION['role'];
    
    $allowed = false;
    if (is_array($allowed_roles)) {
        if (in_array($role, $allowed_roles)) {
            $allowed = true;
        }
    } else {
        if ($role === $allowed_roles) {
            $allowed = true;
        }
    }
    
    if (!$allowed) {
        // Clear variables and redirect with an error message
        header("Location: ../login.php?error=Unauthorized+Access");
        exit();
    }
}
?>
