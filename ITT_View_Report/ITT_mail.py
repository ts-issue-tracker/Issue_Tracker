import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from email.mime.application import MIMEApplication


def send_mail(senderid,password,receiverid):
    #senderid = input("enter sender Email ID:")
    #receiverid = input("enter receiver Email ID:")
    #password = input("Type your password and press enter: ")
    attachment = 'example.xls' #'background1.jpg'#'image.jpeg'

    msg = MIMEMultipart()

    msg['From'] = senderid
    msg['To'] = receiverid
    msg['Subject'] = "Test Image"
    msg.preamble = 'Multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)

    msgText = MIMEText('Test Message')
    msgAlternative.attach(msgText)
    """
    fp = open(attachment, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format(attachment))
    msg.attach(img)
    print(msg.as_string)

    """
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("example2.xls", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="example.xls"')
    msg.attach(part)

    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('mail.Thundersoft.com', 465, context=context)
    f = s.login(senderid, password)
    print("type of s ",type(f))
    s.sendmail(senderid, receiverid, msg.as_string())
    s.quit()


#send_mail()
