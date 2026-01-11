import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
with open("password.json","r") as file:
    data = json.load(file)

SMTP_SERVER = data["server"]
PASSWORD = data["password"]
PORT = data["port"]
USERNAME = data["sender_email"]
Reciever_email = data["reciever_email"]
body = "Holy cow can this actually go through?"
message = MIMEText(body,"plain")

message["From"] = data["sender_email"]
message["To"] = data["reciever_email"]
message["Subject"] = "Sending this via python"




with smtplib.SMTP(SMTP_SERVER,PORT) as server:
    server.starttls()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,Reciever_email,message.as_string())