from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Fcuser
# Create your views here.

def index(request):
    return render(request, 'index.html')
