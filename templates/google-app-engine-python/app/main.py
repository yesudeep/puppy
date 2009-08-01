#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configuration as config
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexPageHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('It works!')


URL_ROUTES = [
    ('/', IndexPageHandler),
]


# Defining a main method allows GAE to cache your module better
# and results in faster processing, so please put your stuff in here.
def main():
    application = webapp.WSGIApplication(URL_ROUTES, config.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()

