# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30,verbose_name='名称')
    address=models.CharField(max_length=50,verbose_name='地址')
    city=models.CharField(max_length=60,verbose_name='市')
    state_province=models.CharField(max_length=30,verbose_name='省')
    country=models.CharField(max_length=50,verbose_name='国家')
    website=models.URLField(verbose_name='网址')
    class Meta:
        verbose_name='出版社'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name='名字')
    class Meta:
        verbose_name='作者'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class AuthorDetail(models.Model):
    sex=models.BooleanField(max_length=1,choices=((0,'男'),(1,'女')),verbose_name='性别')
    email=models.EmailField(verbose_name='邮箱')
    address=models.CharField(max_length=50,verbose_name='住址')
    birthday=models.DateField(verbose_name='出生日期')
    author=models.OneToOneField(Author,verbose_name='作者')
    class Meta:
        verbose_name='作者详情'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.author.name
class Book(models.Model):
    title=models.CharField(max_length=100,verbose_name='书名')
    authors=models.ManyToManyField(Author,verbose_name='作者')
    publisher=models.ForeignKey(Publisher,verbose_name='出版社')
    publication_date=models.DateField(verbose_name='出版日期')
    price=models.DecimalField(max_digits=5,decimal_places=2,default=10,verbose_name='价格')
    class Meta:
        verbose_name='书籍'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title