from django.db import models
from django.contrib.auth import get_user_model
from accounts.validators import validate_aadhaar

User=get_user_model()
# Create your models here.
class Customer (models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    aadhaar=models.CharField(unique=True,validators=[validate_aadhaar],max_length=12)
    phoneNumber=models.CharField(blank=True,max_length=10)
    avatar=models.ImageField(upload_to='avatar',blank=True)



    def __str__(self):
        return self.name


