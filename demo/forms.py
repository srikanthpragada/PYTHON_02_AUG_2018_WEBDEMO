from django import forms
from django.forms import ModelForm
from demo.models import Book


class NetPriceForm(forms.Form):
    amount = forms.IntegerField(label="Selling Price")
    qty = forms.IntegerField(label="Quantity Required", min_value=1, max_value=10)


class AddDeptForm(forms.Form):
    name = forms.CharField(label="Department Name", max_length=30)
    location = forms.ChoiceField(label="Department Location",
                                 # (value,text)
                                 choices=[("Mumbai", "Mumbai"),
                                          ("Delhi", "Delhi"),
                                          ("Chennai", "Chennai"), ])

# form created from model
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'author']
