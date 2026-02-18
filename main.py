#main
from src.models import Transaction, Categories
from src.storage import save_expenses, load_expenses
from src.analytics import filter_by_date_range, filter_by_month, filter_by_category, filter_by_amount
from src.gui import get_date_range, get_month_range, get_expenses_type, get_category, get_amount_bounds
from src.categories import get_all_categories

MONTH_NAMES = {
    1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
    7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"
    }

def main():
    """
    Run the relevant function based on the input number.
    """
    transactions = load_expenses()
    print(f"Loaded {len(transactions)} existing transactions.")

    while True:
        choice = display_menu() # This simultaneously runs display_menu() and stores the input as a variable - the parantheses executes the function

        if choice == "1":
            add_expense(transactions)
        elif choice == "2":
            view_expenses(transactions)
        elif choice == "3":
            view_total(transactions)
        elif choice == "4":
            expenses_analytics(transactions)
        elif choice == "5":
            save_expenses(transactions)
            print("Expenses saved. Goodbye.")
            break
        else:
            print("Error. Please try again.\n")

def display_menu():
    """
    Navbar equivalent
    """
    print("\n=== Expenses Tracker ===")
    print("1. Add a new expense")
    print("2. View expenses")
    print("3. View total expenses")
    print ("4. Expenses analytics")
    print ("5. Quit")
    return input("Choose an option: ")

def add_expense(transactions):
    """
    Adds an expense to data/expenses.csv
    """
    print("\n--- Add an Expense ---")
    date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount: "))
    if amount < 0:
        print ("Invalid amount. Amount must be greater than 0.")
        return
    
    category = input("Category: ").lower()
    if category not in get_all_categories():
        print (f"Invalid category. Please select from: {', ' .join(get_all_categories())}")
        return
    
    vendor = input("Vendor: ")
    notes = input("Notes (if applicable): ")

    new_transaction = Transaction(date, amount, category, vendor, notes)
    transactions.append(new_transaction)
    print ("Expense added!")

def view_expenses(transactions):
    """
    See my expenses using load_expenses
    """ 
    expense_type = get_expenses_type()

    if expense_type == "date":

        start_year, start_month, end_year, end_month = get_month_range()
        filtered_transactions = filter_by_month(transactions, start_month, start_year, end_month, end_year)

        print(f"\n--- All Expenses from {MONTH_NAMES[start_month]} {start_year} to {MONTH_NAMES[end_month]} {end_year} ---")

    elif expense_type == "amount":
        amount_lower_bound, amount_upper_bound = get_amount_bounds()
        filtered_transactions = filter_by_amount(transactions, amount_lower_bound, amount_upper_bound)

        print(f"\n--- All Expenses between {amount_lower_bound} and {amount_upper_bound} ---")

    elif expense_type == "category":
        category_type = get_category(transactions)
        filtered_transactions = filter_by_category(transactions, category_type)

        print(f"\n--- All Expenses in the {category_type} category ---")
    
    else:
        print ("Invalid filter type.")
        return

    if not filtered_transactions:
        print("No transactions available.")
        return
    
    for t in filtered_transactions:
        print (t) # Uses the __str__ method from the Transaction class

def expenses_analytics(transations):
    """
    Various analytics modules for my expenses
    """
    print ("\n--- All Analytics ---")

def view_total(transactions):
    """
    See the sum of my expenses using load_expenses
    """
    total = sum(t.amount for t in transactions)
    print(f"\nTotal spending: £{total:.2f}")

    get_all_categories()

if __name__ == "__main__":
    main()
