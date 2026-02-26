// Get popup elements

const popup = document.getElementById('add-expense-popup');
const openBtn = document.getElementById('navbar-add-expense-btn');
const closeBtn = document.getElementById('close-popup');
const cancelBtn = document.getElementsByClassName('form-cancel-btn');
const submitForm = document.getElementsByClassName('form-submit-btn');

// Open popup

openBtn.addEventListener('click', () => {
    popup.classList.add('active');
    populateCategoryDropdown();
    setDefaultDate();
})

// Populate category dropdown

async function populateCategoryDropdown() {
    const categorySelect = document.getElementById('expense-form-category');
    
    const response = await fetch('http://localhost:8000/api/categories');
    const categoryNames = await response.json();

    categorySelect.innerHTML = '';

    categoryNames.categories.forEach(cat => {
        const option = document.createElement('option');
        option.value = cat;
        option.textContent = cat;
        categorySelect.appendChild(option);
    })
};

// Set default date to today

function setDefaultDate() {
    const dateInput = document.getElementById('expense-form-date');
    const today = new Date().toISOString().split('T')[0];
    dateInput.value = today;
};

// Close popup

function closePopup() {
    popup.classList.remove('active');
    form.reset();
    };

closeBtn.addEventListener('click', closePopup);
cancelBtn.addEventListener('click', closePopup);

popup.addEventListener('click', (e) => {
    if (e.target === popup) {
        closePopup();
    }
})

// Add a new expense

async function addExpense() {
    const form = document.getElementById('add-expense-form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault;

        const formData = {
            date: document.getElementById('expense-form-date').value,
            amount: document.getElementById('expense-form-amount').value,
            category: document.getElementById('expense-form-category').value,
            vendor: document.getElementById('expense-form-vendor').value,
            notes: document.getElementById('expense-form-notes').value
        };
        
        console.log('Submitting: ', formData);

        try {
            const response = await fetch('http://localhost:8000/api/expense', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
        
            if (response.ok) {

            }
        }
    })
}
