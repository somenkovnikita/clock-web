#!/bin/python3 
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.options

import handlers.api
import handlers.clock

tornado.options.define("port", default=8080, help="port to listen on")


def make_clock_web_app():
    return tornado.web.Application([
        (r"/api", handlers.api.ApiHandler),
        (r"/clock", handlers.clock.ClockHandler),
    ])


def parst_options():
    tornado.options.parse_command_line()


def main():
    app = make_clock_web_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
