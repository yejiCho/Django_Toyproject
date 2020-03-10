from django import forms
from django.contrib.auth.hashers import check_password,make_password #check_password 암호화,입력받은 값과 DB안에 있는 인코딩 된값 비교
from .models import Fcuser

class RegisterForm(forms.Form):
    # 입력받을 값
    email = forms.EmailField(
        error_messages={
            'required':'이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        }
        ,
        widget=forms.PasswordInput, label='비밀번호'
        # 비밀번호이기 때문에 widget 지정
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    # validation
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        # password and re_password -> True && password 와 re_password가 다르면
        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            # 회원가입
            # DB에 저장
            else:
                fcuser = Fcuser(
                    email = email,
                    password = make_password(password)
                )
                fcuser.save()

class LoginForm(forms.Form):
    # 입력받을 값
    email = forms.EmailField(
        error_messages={
            'required':'이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        }
        ,
        widget=forms.PasswordInput, label='비밀번호'
        # 비밀번호이기 때문에 widget 지정
    )

    # validation
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoesNotExist:
                self.add_error('email','아이디가 없습니다.')
                return
            # 암호화 
            if not check_password(password, fcuser.password):
                self.add_error('password','비밀번호가 틀렸습니다.')
            else:
                # 성공한 지점
                self.email = fcuser.email