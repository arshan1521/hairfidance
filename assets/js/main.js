// assets/js/main.js
// General front-end logic and dynamic UI behavior for HairFidence

document.addEventListener('DOMContentLoaded', function() {
    
    // Dynamic Role-based registration field toggles
    const roleSelect = document.getElementById('register_role');
    if (roleSelect) {
        const donorFields = document.getElementById('donor_fields');
        const patientFields = document.getElementById('patient_fields');
        const ngoFields = document.getElementById('ngo_fields');

        function toggleRoleFields() {
            const role = roleSelect.value;
            
            // Hide all first
            if (donorFields) donorFields.style.display = 'none';
            if (patientFields) patientFields.style.display = 'none';
            if (ngoFields) ngoFields.style.display = 'none';

            // Show selected
            if (role === 'donor') {
                if (donorFields) donorFields.style.display = 'block';
            } else if (role === 'patient') {
                if (patientFields) patientFields.style.display = 'block';
            } else if (role === 'ngo') {
                if (ngoFields) ngoFields.style.display = 'block';
            }
        }

        roleSelect.addEventListener('change', toggleRoleFields);
        toggleRoleFields(); // Run on load in case of browser auto-fill
    }

    // Password Match Validation
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const registerForm = document.getElementById("register_form");

    if (registerForm && password && confirmPassword) {
        registerForm.addEventListener('submit', function(event) {
            if (password.value !== confirmPassword.value) {
                event.preventDefault();
                alert("Passwords do not match!");
            }
        });
    }

    // Image/File Input Previews
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                const fileName = this.files[0].name;
                const fileLabel = document.querySelector(`label[for="${this.id}"] .upload-text`);
                if (fileLabel) {
                    fileLabel.textContent = `Selected: ${fileName}`;
                }
            }
        });
    });

    // Alert Auto-Dismiss after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s ease';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // ZOOM MODAL LOGIC
    const zoomOverlay = document.getElementById('zoomOverlay');
    const zoomImg = document.getElementById('zoomImg');
    const zoomLength = document.getElementById('zoomLength');
    const zoomType = document.getElementById('zoomType');
    const zoomClose = document.getElementById('zoomClose');
    const zoomInBtn = document.getElementById('zoomInBtn');
    const zoomOutBtn = document.getElementById('zoomOutBtn');
    const zoomResetBtn = document.getElementById('zoomResetBtn');
    const zoomVerificationSection = document.getElementById('zoomVerificationSection');

    let currentScale = 1;
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let translateX = 0;
    let translateY = 0;

    function updateImageTransform() {
        if (zoomImg) {
            zoomImg.style.transform = `scale(${currentScale}) translate(${translateX}px, ${translateY}px)`;
        }
    }

    function resetZoom() {
        currentScale = 1;
        translateX = 0;
        translateY = 0;
        updateImageTransform();
    }

    if (zoomOverlay && zoomImg) {
        // Close modal when close button is clicked or clicking outside container
        zoomClose.addEventListener('click', () => {
            zoomOverlay.classList.remove('active');
            resetZoom();
        });

        zoomOverlay.addEventListener('click', (e) => {
            if (e.target === zoomOverlay) {
                zoomOverlay.classList.remove('active');
                resetZoom();
            }
        });

        // Zoom Controls
        zoomInBtn.addEventListener('click', () => {
            currentScale = Math.min(currentScale + 0.3, 4.0);
            updateImageTransform();
        });

        zoomOutBtn.addEventListener('click', () => {
            currentScale = Math.max(currentScale - 0.3, 0.5);
            updateImageTransform();
        });

        zoomResetBtn.addEventListener('click', resetZoom);

        // Mouse Drag Panning
        zoomImg.addEventListener('mousedown', (e) => {
            e.preventDefault();
            if (currentScale <= 1) return; // Only pan when zoomed in
            isDragging = true;
            zoomImg.style.transition = 'none'; // Disable transition during drag for smoothness
            startX = e.clientX - translateX;
            startY = e.clientY - translateY;
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            translateX = e.clientX - startX;
            translateY = e.clientY - startY;
            updateImageTransform();
        });

        window.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                zoomImg.style.transition = 'transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1)';
            }
        });

        // Setup triggers for all zoomable images (catalog images and thumbnails)
        const zoomableImages = document.querySelectorAll('.catalog-img, .thumbnail-image');
        zoomableImages.forEach(img => {
            img.addEventListener('click', function() {
                const src = this.getAttribute('src');
                const length = this.getAttribute('data-length') || 'N/A';
                const type = this.getAttribute('data-type') || 'N/A';
                const requestId = this.getAttribute('data-request-id');
                const verified = this.getAttribute('data-verified');

                // Load source into modal img
                zoomImg.src = src;
                zoomLength.textContent = length + (length !== 'N/A' ? ' cm' : '');
                zoomType.textContent = type;

                // Configure verification panel
                if (requestId) {
                    if (verified === '1') {
                        zoomVerificationSection.innerHTML = `
                            <div class="zoom-badge-verified">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="20 6 9 17 4 12"></polyline>
                                </svg>
                                Image Verified by Survivor
                            </div>
                        `;
                    } else {
                        zoomVerificationSection.innerHTML = `
                            <form action="dashboard.php" method="POST">
                                <input type="hidden" name="verify_request_image" value="1">
                                <input type="hidden" name="request_id" value="${requestId}">
                                <div class="verification-consent">
                                    <input type="checkbox" id="verify_consent" name="verify_consent" required>
                                    <label for="verify_consent">
                                        I verify that I have checked the detailed zoom image of this hair specimen and confirm it matches my preferences.
                                    </label>
                                </div>
                                <button type="submit" class="btn btn-secondary" style="width: 100%; border-radius: var(--radius-sm); padding: 0.6rem; font-size: 0.85rem;">
                                    Confirm Visual Verification
                                </button>
                            </form>
                        `;
                    }
                    zoomVerificationSection.style.display = 'block';
                } else {
                    // It's a catalog image (no request created yet)
                    zoomVerificationSection.innerHTML = `
                        <p style="font-size: 0.85rem; color: var(--dark-muted)">
                            Verify details & texture alignment in zoom mode before routing your request via an NGO.
                        </p>
                    `;
                    zoomVerificationSection.style.display = 'block';
                }

                // Show overlay
                zoomOverlay.classList.add('active');
                resetZoom();
            });
        });
    }
});

