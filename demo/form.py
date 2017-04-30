# -*- coding: utf-8 -*-
from django import forms
from demo.models import *
class PublisherForm(forms.ModelForm):
    # name=forms.CharField(label='名称',error_messages={'required':'名称必填'})
    # address = forms.CharField(label='地址',error_messages={'required':'地址必填'})
    # city = forms.CharField(label='城市',error_messages={'required':'城市必填'})
    # state_province = forms.CharField(label='省份',error_messages={'required':'省份必填'})
    # country = forms.CharField(label='国家',error_messages={'required':'国家必填'})
    # website = forms.URLField(label='网址',error_messages={'required':'网址必填'})
    class Meta:
        model=Publisher
        exclude=('id',)