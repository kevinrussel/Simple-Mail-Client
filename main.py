import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
with open("password.json","r") as file:
    data = json.load(file)


message = MIMEMultipart()
message["From"] = data["sender_email"]
message["To"] = data["reciever_email"]
# SMTP_SERVER = 