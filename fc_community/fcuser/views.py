from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Fcuser
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    # folder/folder/register.html
    elif request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # passwordcheck = request.POST['passwordcheck']
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        passwordcheck = request.POST.get('passwordcheck',None)
        

        res_data = {}

        if not (username and password and passwordcheck):
            res_data['error'] = 'input all data'
        elif password != passwordcheck:
            res_data["error"] = "not match passwrod"
            # return HttpResponse('not match password')
        else:
            fcuser = Fcuser(
            username = username,
            # password = password
            password = make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)

        # if password != passwordcheck:
        #     return HttpResponse('not match password')

        # fcuser = Fcuser(
        #     username = username,
        #     password = password
        # )

        # fcuser.save()

        # return render(request, 'register.html')
