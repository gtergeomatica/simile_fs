# -*- coding: utf-8 -*-

from py4web import action, HTTP

from .istsos_auth import IstsosAuth
from .common import session, unauthenticated, auth, logger
from .tools import get_form

istsos = IstsosAuth()


# @action("get_token", method=["GET", "POST"])
@action("istsos", method=["GET", "POST"])
@action("istsos.json", method=["GET", "POST"])
@action.uses(session, auth)
def get_istsos_token():
    """ """
    form = get_form()
    # logger.debug(f'FORMKEY 1: {form.formkey}')
    if form.accepted:
        return istsos.json()
    else:
        raise HTTP(401)
