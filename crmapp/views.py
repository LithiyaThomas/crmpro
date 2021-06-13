from django.shortcuts import render
from django.http import HttpResponse
from . models import Customer
from . models import Items
from . models import Billaddress
from . models import Item_groups
from . forms import CustomerForm,ItemForm
from django.shortcuts import redirect


# Create your views here.
def add(request):
    customer1=Customer.objects.all()

    if request.method == 'POST':
        company=request.POST.get('company','')
        VAT = request.POST.get('VAT','')
        phone = request.POST.get('phone','')
        website = request.POST.get('website','')
        groups = request.POST.get('groups','')
        currency = request.POST.get('currency','')
        language = request.POST.get('language','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zipcode = request.POST.get('zipcode','')
        country = request.POST.get('country','')
        customer=Customer(company=company,VAT=VAT,phone=phone,website=website,groups=groups,currency=currency,language=language,address=address,city=city,state=state,zipcode=zipcode,country=country)
        customer.save()
    return render(request,"index.html",{'customer1':customer1})
def itemadd(request):
    item1=Items.objects.all()

    if request.method == 'POST':
        description=request.POST.get('description','')
        long_description = request.POST.get('long_description','')
        rate = request.POST.get('rate','')
        tax1 = request.POST.get('tax1','')
        tax2 = request.POST.get('tax2','')
        unit = request.POST.get('unit','')
        items=Items(description=description,long_description=long_description,rate=rate,tax1=tax1,tax2=tax2,unit=unit)
        items.save()
    return render(request,"customer.html",{'item1':item1})
def itemgroups(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        item_groups = Item_groups(name=name)
        item_groups.save()
    return render(request,"items.html")
def custgroup(request):
    return render(request,"custgroup.html")
def billadd(request):
    if request.method == 'POST':
        bill_street = request.POST.get('bill_street', '')
        bill_city = request.POST.get('bill_city', '')
        bill_state = request.POST.get('bill_state', '')
        bill_zipcode = request.POST.get('bill_zipcode', '')
        bill_country = request.POST.get('bill_country', '')
        ship_street = request.POST.get('ship_street', '')
        ship_city = request.POST.get('ship_city', '')
        ship_state = request.POST.get('ship_state', '')
        ship_zipcode = request.POST.get('ship_zipcode', '')
        ship_country = request.POST.get('ship_country', '')
        billaddress = Billaddress(bill_street=bill_street, bill_city=bill_city, bill_state=bill_state, bill_zipcode=bill_zipcode, bill_country=bill_country,ship_street=ship_street,ship_city=ship_city,ship_state=ship_state,ship_zipcode=ship_zipcode,ship_country=ship_country)
        billaddress.save()
    return render(request,"billing.html")
def delete(request,id):
    customer=Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    customer=Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'customer': customer})

def delete1(request,iid):
    item=Items.objects.get(iid=iid)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'delete.html')
def update1(request,id):
    item=Items.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'item':item})
def proposal(request):
    return render(request, "proposal.html")
def invoice(request):
    return render(request, "invoice.html")