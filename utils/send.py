'''
https://realpython.com/python-send-email/
'''

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import smtp_port, smtp_server, smtp_password, sender_email, receiver_email

def sendmail(subject, content):
	message = MIMEMultipart("alternative")
	message["Subject"] = subject
	message["From"] = sender_email
	message["To"] = receiver_email

	# Turn these into plain MIMEText objects
	part1 = MIMEText(content, "plain")

	# Add plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)

	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
		server.login(sender_email, smtp_password)
		server.sendmail(sender_email, receiver_email, message.as_string())
