import streamlit as st

st.set_page_config(page_title="Mortgage Calculator", layout="centered")

st.title("🏠 Mortgage Calculator")

# Inputs
home_price = st.number_input("Home Price ($)", min_value=1000.0, value=300000.0, step=1000.0, format="%.2f")
down_payment = st.number_input("Down Payment ($)", min_value=0.0, value=60000.0, step=1000.0, format="%.2f")
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=6.5, step=0.1, format="%.2f")
years = st.number_input("Loan Term (Years)", min_value=1, max_value=50, value=30)

# Derived value
loan_amount = home_price - down_payment

st.markdown(f"**Loan Amount:** ${loan_amount:,.2f}")

# Calculation
if st.button("Calculate Monthly Payment"):
    if loan_amount <= 0:
        st.error("Down payment must be less than the home price.")
    else:
        monthly_rate = rate / 100 / 12
        months = years * 12

        if monthly_rate == 0:
            payment = loan_amount / months
        else:
            payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

        st.success(f"Estimated Monthly Payment: **${payment:,.2f}**")
