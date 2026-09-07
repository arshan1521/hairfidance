<?php
// config/db.php
// Database Configuration using PDO

$host = 'localhost';
$db   = 'hairfidence';
$user = 'root';
$pass = ''; // Default XAMPP MySQL password is empty
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
     // Output a user-friendly message or log the error
     die("Database connection failed. Please ensure MySQL is running in XAMPP and the database is imported. Error: " . $e->getMessage());
}
?>
