from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Function to calculate financial score based on user input
def calculate_financial_score(income, savings, total_expenses, loan_payments, credit_card_spending, financial_goals_met):
    # Calculate ratios
    savings_ratio = savings / income
    expenses_ratio = total_expenses / income
    loan_payments_ratio = loan_payments / income
    credit_card_spending_ratio = credit_card_spending / income
    total_spending_ratio = total_expenses / income
    goals_met = financial_goals_met / 100  # Normalize goals met (percentage)
    
    # Calculate weighted financial score
    financial_score = (
        savings_ratio * 0.20 +
        expenses_ratio * 0.15 +
        loan_payments_ratio * 0.15 +
        credit_card_spending_ratio * 0.10 +
        total_spending_ratio * 0.10 +
        goals_met * 0.15 
        # essential_spending_ratio * 0.15
    )
    return round(financial_score, 2)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get user input from the form
    income = float(request.form['income'])
    savings = float(request.form['savings'])
    total_expenses = float(request.form['total_expenses'])
    loan_payments = float(request.form['loan_payments'])
    credit_card_spending = float(request.form['credit_card_spending'])
    financial_goals_met = float(request.form['financial_goals_met'])
    # essential_spending_ratio = float(request.form['essential_spending_ratio'])

    # Calculate the financial score
    score = calculate_financial_score(income, savings, total_expenses, loan_payments, credit_card_spending, financial_goals_met)
    
    # Return the score to the user
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
