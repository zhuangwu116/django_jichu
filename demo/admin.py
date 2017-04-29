# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from demo.models import *
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)
