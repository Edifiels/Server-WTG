import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
