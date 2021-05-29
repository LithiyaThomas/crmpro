from django.contrib import admin
from . models import Items
from . models import Item_groups
from . models import Customer
from . models import Billaddress

# Register your models here.
admin.site.register(Items)
admin.site.register(Item_groups)
admin.site.register(Customer)
admin.site.register(Billaddress)