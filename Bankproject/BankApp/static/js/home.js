// Modal functionality
function openModal(modalType) {
    const modal = document.getElementById(modalType + 'Modal');
    modal.style.display = 'block';
}

function closeModal(modalType) {
    const modal = document.getElementById(modalType + 'Modal');
    modal.style.display = 'none';
}

function switchModal(modalType) {
    closeModal('login');
    closeModal('signup');
    openModal(modalType);
}

// Close modal when clicking outside
window.onclick = function(event) {
    const loginModal = document.getElementById('loginModal');
    const signupModal = document.getElementById('signupModal');
    
    if (event.target === loginModal) {
        loginModal.style.display = 'none';
    }
    if (event.target === signupModal) {
        signupModal.style.display = 'none';
    }
}

// PIN input validation
document.addEventListener('DOMContentLoaded', function() {
    const pinInput = document.getElementById('pin');
    if (pinInput) {
        pinInput.addEventListener('input', function(e) {
            this.value = this.value.replace(/\D/g, '').slice(0, 4);
        });
    }
});

// Form submission handling
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('#loginModal .auth-form');
    const signupForm = document.querySelector('#signupModal .auth-form');
    
    // if (loginForm) {
    //     loginForm.addEventListener('submit', function(e) {
    //         e.preventDefault();
    //         // Add your login logic here
    //         alert('Login functionality would be implemented here');
    //     });
    // }
    
    // if (signupForm) {
    //     signupForm.addEventListener('submit', function(e) {
    //         e.preventDefault();
    //         // Add your signup logic here
    //         alert('Signup functionality would be implemented here');
    //     });
    // }
});

