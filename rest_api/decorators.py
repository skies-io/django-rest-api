# -*- coding: utf-8 -*-

from rest_api.errors import ResponseError, ResponseForbidden


def get_data(keys, default={}, method="POST"):
    def get_data_wrap(function):
        def get_data_decorator(self, session, request, *args, **kwargs):
            tab = getattr(request, method, [])
            errors = []
            data = {}
            for key in keys:
                if key in tab:
                    data[key] = tab[key]
                elif key in default:
                    data[key] = default[key]
                else:
                    errors.append("You must defined: '" + str(key) + "'")
            if len(errors):
                raise ResponseError("You must provide all mandatory fields.", details=errors)
            return function(self, session, request, data, *args, **kwargs)
        return get_data_decorator
    return get_data_wrap


def must_be_in_rights(rights):
    def must_be_in_rights_wrap(function):
        def must_be_in_rights_decorator(self, session, request, *args, **kwargs):
            if not session or not session.is_connected():
                raise ResponseForbidden("You must be logged in to use this action.", code=401)
            if not session.check_right(rights):
                raise ResponseForbidden(details=["You are not allowed to access to this action."])
            return function(self, session, request, *args, **kwargs)
        return must_be_in_rights_decorator
    return must_be_in_rights_wrap


def must_be_connected(function):
    def must_be_connected_decorator(self, session, request, **kwargs):
        if not session or not session.is_connected():
            raise ResponseForbidden("You must be logged in to use this action.", code=401)
        return function(self, session, request, **kwargs)
    return must_be_connected_decorator

