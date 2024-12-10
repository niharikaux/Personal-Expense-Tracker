def add_expense(username, date, category, amount):
    """
    Adds a new expense for the specified user.

    Args:
        username (str): The user's identifier.
        date (str): The date of the expense.
        category (str): The category of the expense.
        amount (float): The amount of the expense.

    Returns:
        None
    """
    expense_file = f"{username}_expenses.csv"

    # Append the new expense to the user's CSV file
    with open(expense_file, 'a') as file:
        file.write(f"{date},{category},{amount}\n")


def get_expenses(username):
    """
    Retrieves all expenses for the specified user.

    Args:
        username (str): The user's identifier.

    Returns:
        list: A list of expenses as dictionaries.
    """
    expense_file = f"{username}_expenses.csv"
    expenses = []

    # Read the expense file and parse each line into a dictionary
    with open(expense_file, 'r') as file:
        for line in file:
            date, category, amount = line.strip().split(',')
            expenses.append({
                'date': date,
                'category': category,
                'amount': float(amount)
            })

    return expenses