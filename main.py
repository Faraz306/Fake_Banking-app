import streamlit as st

st.title("YF Bank")
password = st.text_input("Enter your password", key="5", type="password")
if password == '':
    st.error("Please enter a password.")
else:
    name = st.text_input("Enter your name", key="1")
    balance = st.text_input("Enter your balance.", key="2")
    if balance == '':
        balance = 0
    else:
        balance = float(balance)
    if name and balance:
        st.success(f"Successfully verified as {name}.")
    one_to_pay = st.text_input("Enter the name of the person to pay.", key="3")
    payment_box = st.text_input(f"how much to pay to {one_to_pay}?", key="4")
    if payment_box == '':
        payment_box = 0
    else:
        payment_box = float(payment_box)
    if one_to_pay and payment_box:
        if balance > payment_box:
            with open("Payments.csv", 'a') as f:
                f.write(f"You payed {payment_box} to {one_to_pay}. your balance is {balance - payment_box}.\n")
                with open("Account.csv", 'a') as f:
                    f.write(
                        f"Your name is {name} and your balance is {balance}. after paying {payment_box} to {one_to_pay}, your balance is {balance - payment_box}.\n")
                st.success(f"You have successfully paid {payment_box}.Check history page.")
        else:
            st.error("The balance is smaller than the paying amount!")