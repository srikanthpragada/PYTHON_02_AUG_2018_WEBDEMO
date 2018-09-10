from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

def  net_price_calculator(request):
    netamount = 0
    amount = ""
    qty = ""
    if 'amount' in request.GET:
        # calculate net amount
        amount = int(request.GET['amount'])
        qty = int(request.GET['qty'])
        netamount = amount * qty
        if qty > 5:
            netamount = netamount * 0.90

    return render(request,'net_price_calculator.html',
                   {'netamount': netamount, "amount" : amount, "qty": qty})


def  net_price(request):
    print("Request type : ", request.method)
    if request.method == "POST":
        # calculate net amount
        amount = int(request.POST['amount'])
        qty = int(request.POST['qty'])
        netamount = amount * qty
        if qty > 5:
            netamount = netamount * 0.90
        return render(request,'net_price.html',
                   {'netamount': netamount, "amount" : amount, "qty": qty})
    else:  # Get request
        return render(request, 'net_price.html')


def  net_price_with_form(request):
    if request.method == "POST":
        # calculate net amount
        amount = int(request.POST['amount'])
        qty = int(request.POST['qty'])
        netamount = amount * qty
        if qty > 5:
            netamount = netamount * 0.90
        return render(request,'net_price.html',
                   {'netamount': netamount, "amount" : amount, "qty": qty})
    else:  # Get request
        return render(request, 'net_price.html')



def show_product(request):
    p = Product("iPhone X", 80000)  # Model
    return render(request, 'product_info.html', {"product": p})


def show_products_list(request):
    products = [Product("iPhone X", 80000),
                Product("Google Pixel XL", 60000),
                Product("Samsung S9 Plus", 70000)]

    avg = sum([p.price for p in products]) / len(products)

    return render(request, 'products_list.html',
                   {"products": products , "average" : avg})
