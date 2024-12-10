# Overview

The Personal Expense Tracker is a Python and Flask-based web application that allows users to:

1. Track expenses by date, category, and amount.
2. Set budgets for specific categories.
3. Visualize spending patterns using bar charts.

This document provides technical details for developers who need to understand, maintain, or extend the project. It assumes familiarity with Python, Flask, and general web development concepts.


# Project Structure

project/
├── main.py                 # Entry point for running the Flask application
├── requirements.txt        # Lists all dependencies
├── modules/                # Contains reusable logic
│   ├── expense_tracker.py  # Functions for managing expenses
│   ├── budget_manager.py   # Functions for managing budgets
├── static/                 # Static assets for the app
│   ├── styles.css          # CSS file for styling
│   ├── charts/             # Directory for saving generated visualizations
├── templates/              # HTML templates for rendering pages
│   ├── index.html          # Dashboard page
│   ├── visualize.html      # Visualization page
├── user1_budget.csv        # Example CSV file for budget data
├── user1_expense.csv       # Example CSV file for expense data
├── doc/                    # Documentation folder
│   ├── developer_guide.md  # This file

# Specifications and Features

Implemented Features:

1. Expense Tracking: Users can add, view, and delete expenses.
2. Budget Management: Users can set budgets for different categories.
3. Visualization: Expenses are visualized using bar charts.
4. File-Based Data Storage: Expenses and budgets are stored in CSV files.

Features Not Implemented:

1. Multi-User Support: Currently supports only one default user (user1).
2. Dynamic Categories: Categories are predefined and cannot be customized by users.

# Installation and Deployment Notes

Prerequisites:

1. Python 3.x
2. Pip (Python Package Manager)

Installation:

1. Clone the repository.
2. Install dependencies:
          pip install -r requirements.txt

Deployment Notes:

1. Ensure the static/charts/ directory has write permissions.
2. In production, disable Flask's debug mode:
         app.run(debug=False)

# User Interaction and Code Walkthrough

User Interaction Flow

1. Dashboard (Homepage):
   Users can add expenses, set budgets, and view a summary of expenses.

2. Expense Deletion:
   Users can delete specific expenses from the dashboard.

3. Visualization:
   Users can view a bar chart of expenses grouped by category.

# Code Walkthrough

A. Entry Point (main.py):

1. Purpose: Defines Flask routes and serves as the application entry point.
2. Routes:
    a. /: Renders the dashboard and displays expenses, budgets, and status.
    b. /add-expense: Handles expense addition.
    c. /set-budget: Handles budget setting.
    d. /delete-expense: Handles expense deletion.
    e./visualize: Generates and displays a bar chart.

B. Modules:

1. expense_tracker.py:

    a. Functions:
        i.  add_expense(username, date, category, amount): Appends an expense to the user's CSV file.
        ii. get_expenses(username): Reads expenses from the user's CSV file and returns them as a 
        list of dictionaries.

     b. Purpose: Handles all expense-related operations.

2. budget_manager.py:

     a. Functions:
         i. set_budget(username, category, budget_amount): Saves a budget for a specific category.
         ii. get_all_budgets(username): Reads budgets from the user's CSV file and returns them as a  dictionary.
         iii. check_budget_status(username, expenses): Compares expenses to budgets and returns budget statuses (e.g., "Under Budget" or "Exceeded").

     b. Purpose: Manages budget-related operations.

3. Templates:

a. index.html: Displays the dashboard, including forms for adding expenses and setting budgets, and a summary table of expenses and budgets.

b. visualize.html: Displays a bar chart of expenses grouped by category.

# Known Issues and Limitations

A. Minor Bugs:

     1. Expense Deletion Logic:

          a. Issue: Deleting an expense is based on exact matches of date, category, and amount. Duplicate entries with identical values cannot be uniquely identified.
          b. Fix: Use unique expense IDs.

     2. Error Handling:

          a. Issue: Missing or corrupted CSV files can crash the app.
          b. Fix: Add error handling for file operations.

B. Major Bugs:

None identified at the time of documentation.

C. Computational Inefficiencies:

Using CSV files for data storage can become slow for large datasets. Migrating to a relational database like SQLite or PostgreSQL would improve performance and scalability.

# Future Work

1. Multi-User Support:
   Add user authentication and separate CSV files or database tables for each user.

2. Dynamic Categories:
   Allow users to create, edit, or delete categories.

3. Improved Visualizations:
   Add support for other chart types (e.g., pie charts, trend graphs).

4. Database Integration:
   Replace CSV files with a relational database to handle larger datasets efficiently.

5. Unit Testing:
   Implement automated tests for key functions (e.g., add_expense, set_budget).

# Ongoing Development and Maintenance

1. Modular Design: The project is structured into modules (expense_tracker.py and budget_manager.py) to ensure maintainability.

2. Error Handling: Future development should include robust error handling for file operations and user input validation.

3. Extensibility: To extend functionality (e.g., multi-user support), consider using Flask extensions like Flask-Login for authentication and session management.

# Graphics and Visual Aids

Application Flow Diagram:

User --> Add Expense --> [expense_tracker.py] --> Updates user1_expense.csv
User --> Set Budget --> [budget_manager.py] --> Updates user1_budget.csv
User --> View Visualization --> [main.py] --> Uses Matplotlib to create a bar chart

Example File Format:

user1_expense.csv:
2024-11-04,Food,60.0
2024-11-22,Food,80.0

user1_budget.csv:
Food,100.0
Transport,250.0
