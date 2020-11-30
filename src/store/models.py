from django.db import models
from django.contrib.auth import get_user_model
from accounts.validators import validate_aadhaar
from products.imagepath import get_filename

User=get_user_model()
# Create your models here.

def upload_image_path(instance, filename):
    name, ext = get_filename(filename)
    if (instance.pk):
        new_filename=instance.pk 
    else :
        new_filename=uuid4().hex
    final_name = f"{new_filename}{ext}"
    return f"avatars/{final_name}"

class Customer (models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    aadhaar=models.CharField(unique=True,validators=[validate_aadhaar],max_length=12)
    phoneNumber=models.CharField(blank=True,max_length=10)
    avatar=models.ImageField(upload_to=upload_image_path,blank=True,default='avatars/avatar.png')



    def __str__(self):
        return self.name


    @property
    def imageURL(self):
       try:
           url=self.avatar.url
       except:
           url= ''    
       return url 