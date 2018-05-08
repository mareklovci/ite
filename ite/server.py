#!/usr/bin/env python
# coding: utf-8
"""Server!"""

import os
from os.path import dirname, join

import tornado.escape
import tornado.web
import tornado.ioloop as ioloop
from tornado.web import StaticFileHandler
from ite.search import search


root = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/www/')


# noinspection PyAbstractClass
class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(join(root, 'index.html'))


# noinspection PyAbstractClass
class SearchHandler(tornado.web.RequestHandler):

    def get(self):
        param = self.get_argument('text', None)
        data = search(param)

        self.set_header('Content-Type', 'text/html')
        self.render(join(root, 'search.html'), data=data)


def main():
    # Nastaveni handleru (pristupovych bodu)
    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/search', SearchHandler),
        # Handler vracejici staticke soubory, napr. png, zip atp.
        (r'/(.*)', StaticFileHandler, {'path': root}),
    ], autoescape=None, template_path=root)
    # Nastaveni portu, na kterem Tornado posloucha
    app.listen(8885)
    # Spusteni serveru
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
