import tornado

import json
import time

class ApiHandler(tornado.web.RequestHandler):
    def _write_json(self, obj):
        output = json.dumps(obj)
        self.write(output)

    def get(self):
        response = dict()
        response["data"] = dict(time=time.strftime('%X %x %Z'))

        self._write_json(response)
