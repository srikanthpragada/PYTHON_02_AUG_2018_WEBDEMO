from django.contrib import admin
from django.urls import path
from . import views
from . import dept_views


urlpatterns = [
    path('product/', views.show_product),
    path('products/', views.show_products_list),
    path('netprice/', views.net_price_calculator),
    path('netprice2/', views.net_price),
    path('netprice3/', views.net_price_with_form),
    path('add_dept/', dept_views.add_dept),
    path('list_depts/', dept_views.list_depts),

]
