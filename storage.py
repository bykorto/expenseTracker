#src.storage
import csv
import os
from src.models import Transaction

DATA_FILE = "data/expenses.csv"

def save_expenses(transactions):
    """
    Create a new DATA_FILE if it doesn't exist, and save the expense which was input by the user there
    """
    os.makedirs("data", exist_ok=True) # Create data directory if it doesn't exist

    with open(DATA_FILE, 'w', newline='') as file: # Creates the expenses.csv file if it doesn't exist
        writer = csv.writer(file) # Writes in the designated file
        writer.writerow(["date", "amount", "category", "vendor", "notes"]) # Creates header row
        for t in transactions:
            writer.writerow([t.date, t.amount, t.category, t.vendor, t.notes])
    
def load_expenses():
    """
    Load transactions from expenses.csv and return a list of objects
    """
    transactions = []

    if not os.path.exists(DATA_FILE):
        return transactions # Return an empty list if data/expenses.csv doesn't exist yet
    
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file) # Reads each row as a dictionary

        for row in reader:
            t = Transaction(
                date=row["date"],
                amount=float(row["amount"]),
                category=row["category"],
                vendor=row["vendor"],
                notes=row["notes"]
            )
            transactions.append(t)

    return transactions
