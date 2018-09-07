from django.db import models


# Create your models here.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
