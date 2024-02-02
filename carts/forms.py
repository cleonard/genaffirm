from django import forms


class CartForm(forms.Form):
    name = forms.CharField(label="Cart Name")
    notes = forms.CharField(widget=forms.Textarea)
    amount = forms.IntegerField(label="Amount (whole dollars)")
