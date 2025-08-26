from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Firstname=models.CharField(max_length=25,blank=True,null=True)
    Lastname=models.CharField(max_length=25,blank=True,null=True)
    Email=models.CharField(max_length=500,blank=True,null=True)
    Phonenumber=models.IntegerField(default=0,blank=True,null=True)
    Pin=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.user.firstname + "profile"
