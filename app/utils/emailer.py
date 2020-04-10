from app import LOGGER, app

import traceback
import smtplib
import email
from email.message import EmailMessage

SMTP_USERNAME = app.config.get('SMTP_USERNAME')
SMTP_PASSWORD = app.config.get('SMTP_PASSWORD')
SMTP_SENDER_NAME = app.config.get('SMTP_SENDER_NAME')
SMTP_SENDER_EMAIL = app.config.get('SMTP_SENDER_EMAIL')
SMTP_HOST = app.config.get('SMTP_HOST')
SMTP_PORT = app.config.get('SMTP_PORT')


def send_mail(recipient, subject, body_text='', body_html='', charset='UTF-8', mail_type='AMZ', file_name='', file_path='', sender_name=None, sender_email=None):
    """Sends an email.
    """
    sender_name = sender_name or SMTP_SENDER_NAME
    sender_email = sender_email or SMTP_SENDER_EMAIL

    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email.utils.formataddr((sender_name, sender_email))
        msg['To'] = recipient

        msg.set_content(body_text)

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            smtp.send_message(msg=msg)

    except Exception as e:
        LOGGER.error('Exception {} while trying to send emal: {}, {} '.format(
            e, traceback.format_exc()))
