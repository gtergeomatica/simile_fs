# -*- coding: utf-8 -*-

from py4web import response
from py4web.core import Fixture
from py4web.utils.form import Form
from .common import session

get_form = lambda : Form([], form_name='get_istsos_token', csrf_session=session)

def formInfoThroughCookies():
    form = get_form()
    response.set_cookie("form-name", form.form_name)
    response.set_cookie("form-key", form.formkey)

class CacheIt(Fixture):

    def __init__(self, max_age=60):
        super(CacheIt, self).__init__()
        self.max_age = max_age

    def on_request(self):
        response.headers['Cache-Control'] = f'public, max-age={self.max_age:d}, immutable'
