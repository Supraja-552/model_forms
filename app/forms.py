from django import forms
from app.models import *
class Topic_form(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class Webpage_form(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        labels={'topic_name':'TN','url':'URL'}
        #fields=['name','url','email']
        exclude=('name','url')
        widget={'email':'forms.PasswordInput'}
        
class Access_form(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        widget={
            'author':'forms.PasswordInput'}