import csv
import os

def get_expense_file(username):
    """Generate the file name for storing a user's expenses."""
    return f"{username}_expenses.csv"

def add_expense(username, date, category, amount):
    """Appends a new expense to the user's expense CSV file."""
    expense_file = get_expense_file(username)
    try:
        with open(expense_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])
    except IOError as e:
        print(f"Error writing to file {expense_file}: {e}")

def get_expenses(username):
    """Reads all expenses from the user's expense CSV file and returns them as a list of dictionaries."""
    expense_file = get_expense_file(username)
    expenses = []
    if not os.path.exists(expense_file):
        return expenses  # Return an empty list if the file doesn't exist yet

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