# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def hello(request):
    user=User.objects.all()
    print user.query
    print request.path
    if request.method=='GET':
        print request.GET.get('name')
    if request.method=='POST':
        print request.POST.get('key')
    return render(request,'index.html',locals())