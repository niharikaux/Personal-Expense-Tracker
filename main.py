from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Store expenses in a list of dictionaries
expenses = []

# Route to display the main page
@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

# Route to handle form submission
@app.route('/add-expense', methods=['POST'])
def add_expense():
    # Get form data
    date = request.form.get('date')
    category = request.form.get('category')
    amount = request.form.get('amount')
    
    # Store the expense in a dictionary
    expense = {
        'date': date,
        'category': category,
        'amount': amount
    }
    
    # Add the expense to the list of expenses
    expenses.append(expense)
    
    # Redirect to the main page to display the updated table
    return render_template('index.html', expenses=expenses)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
