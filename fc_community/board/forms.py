# form tag 
from django import forms

class BoardForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요'
        },
        max_length=128, label="제목")
    password = forms.CharField(
        error_messages={
            'required': '내용을 입력하세요'
        },
        widget=forms.Textarea,label="내용")
