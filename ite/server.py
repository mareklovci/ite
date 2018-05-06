#!/usr/bin/env python
# coding: utf-8
"""Server!"""

import io
import os
from os.path import dirname, join

import tornado.web
import tornado.ioloop as ioloop
from tornado.web import StaticFileHandler
from ite.search import search

NONAME = 'UNKNOWN'
root = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/www/')


class MainHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        try:
            # Nacteni obsahu ze souboru
            with io.open(join(root, 'index.html'),
                         encoding='utf-8') as f:
                self.write(f.read())
        except IOError:
            self.set_status(404)
            # Nic jsem nenasel, vracim error.
            self.write('404: Not Found')


class SearchHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        param = self.get_argument('text', None)

        stranky = search(param)

        if param:
            self.set_header('Content-Type', 'text/html')
            self.write(stranky)
        else:
           self.set_header('Content-Type', 'text/html')
           self.write('nic')


if __name__ == '__main__':
    # Nastaveni handleru (pristupovych bodu)
    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/search', SearchHandler),
        # Handler vracejici staticke soubory, napr. png, zip atp.
        (r'/(.*)', StaticFileHandler, {'path': root}),
    ])
    # Nastaveni portu, na kterem Tornado posloucha
    app.listen(8885)
    # Spusteni serveru
    ioloop.IOLoop.current().start()
