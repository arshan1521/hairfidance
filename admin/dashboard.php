<?php
// admin/dashboard.php
require_once '../config/db.php';
require_once '../includes/auth_check.php';

// Enforce that only logged-in Admin can access this page
check_access('admin');

$success_msg = '';
$error_msg = '';

// Handle NGO approval request
if (isset($_GET['approve_ngo'])) {
    $ngo_id = intval($_GET['approve_ngo']);
    try {
        $stmt = $pdo->prepare("UPDATE ngos SET is_approved = 1 WHERE ngo_id = ?");
        $stmt->execute([$ngo_id]);
        $success_msg = "NGO approved successfully.";
    } catch (PDOException $e) {
        $error_msg = "Failed to approve NGO: " . $e->getMessage();
    }
}

// Handle Complaint resolution request
if (isset($_GET['resolve_complaint'])) {
    $complaint_id = intval($_GET['resolve_complaint']);
    try {
        $stmt = $pdo->prepare("UPDATE complaints SET status = 'Resolved' WHERE complaint_id = ?");
        $stmt->execute([$complaint_id]);
        $success_msg = "Complaint marked as Resolved.";
    } catch (PDOException $e) {
        $error_msg = "Failed to resolve complaint: " . $e->getMessage();
    }
}

// Fetch pending NGOs (joining on Login table via login_id)
$pending_ngos = [];
try {
    $stmt = $pdo->query("SELECT n.ngo_id, n.organization_name, n.registration_number, u.email 
                         FROM ngos n 
                         JOIN login u ON n.login_id = u.login_id 
                         WHERE n.is_approved = 0");
    $pending_ngos = $stmt->fetchAll();
} catch (PDOException $e) {
    $error_msg = "Error loading NGOs: " . $e->getMessage();
}

// Fetch all complaints (joining on Login table via login_id)
$complaints = [];
try {
    $stmt = $pdo->query("SELECT c.complaint_id, c.subject, c.description, c.status, c.date_submitted, u.email 
                         FROM complaints c 
                         JOIN login u ON c.login_id = u.login_id 
                         ORDER BY c.date_submitted DESC");
    $complaints = $stmt->fetchAll();
} catch (PDOException $e) {
    $error_msg = "Error loading complaints: " . $e->getMessage();
}

// Fetch statistics
$stats = [
    'users' => 0,
    'ngos' => 0,
    'donations' => 0,
    'requests' => 0
];
try {
    $stats['users'] = $pdo->query("SELECT COUNT(*) FROM login")->fetchColumn();
    $stats['ngos'] = $pdo->query("SELECT COUNT(*) FROM ngos WHERE is_approved = 1")->fetchColumn();
    $stats['donations'] = $pdo->query("SELECT COUNT(*) FROM hair_donation_posts")->fetchColumn();
    $stats['requests'] = $pdo->query("SELECT COUNT(*) FROM hair_requests")->fetchColumn();
} catch (PDOException $e) {
    // Fail silently for stats
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - HairFidence</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

<header>
    <div class="nav-container">
        <a href="../index.php" class="logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: var(--secondary)">
                <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/>
                <path d="M12 6v12M6 12h12"/>
            </svg>
            HairFidence Admin
        </a>
        <ul class="nav-links">
            <li><span style="font-weight: 600; color: var(--dark-muted)">Hello, Admin</span></li>
            <li><a href="../auth/logout.php" class="btn btn-outline" style="padding: 0.5rem 1rem;">Logout</a></li>
        </ul>
    </div>
</header>

<main class="container">
    <div class="animate-fade-in">
        <h2 style="margin-bottom: 2rem; font-size: 2rem;">System Overview</h2>

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

        <!-- Stats Grid -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value"><?php echo $stats['users']; ?></div>
                <div class="stat-label">Total Accounts</div>
            </div>
            <div class="stat-card">
                <div class="stat-value"><?php echo $stats['ngos']; ?></div>
                <div class="stat-label">Approved NGOs</div>
            </div>
            <div class="stat-card">
                <div class="stat-value"><?php echo $stats['donations']; ?></div>
                <div class="stat-label">Hair Donations</div>
            </div>
            <div class="stat-card">
                <div class="stat-value"><?php echo $stats['requests']; ?></div>
                <div class="stat-label">Wig Requests</div>
            </div>
        </div>

        <div style="margin-top: 3rem;">
            <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">NGO Account Verification</h3>
            <?php if (count($pending_ngos) === 0): ?>
                <div class="glass-card" style="padding: 1.5rem; text-align: center; color: var(--dark-muted);">
                    No pending NGO registrations found.
                </div>
            <?php else: ?>
                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>Organization Name</th>
                                <th>Registration ID</th>
                                <th>Email Address</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($pending_ngos as $ngo): ?>
                                <tr>
                                    <td><strong><?php echo htmlspecialchars($ngo['organization_name']); ?></strong></td>
                                    <td><code><?php echo htmlspecialchars($ngo['registration_number']); ?></code></td>
                                    <td><?php echo htmlspecialchars($ngo['email']); ?></td>
                                    <td>
                                        <a href="dashboard.php?approve_ngo=<?php echo $ngo['ngo_id']; ?>" class="btn btn-secondary" style="padding: 0.4rem 0.8rem; font-size: 0.85rem; border-radius: var(--radius-sm)">
                                            Approve
                                        </a>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            <?php endif; ?>
        </div>

        <div style="margin-top: 3rem;">
            <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">User Complaints & Feedback</h3>
            <?php if (count($complaints) === 0): ?>
                <div class="glass-card" style="padding: 1.5rem; text-align: center; color: var(--dark-muted);">
                    No user complaints logged.
                </div>
            <?php else: ?>
                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>User Email</th>
                                <th>Subject</th>
                                <th>Details</th>
                                <th>Status</th>
                                <th>Date Filed</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($complaints as $comp): ?>
                                <tr>
                                    <td><?php echo htmlspecialchars($comp['email']); ?></td>
                                    <td><strong><?php echo htmlspecialchars($comp['subject']); ?></strong></td>
                                    <td><?php echo htmlspecialchars($comp['description']); ?></td>
                                    <td>
                                        <span class="badge <?php echo $comp['status'] === 'Resolved' ? 'badge-success' : 'badge-warning'; ?>">
                                            <?php echo htmlspecialchars($comp['status']); ?>
                                        </span>
                                    </td>
                                    <td><?php echo date('d M Y, H:i', strtotime($comp['date_submitted'])); ?></td>
                                    <td>
                                        <?php if ($comp['status'] === 'Pending'): ?>
                                            <a href="dashboard.php?resolve_complaint=<?php echo $comp['complaint_id']; ?>" class="btn btn-outline" style="padding: 0.4rem 0.8rem; font-size: 0.85rem; border-radius: var(--radius-sm)">
                                                Resolve
                                            </a>
                                        <?php else: ?>
                                            <span style="color: var(--dark-muted); font-size: 0.85rem; font-weight: 600;">No Action</span>
                                        <?php endif; ?>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            <?php endif; ?>
        </div>
    </div>
</main>

<footer>
    <p>&copy; <?php echo date('Y'); ?> HairFidence. Connecting Donors, NGOs, and Cancer Survivors.</p>
</footer>

<script src="../assets/js/main.js"></script>
</body>
</html>
