# -*- coding: utf-8 -*-

from py4web.core import Fixture


class CacheIt(Fixture):

    def __init__(self, max_age=60):
        super(CacheIt, self).__init__()
        self.max_age = max_age

    def on_request(self):
        response.headers['Cache-Control'] = f'public, max-age={self.max_age:d}, immutable'
