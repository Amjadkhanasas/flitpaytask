from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices


# Create your models here.
class Table1_Tempuser(models.Model):   
    mobilenumber = models.IntegerField()
    otp = models.CharField(max_length=100,null=True,blank=True)
    expiretime = models.TimeField(auto_now_add=True)
    createdtime = models.TimeField(auto_now_add=True)   

Choices = (("Active","Active"),
("InActive","InActive"))
class Table2_Customer(models.Model):

    customername =models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    mobilenumber = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=Choices,max_length=100)

class Table4_tradetype(models.Model):
    tradeid = models.IntegerField()
    tradetype = models.CharField(max_length=100)
    status = models.CharField(choices=Choices,max_length=100)
    
class Table3_tradesman(models.Model):
    Table_4_id = models.ForeignKey(Table4_tradetype,on_delete=models.CASCADE)
    tradesman_name = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=Choices,max_length=100)


    
class Table6_Image_Uplodad(models.Model):
    Table2_id = models.ForeignKey(Table2_Customer,on_delete=models.CASCADE)
    status = models.CharField(choices=Choices,max_length=100)
    imagepath = models.ImageField()
    created_date = models.DateField(auto_now_add=True)



Choices = (("Pending","Pending"),
("Booked","Booked"),("Cancel","Cancel"))


class Table5_booktradesman(models.Model):
    Table2_id = models.ForeignKey(Table2_Customer,on_delete=models.CASCADE)
    Table3_id =models.ForeignKey(Table3_tradesman,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(choices=Choices,max_length=100)


#class login(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField(blank=True)
    














