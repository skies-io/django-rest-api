# -*- coding: utf-8 -*-

from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=128)


class Project(models.Model):
    owner = models.ForeignKey(User)
    contributors = models.ManyToManyField(User, related_name='project_contributors')
    name = models.CharField(max_length=128)
