from flask import Flask, render_template, request
from modules.expense_tracker import add_expense, get_expenses
from modules.budget_manager import set_budget, get_all_budgets, check_budget_status
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Default username for simplicity
USERNAME = "user1"

@app.route('/', methods=['GET'])
def index():
    username = request.args.get('username', USERNAME)
    expenses = get_expenses(username)
    budgets = get_all_budgets(username)
    budget_status = check_budget_status(username, expenses)
    return render_template('index.html', expenses=expenses, budgets=budgets, budget_status=budget_status, username=username)

@app.route('/add-expense', methods=['POST'])
def add_expense_route():
    username = request.form.get('username', USERNAME)
    date = request.form.get('date')
    category = request.form.get('category')
    try:
        amount = float(request.form.get('amount'))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        return "Invalid amount. Please enter a positive number."

    add_expense(username, date, category, amount)
    return index()

@app.route('/set-budget', methods=['POST'])
def set_budget_route():
    username = request.form.get('username', USERNAME)
    category = request.form.get('budget-category')
    try:
        budget_amount = float(request.form.get('budget-amount'))
        if budget_amount <= 0:
            raise ValueError("Budget amount must be positive.")
    except ValueError:
        return "Invalid budget amount. Please enter a positive number."

    set_budget(username, category, budget_amount)
    return index()

@app.route('/visualize', methods=['GET'])
def visualize():
    username = USERNAME
    expenses = get_expenses(username)
    categories = {}
    for expense in expenses:
        categories[expense['category']] = categories.get(expense['category'], 0) + expense['amount']

    plt.figure(figsize=(10, 6))
    plt.bar(categories.keys(), categories.values(), color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount Spent')

    chart_path = f'static/charts/{username}_expense_chart.png'
    os.makedirs('static/charts', exist_ok=True)
    plt.savefig(chart_path)
    plt.close()

    return render_template('visualize.html', chart_path=chart_path, username=username)

if __name__ == "__main__":
    app.run(debug=True)