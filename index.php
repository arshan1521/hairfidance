<?php
// index.php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HairFidence - Cancer Patient Hair Donation Management</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        /* Unique home animations and styling overlays */
        .hero-banner {
            padding: 8rem 2rem 6rem 2rem;
            position: relative;
            background: linear-gradient(135deg, rgba(14, 165, 233, 0.05) 0%, rgba(16, 185, 129, 0.05) 100%);
            border-bottom: 1px solid var(--border-color);
        }
        .stats-section {
            background: white;
            padding: 5rem 2rem;
            border-bottom: 1px solid var(--border-color);
        }
        .info-card {
            background: var(--light);
            border-radius: var(--radius-md);
            padding: 2rem;
            border: 1px solid var(--border-color);
            transition: var(--transition);
        }
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
        }
        .feature-icon {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-sm);
            background: rgba(14, 165, 233, 0.1);
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        }
        .info-card:nth-child(2) .feature-icon {
            background: rgba(16, 185, 129, 0.1);
            color: var(--secondary);
        }
        .info-card:nth-child(3) .feature-icon {
            background: rgba(124, 58, 237, 0.1);
            color: #7c3aed;
        }
    </style>
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
            <li><a href="index.php" class="nav-item active">Home</a></li>
            <?php if (isset($_SESSION['user_id'])): ?>
                <li><a href="auth/dashboard_redirect.php" class="nav-item">Dashboard</a></li>
                <li><a href="auth/logout.php" class="btn btn-outline" style="padding: 0.5rem 1rem;">Logout (<?php echo htmlspecialchars($_SESSION['name']); ?>)</a></li>
            <?php else: ?>
                <li><a href="login.php" class="nav-item">Login</a></li>
                <li><a href="register.php" class="btn btn-primary" style="color: white; padding: 0.5rem 1rem;">Register</a></li>
            <?php endif; ?>
        </ul>
    </div>
</header>

<section class="hero-banner">
    <div class="hero animate-fade-in">
        <h1>Restoring Confidence, One Lock at a Time.</h1>
        <p>HairFidence is a secure, digital platform designed to bridge the gap between hair donors, verified cancer patients, and compassionate NGOs to streamline wig making and distribution.</p>
        <div class="cta-group">
            <?php if (isset($_SESSION['user_id'])): ?>
                <a href="auth/dashboard_redirect.php" class="btn btn-primary">Go to Dashboard</a>
            <?php else: ?>
                <a href="register.php" class="btn btn-primary">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                    </svg>
                    Donate Hair
                </a>
                <a href="register.php" class="btn btn-secondary">
                    Request a Wig
                </a>
            <?php endif; ?>
        </div>
    </div>
</section>

<section class="stats-section">
    <div class="container">
        <h2 style="text-align: center; margin-bottom: 3rem; font-size: 2.2rem;">Impact Dashboard</h2>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">1,420+</div>
                <div class="stat-label">Hair Donations</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">380+</div>
                <div class="stat-label">Wigs Distributed</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">15+</div>
                <div class="stat-label">Active Partner NGOs</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">99%</div>
                <div class="stat-label">Trust Index</div>
            </div>
        </div>
    </div>
</section>

<section style="padding: 6rem 2rem; background: var(--light);">
    <div class="container">
        <h2 style="text-align: center; margin-bottom: 4rem; font-size: 2.2rem;">How HairFidence Works</h2>
        <div class="grid-3">
            <div class="info-card">
                <div class="feature-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/>
                        <path d="M12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/>
                    </svg>
                </div>
                <h3>1. Donors post detail</h3>
                <p>Individuals fill details about their hair (length, quality, shade) and submit a visual check post. Hair is logged securely in our records.</p>
            </div>
            <div class="info-card">
                <div class="feature-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                        <polyline points="10 9 9 9 8 9"/>
                    </svg>
                </div>
                <h3>2. NGOs Authenticate</h3>
                <p>Reputable medical NGOs inspect medical transcripts uploaded by cancer survivors requesting wig support, preventing resource misallocation.</p>
            </div>
            <div class="info-card">
                <div class="feature-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                        <line x1="16" y1="2" x2="16" y2="6"/>
                        <line x1="8" y1="2" x2="8" y2="6"/>
                        <line x1="3" y1="10" x2="21" y2="10"/>
                    </svg>
                </div>
                <h3>3. Custom Delivery</h3>
                <p>When patient matches are authorized, NGOs facilitate local wig manufacturing drives, delivering final wigs to patients with tracking logs.</p>
            </div>
        </div>
    </div>
</section>

<footer>
    <p>&copy; <?php echo date('Y'); ?> HairFidence. Connecting Donors, NGOs, and Cancer Survivors.</p>
    
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
