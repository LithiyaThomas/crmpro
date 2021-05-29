from django.db import models

# Create your models here.
class Items(models.Model):
    description=models.CharField(max_length=150)
    long_description = models.TextField(max_length=250)
    rate = models.IntegerField()
    tax1 = models.IntegerField()
    tax2 = models.IntegerField()
    unit = models.IntegerField()
    def __str__(self):
        return self.description


class Item_groups(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Customer(models.Model):
    company=models.CharField(max_length=150)
    VAT = models.CharField(max_length=100)
    phone = models.IntegerField()
    website = models.CharField(max_length=100)
    groups = models.CharField(max_length=200)
    currency= models.CharField(max_length=25)
    language= models.CharField(max_length=100)
    address= models.TextField(max_length=150)
    city= models.CharField(max_length=150)
    state= models.CharField(max_length=150)
    zipcode= models.CharField(max_length=25)
    country= models.CharField(max_length=100)
    def __str__(self):
        return self.company
class Billaddress(models.Model):
    bill_street= models.TextField(max_length=150)
    bill_city = models.CharField(max_length=150)
    bill_state= models.CharField(max_length=150)
    bill_zipcode= models.CharField(max_length=25)
    bill_country= models.CharField(max_length=100)
    ship_street = models.TextField(max_length=150)
    ship_city = models.CharField(max_length=150)
    ship_state = models.CharField(max_length=150)
    ship_zipcode = models.CharField(max_length=25)
    ship_country = models.CharField(max_length=100)
    def __str__(self):
        return self.bill_street
