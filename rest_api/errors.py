# -*- coding: utf-8 -*-


class ResponseError(Exception):
    def __init__(self, error, details=None, code=400):
        self.error = error
        self.details = details or []
        self.code = code

    def get_response(self):
        data = {'error': self.error, 'error_code': self.code, 'error_details': self.details}
        from rest_api.API import API
        return API.make_response(data, self.code)


class ResponseNotFound(ResponseError):
    def __init__(self, error="Not Found", details=None, code=404):
        super().__init__(error, details, code)


class ResponseForbidden(ResponseError):
    def __init__(self, error="Forbidden", details=None, code=403):
        super().__init__(error, details, code)


class ResponseNotImplemented(ResponseError):
    def __init__(self, error="Not Implemented", details=None, code=501):
        super().__init__(error, details, code)


class ResponseMethodNotAllowed(ResponseError):
    def __init__(self, error="Method Not Allowed", details=None, code=405):
        super().__init__(error, details, code)
