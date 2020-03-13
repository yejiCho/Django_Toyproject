from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

# 상품목록만들기
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

