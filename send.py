import smtplib, ssl, threading
import getpass

#--- SET UP & VARIABLES ---#
port = 587 
smtp_server = "smtp.gmail.com"
sender = "aaron.aguerrevere@gmail.com"
receiver = "q.aguerrevere@gmail.com"
password = getpass.getpass("Type your password and press enter:")
message = """\
Subject: Hi world

Test."""

#--- EXEC FUNCTIONS ---#

def send_emails():
    threading.Timer(5.0, send_emails).start()
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

send_emails()