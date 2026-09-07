<?php
// ngo/dashboard.php
require_once '../config/db.php';
require_once '../includes/auth_check.php';

// Enforce that only logged-in NGOs can access this page
check_access('ngo');

$ngo_id = $_SESSION['ngo_id'];
$success_msg = '';
$error_msg = '';

// Handle Campaign Creation
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['create_campaign'])) {
    $title = trim($_POST['title']);
    $description = trim($_POST['description']);
    $event_date = $_POST['event_date'];
    $location = trim($_POST['location']);

    if (empty($title) || empty($description) || empty($event_date) || empty($location)) {
        $error_msg = "Please fill in all campaign details.";
    } else {
        try {
            $stmt = $pdo->prepare("INSERT INTO campaigns (ngo_id, title, description, event_date, location) VALUES (?, ?, ?, ?, ?)");
            $stmt->execute([$ngo_id, $title, $description, $event_date, $location]);
            $success_msg = "Campaign posted successfully!";
        } catch (PDOException $e) {
            $error_msg = "Failed to post campaign: " . $e->getMessage();
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

// Handle Hair Request Approvals
if (isset($_GET['approve_request'])) {
    $request_id = intval($_GET['approve_request']);
    try {
        $pdo->beginTransaction();
        
        // Update request status to Approved
        $stmt = $pdo->prepare("UPDATE hair_requests SET status = 'Approved' WHERE request_id = ? AND ngo_id = ?");
        $stmt->execute([$request_id, $ngo_id]);

        // Get matching post_id to update its status to Donated
        $stmt = $pdo->prepare("SELECT post_id FROM hair_requests WHERE request_id = ?");
        $stmt->execute([$request_id]);
        $post_id = $stmt->fetchColumn();

        if ($post_id) {
            $stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Donated' WHERE post_id = ?");
            $stmt->execute([$post_id]);
        }

        $pdo->commit();
        $success_msg = "Donation request approved and marked as Donated.";
    } catch (PDOException $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        $error_msg = "Error approving request: " . $e->getMessage();
    }
}

// Handle Hair Request Rejections
if (isset($_GET['reject_request'])) {
    $request_id = intval($_GET['reject_request']);
    try {
        $pdo->beginTransaction();
        
        // Update request status to Rejected
        $stmt = $pdo->prepare("UPDATE hair_requests SET status = 'Rejected' WHERE request_id = ? AND ngo_id = ?");
        $stmt->execute([$request_id, $ngo_id]);

        // Get matching post_id to unlock it back to Available
        $stmt = $pdo->prepare("SELECT post_id FROM hair_requests WHERE request_id = ?");
        $stmt->execute([$request_id]);
        $post_id = $stmt->fetchColumn();

        if ($post_id) {
            $stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Available' WHERE post_id = ?");
            $stmt->execute([$post_id]);
        }

        $pdo->commit();
        $success_msg = "Donation request rejected. Hair post is unlocked back to Available status.";
    } catch (PDOException $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        $error_msg = "Error rejecting request: " . $e->getMessage();
    }
}

// Handle physical hair donation verification (Verify Hair Donations)
if (isset($_GET['verify_donation'])) {
    $post_id = intval($_GET['verify_donation']);
    try {
        $stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Donated' WHERE post_id = ?");
        $stmt->execute([post_id]);
        $success_msg = "Hair donation verified physically and marked as Donated.";
    } catch (PDOException $e) {
        $error_msg = "Verification failed: " . $e->getMessage();
    }
}

// Fetch requests assigned to this NGO
$requests = [];
try {
    $stmt = $pdo->prepare("SELECT r.request_id, r.status as request_status, r.request_date,
                                 p.full_name as patient_name, p.phone as patient_phone, p.medical_report_url,
                                 d.hair_length, d.hair_type, d.post_id
                          FROM hair_requests r
                          JOIN patients p ON r.patient_id = p.patient_id
                          JOIN hair_donation_posts d ON r.post_id = d.post_id
                          WHERE r.ngo_id = ?
                          ORDER BY r.request_date DESC");
    $stmt->execute([$ngo_id]);
    $requests = $stmt->fetchAll();
} catch (PDOException $e) {
    $error_msg = "Error fetching requests: " . $e->getMessage();
}

// Fetch campaigns posted by this NGO
$my_campaigns = [];
try {
    $stmt = $pdo->prepare("SELECT * FROM campaigns WHERE ngo_id = ? ORDER BY event_date ASC");
    $stmt->execute([$ngo_id]);
    $my_campaigns = $stmt->fetchAll();
} catch (PDOException $e) {
    // Fail silently
}

// Fetch all hair donation posts in the system (View Hair Donation Posts)
$all_donations = [];
try {
    $stmt = $pdo->query("SELECT d.*, dn.full_name as donor_name 
                         FROM hair_donation_posts d
                         JOIN donors dn ON d.donor_id = dn.donor_id
                         ORDER BY d.post_id DESC");
    $all_donations = $stmt->fetchAll();
} catch (PDOException $e) {
    // Fail silently
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NGO Dashboard - HairFidence</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
        .dashboard-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
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
            HairFidence NGO
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
            <h2>NGO Management Panel</h2>
            <p>Verify medical credentials, approve wig requests, and publish community donation drives.</p>
        </div>

        <!-- System feedback alerts -->
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
            <!-- Left Side: Requests for Wig validation -->
            <div>
                <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">Manage Hair Requests</h3>
                <?php if (count($requests) === 0): ?>
                    <div class="glass-card" style="padding: 2rem; text-align: center; color: var(--dark-muted);">
                        No patient hair donation requests assigned to your NGO at this time.
                    </div>
                <?php else: ?>
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>Patient Details</th>
                                    <th>Hair Needed</th>
                                    <th>Medical Report</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($requests as $req): ?>
                                    <tr>
                                        <td>
                                            <strong><?php echo htmlspecialchars($req['patient_name']); ?></strong><br>
                                            <span style="font-size: 0.85rem; color: var(--dark-muted)"><?php echo htmlspecialchars($req['patient_phone']); ?></span>
                                        </td>
                                        <td>
                                            Length: <?php echo htmlspecialchars($req['hair_length']); ?> cm<br>
                                            Type: <?php echo htmlspecialchars($req['hair_type']); ?>
                                        </td>
                                        <td>
                                            <a href="../<?php echo htmlspecialchars($req['medical_report_url']); ?>" target="_blank" class="btn btn-outline" style="padding: 0.3rem 0.6rem; font-size: 0.8rem; border-radius: var(--radius-sm)">
                                                View PDF / File
                                            </a>
                                        </td>
                                        <td>
                                            <span class="badge <?php 
                                                if ($req['request_status'] === 'Approved') echo 'badge-success';
                                                elseif ($req['request_status'] === 'Rejected') echo 'badge-danger';
                                                else echo 'badge-warning';
                                            ?>">
                                                <?php echo htmlspecialchars($req['request_status']); ?>
                                            </span>
                                        </td>
                                        <td>
                                            <?php if ($req['request_status'] === 'Pending'): ?>
                                                <div style="display: flex; gap: 0.5rem;">
                                                    <a href="dashboard.php?approve_request=<?php echo $req['request_id']; ?>" class="btn btn-secondary" style="padding: 0.3rem 0.6rem; font-size: 0.8rem; border-radius: var(--radius-sm)">
                                                        Approve
                                                    </a>
                                                    <a href="dashboard.php?reject_request=<?php echo $req['request_id']; ?>" class="btn btn-outline" style="padding: 0.3rem 0.6rem; font-size: 0.8rem; border-radius: var(--radius-sm); color: #b91c1c; border-color: #fca5a5;">
                                                        Reject
                                                    </a>
                                                </div>
                                            <?php else: ?>
                                                <span style="color: var(--dark-muted); font-size: 0.85rem; font-weight: 600;">Processed</span>
                                            <?php endif; ?>
                                        </td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                <?php endif; ?>

                <div style="margin-top: 3rem; margin-bottom: 3rem;">
                    <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">View Hair Donation Posts</h3>
                    <?php if (count($all_donations) === 0): ?>
                        <p style="color: var(--dark-muted)">No hair donation posts in the system.</p>
                    <?php else: ?>
                        <div class="table-responsive">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Post ID</th>
                                        <th>Donor Name</th>
                                        <th>Length</th>
                                        <th>Texture</th>
                                        <th>Status</th>
                                        <th>Verify Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php foreach ($all_donations as $don): ?>
                                        <tr>
                                            <td><code>#<?php echo $don['post_id']; ?></code></td>
                                            <td><strong><?php echo htmlspecialchars($don['donor_name']); ?></strong></td>
                                            <td><?php echo htmlspecialchars($don['hair_length']); ?> cm</td>
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
                                            <td>
                                                <?php if ($don['status'] !== 'Donated'): ?>
                                                    <a href="dashboard.php?verify_donation=<?php echo $don['post_id']; ?>" class="btn btn-secondary" style="padding: 0.3rem 0.6rem; font-size: 0.8rem; border-radius: var(--radius-sm)">
                                                        Verify & Complete
                                                    </a>
                                                <?php else: ?>
                                                    <span style="color: var(--secondary); font-size: 0.85rem; font-weight: 600;">✓ Verified</span>
                                                <?php endif; ?>
                                            </td>
                                        </tr>
                                    <?php endforeach; ?>
                                </tbody>
                            </table>
                        </div>
                    <?php endif; ?>
                </div>

                <div style="margin-top: 3rem;">
                    <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">Our Campaigns</h3>
                    <?php if (count($my_campaigns) === 0): ?>
                        <p style="color: var(--dark-muted)">No drives deployed yet. Use the form on the right to post one.</p>
                    <?php else: ?>
                        <div class="grid-3" style="grid-template-columns: 1fr 1fr; gap: 1rem;">
                            <?php foreach ($my_campaigns as $camp): ?>
                                <div class="glass-card" style="padding: 1.5rem; border-radius: var(--radius-md)">
                                    <h4 style="color: var(--primary); margin-bottom: 0.5rem;"><?php echo htmlspecialchars($camp['title']); ?></h4>
                                    <p style="font-size: 0.9rem; color: var(--dark-muted); margin-bottom: 0.5rem;"><?php echo htmlspecialchars($camp['description']); ?></p>
                                    <div style="font-size: 0.8rem; font-weight: 600; color: var(--dark)">
                                        📅 Date: <?php echo date('d M Y', strtotime($camp['event_date'])); ?><br>
                                        📍 Location: <?php echo htmlspecialchars($camp['location']); ?>
                                    </div>
                                </div>
                            <?php endforeach; ?>
                        </div>
                    <?php endif; ?>
                </div>
            </div>

            <!-- Right Side: Forms for Action -->
            <div>
                <!-- Create Campaign Drive Form -->
                <div class="glass-card" style="padding: 1.8rem; margin-bottom: 2rem; border-radius: var(--radius-md)">
                    <h3 style="font-size: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Create Campaign</h3>
                    <form action="dashboard.php" method="POST">
                        <input type="hidden" name="create_campaign" value="1">
                        <div class="form-group">
                            <label for="camp_title">Campaign Title</label>
                            <input type="text" id="camp_title" name="title" class="form-control" placeholder="Cancer Awareness Run" required>
                        </div>
                        <div class="form-group">
                            <label for="camp_desc">Description</label>
                            <textarea id="camp_desc" name="description" class="form-control" placeholder="Describe the purpose and event agenda..." required></textarea>
                        </div>
                        <div class="form-group">
                            <label for="camp_date">Event Date</label>
                            <input type="date" id="camp_date" name="event_date" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="camp_loc">Location / Venue</label>
                            <input type="text" id="camp_loc" name="location" class="form-control" placeholder="Campus Auditorium, Building A" required>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Publish Event</button>
                    </form>
                </div>

                <!-- Submit Complaint Form -->
                <div class="glass-card" style="padding: 1.8rem; border-radius: var(--radius-md)">
                    <h3 style="font-size: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Submit Ticket / Issue</h3>
                    <form action="dashboard.php" method="POST">
                        <input type="hidden" name="submit_complaint" value="1">
                        <div class="form-group">
                            <label for="comp_subj">Subject</label>
                            <input type="text" id="comp_subj" name="subject" class="form-control" placeholder="Technical issue, account bugs..." required>
                        </div>
                        <div class="form-group">
                            <label for="comp_desc">Details</label>
                            <textarea id="comp_desc" name="description" class="form-control" placeholder="Describe your complaint here..." required></textarea>
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
