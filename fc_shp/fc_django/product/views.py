from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
# Create your views here.

# 상품목록만들기
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

# 상품등록하기
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
