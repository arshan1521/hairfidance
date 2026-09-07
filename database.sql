-- Create database if not exists
CREATE DATABASE IF NOT EXISTS `hairfidence`;
USE `hairfidence`;

-- Drop existing tables to prevent conflicts and ensure a clean schema rebuild
DROP TABLE IF EXISTS `complaints`;
DROP TABLE IF EXISTS `campaigns`;
DROP TABLE IF EXISTS `hair_requests`;
DROP TABLE IF EXISTS `hair_donation_posts`;
DROP TABLE IF EXISTS `ngos`;
DROP TABLE IF EXISTS `patients`;
DROP TABLE IF EXISTS `donors`;
DROP TABLE IF EXISTS `login`;

-- 1. Login Table (Core credentials and authentication)
CREATE TABLE IF NOT EXISTS `login` (
    `login_id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(150) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL, -- Stores the hashed password
    `role` ENUM('admin', 'ngo', 'donor', 'patient') NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Donors Table
CREATE TABLE IF NOT EXISTS `donors` (
    `donor_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL,
    `address` TEXT NOT NULL,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Patients Table
CREATE TABLE IF NOT EXISTS `patients` (
    `patient_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL,
    `address` TEXT NOT NULL,
    `medical_report_url` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. NGOs Table
CREATE TABLE IF NOT EXISTS `ngos` (
    `ngo_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `organization_name` VARCHAR(150) NOT NULL,
    `registration_number` VARCHAR(100) NOT NULL,
    `is_approved` TINYINT(1) DEFAULT 0, -- 0 = Pending, 1 = Approved
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Hair Donation Posts Table
CREATE TABLE IF NOT EXISTS `hair_donation_posts` (
    `post_id` INT AUTO_INCREMENT PRIMARY KEY,
    `donor_id` INT NOT NULL,
    `hair_length` DECIMAL(5,2) NOT NULL,
    `hair_type` VARCHAR(50) NOT NULL,
    `image_url` VARCHAR(255) NOT NULL,
    `status` ENUM('Available', 'Processing', 'Donated') DEFAULT 'Available',
    FOREIGN KEY (`donor_id`) REFERENCES `donors`(`donor_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. Hair Requests Table
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

-- 7. Campaigns Table
CREATE TABLE IF NOT EXISTS `campaigns` (
    `campaign_id` INT AUTO_INCREMENT PRIMARY KEY,
    `ngo_id` INT NOT NULL,
    `title` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `event_date` DATE NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`ngo_id`) REFERENCES `ngos`(`ngo_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8. Complaints Table
CREATE TABLE IF NOT EXISTS `complaints` (
    `complaint_id` INT AUTO_INCREMENT PRIMARY KEY,
    `login_id` INT NOT NULL,
    `subject` VARCHAR(150) NOT NULL,
    `description` TEXT NOT NULL,
    `status` ENUM('Pending', 'Resolved') DEFAULT 'Pending',
    `date_submitted` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`login_id`) REFERENCES `login`(`login_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed Default Admin User in Login table
-- Email: admin@hairfidence.com
-- Password: adminpassword (hashed using PHP PASSWORD_DEFAULT / Bcrypt)
INSERT INTO `login` (`login_id`, `email`, `password`, `role`)
VALUES (1, 'admin@hairfidence.com', '$2y$10$fSVaG3kV8s//9BkYqmTF/OvKFvnjj/pNYbm4TOikDewu876fnrile', 'admin')
ON DUPLICATE KEY UPDATE `email` = `email`;
