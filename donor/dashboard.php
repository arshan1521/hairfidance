<?php
// donor/dashboard.php
require_once '../config/db.php';
require_once '../includes/auth_check.php';

// Enforce that only logged-in Donors can access this page
check_access('donor');

$donor_id = $_SESSION['donor_id'];
$success_msg = '';
$error_msg = '';

// Handle Hair Donation Post Creation
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_donation'])) {
    $hair_length = trim($_POST['hair_length']);
    $hair_type = $_POST['hair_type'];

    if (empty($hair_length) || empty($hair_type) || empty($_FILES['hair_photo']['name'])) {
        $error_msg = "Please fill in all donation fields and upload a hair photo.";
    } else {
        try {
            // Handle File Upload
            $file_name = $_FILES['hair_photo']['name'];
            $file_tmp = $_FILES['hair_photo']['tmp_name'];
            $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
            $allowed_exts = ['jpg', 'jpeg', 'png'];

            if (!in_array($file_ext, $allowed_exts)) {
                throw new Exception("Invalid image type. Allowed: JPG, JPEG, PNG.");
            }

            // Create directory if not exists
            $upload_dir = '../uploads/hair_photos/';
            if (!is_dir($upload_dir)) {
                mkdir($upload_dir, 0777, true);
            }

            $new_file_name = 'hair_' . $donor_id . '_' . time() . '.' . $file_ext;
            $dest_path = $upload_dir . $new_file_name;

            // Database path relative to project root
            $db_path = 'uploads/hair_photos/' . $new_file_name;

            if (!move_uploaded_file($file_tmp, $dest_path)) {
                throw new Exception("Failed to upload hair photo. Try again.");
            }

            // Insert donation post into hair_donation_posts table using image_url
            $stmt = $pdo->prepare("INSERT INTO hair_donation_posts (donor_id, hair_length, hair_type, image_url, status) VALUES (?, ?, ?, ?, 'Available')");
            $stmt->execute([$donor_id, $hair_length, $hair_type, $db_path]);
            
            $success_msg = "Hair donation post created successfully! It is now visible to Patients in the catalog.";
        } catch (Exception $e) {
            $error_msg = $e->getMessage();
        }
    }
}

// Handle Complaint submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit_complaint'])) {
    $subject = trim($_POST['subject']);
    $description = trim($_POST['description']);
    $login_id = $_SESSION['login_id']; // Use login_id

    if (empty($subject) || empty($description)) {
        $error_msg = "Please fill in subject and description.";
    } else {
        try {
            $stmt = $pdo->prepare("INSERT INTO complaints (login_id, subject, description, status) VALUES (?, ?, ?, 'Pending')");
            $stmt->execute([$login_id, $subject, $description]);
            $success_msg = "Complaint submitted to Admin successfully.";
        } catch (PDOException $e) {
            $error_msg = "Failed to log complaint: " . $e->getMessage();
        }
    }
}

// Fetch donor's donation history (using post_id DESC sorting)
$donations = [];
try {
    $stmt = $pdo->prepare("SELECT * FROM hair_donation_posts WHERE donor_id = ? ORDER BY post_id DESC");
    $stmt->execute([$donor_id]);
    $donations = $stmt->fetchAll();
} catch (PDOException $e) {
    $error_msg = "Error fetching history: " . $e->getMessage();
}

// Fetch active campaigns (NGO drives) joining on NGO profile table
$campaigns = [];
try {
    $stmt = $pdo->query("SELECT c.*, n.organization_name 
                         FROM campaigns c 
                         JOIN ngos n ON c.ngo_id = n.ngo_id 
                         ORDER BY c.event_date ASC");
    $campaigns = $stmt->fetchAll();
} catch (PDOException $e) {
    // Fail silently
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donor Dashboard - HairFidence</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
        .dashboard-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }
        .donation-image-preview {
            width: 80px;
            height: 80px;
            object-fit: cover;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
        }
        @media (max-width: 900px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

<header>
    <div class="nav-container">
        <a href="../index.php" class="logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: var(--secondary)">
                <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/>
                <path d="M12 6v12M6 12h12"/>
            </svg>
            HairFidence Donor
        </a>
        <ul class="nav-links">
            <li><span style="font-weight: 600; color: var(--dark-muted)">Hello, <?php echo htmlspecialchars($_SESSION['name']); ?></span></li>
            <li><a href="../auth/logout.php" class="btn btn-outline" style="padding: 0.5rem 1rem;">Logout</a></li>
        </ul>
    </div>
</header>

<main class="container">
    <div class="animate-fade-in">
        <div class="auth-header" style="text-align: left; margin-bottom: 2rem;">
            <h2>Donor Hub</h2>
            <p>Share your hair donation posts, track their status through processing and donation, and browse upcoming NGO donation drives.</p>
        </div>

        <!-- Alert messages -->
        <?php if (!empty($success_msg)): ?>
            <div class="alert alert-success">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                <?php echo htmlspecialchars($success_msg); ?>
            </div>
        <?php endif; ?>
        <?php if (!empty($error_msg)): ?>
            <div class="alert alert-danger">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
                <?php echo htmlspecialchars($error_msg); ?>
            </div>
        <?php endif; ?>

        <div class="dashboard-grid">
            <!-- Left Side: My Donations & Campaigns -->
            <div>
                <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">View Donation Status</h3>
                <?php if (count($donations) === 0): ?>
                    <div class="glass-card" style="padding: 2.5rem; text-align: center; color: var(--dark-muted); margin-bottom: 3rem;">
                        You haven't posted any hair donations yet. Use the form on the right to post your first donation!
                    </div>
                <?php else: ?>
                    <div class="table-responsive" style="margin-bottom: 3rem;">
                        <table>
                            <thead>
                                <tr>
                                    <th>Photo</th>
                                    <th>Hair Length</th>
                                    <th>Hair Type</th>
                                    <th>Status (Pipeline)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($donations as $don): ?>
                                    <tr>
                                        <td>
                                            <img src="../<?php echo htmlspecialchars($don['image_url']); ?>" alt="Hair Donation" class="donation-image-preview">
                                        </td>
                                        <td><strong><?php echo htmlspecialchars($don['hair_length']); ?> cm</strong></td>
                                        <td><?php echo htmlspecialchars($don['hair_type']); ?></td>
                                        <td>
                                            <span class="badge <?php 
                                                if ($don['status'] === 'Available') echo 'badge-info';
                                                elseif ($don['status'] === 'Processing') echo 'badge-warning';
                                                else echo 'badge-success';
                                            ?>">
                                                <?php echo htmlspecialchars($don['status']); ?>
                                            </span>
                                        </td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                <?php endif; ?>

                <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">View Campaigns</h3>
                <?php if (count($campaigns) === 0): ?>
                    <p style="color: var(--dark-muted)">No NGO campaigns registered currently.</p>
                <?php else: ?>
                    <div class="grid-3" style="grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                        <?php foreach ($campaigns as $camp): ?>
                            <div class="glass-card" style="padding: 1.5rem; border-radius: var(--radius-md)">
                                <span class="badge badge-info" style="margin-bottom: 0.5rem; font-size: 0.65rem;"><?php echo htmlspecialchars($camp['organization_name']); ?></span>
                                <h4 style="margin-bottom: 0.5rem;"><?php echo htmlspecialchars($camp['title']); ?></h4>
                                <p style="font-size: 0.85rem; color: var(--dark-muted); margin-bottom: 0.8rem;"><?php echo htmlspecialchars($camp['description']); ?></p>
                                <div style="font-size: 0.8rem; font-weight: 600; color: var(--dark);">
                                    📅 Date: <?php echo date('d M Y', strtotime($camp['event_date'])); ?><br>
                                    📍 Venue: <?php echo htmlspecialchars($camp['location']); ?>
                                </div>
                            </div>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>
            </div>

            <!-- Right Side: Forms for Action -->
            <div>
                <!-- Add Hair Donation Post Form -->
                <div class="glass-card" style="padding: 1.8rem; margin-bottom: 2rem; border-radius: var(--radius-md)">
                    <h3 style="font-size: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Add Hair Donation</h3>
                    <form action="dashboard.php" method="POST" enctype="multipart/form-data">
                        <input type="hidden" name="add_donation" value="1">
                        
                        <div class="form-group">
                            <label for="hair_length">Hair Length (in cm)</label>
                            <input type="number" id="hair_length" name="hair_length" step="0.1" class="form-control" placeholder="Minimum length: 20 cm" required min="1">
                        </div>

                        <div class="form-group">
                            <label for="hair_type">Hair Texture / Type</label>
                            <select id="hair_type" name="hair_type" class="form-control form-select" required>
                                <option value="" disabled selected>-- Select Type --</option>
                                <option value="Straight">Straight</option>
                                <option value="Wavy">Wavy</option>
                                <option value="Curly">Curly</option>
                                <option value="Coily">Coily</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="hair_photo">Hair Photograph (Required)</label>
                            <input type="file" id="hair_photo" name="hair_photo" class="form-control" required>
                            <span style="font-size: 0.8rem; color: var(--dark-muted)">Upload a clear photo of the cut hair ponytail. JPG, PNG only.</span>
                        </div>

                        <button type="submit" class="btn btn-primary" style="width: 100%;">Post Donation</button>
                    </form>
                </div>

                <!-- Submit Complaint Form -->
                <div class="glass-card" style="padding: 1.8rem; border-radius: var(--radius-md)">
                    <h3 style="font-size: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Submit Ticket / Issue</h3>
                    <form action="dashboard.php" method="POST">
                        <input type="hidden" name="submit_complaint" value="1">
                        <div class="form-group">
                            <label for="comp_subj">Subject</label>
                            <input type="text" id="comp_subj" name="subject" class="form-control" placeholder="Reporting issue..." required>
                        </div>
                        <div class="form-group">
                            <label for="comp_desc">Details</label>
                            <textarea id="comp_desc" name="description" class="form-control" placeholder="Describe your issue..." required></textarea>
                        </div>
                        <button type="submit" class="btn btn-outline" style="width: 100%;">File Complaint</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</main>

<footer>
    <p>&copy; <?php echo date('Y'); ?> HairFidence. Connecting Donors, NGOs, and Cancer Survivors.</p>
</footer>

<script src="../assets/js/main.js"></script>
</body>
</html>
