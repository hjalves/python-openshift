# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")

application = tornado.web.Application([
    (r"/", MainHandler),
])

port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', '8080'))
ip = os.environ.get('OPENSHIFT_PYTHON_IP', 'localhost')

if __name__ == "__main__":
    application.listen(port, ip)
    tornado.ioloop.IOLoop.current().start()
