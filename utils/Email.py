'''
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
https://realpython.com/python-send-email/
'''

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import smtp_port, smtp_server, smtp_password, sender_email, receiver_email

class Email:
	__instance = None

	def __init__(self):
		''' Virtually private constructor. '''
		if Email.__instance is not None:
			raise Exception("This class is a singleton!")
		else:
			Email.__instance = self

	@staticmethod
	def get_instance():
		''' Static access method. '''
		if Email.__instance is None:
			Email()
		return Email.__instance

	def login(self):
		try:
			self.__server = smtplib.SMTP_SSL(smtp_server, smtp_port)
			self.__server.login(sender_email, smtp_password)
		except Exception as e:
			print(e)

	def quit(self):
		self.__server.quit()

	def send(self, subject, content):
		message = MIMEMultipart("alternative")
		message["Subject"] = subject
		message["From"] = sender_email
		message["To"] = receiver_email

		# Turn these into html MIMEText objects
		part2 = MIMEText(content, "html")

		# Add HTML parts to MIMEMultipart message
		# The email client will try to render the last part first
		message.attach(part2)
		print(message.as_string())
		try:
			self.__server.sendmail(sender_email, receiver_email, message.as_string())
		except Exception as e:
			print(e)
