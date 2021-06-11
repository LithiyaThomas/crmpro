from . models import Customer,Items
from django import forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['company','VAT','phone','website','groups','currency','language','address','city','state','zipcode','country']

class ItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=['description','long_description','rate','tax1','tax2','unit']