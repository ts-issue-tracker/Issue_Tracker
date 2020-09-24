import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
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

def sending_mail_with_attachment(login,password,toaddrs,msgtxt,subject):
    attachment = 'example.xls'

    msg = MIMEMultipart()

    msg['From'] = login
    msg['To'] = toaddrs
    msg['Subject'] = subject
    msg.preamble = msgtxt#'Multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)

    msgText = MIMEText('PFA of filtered CR details')
    msgAlternative.attach(msgText)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("filterData.xls", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="filterData.xls"')
    msg.attach(part)

    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('mail.Thundersoft.com', 465, context=context)
    f = s.login(login, password)
    print("type of s ", type(f))
    s.sendmail(login, toaddrs, msg.as_string())
    s.quit()
