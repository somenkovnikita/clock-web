import tornado

import json
import time


class ApiHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        super(ApiHandler, self).set_default_headers()
        self.set_header('Content-Type', 'application/json')

    def get_time(self):
        response = dict()
        response["data"] = dict(time=time.strftime('%X %x %Z'))
        self.write(json.dumps(response))

    def get(self, method):
        if method == "time":
            self.get_time()
            return
        raise tornado.web.HTTPError(
            status_code=404,
            reason="Invalid method")

