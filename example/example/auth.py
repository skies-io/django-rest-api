# -*- coding: utf-8 -*-

from rest_api.auth import BaseAuthREST


class AuthSession(BaseAuthREST):
    def __init__(self, request):
        self.request = request
        # try:
        #     if 'HTTP_AUTHORIZATION' in request.META:
        #         self.login_api_key(request.META['HTTP_AUTHORIZATION'])
        # except AuthApiKeyBad:
        #     raise ResponseForbidden(details=["Bad API key."])
        # except AuthApiKeyExpire:
        #     raise ResponseForbidden(details=["API key expired."])

    def is_connected(self):
        # Don't not this, only for this example
        return True

    def check_right(self, rights, _all=False):
        # Don't not this, only for this example
        return True
