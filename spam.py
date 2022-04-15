import smtplib, ssl

sender = input("Sender email?")
sender_password = input("Password:")
receiver = input("Send to who")


def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = sender
    password = sender_password
    receiver_email = receiver

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.login(sender_email,password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally: 
        server.quit


sendEmail("whats up homie this is a bot i made. i wont spam u though ")

