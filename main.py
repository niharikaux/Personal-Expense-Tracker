from flask import Flask, render_template, request
from modules.expense_tracker import add_expense, get_expenses
from modules.budget_manager import set_budget, get_all_budgets, check_budget_status
import matplotlib.pyplot as plt
import os

# Create a Flask app instance
app = Flask(__name__)

# Default username for simplicity
USERNAME = "user1"

@app.route('/', methods=['GET'])
def index():
    """
    Renders the main dashboard page with the user's expenses, budgets,
    and the total amount spent.
    """
    # Get username from query parameters or use default
    username = request.args.get('username', USERNAME)

    # Retrieve user data
    expenses = get_expenses(username)
    budgets = get_all_budgets(username)
    budget_status = check_budget_status(username, expenses)

    # Calculate total amount spent
    total_spent = sum(expense['amount'] for expense in expenses)

    # Render the dashboard with all required data
    return render_template('index.html', expenses=expenses, budgets=budgets,
                           budget_status=budget_status, total_spent=total_spent,
                           username=username)

@app.route('/add-expense', methods=['POST'])
def add_expense_route():
    """
    Handles the addition of a new expense. Validates the input before adding.
    """
    username = request.form.get('username', USERNAME)
    date = request.form.get('date')
    category = request.form.get('category')

    # Validate the amount input
    try:
        amount = float(request.form.get('amount'))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        return "Invalid amount. Please enter a positive number."

    # Add the expense using the helper function
    add_expense(username, date, category, amount)
    return index()

@app.route('/set-budget', methods=['POST'])
def set_budget_route():
    """
    Handles the setting of a budget for a specific category.
    """
    username = request.form.get('username', USERNAME)
    category = request.form.get('budget-category')

    # Validate the budget amount input
    try:
        budget_amount = float(request.form.get('budget-amount'))
        if budget_amount <= 0:
            raise ValueError("Budget amount must be positive.")
    except ValueError:
        return "Invalid budget amount. Please enter a positive number."

    # Set the budget using the helper function
    set_budget(username, category, budget_amount)
    return index()

@app.route('/delete-expense', methods=['POST'])
def delete_expense():
    """
    Handles the deletion of an expense based on the provided data.
    """
    username = request.form.get('username', USERNAME)
    date = request.form.get('date')
    category = request.form.get('category')
    amount = float(request.form.get('amount'))

    # Retrieve all expenses and filter out the one to delete
    expenses = get_expenses(username)
    updated_expenses = [e for e in expenses if not (e['date'] == date and e['category'] == category and e['amount'] == amount)]

    # Overwrite the expense file with updated data
    expense_file = f"{username}_expenses.csv"
    with open(expense_file, 'w') as file:
        for expense in updated_expenses:
            file.write(f"{expense['date']},{expense['category']},{expense['amount']}\n")

    return index()

@app.route('/visualize', methods=['GET'])
def visualize():
    """
    Generates a bar chart of expenses grouped by category and renders it on the visualization page.
    """
    username = USERNAME

    # Retrieve expenses for the user
    expenses = get_expenses(username)

    # Group expenses by category and calculate totals
    category_totals = {}
    for expense in expenses:
        category_totals[expense['category']] = category_totals.get(expense['category'], 0) + expense['amount']

    # Generate the bar chart using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(category_totals.keys(), category_totals.values(), color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount Spent')

    # Save the chart as an image in the static directory
    chart_path = 'static/charts/expense_chart.png'
    os.makedirs('static/charts', exist_ok=True)
    plt.savefig(chart_path)
    plt.close()

    # Render the visualization page with the chart
    return render_template('visualize.html', chart_path=chart_path)

if __name__ == "__main__":
    # Start the Flask application in debug mode
    app.run(debug=True)