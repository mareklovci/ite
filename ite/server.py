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

root = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/www/')


class MainHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        try:
            # Nacteni obsahu ze souboru
            with io.open(join(root, 'index.html'),
                         encoding='utf-8') as f:
                self.write(f.read().format('<h1>Úvodní stránka</h1>'
                                           '<p class="lead">Prosím zadejte hledané slovo.</p>'))
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
            try:
                # Nacteni obsahu ze souboru
                with io.open(join(root, 'index.html'),
                             encoding='utf-8') as f:
                    self.write(f.read().format(stranky))
            except IOError:
                self.set_status(404)
                # Nic jsem nenasel, vracim error.
                self.write('404: Not Found')

            self.set_header('Content-Type', 'text/html')
            self.write(stranky)
        else:
            try:
                # Nacteni obsahu ze souboru
                with io.open(join(root, 'index.html'),
                             encoding='utf-8') as f:
                    self.write(f.read().format('<h1>Žádný výsledek nenalezen</h1>'))
            except IOError:
                self.set_status(404)
                # Nic jsem nenasel, vracim error.
                self.write('404: Not Found')


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
