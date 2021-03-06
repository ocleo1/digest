import tornado.ioloop
import tornado.web

import blogs
from utils import Email

TWENTY_MINS_IN_MILLISECONDS = 20 * 60 * 1000

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world")

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

def digesting():
	email = Email.get_instance()
	email.login()
	blogs.RisingStack.get()
	email.quit()

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	digesting()
	scheduler = tornado.ioloop.PeriodicCallback(digesting, TWENTY_MINS_IN_MILLISECONDS)
	scheduler.start()
	tornado.ioloop.IOLoop.current().start()
