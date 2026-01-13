import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import json



def add_image(image_name):
    html = """\
        <html>
        <body>
            <p>Hi,<br>
            This is a <b>test</b> email with an embedded image.<br>
            Here is an image: <img src="cid:image1"></p>
        </body>
        </html>
        """




def create_message_object(username, reciever_email):
    body = "Holy cow this can actually go through pt 4?"
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = reciever_email
    message["Subject"] = "Sending this via python"
    message.attach(MIMEText(body,"plain"))
    return message



def send_mail(SMTP_SERVER, PORT, USERNAME, PASSWORD, RECIEVER_EMAIL, message):

    # Specify the path to your embedded image
    image_path = "cat.webp"  # Change this to the correct path
    
    with open(image_path, "rb") as img:
            msg_img = MIMEImage(img.read(), name="catp.wep")
            msg_img.add_header("Content-ID", "<iamge1>")
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
    RECIEVER_EMAIL = data["reciever_email"]
    return SMTP_SERVER,PASSWORD,PORT,USERNAME,RECIEVER_EMAIL



def main():
    mail_server,password,port,username,reciever_mail= open_json("password.json")
    message = create_message_object(username, reciever_mail)
    send_mail(mail_server,port,username,password,reciever_mail,message)

if __name__ == "__main__":
    main()