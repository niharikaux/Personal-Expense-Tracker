# modules/expense_tracker.py

# Function to add an expense to the list
def add_expense(expenses, date, category, amount):
    expense = {
        'date': date,
        'category': category,
        'amount': amount
    }
    expenses.append(expense)

# Function to retrieve the current list of expenses
def get_expenses(expenses):
    return expenses
