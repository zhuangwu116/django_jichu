from django import forms
class PublisherForm(forms.Form):
    name=forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    state_province = forms.CharField()
    country = forms.CharField()
    website = forms.URLField()