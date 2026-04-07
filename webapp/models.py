from django.db import models

# Create your models here.
class RegistrationDb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    confirm_password = models.CharField(max_length=100,null=True,blank=True)
class Appointment(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Doctor=models.CharField(max_length=100,null=True,blank=True)
    Appointment_Date=models.DateField(null=True,blank=True)
    Appointment_Time=models.TimeField(null=True,blank=True)
    Reason=models.CharField(max_length=100,null=True,blank=True)
class ContactDb(models.Model):
    Name = models.CharField(max_length=100,unique=True)
    Email = models.EmailField(null=True,blank=True)
    Message = models.TextField(null=True,blank=True)
