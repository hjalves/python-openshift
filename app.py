# -*- coding: utf-8 -*-

import os
import sys
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")
        print("Whatever")
        print("STDERR", file=sys.stderr)

application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8080)
    print("Tornado serving on 8080....")
    tornado.ioloop.IOLoop.current().start()
