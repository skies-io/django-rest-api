# -*- coding: utf-8 -*-

from rest_api.API import API
from rest_api.errors import ResponseError, ResponseNotFound, ResponseNotImplemented
from rest_api.decorators import must_be_connected, get_data
from example.models import Project, User
from django.conf.urls import url


class ProjectAPI(API):
    format_object = {
        "id": {},
        "name": {},
        "owner": {
            "object": {
                "id": {"field": "owner__id"},
                "email": {"field": "owner__email"}
            }
        },
        "contributors": {
            "list": False,
            "object_list": "contributors",
            "object_list_order": "id",
            "object": {
                "id": {"field": "id"},
                "email": {"field": "email"}
            }
        }
    }

    # GET /api/1.0/project : get projects
    @must_be_connected
    def method_get_list(self, session, request, **kwargs):
        obj = Project.objects.select_related('user').all()
        data = self.pagination(request, obj)
        data["results"] = [self.format(item) for item in data["results"]]
        return self.response(data)

    # GET /api/1.0/project/<id> : get details of a project
    @must_be_connected
    def method_get_detail(self, session, request, _id, **kwargs):
        try:
            project = Project.objects.get(pk=_id)
        except:
            raise ResponseNotFound(details=["Project not found"])
        return self.response(self.format(project))

    # POST /api/1.0/project : add a new project
    @must_be_connected
    @get_data(["name", "owner_id"])
    def method_post_list(self, session, request, data, **kwargs):
        try:
            owner = User.objects.get(pk=data["owner_id"])
        except:
            raise ResponseNotFound(details=["Owner not found"])
        try:
            project = Project.objects.create(name=data["name"], owner=owner)
        except Exception as e:
            raise ResponseError("Unable to create the project.", details=[str(e)])
        return self.response(self.format(project), code=201)

    # PUT /api/1.0/project/<id> : update a project
    @must_be_connected
    @get_data(["name", "owner_id"])
    def method_put_detail(self, session, request, _id, data, **kwargs):
        # Update project...
        raise ResponseNotImplemented()

    # DELETE /api/1.0/project/<id> : delete a project
    @must_be_connected
    def method_delete_detail(self, session, request, _id, **kwargs):
        # Delete project...
        raise ResponseNotImplemented()

    """
        Contributors
    """

    def prepend_urls(self):
        urls = super().prepend_urls()
        urls.append(url(r"^%s/(?P<_id>[0-9]+)/contributors(/?)$" % self.resource_name,
                        self.dispatch_api("contributors_list")))
        urls.append(url(r"^%s/(?P<_id>[0-9]+)/contributors/(?P<_id2>[0-9]+)(/?)$" % self.resource_name,
                        self.dispatch_api("contributors_detail")))
        return urls

    format_object_contributors = {
        "id": {},
        "email": {}
    }

    # GET /api/1.0/project/<id>/contributors : get contributors
    @must_be_connected
    def method_get_contributors_list(self, session, request, _id, **kwargs):
        try:
            project = Project.objects.get(pk=_id)
        except:
            raise ResponseNotFound(details=["Project not found"])
        data = self.pagination(request, project.contributors.all())
        data["results"] = [self.format(item, _format=self.format_object_contributors) for item in data["results"]]
        return self.response(data)

    # POST /api/1.0/project/<id>/contributors : add a contributor
    @must_be_connected
    def method_post_contributors_list(self, session, request, _id, **kwargs):
        # Add a contributor...
        raise ResponseNotImplemented()

    # DELETE /api/1.0/project/<id>/contributors/<id> : remove a contributor
    @must_be_connected
    def method_delete_contributors_detail(self, session, request, _id, _id2, **kwargs):
        # Remove a contributor...
        raise ResponseNotImplemented()

