# Sending email with attachment

import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "nfsfpzlmxkaggmtj"
SENDER = "app8flask@gmail.com"
RECEIVER = "app8flask@gmail.com"

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("hey, we just saw a new customer arriving")
    
    # rb means read in binary mode because we are reading image and not text
    with open(image_path, "rb") as file:
        content = file.read()
        
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit
    
    print("send_email function ended")
    
if __name__ == "__main__":
    send_email(image_path="app9/image.png")
    