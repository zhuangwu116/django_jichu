# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=60)
    state_province=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    website=models.URLField()
class Author(models.Model):
    name=models.CharField(max_length=30)
class AuthorDetail(models.Model):
    sex=models.BooleanField(max_length=1,choices=((0,'男'),(1,'女')))
    email=models.EmailField()
    address=models.CharField(max_length=50)
    birthday=models.DateField()
    author=models.OneToOneField(Author)
class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField()