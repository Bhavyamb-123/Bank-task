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


// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
    }

    // Load transaction data if on account page
    if (document.getElementById('transactionList')) {
        loadTransactions();
        setupTransactionFilter();
    }
});

// Transaction data
const transactions = [
    {
        id: 1,
        type: 'credit',
        description: 'Salary Deposit',
        category: 'Income',
        amount: 5000.00,
        date: '2024-01-15',
        icon: '💰'
    },
    {
        id: 2,
        type: 'debit',
        description: 'Grocery Store',
        category: 'Food & Dining',
        amount: 125.50,
        date: '2024-01-14',
        icon: '🛒'
    },
    {
        id: 3,
        type: 'debit',
        description: 'Electric Bill',
        category: 'Utilities',
        amount: 89.25,
        date: '2024-01-13',
        icon: '⚡'
    },
    {
        id: 4,
        type: 'credit',
        description: 'Freelance Payment',
        category: 'Income',
        amount: 750.00,
        date: '2024-01-12',
        icon: '💻'
    },
    {
        id: 5,
        type: 'debit',
        description: 'Gas Station',
        category: 'Transportation',
        amount: 45.80,
        date: '2024-01-11',
        icon: '⛽'
    },
    {
        id: 6,
        type: 'debit',
        description: 'Coffee Shop',
        category: 'Food & Dining',
        amount: 12.75,
        date: '2024-01-10',
        icon: '☕'
    },
    {
        id: 7,
        type: 'debit',
        description: 'Online Shopping',
        category: 'Shopping',
        amount: 199.99,
        date: '2024-01-09',
        icon: '📦'
    },
    {
        id: 8,
        type: 'credit',
        description: 'Bank Interest',
        category: 'Income',
        amount: 25.50,
        date: '2024-01-08',
        icon: '🏦'
    }
];

// Load and display transactions
function loadTransactions(filter = 'all') {
    const transactionList = document.getElementById('transactionList');
    if (!transactionList) return;

    let filteredTransactions = transactions;
    
    if (filter === 'credit') {
        filteredTransactions = transactions.filter(t => t.type === 'credit');
    } else if (filter === 'debit') {
        filteredTransactions = transactions.filter(t => t.type === 'debit');
    }

    transactionList.innerHTML = filteredTransactions.map(transaction => {
        const formattedDate = new Date(transaction.date).toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric'
        });
        
        const amountPrefix = transaction.type === 'credit' ? '+' : '-';
        const amountClass = transaction.type === 'credit' ? 'credit' : 'debit';
        
        return `
            <div class="transaction-item">
                <div class="transaction-info">
                    <div class="transaction-icon ${transaction.type}">
                        ${transaction.icon}
                    </div>
                    <div class="transaction-details">
                        <h4>${transaction.description}</h4>
                        <p>${transaction.category}</p>
                    </div>
                </div>
                <div class="transaction-amount">
                    <div class="amount ${amountClass}">
                        ${amountPrefix}$${transaction.amount.toFixed(2)}
                    </div>
                    <div class="date">${formattedDate}</div>
                </div>
            </div>
        `;
    }).join('');
}

// Setup transaction filter
function setupTransactionFilter() {
    const filterSelect = document.querySelector('.filter-select');
    if (!filterSelect) return;

    filterSelect.addEventListener('change', function() {
        const filterValue = this.value.toLowerCase();
        let filter = 'all';
        
        if (filterValue.includes('credit')) {
            filter = 'credit';
        } else if (filterValue.includes('debit')) {
            filter = 'debit';
        }
        
        loadTransactions(filter);
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading animation for buttons
document.querySelectorAll('.btn-primary, .btn-secondary').forEach(button => {
    button.addEventListener('click', function() {
        if (!this.classList.contains('loading')) {
            this.classList.add('loading');
            const originalText = this.textContent;
            this.textContent = 'Loading...';
            
            setTimeout(() => {
                this.classList.remove('loading');
                this.textContent = originalText;
            }, 2000);
        }
    });
});

