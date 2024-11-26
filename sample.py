import streamlit as st

# Function to calculate financial score based on inputs
def calculate_financial_score(income, savings, total_expenses, loan_payments, credit_card_spending, financial_goals_met, essential_spending_ratio=0.6):
    # Calculate the ratios based on the inputs
    savings_ratio = savings / income
    expenses_ratio = total_expenses / income
    loan_payments_ratio = loan_payments / income
    credit_card_spending_ratio = credit_card_spending / income
    total_spending_ratio = total_expenses / income
    goals_met = financial_goals_met / 100  # Assuming it's a percentage (0 to 100)

    # Calculate the weighted financial score
    financial_score = (
        savings_ratio * 0.20 +
        expenses_ratio * 0.15 +
        loan_payments_ratio * 0.15 +
        credit_card_spending_ratio * 0.10 +
        total_spending_ratio * 0.10 +
        goals_met * 0.15 +
        essential_spending_ratio * 0.15
    )

    return financial_score

# Function to give financial advice based on the score
def financial_advice(score):
    if score >= 0.8:
        return "Excellent financial health! Keep up the good work. You're saving well, managing your expenses and loans, and meeting your financial goals."
    elif score >= 0.6:
        return "Good financial health. You're doing well, but consider increasing your savings rate and monitoring your credit card spending."
    elif score >= 0.4:
        return "Average financial health. You may want to work on reducing your expenses and loan payments. Consider focusing more on your savings goals."
    else:
        return "Poor financial health. Consider reviewing your expenses, focusing on paying down debt, and building up savings. Seek professional financial advice."

# Streamlit app layout
st.title("Financial Health Score Calculator")

# User Inputs
income = st.number_input("Enter your monthly income ($):", min_value=0, value=5000, step=100)
savings = st.number_input("Enter your savings ($):", min_value=0, value=1000, step=100)
total_expenses = st.number_input("Enter your total monthly expenses ($):", min_value=0, value=2500, step=100)
loan_payments = st.number_input("Enter your monthly loan payments ($):", min_value=0, value=500, step=100)
credit_card_spending = st.number_input("Enter your monthly credit card spending ($):", min_value=0, value=300, step=50)
financial_goals_met = st.slider("What percentage of your financial goals have you met?", 0, 100, 80)

# Button to calculate the score
if st.button("Calculate Financial Health Score"):
    score = calculate_financial_score(income, savings, total_expenses, loan_payments, credit_card_spending, financial_goals_met)

    # Display results
    st.subheader(f"Your Financial Health Score: {score:.2f}")
    st.write(financial_advice(score))
