from django import forms


class NetPriceForm(forms.Form):
    amount = forms.IntegerField(label="Selling Price")
    qty = forms.IntegerField(label="Quantity Required", min_value=1, max_value=10)
