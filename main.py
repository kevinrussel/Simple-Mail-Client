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




def create_message_object(username, reciever_email):
    body = "Holy cow this can actually go through pt 7?"
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = reciever_email
    message["Subject"] = "Sending this via python"
    message.attach(MIMEText(body,"plain"))
    return message



def send_mail(SMTP_SERVER, PORT, USERNAME, PASSWORD, RECIEVER_EMAIL, message):

    # Specify the path to your embedded image
    image_path = "cat.webp"  # Change this to the correct path
    html_img = add_image()
    message.attach(MIMEText(html_img, "html"))
    with open(image_path, "rb") as img:
            msg_img = MIMEImage(img.read(), name="mily-way.jpg")
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
    RECIEVER_EMAIL = data["reciever_email"]
    return SMTP_SERVER,PASSWORD,PORT,USERNAME,RECIEVER_EMAIL



def main():
    mail_server,password,port,username,reciever_mail= open_json("password.json")
    message = create_message_object(username, reciever_mail)
    send_mail(mail_server,port,username,password,reciever_mail,message)

if __name__ == "__main__":
    main()