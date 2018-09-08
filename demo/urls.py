from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('product/', views.show_product),
    path('products/', views.show_products_list),
    path('netprice/', views.net_price_calculator),
    path('netprice2/', views.net_price),

]
