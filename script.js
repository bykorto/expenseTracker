// Get current month and year for expenses table

function getCurrentMonthYear() {
    const now = new Date();
    return {
        year: now.getFullYear(),
        month: now.getMonth + 1
    }
}

// Load expenses from the current month from expenses.csv

async function loadExpensesByMonth(year, month) {
    try {
        const response = await fetch(`http://localhost:8000/api/transactions/filter/${year}/${month}`);
        const data = await response.json

        displayExpenses(data, year, month);
    } catch (error) {
        console.error('Error loading expenses: ', error);
    }
}

// Display expenses in the table

function displayExpenses(expenses, year, month) {
    
    // Update expenses header text
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    document.querySelector('.expenses-header-text h1').textContent = 
        `All Expenses in ${monthNames[month - 1]} ${year}`;

    // Get table body
    let tbody = document.querySelector('.expenses-table-section table tbody');
    if (!tbody) {
        tbody = document.createElement('tbody');
        document.querySelector('.expenses-table-section table').appendChild(tbody);
    }

    // Clear existing rows
    tbody.innerHTML = '';

    // Add rows for each expense
    expenses.forEach(expense => {
        const row = document.createElement ('tr');
        row.innerHTML = `
        <td>${expense.date}</td>
        <td>${expense.amount.toFixed(2)}</td>
        <td>${expense.vendor || '-'}</td>
        `;
        tbody.append(row);
    });

    // Show message if no expenses available
    if (expenses.length == 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center;">No Expenses Found</td></tr>';
    }
}

// Populate month and year dropdown

function populateFilters() {
    const { year, month } = getCurrentMonthYear();

    // Populate filters
    const monthSelect = document.getElementById('expenses-filter-month');
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    monthNames.forEach((name, index) => {
        
    })
}

// Load on bootup

window.addEventListener('DOMContentLoaded', () => {
    populateFilters();
    const { year, month } = getCurrentMonthYear();
    loadExpensesByMonth(year, month);
})

