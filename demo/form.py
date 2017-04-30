# -*- coding: utf-8 -*-
from django import forms
from demo.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
#表单字段的验证器
# def validate_name(value):
#     try:
#
#         print "validate_name："+value
#         Publisher.objects.get(name=value)
#         raise ValidationError('%s的信息已存在'%value)
#     except Publisher.DoesNotExist:
#         print ("zhuangwu:"+"doesnotexist")
class PublisherForm(forms.ModelForm):
    # name=forms.CharField(label='名称',error_messages={'required':'名称必填'})
    # address = forms.CharField(label='地址',error_messages={'required':'地址必填'})
    # city = forms.CharField(label='城市',error_messages={'required':'城市必填'})
    # state_province = forms.CharField(label='省份',error_messages={'required':'省份必填'})
    # country = forms.CharField(label='国家',error_messages={'required':'国家必填'})
    # website = forms.URLField(label='网址',error_messages={'required':'网址必填'})
    # name=forms.CharField(label='名称',validators=[validate_name])
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     try:
    #         Publisher.objects.get(name=name)
    #         raise ValidationError('%s的信息已存在'%name)
    #     except Publisher.DoesNotExist:
    #         print ("zhuangwu:"+"doesnotexist")
    #     return name
    def clean(self):
        cleaned_data=super(PublisherForm,self).clean()
        name = cleaned_data['name']
        try:
            Publisher.objects.get(name=name)
            self.add_error('name','表单已存在')
        except Publisher.DoesNotExist:
            print ("zhuangwu:"+"doesnotexist")
        return cleaned_data
    class Meta:
        model=Publisher
        exclude=('id',)