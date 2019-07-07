#!/bin/python3 
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.options

import settings
import handlers.api
import handlers.clock

import database.timedb
import database.emulator


tornado.options.define("port", default=8080, 
                       help="port to listen on")
tornado.options.define("timedbpath", default="timedb.txt", 
                       help="path to timedb")


def make_clock_web_app(timedbpath):
    timedb = database.timedb.TimeDB.load(timedbpath)

    fake_acticity = database.emulator.TimeDBActivityEmulator(timedb)
    fake_acticity.start()

    handlers_ = [
        (r"/api/(.+)", handlers.api.ApiHandler, dict(timedb=timedb)),
        (r"/clock", handlers.clock.ClockHandler),
    ]

    application = tornado.web.Application(
        handlers=handlers_,
        template_path=settings.TEMPLATE_PATH,
        static_path=settings.STATIC_PATH
    )

    return application, fake_acticity


def main():
    tornado.options.parse_command_line()
    app, fa = make_clock_web_app(tornado.options.options.timedbpath)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
        fa.stop()

if __name__ == "__main__":
    main()
