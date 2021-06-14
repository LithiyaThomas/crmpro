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
class EstimateForm(forms.ModelForm):
    class Meta:
        model=Estimates
        fields=['estimate_no','expiry_date','estimate_date','status1','reference','discount_type1','currency1','sale_agent','admin_note']
class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['invoice_no','due_date','invoice_date','recurring','discount_type2','currency2','sale_agent1','admin_note1']
