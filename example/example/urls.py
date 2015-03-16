# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_api.register import RegisterAPI
from example.api_v1.project import ProjectAPI

api_v1 = RegisterAPI("1.0")
api_v1.register(ProjectAPI())  # /api/1.0/project

urlpatterns = patterns(
    'example',
    url(r'^api/', include(api_v1.urls))
)
