<?php
// scripts/clear_db.php - Clear all transactional and user records from the database
require_once __DIR__ . '/../config/db.php';

try {
    echo "Disabling foreign key constraints...\n";
    $pdo->exec("SET FOREIGN_KEY_CHECKS = 0;");

    $tables = [
        'complaints',
        'campaigns',
        'hair_requests',
        'hair_donation_posts',
        'ngos',
        'patients',
        'donors',
        'login'
    ];

    foreach ($tables as $table) {
        $pdo->exec("TRUNCATE TABLE `$table`;");
        echo "Truncated table: `$table`\n";
    }

    echo "Re-enabling foreign key constraints...\n";
    $pdo->exec("SET FOREIGN_KEY_CHECKS = 1;");

    // Re-seed default admin user so the platform can still be accessed
    $adminPasswordHash = '$2y$10$fSVaG3kV8s//9BkYqmTF/OvKFvnjj/pNYbm4TOikDewu876fnrile'; // 'adminpassword'
    $stmt = $pdo->prepare("INSERT INTO `login` (`login_id`, `email`, `password`, `role`) VALUES (1, 'admin@hairfidence.com', ?, 'admin')");
    $stmt->execute([$adminPasswordHash]);
    echo "Seeded default Admin account (email: admin@hairfidence.com | password: adminpassword)\n";

    echo "\nVerification of row counts:\n";
    foreach ($tables as $table) {
        $count = $pdo->query("SELECT COUNT(*) FROM `$table`")->fetchColumn();
        echo "  - $table: $count rows\n";
    }

    echo "\nDatabase content successfully cleared!\n";
} catch (Exception $e) {
    echo "Error clearing database: " . $e->getMessage() . "\n";
    exit(1);
}
