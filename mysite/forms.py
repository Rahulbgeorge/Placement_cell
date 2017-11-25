from django import forms
from django.http import HttpResponse
from . import models

class login_form(forms.Form):
    username=forms.CharField(label="Username",max_length=30)
    password=forms.CharField(label="Password",widget=forms.PasswordInput)

class notification_form(forms.Form):
    topic=forms.CharField(label='',max_length=150,widget=forms.TextInput(attrs={'placeholder': '                Topic'}))
    content=forms.CharField(label='',max_length=600,widget=forms.Textarea(attrs={'cols': 80, 'rows': 50,'placeholder':'Content'}))
    file=forms.FileField(label='picture',required=False)
