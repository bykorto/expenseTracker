from src.models import Categories

BUCKETS = ["Needs", "Wants", "Savings", "Growth"]

CATEGORIES = [
    Categories("Rent", "Needs", 0),
    Categories("Bills", "Needs", 0),
    Categories("Groceries", "Needs", 0),
    Categories("Transport", "Needs", 0),

    Categories("Food/drinks", "Wants", 0),
    Categories("Entertainment", "Wants", 0),
    Categories("Hobbies", "Wants", 0),
    Categories("Others", "Wants", 0),

    Categories("Emergency", "Savings", 0),
    Categories("Rainy Day", "Savings", 0),
    Categories("Stocks", "Savings", 0),

    Categories("MU", "Growth", 0),
    Categories("Koan Studios", "Growth", 0),
]

def get_all_categories():
    return [cat.cat_name for cat in CATEGORIES]

def get_all_buckets():
    return [cat.bucket for cat in CATEGORIES]

def get_category_bucket(category_name):
    """
    Look up which bucket a category sits in
    """
    for cat in CATEGORIES:
        if cat.cat_name == category_name:
            return (cat.bucket)
    return None
