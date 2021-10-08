# -*- coding: utf-8 -*-

from py4web import action, HTTP

from .istsos_auth import IstsosAuth
from .common import session, unauthenticated
from .tools import get_form

istsos = IstsosAuth()


@action("istsos", method=["GET", "POST"])
@action("istsos.json", method=["GET", "POST"])
@unauthenticated
def get_istsos_token():
    """ """
    form = get_form()
    if form.accepted:
        return istsos.json()
    else:
        raise HTTP(401)
