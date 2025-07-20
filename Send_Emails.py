import smtplib, ssl
host = "smtp.gmail.com"
port = 465

username = "mallisettisivapavan@gmail.com"
password = "tcue bnsj lfxn ftvs"  # Use your App Password here

receiver = "mallisettisivapavan@gmail.com"
my_context = ssl.create_default_context()

message = """Subject: Test Email\n\n Hi Mummy...!!"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
