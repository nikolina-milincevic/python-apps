import streamlit as st
from send_email import send_email

st.header("Contact us")

with st.form(key="sending_email"):
    user_email = st.text_input("Enter your email")
    topic = st.selectbox("Topic", ("Job Inquiries", "Project Proposals", "Other"))
    user_message = st.text_area("Enter your message")

    message = f"""\
    Subject: New email from {user_email}

    From: {user_email}
    Topic: {topic}
    {user_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)