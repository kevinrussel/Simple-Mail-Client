import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json




def create_message_object(username, reciever_email):
    body = "Holy cow this can actually go through pt 3?"
    message = MIMEText(body,"plain")
    message["From"] = username
    message["To"] = reciever_email
    message["Subject"] = "Sending this via python"
    return message



def send_mail(SMTP_SERVER, PORT, USERNAME, PASSWORD, RECIEVER_EMAIL, message):
    with smtplib.SMTP(SMTP_SERVER,PORT) as server:
        server.starttls()
        server.login(USERNAME,PASSWORD)
        server.sendmail(USERNAME,RECIEVER_EMAIL,message.as_string())



def open_json(json_file):
    with open(json_file,"r") as file:
        data = json.load(file)
    SMTP_SERVER = data["server"]
    PASSWORD = data["password"]
    PORT = data["port"]
    USERNAME = data["sender_email"]
    RECIEVER_EMAIL = data["reciever_email"]
    return SMTP_SERVER,PASSWORD,PORT,USERNAME,RECIEVER_EMAIL



def main():
    mail_server,password,port,username,reciever_mail= open_json("password.json")
    message = create_message_object(username, reciever_mail)
    send_mail(mail_server,port,username,password,reciever_mail,message)

if __name__ == "__main__":
    main()