import os
import csv

def get_budget_file(username):
    """Generate the file name for storing a user's budget data."""
    return f"{username}_budgets.csv"

def set_budget(username, category, budget_amount):
    """Sets or updates a budget for a specific category in the user's budget CSV file."""
    budget_file = get_budget_file(username)
    budget_data = get_all_budgets(username)
    budget_data[category] = budget_amount

    try:
        with open(budget_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for cat, amount in budget_data.items():
                writer.writerow([cat, amount])
    except IOError as e:
        print(f"Error writing to budget file: {e}")

def get_all_budgets(username):
    """Retrieves all budgets from the user's budget CSV file and returns them as a dictionary."""
    budget_file = get_budget_file(username)
    budgets = {}
    if not os.path.exists(budget_file):
        return budgets

    try:
        with open(budget_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    budgets[row[0]] = float(row[1])
    except IOError as e:
        print(f"Error reading from budget file: {e}")
    except ValueError:
        print("Invalid data format in budget file.")
    
    return budgets

def check_budget_status(username, expenses):
    """Checks if expenses are approaching or exceeding the set budget for each category."""
    budget_data = get_all_budgets(username)
    budget_status = {}

    for category, budget in budget_data.items():
        total_spent = sum(exp['amount'] for exp in expenses if exp['category'] == category)
        
        if total_spent >= budget:
            budget_status[category] = "Exceeded"
        elif total_spent >= 0.8 * budget:
            budget_status[category] = "Approaching"
        else:
            budget_status[category] = "Under Budget"
    
    return budget_status