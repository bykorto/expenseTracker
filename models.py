#src.models
import datetime

class Transaction():
    def __init__(self, date, amount, category, vendor, notes):
        self.date = date # store as string, YYYY-MM-DD
        self.amount = amount
        self.category = category # categories to be defined
        self.vendor = vendor
        self.notes = notes
    
    def __str__(self):
        return f"{self.date}: £{self.amount} - {self.category} from {self.vendor} ({self.notes})"

class Categories():
    def __init__(self, cat_name, bucket, budget):
        self.cat_name = cat_name
        self.bucket = bucket
        self.budget = budget
