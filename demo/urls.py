from django.contrib import admin
from django.urls import path
from . import views
from . import dept_views, book_views, ajax_views

urlpatterns = [
    path('product/', views.show_product),
    path('products/', views.show_products_list),
    path('netprice/', views.net_price_calculator),
    path('netprice2/', views.net_price),
    path('netprice3/', views.net_price_with_form),
    path('add_dept/', dept_views.add_dept),
    path('list_depts/', dept_views.list_depts),
    path('book_home/', book_views.book_home),
    path('add_book/', book_views.add_book),
    path('list_books/', book_views.list_books),
    path('search_books/', book_views.search_books),
    path('ajax/', ajax_views.ajax_demo),
    path('ajax_now/', ajax_views.now),
    path('ajax_get_title/', ajax_views.get_title),
]
