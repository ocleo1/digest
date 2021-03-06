import time
import requests

from bs4 import BeautifulSoup
from utils import Email


class RisingStack:
	ORIGIN = "https://blog.risingstack.com"

	@classmethod
	def get(cls):
		email = Email.get_instance()
		r = requests.get(cls.ORIGIN)
		soup = BeautifulSoup(r.text, "html.parser")
		for post in soup.find_all("article"):
			header = post.find("header", attrs={ "class": "post-header" })
			a = header.find("a")
			subject = f'[RisingStack] {a.get_text()}'
			link = f'{cls.ORIGIN}{a.get("href")}'
			section = post.find("section", attrs={ "class": "post-content" })
			content = f'''
			<html>
				<body>
					<p>{section.get_text()}</p>
					<a href="{link}">{link}</a>
				</body>
			</html>
			'''
			email.send(subject, content)
			time.sleep(10)
