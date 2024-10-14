from flask import Flask, render_template, request
from modules.expense_tracker import add_expense, get_expenses  # Import from expense_tracker.py

# Initialize Flask app
app = Flask(__name__)

# Store expenses in a list (for now, until database integration)
expenses = []

# Route to display the main page
@app.route('/')
def index():
    return render_template('index.html', expenses=get_expenses(expenses))

# Route to handle expense submission
@app.route('/add-expense', methods=['POST'])
def add_expense_route():
    date = request.form.get('date')
    category = request.form.get('category')
    amount = request.form.get('amount')

    # Add expense using the function from expense_tracker
    add_expense(expenses, date, category, amount)

    return render_template('index.html', expenses=get_expenses(expenses))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)