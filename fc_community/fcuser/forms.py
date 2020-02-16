# form tag 
from django import forms
from .models import Fcuser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="username")
    password = forms.CharField(widget=forms.PasswordInput,label="password")