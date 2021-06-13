from django.contrib import admin
from . models import Items
from . models import Item_groups,Invoice
from . models import Customer,Estimates
from . models import Billaddress,Proposal

# Register your models here.
admin.site.register(Items)
admin.site.register(Item_groups)
admin.site.register(Customer)
admin.site.register(Billaddress)
admin.site.register(Proposal)
admin.site.register(Estimates)
admin.site.register(Invoice)