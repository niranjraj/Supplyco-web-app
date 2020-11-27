from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    aadhar= models.IntegerField(unique=True)
    phoneNumber=models.CharField(blank=True,max_length=10)
    avatar=models.ImageField(upload_to='avatar',blank=True)



    def __str__(self):
        return self.name


