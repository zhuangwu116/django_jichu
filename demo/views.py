# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from demo.models import *
# Create your views here.
def hello(request):
    user=User.objects.all()
    value1=''
    value2='<a href="/">百度</a>'
    print user.query
    print request.path
    if request.method=='GET':
        print request.GET.get('name')
    if request.method=='POST':
        print request.POST.get('key')
    return render(request,'index.html',locals())
def add_publisher(request):
    if request.method=='POST':
        name=request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        state_province = request.POST['state_province']
        country = request.POST['country']
        website = request.POST['website']
        Publisher.objects.create(name=name,
                                 address=address,
                                 city=city,
                                 state_province=state_province,
                                 country=country,
                                 website=website)
        return HttpResponse('添加成功')
    else:
        return render(request,'add_publisher.html',locals())