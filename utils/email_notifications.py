from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_notification(recipient_email, num_days):
    load_dotenv()
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = os.getenv('SENDER_EMAIL')
    recipient_email = recipient_email
    password = os.getenv('PASSWORD')

    message = MIMEMultipart("alternative")
    message["Subject"] = "Landsat Alert"
    message["From"] = sender_email
    message["To"] = recipient_email

    text = f"""\
    Hello,

    The Landsat satalite will be flying over in {num_days} days!

    Good Luck!
    """

    body = MIMEText(text, "plain")

    message.attach(body)

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()

