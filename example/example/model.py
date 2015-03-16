# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.query import QuerySet


class ExampleQuerySet(QuerySet):
    def list_values(self, *args, **kwargs):
        data = []
        for item in self:
            data.append(item.values(*args, **kwargs))
        return data

    def list_multiple_values(self, base, **kwargs):
        data = self.list_values(**base)
        for index, value in enumerate(data):
            for elem in kwargs:
                value[elem] = getattr(self[index], elem).all().list_values(*kwargs[elem])
        return data


class BaseExampleModel(models.Model):
    objects = ExampleQuerySet().as_manager()

    class Meta:
        abstract = True

    def get_attribute(self, name, instance=None):
        if not instance:
            instance = self
        if hasattr(instance, name):
            return getattr(instance, name)
        names = name.split('__')
        name = names.pop(0)
        if len(names) == 0:
            return None
        if hasattr(instance, name):
            value = getattr(instance, name)
            if value is None:
                return None
            return instance.get_attribute("__".join(names), instance=value)
        return None

    def values(self, *args, **kwargs):
        data = dict()
        for arg in args:
            data[arg] = self.get_attribute(arg)
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                data[arg] = self.values(**kwargs[arg])
            else:
                data[arg] = self.get_attribute(kwargs[arg] if kwargs[arg] else arg)
        return data
