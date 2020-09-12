from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=12)
  desc= models.TextField()
  date = models.DateField()

class login(models.Model):
   username = models.CharField(max_length=50)
   password = models.CharField(max_length=50)    

class Register(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=12)
  date = models.DateField()

   