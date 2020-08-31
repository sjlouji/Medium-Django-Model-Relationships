from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)

class Account(models.Model):
    person = models.ForeignKey("Person",on_delete=models.CASCADE)
    account_number = models.TextField()
    balance = models.TextField(max_length=100)