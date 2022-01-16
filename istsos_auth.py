# -*- coding: utf-8 -*-

from . import settings
import requests

DEFAULT_USERNAME = settings.ISTSOS_USERNAME
DEFAULT_PASSWORD = settings.ISTSOS_PASSWORD


class IstsosAuth(object):
    """docstring for IstsosAuth."""

    url = 'https://istsos.ddns.net/auth/realms/istsos/protocol/openid-connect/token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    DEFAULTS = {
        'grant_type': 'password',
        'client_id': 'istsos-istsos'
    }

    def __init__(self, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD):
        super(IstsosAuth, self).__init__()
        self.args = dict(self.DEFAULTS, username=username, password=password)

    def __call__(self):
        response = requests.post(
            self.url, data=self.args, headers=self.headers
        )

        return response

    def json(self):
        return self().json()

    def get_token(self):
        response = self()
        return response.json()['access_token']


if __name__ == '__main__':
    istsos = IstsosAuth()
    token = istsos.get_token()
