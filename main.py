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
    
    # Calculate total spent
    total_spent = sum(expense['amount'] for expense in expenses)
    
    return render_template('index.html', expenses=expenses, budgets=budgets, 
                           budget_status=budget_status, total_spent=total_spent, 
                           username=username)

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

@app.route('/delete-expense', methods=['POST'])
def delete_expense():
    username = request.form.get('username', USERNAME)
    date = request.form.get('date')
    category = request.form.get('category')
    amount = float(request.form.get('amount'))

    expenses = get_expenses(username)
    updated_expenses = [e for e in expenses if not (e['date'] == date and e['category'] == category and e['amount'] == amount)]

    expense_file = f"{username}_expenses.csv"
    with open(expense_file, 'w') as file:
        for expense in updated_expenses:
            file.write(f"{expense['date']},{expense['category']},{expense['amount']}\n")

    return index()

@app.route('/visualize', methods=['GET'])
def visualize():
    username = USERNAME
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

    # Save the chart as an image
    chart_path = 'static/charts/expense_chart.png'
    os.makedirs('static/charts', exist_ok=True)
    plt.savefig(chart_path)
    plt.close()

    return render_template('visualize.html', chart_path=chart_path)

if __name__ == "__main__":
    app.run(debug=True)