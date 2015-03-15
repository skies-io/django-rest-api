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
                    errors.append("Vous devez définir : '" + str(key) + "'")
            if len(errors):
                raise ResponseError("Vous devez fournir tous les champs obligatoires.", details=errors)
            return function(self, session, request, data, *args, **kwargs)
        return get_data_decorator
    return get_data_wrap


def must_be_in_rights(rights):
    def must_be_in_rights_wrap(function):
        def must_be_in_rights_decorator(self, session, request, *args, **kwargs):
            if not session.is_connected():
                raise ResponseForbidden("Vous devez être connecté pour accéder à cette action.", code=401)
            if not session.check_right(rights):
                raise ResponseForbidden(details=["Vous n'êtes pas autorisé à accéder à cette action."])
            return function(self, session, request, *args, **kwargs)
        return must_be_in_rights_decorator
    return must_be_in_rights_wrap


def must_be_connected(function):
    def must_be_connected_decorator(self, session, request, **kwargs):
        if not session.is_connected():
            raise ResponseForbidden("Vous devez être connecté pour accéder à cette action.", code=401)
        return function(self, session, request, **kwargs)
    return must_be_connected_decorator

