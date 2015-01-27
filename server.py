import tornado.ioloop
import tornado.web
import json
from db import SQLHandler
from main import MainHandler
from point import PointToIDHandler


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/point", PointToIDHandler),
    (r"/db", SQLHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()