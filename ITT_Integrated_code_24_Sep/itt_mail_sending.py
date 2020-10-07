import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate
import datetime as dt
import time

def sending_mail(login,password,toaddrs,msgtxt,subject):
    msg_to_return=""
    SMTPServer = "mail.thundersoft.com"
    port = 465  # 587
    receiverlist = list(toaddrs.split(","))
    msg = EmailMessage()
    msg.set_content(msgtxt)
    msg['Subject'] =subject
    msg['From'] = login
    msg['To'] = ",".join(receiverlist)
    msg["Date"] = formatdate(localtime=True)
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
        msg_to_return += "Recipient Mail ID do not exist"
    else:
        server.ehlo()
        server.quit()
        msg_to_return+="Mail Sent Successfully"
    return msg_to_return

def sending_mail_with_attachment(login,password,toaddrs,msgtxt,subject):

    msg_to_return=""
    msg = MIMEMultipart()
    SMTPServer = "mail.thundersoft.com"
    port = 465  # 587
    receiverlist = list(toaddrs.split(","))
    msg['From'] = login
    msg['To'] = ",".join(receiverlist)#toaddrs
    msg['Subject'] = subject
    msg["Date"] = formatdate(localtime=True)
    msg.preamble = msgtxt#'Multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)

    msgText = MIMEText('Hi,\n\nPFA of CR details.\n\nRegards,\nIssue Tracker')
    msgAlternative.attach(msgText)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("CR_Data.xls", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="CR_Data.xls"')
    msg.attach(part)

    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('mail.Thundersoft.com', 465, context=context)
    try:
        s.login(login,password)
        s.sendmail(login,receiverlist,msg.as_string())#toaddrs,msg.as_string())
    except smtplib.SMTPAuthenticationError:
        msg_to_return+="Incorrect Sender Mail ID/Password"
    except smtplib.SMTPRecipientsRefused:
        msg_to_return += "Recipient Mail ID do not exist"
    else:
        s.ehlo()
        s.quit()
        msg_to_return+="Mail Sent Successfully"
    return msg_to_return
