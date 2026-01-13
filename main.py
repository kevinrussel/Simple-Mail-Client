import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import json



def add_image():
    html = """\
        <html>
        <body>
            <p> 
            Here is an image: <img src="cid:image1"></p>
        </body>
        </html>
        """
    return html

def create_message():
    message = input("What is the message you would like to say?")
    return message


def create_message_body():
    message_body = input("Print yes if you would like to make your own message, or no if ou would like to use the premade message")
    message = ''
    if (message_body == "yes"):
        message = create_message()
    elif (message_body == "no"):
        with open("message.txt", encoding="utf-8") as file:
            message = file.read()
    
    return message

def create_message_object(username, reciever_email):
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = reciever_email
    message["Subject"] = input("What would you like the Subject of the email to be?")
    body = create_message_body()
    message.attach(MIMEText(body,"plain"))
    return message



def send_mail(SMTP_SERVER, PORT, USERNAME, PASSWORD, RECIEVER_EMAIL, message):

    image_path = "cat.jpg"
    html_img = add_image()
    message.attach(MIMEText(html_img, "html"))
    with open(image_path, "rb") as img:
            msg_img = MIMEImage(img.read(), name="cat.jpg")
            msg_img.add_header("Content-ID", "<image1>")
            msg_img.add_header("Content-Disposition", "inline")  # Ensures inline display
            message.attach(msg_img)
   
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
    return SMTP_SERVER,PASSWORD,PORT,USERNAME


def get_sender():
    email_address = input("Please enter in the address of the person you wish to send this email to.")
    return email_address

def main():
    mail_server,password,port,username= open_json("password.json")
    reciever_mail = get_sender()
    message = create_message_object(username, reciever_mail)
    send_mail(mail_server,port,username,password,reciever_mail,message)

if __name__ == "__main__":
    main()