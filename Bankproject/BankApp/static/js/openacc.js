let currentStep = 1;
const totalSteps = 4;
let selectedAccountType = '';

// Initialize form
document.addEventListener('DOMContentLoaded', function() {
    // Account type selection
    const accountCards = document.querySelectorAll('.account-type-card');
    accountCards.forEach(card => {
        card.addEventListener('click', function() {
            accountCards.forEach(c => c.classList.remove('selected'));
            this.classList.add('selected');
            selectedAccountType = this.dataset.type;
        });
    });

    // Form submission
    document.getElementById('accountForm').addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Application submitted successfully! We will review your application and contact you within 2-3 business days.');
    });

    updateFormDisplay();
});

function changeStep(direction) {
    if (direction === 1 && currentStep < totalSteps) {
        if (validateCurrentStep()) {
            currentStep++;
            updateFormDisplay();
            updateReviewData();
        }
    } else if (direction === -1 && currentStep > 1) {
        currentStep--;
        updateFormDisplay();
    }
}

function validateCurrentStep() {
    switch(currentStep) {
        case 1:
            if (!selectedAccountType) {
                alert('Please select an account type.');
                return false;
            }
            break;
        case 2:
            const requiredFields = ['firstName', 'lastName', 'email', 'phone', 'dateOfBirth', 'ssn', 'address', 'city', 'state', 'zipCode', 'employment', 'income'];
            for (let field of requiredFields) {
                const element = document.getElementById(field);
                if (!element.value.trim()) {
                    alert(`Please fill in the ${field.replace(/([A-Z])/g, ' $1').toLowerCase()} field.`);
                    element.focus();
                    return false;
                }
            }
            break;
        case 3:
            const securityQ1 = document.getElementById('securityQuestion1');
            const securityQ2 = document.getElementById('securityQuestion2');
            if (!securityQ1.value.trim() || !securityQ2.value.trim()) {
                alert('Please answer both security questions.');
                return false;
            }
            break;
        case 4:
            const agreeTerms = document.getElementById('agreeTerms');
            if (!agreeTerms.checked) {
                alert('Please agree to the Terms and Conditions to continue.');
                return false;
            }
            break;
    }
    return true;
}

function updateFormDisplay() {
    // Hide all steps
    document.querySelectorAll('.form-step').forEach(step => {
        step.classList.remove('active');
    });
    
    // Show current step
    document.getElementById(`step${currentStep}`).classList.add('active');
    
    // Update progress bar
    document.querySelectorAll('.progress-step').forEach((step, index) => {
        step.classList.remove('active', 'completed');
        if (index + 1 === currentStep) {
            step.classList.add('active');
        } else if (index + 1 < currentStep) {
            step.classList.add('completed');
        }
    });
    
    // Update navigation buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    
    prevBtn.style.display = currentStep === 1 ? 'none' : 'inline-block';
    nextBtn.style.display = currentStep === totalSteps ? 'none' : 'inline-block';
    submitBtn.style.display = currentStep === totalSteps ? 'inline-block' : 'none';
}

function updateReviewData() {
    if (currentStep === 4) {
        // Update account type
        document.getElementById('reviewAccountType').textContent = 
            selectedAccountType === 'checking' ? 'Checking Account' : 'Savings Account';
        
        // Update personal info
        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        document.getElementById('reviewName').textContent = `${firstName} ${lastName}`;
        document.getElementById('reviewEmail').textContent = document.getElementById('email').value;
        document.getElementById('reviewPhone').textContent = document.getElementById('phone').value;
    }
}