from email.message import EmailMessage
from Email import password
import ssl
import smtplib

email_sender = 'kambleshrinivas33@gmail.com'
email_password='@1VRkamble'

email_receiver='kableshrinivas10@gmail.com'

subject='Mission Sucessfull'
body='''
Congratulation
'''

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
