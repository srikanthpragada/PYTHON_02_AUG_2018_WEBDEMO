from django.db import models


# Create your models here.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Book (models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    author = models.CharField(max_length=50, null=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
