from app import app, mail
from flask_mail import Message

'''
Function to send any emails
for Lowell Dashboard
'''


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)
