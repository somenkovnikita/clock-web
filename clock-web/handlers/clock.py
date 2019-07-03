import tornado.template
import tornado.web


class ClockHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.loader = tornado.template.Loader("static/templates")

    def get(self):
        template = self.loader.load("index.html")
        self.write(template.generate(title="clock-web", time="15:25"))

