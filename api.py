from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.storage import load_expenses, save_expenses
from src.models import Transaction, Categories
from src.analytics import (
    filter_by_date_range, 
    filter_by_month, 
    filter_by_category, 
    filter_by_amount
)
from src.categories import (
    get_all_buckets,
    get_all_categories,
    get_category_bucket
)

app = FastAPI(title="Expense Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransactionCreate(BaseModel):
    date: str
    amount: float
    category: str
    vendor: str
    notes: str

class TransactionResponse(BaseModel):
    date: str
    amount: float
    category: str
    bucket: str = None
    vendor: str = None
    notes: str = None

# ========== ENDPOINTS ==========

@app.get("/")
def root():
    """ API health check """
    return {"message": "API is running"}

@app.get("/api/transactions", response_model = list[TransactionResponse]) # pulls all transactions
def get_all_transactions():
    transactions = load_expenses()
    return [
        {
            "date": t.date,
            "amount": t.amount,
            "category": t.category,
            #"bucket": get_category_bucket(t.category),
            #"vendor": t.vendor,
            #"notes": t.notes
        }
        for t in transactions
    ]

@app.get("/api/categories")
def get_categories():
    return {
        "categories": get_all_categories()
    }

@app.post("/api/expense", response_model = TransactionResponse) # saves new expense
def create_transaction(t: TransactionCreate):
    transactions = load_expenses()
    new_transaction = Transaction(
        date = t.date,
        amount = t.amount,
        category = t.category,
        vendor = t.vendor,
        notes = t.notes
    )
    transactions.append(new_transaction)
    save_expenses(transactions)
    
    return {
        "date": new_transaction.date,
        "amount": new_transaction.amount,
        "category": new_transaction.category,
        "bucket": get_category_bucket(new_transaction.category),
        "vendor": new_transaction.vendor,
        "notes": new_transaction.notes
    }

@app.get("/api/transactions/filter/month/{year}/{month}", response_model = list[TransactionResponse])
def get_transactions_filtered_by_month(year: int, month: int):
    transactions = load_expenses()
    filtered_transactions = filter_by_month(transactions, year, month, year, month)
    return [
        {
            "date": t.date,
            "amount": t.amount,
            "category": t.category,
            "bucket": get_category_bucket(t.category),
            "vendor": t.vendor,
            "notes": t.notes
        }
        for t in filtered_transactions
    ]
