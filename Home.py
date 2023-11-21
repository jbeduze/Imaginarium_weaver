import streamlit as st
from st_paywall import add_auth

st.title("Welcome to Imaginarium Weaver")

add_auth(required=True)

st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write("congrats on your future winnings now get in there champ")
st.write(f'for your records and future logins, your email is: {st.session_state.email}')
