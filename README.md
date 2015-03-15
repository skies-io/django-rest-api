# Django REST API

In settings :
```python
REST_AUTH_SESSION_ENGINE = "my_site.auth.AuthSession"
```

Example of this class :
```python
from rest_api.auth import BaseAuthREST

class AuthSession(BaseAuthREST):
    def __init__(self, request):
        self.request = request
        try:
            if 'HTTP_AUTHORIZATION' in request.META:
                self.login_api_key(request.META['HTTP_AUTHORIZATION'])
        except AuthApiKeyBad:
            raise ResponseForbidden(details=["Mauvaise clé API."])
        except AuthApiKeyExpire:
            raise ResponseForbidden(details=["Clé API expirée."])

    def is_connected(self):
        return ...

    def check_right(self, rights, _all=False):
        return ...
```

Register API :
```python
from django.conf.urls import patterns, url, include
from rest_api.register import RegisterAPI
from my_site.api_v1.user import UserAPI
from my_site.api_v1.project import ProjectAPI

api_v1 = RegisterAPI("1.0")
api_v1.register(UserAPI()) # /api/1.0/user
api_v1.register(ProjectAPI()) # /api/1.0/project

urlpatterns = patterns(
    'my_site',
    url(r'^api/', include(api_v1.urls))
)
```
