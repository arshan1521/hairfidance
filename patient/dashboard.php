<?php
// patient/dashboard.php
require_once '../config/db.php';
require_once '../includes/auth_check.php';

// Enforce that only logged-in Patients can access this page
check_access('patient');

$patient_id = $_SESSION['patient_id'];
$success_msg = '';
$error_msg = '';

// Handle Hair Request Image Verification
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['verify_request_image'])) {
    $request_id = intval($_POST['request_id']);
    if (empty($request_id)) {
        $error_msg = "Invalid request reference.";
    } else {
        try {
            $stmt = $pdo->prepare("UPDATE hair_requests SET patient_verified = 1 WHERE request_id = ? AND patient_id = ?");
            $stmt->execute([$request_id, $patient_id]);
            $success_msg = "You have successfully verified and confirmed the hair specimen image.";
        } catch (PDOException $e) {
            $error_msg = "Verification update failed: " . $e->getMessage();
        }
    }
}

// Handle Hair Request Submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['request_hair'])) {
    $post_id = intval($_POST['post_id']);
    $ngo_id = intval($_POST['ngo_id']);

    if (empty($post_id) || empty($ngo_id)) {
        $error_msg = "Please select an NGO to handle your request.";
    } else {
        try {
            $pdo->beginTransaction();

            // Double check if post is still 'Available' to prevent race conditions
            $check_stmt = $pdo->prepare("SELECT status FROM hair_donation_posts WHERE post_id = ? FOR UPDATE");
            $check_stmt->execute([$post_id]);
            $current_status = $check_stmt->fetchColumn();

            if ($current_status !== 'Available') {
                throw new Exception("This hair asset has already been requested by someone else.");
            }

            // 1. Create a request entry
            $stmt = $pdo->prepare("INSERT INTO hair_requests (patient_id, post_id, ngo_id, status) VALUES (?, ?, ?, 'Pending')");
            $stmt->execute([$patient_id, $post_id, $ngo_id]);

            // 2. Lock the post by setting status to 'Processing'
            $stmt = $pdo->prepare("UPDATE hair_donation_posts SET status = 'Processing' WHERE post_id = ?");
            $stmt->execute([$post_id]);

            $pdo->commit();
            $success_msg = "Your request was successfully submitted and the asset is locked. The selected NGO will verify your records and process it.";
        } catch (Exception $e) {
            if ($pdo->inTransaction()) $pdo->rollBack();
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

// Handle Medical Report Upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['upload_report'])) {
    if (empty($_FILES['medical_report']['name'])) {
        $error_msg = "Please select a file to upload.";
    } else {
        try {
            $file_name = $_FILES['medical_report']['name'];
            $file_tmp = $_FILES['medical_report']['tmp_name'];
            $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
            $allowed_exts = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'];

            if (!in_array($file_ext, $allowed_exts)) {
                throw new Exception("Invalid file type. Allowed: PDF, DOC, DOCX, JPG, PNG.");
            }

            $upload_dir = '../uploads/medical_reports/';
            if (!is_dir($upload_dir)) {
                mkdir($upload_dir, 0777, true);
            }

            $new_file_name = 'report_' . $_SESSION['login_id'] . '_' . time() . '.' . $file_ext;
            $dest_path = 'uploads/medical_reports/' . $new_file_name;

            if (!move_uploaded_file($file_tmp, '../' . $dest_path)) {
                throw new Exception("Failed to upload report file.");
            }

            // Update in database
            $stmt = $pdo->prepare("UPDATE patients SET medical_report_url = ? WHERE patient_id = ?");
            $stmt->execute([$dest_path, $patient_id]);

            $success_msg = "Medical report uploaded and updated successfully.";
        } catch (Exception $e) {
            $error_msg = $e->getMessage();
        }
    }
}

// Fetch patient profile details
$patient_profile = [];
try {
    $stmt = $pdo->prepare("SELECT * FROM patients WHERE patient_id = ?");
    $stmt->execute([$patient_id]);
    $patient_profile = $stmt->fetch();
} catch (PDOException $e) {
    // Fail silently
}

// Filter inputs for Catalog
$filter_type = $_GET['hair_type'] ?? '';
$catalog_query = "SELECT d.*, dn.full_name as donor_name 
                  FROM hair_donation_posts d
                  JOIN donors dn ON d.donor_id = dn.donor_id
                  WHERE d.status = 'Available'";
$params = [];

if (!empty($filter_type)) {
    $catalog_query .= " AND d.hair_type = ?";
    $params[] = $filter_type;
}
$catalog_query .= " ORDER BY d.post_id DESC";

// Fetch Available Hair Catalog
$catalog = [];
try {
    $stmt = $pdo->prepare($catalog_query);
    $stmt->execute($params);
    $catalog = $stmt->fetchAll();
} catch (PDOException $e) {
    $error_msg = "Error loading catalog: " . $e->getMessage();
}

// Fetch list of active/approved NGOs for patient selection
$ngos = [];
try {
    $stmt = $pdo->query("SELECT ngo_id, organization_name FROM ngos WHERE is_approved = 1");
    $ngos = $stmt->fetchAll();
} catch (PDOException $e) {
    // Fail silently
}

// Fetch requests submitted by this patient
$my_requests = [];
try {
    $stmt = $pdo->prepare("SELECT r.request_id, r.status as request_status, r.request_date, r.patient_verified,
                                 n.organization_name as ngo_name,
                                 d.hair_length, d.hair_type, d.image_url
                          FROM hair_requests r
                          JOIN ngos n ON r.ngo_id = n.ngo_id
                          JOIN hair_donation_posts d ON r.post_id = d.post_id
                          WHERE r.patient_id = ?
                          ORDER BY r.request_date DESC");
    $stmt->execute([$patient_id]);
    $my_requests = $stmt->fetchAll();
} catch (PDOException $e) {
    // Fail silently
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Dashboard - HairFidence</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
        .dashboard-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }
        .catalog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-top: 1rem;
        }
        .catalog-card {
            background: white;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            display: flex;
            flex-direction: column;
        }
        .catalog-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-md);
        }
        .catalog-img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
        .catalog-body {
            padding: 1.25rem;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .request-form {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        .thumbnail-image {
            width: 50px;
            height: 50px;
            object-fit: cover;
            border-radius: var(--radius-sm);
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
            HairFidence Patient
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
            <h2>Patient Portal</h2>
            <p>Browse our catalog of verified hair donations, request custom wig manufacturing, and track verification status.</p>
        </div>

        <!-- Alert notifications -->
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
            <!-- Left Side: Catalog and Request History -->
            <div>
                <!-- Catalog Filters -->
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem; margin-bottom: 1rem;">
                    <h3 style="font-size: 1.5rem;">Browse Available Hair</h3>
                    <form action="dashboard.php" method="GET" style="display: flex; gap: 0.5rem; align-items: center;">
                        <label for="filter_type" style="font-size: 0.85rem; font-weight: 600; color: var(--dark-muted)">Filter:</label>
                        <select id="filter_type" name="hair_type" class="form-control form-select" style="padding: 0.4rem 1rem; font-size: 0.85rem; width: auto;" onchange="this.form.submit()">
                            <option value="">All Textures</option>
                            <option value="Straight" <?php echo $filter_type === 'Straight' ? 'selected' : ''; ?>>Straight</option>
                            <option value="Wavy" <?php echo $filter_type === 'Wavy' ? 'selected' : ''; ?>>Wavy</option>
                            <option value="Curly" <?php echo $filter_type === 'Curly' ? 'selected' : ''; ?>>Curly</option>
                            <option value="Coily" <?php echo $filter_type === 'Coily' ? 'selected' : ''; ?>>Coily</option>
                        </select>
                    </form>
                </div>

                <!-- Catalog Grid -->
                <?php if (count($catalog) === 0): ?>
                    <div class="glass-card" style="padding: 2.5rem; text-align: center; color: var(--dark-muted); margin-bottom: 3rem;">
                        No matching hair donations available in the inventory currently. Please check back later.
                    </div>
                <?php else: ?>
                    <div class="catalog-grid" style="margin-bottom: 3rem;">
                        <?php foreach ($catalog as $item): ?>
                            <div class="catalog-card">
                                <img src="../<?php echo htmlspecialchars($item['image_url']); ?>" 
                                     alt="Hair Specimen" 
                                     class="catalog-img"
                                     data-length="<?php echo htmlspecialchars($item['hair_length']); ?>"
                                     data-type="<?php echo htmlspecialchars($item['hair_type']); ?>">
                                <div class="catalog-body">
                                    <div>
                                        <h4 style="font-size: 1.1rem; color: var(--dark); margin-bottom: 0.25rem;">Length: <?php echo htmlspecialchars($item['hair_length']); ?> cm</h4>
                                        <p style="font-size: 0.85rem; color: var(--dark-muted); margin-bottom: 1rem;">Texture: <strong><?php echo htmlspecialchars($item['hair_type']); ?></strong></p>
                                    </div>
                                    
                                    <!-- Request Setup -->
                                    <form action="dashboard.php" method="POST" class="request-form">
                                        <input type="hidden" name="post_id" value="<?php echo $item['post_id']; ?>">
                                        <input type="hidden" name="request_hair" value="1">
                                        
                                        <label for="ngo_select_<?php echo $item['post_id']; ?>" style="font-size: 0.75rem; font-weight: 700; color: var(--dark-muted); margin-bottom: -0.25rem;">Route via NGO:</label>
                                        <select id="ngo_select_<?php echo $item['post_id']; ?>" name="ngo_id" class="form-control form-select" style="padding: 0.4rem; font-size: 0.8rem;" required>
                                            <option value="" disabled selected>-- Select NGO --</option>
                                            <?php foreach ($ngos as $n): ?>
                                                <option value="<?php echo $n['ngo_id']; ?>"><?php echo htmlspecialchars($n['organization_name']); ?></option>
                                            <?php endforeach; ?>
                                        </select>
                                        
                                        <button type="submit" class="btn btn-secondary" style="padding: 0.5rem; font-size: 0.85rem; width: 100%; border-radius: var(--radius-sm);">
                                            Send Hair Request
                                        </button>
                                    </form>
                                </div>
                            </div>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>

                <!-- Request Track Section -->
                <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">View Request Status</h3>
                <?php if (count($my_requests) === 0): ?>
                    <p style="color: var(--dark-muted)">You haven't requested any hair assets yet.</p>
                <?php else: ?>
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>Hair Item</th>
                                    <th>Handling NGO</th>
                                    <th>Request Date</th>
                                    <th>Status</th>
                                    <th>Image Verification</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($my_requests as $req): ?>
                                    <tr>
                                        <td>
                                            <div style="display: flex; align-items: center; gap: 0.75rem;">
                                                <img src="../<?php echo htmlspecialchars($req['image_url']); ?>" 
                                                     alt="Wig Specimen" 
                                                     class="thumbnail-image"
                                                     data-length="<?php echo htmlspecialchars($req['hair_length']); ?>"
                                                     data-type="<?php echo htmlspecialchars($req['hair_type']); ?>"
                                                     data-request-id="<?php echo $req['request_id']; ?>"
                                                     data-verified="<?php echo $req['patient_verified']; ?>">
                                                <div>
                                                    <strong>Length: <?php echo htmlspecialchars($req['hair_length']); ?> cm</strong><br>
                                                    <span style="font-size: 0.8rem; color: var(--dark-muted)">Type: <?php echo htmlspecialchars($req['hair_type']); ?></span>
                                                </div>
                                            </div>
                                        </td>
                                        <td><strong><?php echo htmlspecialchars($req['ngo_name']); ?></strong></td>
                                        <td><?php echo date('d M Y, H:i', strtotime($req['request_date'])); ?></td>
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
                                            <?php if ($req['patient_verified'] == 1): ?>
                                                <span class="badge badge-success" style="display: inline-flex; align-items: center; gap: 0.25rem;">
                                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                                                        <polyline points="20 6 9 17 4 12"></polyline>
                                                    </svg>
                                                    Verified
                                                </span>
                                            <?php else: ?>
                                                <button type="button" class="btn btn-outline" 
                                                        style="padding: 0.3rem 0.6rem; font-size: 0.75rem; border-radius: var(--radius-sm); border-color: var(--secondary); color: var(--secondary); font-weight: 600;"
                                                        onclick="document.querySelector('img[data-request-id=\'<?php echo $req['request_id']; ?>\']').click();">
                                                    Zoom & Verify
                                                </button>
                                            <?php endif; ?>
                                        </td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                <?php endif; ?>
            </div>

            <!-- Right Side: Complaint Actions -->
            <div>
                <!-- Upload Medical Report Form -->
                <div class="glass-card" style="padding: 1.8rem; margin-bottom: 2rem; border-radius: var(--radius-md)">
                    <h3 style="font-size: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.5rem;">Upload Medical Report</h3>
                    <?php if (!empty($patient_profile['medical_report_url'])): ?>
                        <div style="margin-bottom: 1.5rem; font-size: 0.9rem;">
                            <span style="color: var(--dark-muted)">Current Report:</span><br>
                            <a href="../<?php echo htmlspecialchars($patient_profile['medical_report_url']); ?>" target="_blank" class="btn btn-outline animate-fade-in" style="padding: 0.4rem 0.8rem; font-size: 0.85rem; margin-top: 0.5rem; display: inline-flex; width: 100%;">
                                📄 View Uploaded Report
                            </a>
                        </div>
                    <?php endif; ?>
                    <form action="dashboard.php" method="POST" enctype="multipart/form-data">
                        <input type="hidden" name="upload_report" value="1">
                        <div class="form-group">
                            <label for="med_report_upload">Select New Report</label>
                            <input type="file" id="med_report_upload" name="medical_report" class="form-control" required>
                            <span style="font-size: 0.75rem; color: var(--dark-muted)">Allowed: PDF, DOC, DOCX, JPG, PNG (Max 5MB)</span>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Upload Report</button>
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
                            <textarea id="comp_desc" name="description" class="form-control" placeholder="Describe your issue here..." required></textarea>
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

<!-- ZOOM & VERIFY MODAL OVERLAY -->
<div id="zoomOverlay" class="zoom-modal-overlay">
    <div class="zoom-modal-container">
        <div class="zoom-modal-header">
            <h3>Inspect Specimen</h3>
            <button type="button" id="zoomClose" class="zoom-modal-close-btn" title="Close modal">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
        
        <!-- Image viewport with floating controls -->
        <div class="zoom-image-viewport">
            <img id="zoomImg" src="" alt="Specimen Zoom" class="zoom-image-element">
            <div class="zoom-controls-toolbar">
                <button type="button" id="zoomInBtn" class="zoom-tool-btn" title="Zoom In">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        <line x1="11" y1="8" x2="11" y2="14"></line>
                        <line x1="8" y1="11" x2="14" y2="11"></line>
                    </svg>
                </button>
                <button type="button" id="zoomOutBtn" class="zoom-tool-btn" title="Zoom Out">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        <line x1="8" y1="11" x2="14" y2="11"></line>
                    </svg>
                </button>
                <button type="button" id="zoomResetBtn" class="zoom-tool-btn" title="Reset Zoom">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M23 4v6h-6M1 20v-6h6M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                    </svg>
                </button>
            </div>
        </div>

        <!-- Info & Verification Actions -->
        <div class="zoom-modal-body">
            <div class="zoom-hair-info">
                <div class="zoom-info-item">
                    <div class="zoom-info-label">Specimen Length</div>
                    <div id="zoomLength" class="zoom-info-val">-</div>
                </div>
                <div class="zoom-info-item">
                    <div class="zoom-info-label">Hair Texture</div>
                    <div id="zoomType" class="zoom-info-val">-</div>
                </div>
            </div>

            <div id="zoomVerificationSection" class="zoom-verification-actions">
                <!-- Populated dynamically by JS -->
            </div>
        </div>
    </div>
</div>

<script src="../assets/js/main.js"></script>
</body>
</html>
