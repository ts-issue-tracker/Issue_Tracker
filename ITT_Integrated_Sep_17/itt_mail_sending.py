import smtplib
from email.message import EmailMessage
import datetime as dt
import time

def sending_registration_mail_to(toaddrs):
    fromaddr = "tulasi.jana"
    # toaddrs="tulasi.jana@thundersoft.com"
    SMTPServer = "mail.thundersoft.com"
    port = 465  # 587
    login = "tulasi.jana@thundersoft.com"
    password = "tulasi@tsoft1994"
    msg = EmailMessage()
    msgtxt = "Hey..,You are successfully registered with \"Thundersoft Issue Tracking Tool\""
    msg.set_content(msgtxt)
    msg['Subject'] = "Thundersoft Issue Tracking Tool Registration"
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    server=smtplib.SMTP_SSL(SMTPServer, port)
    #use smtplib.SMTP() if port is 587
    #server.starttls()
    server.ehlo()
    r=server.login(login, password)
    print(r)
    server.send_message(msg)
    server.ehlo()
    server.quit()

def sending_mail_with_selected_statistics_info(login,password,toaddrs,msgtxt):
    msg_to_return=""
    SMTPServer = "mail.thundersoft.com"
    port = 465  # 587
    msg = EmailMessage()
    msg.set_content(msgtxt)
    msg['Subject'] = "Issue Tracking Tool: Selected Statistics Information"
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