from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_name = models.TextField(max_length=100)
    cus_email = models.EmailField()
    cus_mobile = models.TextField(max_length=100)
    
class Products(models.Model):
    cus_id = models.ManyToManyField("Customer",)
    cus_name = models.TextField()
    cus_qty = models.TextField(max_length=100)