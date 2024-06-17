import streamlit as st

st.header("Contact me")

with st.form(key="user_email_input"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed")