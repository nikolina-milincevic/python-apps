import smtplib, ssl

# this now does not work because I used prof's
# username and password which now don't work

host = "smtp.gmail.com"
port = 465

username = "app8flask@gmail.com"
password = "pmuuyjaxfejfpxkc"

receiver = "app8flask@gmail.com"
my_context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)