import smtplib
from email.message import EmailMessage
import datetime as dt
import time

def sending_mail(login,password,toaddrs,msgtxt,subject):
    msg_to_return=""
    SMTPServer = "mail.thundersoft.com"
    port = 465  # 587
    msg = EmailMessage()
    msg.set_content(msgtxt)
    msg['Subject'] =subject
    msg['From'] = login
    msg['To'] = toaddrs
    server=smtplib.SMTP_SSL(SMTPServer, port)
    #use smtplib.SMTP() if port is 587
    #server.starttls() 
    server.ehlo()
    try:
        server.login(login, password)
        server.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        msg_to_return+="Incorrect Mail ID/Password"
    except smtplib.SMTPRecipientsRefused:
        msg_to_return += "Incorrect Recipient Mail ID"
    else:
        server.ehlo()
        server.quit()
        msg_to_return+="Mail Sent Successfully"
    return msg_to_return