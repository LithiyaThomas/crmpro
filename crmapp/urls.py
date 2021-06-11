from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('items/', views.itemadd, name='itemadd'),
    path('itemgroup/', views.itemgroups, name='itemgroups'),
    path('custgroup/', views.custgroup, name='custgroup'),
    path('bill/', views.billadd, name='billadd'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]