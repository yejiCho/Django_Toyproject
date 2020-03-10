from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.

def index(request):
    # 세션에 있는 email주소를 갖고오게 함
    return render(request, 'index.html',{'email':request.session.get('user')})


class RegisterView(FormView):
    # html 이름
    template_name = 'register.html'
    form_class = RegisterForm
    # 정상적으로 값이 들어왔을 경우 success_url 주소로 이동
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # session 유효성검사
    def form_valid(self, form):
        self.request.session['user'] = form.email # 로그인한 이메일을 세션에 저장

        return super().form_valid(form)