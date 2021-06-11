from . models import Customer
from django import forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['company','VAT','phone','website','groups','currency','language','address','city','state','zipcode','country']