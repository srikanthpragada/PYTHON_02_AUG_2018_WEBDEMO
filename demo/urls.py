from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('product/', views.show_product),

]
