import csv
import os

def get_expense_file(username):
    return f"{username}_expenses.csv"

def add_expense(username, date, category, amount):
    expense_file = get_expense_file(username)
    try:
        with open(expense_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])
    except IOError as e:
        print(f"Error writing to file {expense_file}: {e}")

def get_expenses(username):
    expense_file = get_expense_file(username)
    expenses = []
    if not os.path.exists(expense_file):
        return expenses

    try:
        with open(expense_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    expenses.append({
                        'date': row[0],
                        'category': row[1],
                        'amount': float(row[2])
                    })
    except IOError as e:
        print(f"Error reading from file {expense_file}: {e}")
    except ValueError:
        print("Invalid data format in expenses file.")
    
    return expenses