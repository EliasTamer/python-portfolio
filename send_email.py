import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body, user_email):
    host = "smtp.gmail.com"
    port = 465

    username = "eliastamer3@gmail.com"
    password= os.getenv("PASSWORD")
    receiver = "eliastamer3@gmail.com"

    context = ssl.create_default_context()

    # Construct the email message
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())
