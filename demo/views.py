from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

def show_product(request):
    p = Product("iPhone X", 80000)  # Model
    return render(request, 'product_info.html', {"product": p})


def show_products_list(request):
    products = [Product("iPhone X", 80000),
                Product("Google Pixel XL", 60000),
                Product("Samsung S9 Plus", 70000)]
    return render(request, 'products_list.html', {"products": products})
