import tornado.web


class ClockHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="clock-web")

