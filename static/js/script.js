// Form validation and enhancement
document.addEventListener('DOMContentLoaded', function() {
    // Diagnosis form validation
    const diagnosisForm = document.getElementById('diagnosisForm');
    if (diagnosisForm) {
        diagnosisForm.addEventListener('submit', function(e) {
            // Basic validation
            const age = parseInt(document.getElementById('age').value);
            const bp = parseInt(document.getElementById('bp').value);
            const glucose = parseInt(document.getElementById('glucose').value);
            const heartRate = parseInt(document.getElementById('heart_rate').value);
            
            let isValid = true;
            let errorMessage = '';
            
            // Age validation
            if (age < 1 || age > 120) {
                errorMessage += 'Age must be between 1 and 120.\\n';
                isValid = false;
            }
            
            // Blood pressure validation
            if (bp < 60 || bp > 250) {
                errorMessage += 'Blood pressure seems unusual (60-250 mmHg).\\n';
                isValid = false;
            }
            
            // Glucose validation
            if (glucose < 50 || glucose > 500) {
                errorMessage += 'Glucose level seems unusual (50-500 mg/dL).\\n';
                isValid = false;
            }
            
            // Heart rate validation
            if (heartRate < 40 || heartRate > 200) {
                errorMessage += 'Heart rate seems unusual (40-200 bpm).\\n';
                isValid = false;
            }
            
            if (!isValid) {
                e.preventDefault();
                alert(errorMessage);
            }
            else {
                // show spinner and disable submit to indicate progress (frontend only)
                const submitBtn = document.getElementById('submitBtn');
                const spinner = document.getElementById('formSpinner');
                if (submitBtn) submitBtn.disabled = true;
                if (spinner) spinner.classList.add('visible');
            }
        });
    }
    
    // Login form enhancement
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value;
            
            if (username === '' || password === '') {
                e.preventDefault();
                alert('Please fill in all fields');
            }
        });
    }
    
    // Register form enhancement
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value;
            
            if (username === '' || password === '') {
                e.preventDefault();
                alert('Please fill in all fields');
                return;
            }
            
            if (username.length < 3) {
                e.preventDefault();
                alert('Username must be at least 3 characters long');
                return;
            }
            
            if (password.length < 6) {
                e.preventDefault();
                alert('Password must be at least 6 characters long');
                return;
            }
        });
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 500);
        }, 5000);
    });
    
    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Table search functionality (if needed in future)
    const searchInput = document.getElementById('tableSearch');
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const filter = this.value.toLowerCase();
            const table = document.querySelector('.patient-table');
            const rows = table.querySelectorAll('tbody tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(filter) ? '' : 'none';
            });
        });
    }
});

// Utility function to format date
function formatDate(dateString) {
    const options = { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric', 
        hour: '2-digit', 
        minute: '2-digit' 
    };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Print functionality for results
function printResult() {
    window.print();
}

// Console welcome message
console.log('%c Automated Diagnostic System ', 'background: #667eea; color: white; font-size: 20px; padding: 10px;');
console.log('%c Powered by Machine Learning ', 'background: #764ba2; color: white; font-size: 14px; padding: 5px;');
