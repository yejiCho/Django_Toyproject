# form tag 
from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': 'plz input id'
        },
        max_length=32, label="username")
    password = forms.CharField(
        error_messages={
            'required': 'plz input passwd'
        },
        widget=forms.PasswordInput,label="password")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = fcuser.objects.get(username = username)
            if not check_password(password, fcuser.password):
                self.add_error('password', 'not match password')
            else:
                self.user_id = fcuser.id