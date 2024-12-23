import csv
import os

def get_budget_file(username):
    return f"{username}_budgets.csv"

def set_budget(username, category, budget_amount):
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
    budget_data = get_all_budgets(username)
    budget_status = {}
    category_totals = {}

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    for category, total_spent in category_totals.items():
        if category in budget_data:
            budget = budget_data[category]
            if total_spent >= budget:
                budget_status[category] = "Exceeded"
            elif total_spent >= 0.8 * budget:
                budget_status[category] = "Approaching"
            else:
                budget_status[category] = "Under Budget"
        else:
            budget_status[category] = "No Budget Set"

    for category in budget_data:
        if category not in category_totals:
            budget_status[category] = "Under Budget"

    return budget_status