from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home')

def login(request):
    if request.method == 'GET':    
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        res_data = {}
        if not (username and password):
            res_data['error'] = 'input all data'
        else:
            fcuser = Fcuser.objects.get(username = username)
            # fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                return redirect('/')    # go root(home)
                # if passwords correct, login !
                #  session
                #  redirect home_site
                # pass
            else:
                res_data['error'] = 'incorrecr password'

            return render(request, 'login.html',res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    # folder/folder/register.html
    elif request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # passwordcheck = request.POST['passwordcheck']
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        passwordcheck = request.POST.get('passwordcheck',None)
        

        res_data = {}

        if not (username and useremail and password and passwordcheck):
            res_data['error'] = 'input all data'
        elif password != passwordcheck:
            res_data["error"] = "not match passwrod"
            # return HttpResponse('not match password')
        else:
            fcuser = Fcuser(
                username = username,
                # password = password
                useremail = useremail,
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
