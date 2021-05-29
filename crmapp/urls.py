from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('items/', views.itemadd, name='itemadd'),
    path('itemgroup/', views.itemgroups, name='itemgroups'),
    path('custgroup/', views.custgroup, name='custgroup'),
    path('bill/', views.billadd, name='billadd'),
]