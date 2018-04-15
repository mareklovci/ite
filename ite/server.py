#!/usr/bin/env python
# coding: utf-8
"""Server!"""

import io
import os
from os.path import dirname, join

import tornado.web
import tornado.ioloop as ioloop
from tornado.web import StaticFileHandler

NONAME = 'UNKNOWN'
root = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/gui/')


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


class NameHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        name = self.get_argument('name', None)
        if name is not None:
            self.set_cookie('name', name)
        else:
            name = self.get_cookie('name', NONAME)
        # Nastaveni typu dat, ktere odesilame prohlizeci
        self.set_header('Content-Type', 'text/html')
        self.render('form.html', name=name)


class FormHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        name = self.get_cookie('name', NONAME)
        param = self.get_argument('message', None)

        if param:
            self.set_header('Content-Type', 'text/plain')
            self.write('Jmenujete se <b>{}</b> a zadali jste: {}'.format(
                name, param))
        else:
            self.set_header('Content-Type', 'text/html')
            self.write('<html><head>'
                       '<meta content="text/html; charset=UTF-8" /></head>'
                       '<body><form action="/form" method="GET">'
                       '<input type="text" name="message" >'
                       '<input type="submit" value="OK" >'
                       '</form>'
                       u'<a href="/">Hlavní stránka</a>'
                       '</body></html>')


if __name__ == '__main__':
    # Nastaveni handleru (pristupovych bodu)
    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/form', FormHandler),
        (r'/name', NameHandler),
        # Handler vracejici staticke soubory, napr. png, zip atp.
        (r'/(.*)', StaticFileHandler, {'path': root}),
    ])
    # Nastaveni portu, na kterem Tornado posloucha
    app.listen(8885)
    # Spusteni serveru
    ioloop.IOLoop.current().start()
