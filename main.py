from flask import Flask, render_template, request
from modules.expense_tracker import add_expense, get_expenses
from modules.budget_manager import set_budget, check_budget_status

app = Flask(__name__)

# Example username (for multi-user, retrieve this dynamically via login functionality)
USERNAME = "user1"

@app.route('/')
def index():
    expenses = get_expenses(USERNAME)
    budget_status = check_budget_status(USERNAME, expenses)
    return render_template('index.html', expenses=expenses, budget_status=budget_status)

@app.route('/add-expense', methods=['POST'])
def add_expense_route():
    date = request.form.get('date')
    category = request.form.get('category')
    try:
        amount = float(request.form.get('amount'))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        return "Invalid amount. Please enter a positive number."

    add_expense(USERNAME, date, category, amount)
    return index()

@app.route('/set-budget', methods=['POST'])
def set_budget_route():
    category = request.form.get('budget-category')
    try:
        budget_amount = float(request.form.get('budget-amount'))
        if budget_amount <= 0:
            raise ValueError("Budget amount must be positive.")
    except ValueError:
        return "Invalid budget amount. Please enter a positive number."

    set_budget(USERNAME, category, budget_amount)
    return index()

if __name__ == "__main__":
    app.run(debug=True)