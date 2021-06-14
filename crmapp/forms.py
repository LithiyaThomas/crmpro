from . models import Customer,Items,Proposal,Estimates,Invoice
from django import forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['company','VAT','phone','website','groups','currency','language','address','city','state','zipcode','country']

class ItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=['description','long_description','rate','tax1','tax2','unit']
class ProposalForm(forms.ModelForm):
    class Meta:
        model=Proposal
        fields=['subject', 'related', 'date','open_till', 'status','assigned','discount_type','currency','to','address','city','state','zipcode','country','email','phone']
