**Personal Expense Tracker**


**Introduction**

The Personal Expense Tracker is a Python and Flask-based web application that allows users to track their expenses, set budgets for categories, and visualize spending habits. This guide walks you through installation, setup, and usage of the application.


**Installation and Setup**

**Prerequisites**

Make sure the following tools are installed on your system:

**1. Python 3.x**

**2. Pip (Python Package Manager)**



**Steps to Set Up:**

**1. Clone the Repository**

Clone or download the repository into a folder on your system.

**2. Install Dependencies**

Navigate to the project folder in your terminal and run:

pip install -r requirements.txt


**3. Create Required Directories and Files**

1. Ensure the directory static/charts/ exists for saving visualizations.
   
2. Add the following CSV files in the root folder:
   
a. user1_budget.csv for budget information.

b. user1_expense.csv for expense information.


Example content for these files:



**user1_budget.csv**

Food,100.0

Transport,250.0



**user1_expense.csv**

2024-11-04,Food,60.0
2024-11-22,Food,80.0
2024-11-21,Food,50.0
2024-11-22,Transport,100.0



**4. Run the Application**

Start the Flask server by executing:
python main.py


Open your browser and navigate to http://127.0.0.1:5000.



**Using the Application**

**Adding Expenses**

1. Go to the **Add Expense** section.
2. Enter:
   
a. **Date** (select a valid date).

b. **Category** (choose from the dropdown).

c. **Amount** (enter a positive value).


4. Click Add Expense. The expense will appear in the Expense Summary table.

   

**Setting Budgets**

1. In the **Set Budget** section, select:
   
a. **Category** (choose a category to set the budget).

b. **Budget Amount** (enter a positive value).


2. Click **Set Budget**. The budget will be linked to the selected category.



**Viewing Expense Summary**

a. Review all expenses and their associated budget status (e.g., Exceeded, Under Budget) in the **Expense Summary table**.

b. The **Total Amount Spent** is displayed below the table.



**Deleting an Expense**

1. Click the trash icon in the **Action** column for the expense you want to delete.
   
2. The expense will be removed from the table.



**Visualizing Expenses**

1. Click **View Visualizations** at the bottom of the dashboard.
   
2. A bar chart will display the total spending for each category.



**Possible Errors and Fixes**

![Screenshot 2024-12-09 085743](https://github.com/user-attachments/assets/f078c003-b868-42e1-ae38-fa4d3511cd74)



**Known Issues and Limitations**

1. Currently supports only one user (user1).
   
2. Cannot dynamically add or remove categories.
   
3. Visualizations are limited to bar charts.
   
4. Multi-user support is not yet implemented.



**Screenshots**

**Dashboard**

![image](https://github.com/user-attachments/assets/68d1ec80-b22b-4e9a-a5eb-49582607f8e3)

**Visualization**

![image](https://github.com/user-attachments/assets/8edd9f35-50b0-4676-8b10-ee601d0335c1)




<<<<<<< HEAD
=======

>>>>>>> 895adaded16a8f7b98f2634229a895f31c5a0251



