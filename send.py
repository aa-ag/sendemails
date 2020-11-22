import smtplib, ssl
# help(smtplib)

port = 456
sender = "aaron.aguerrevere@gmail.com"
receiver = "q.aguerrevere@gmail.com"
message = "Hello world!"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
