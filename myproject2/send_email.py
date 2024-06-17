import smtplib, ssl

# smarter way is to save password as an environment variable
# so you do that on Mac by opening the Terminal app
# write touch ~/.zshrc open ~/.zshrc
# when the file opens write 
# export PASSWORD="this is my pass"
# then instead of password = "this is my pass"
# in the function send_email, 
# we would write 
# password = os.getenv("PASSWORD")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "app8flask@gmail.com"
    password = "pmuuyjaxfejfpxkc"

    receiver = "app8flask@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
