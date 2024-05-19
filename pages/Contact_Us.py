import streamlit as st
from send_email import send_email
from email.mime.text import MIMEText

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")
    subject = f"New email from {user_email}"
    message = f"From: {user_email}\n\n{raw_message}"
    button = st.form_submit_button("Submit")
    if button:
        send_email(subject, message, user_email)
        st.info("Your email was sent successfully")
