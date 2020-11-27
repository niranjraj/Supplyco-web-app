from django.db import models
import random,os
from uuid  import uuid4



def get_filename(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)
    if (instance.pk):
        new_filename=instance.pk 
    else :
        new_filename=uuid4().hex
    final_name = f"{new_filename}{ext}"
    return f"products/{final_name}"

# Create your models here.
class Product(models.Model):
   title = models.CharField(max_length=50)
   active = models.BooleanField(default=False)
   price = models.DecimalField(max_digits=20, decimal_places=2)
   quantity=models.IntegerField(default=0)
   image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   update_at=models.DateTimeField(auto_now=True) 
   


   def __str__(self):
     return self.title

   @property
   def imageURL(self):
       try:
           url=self.image.url
       except:
           url= ''    
       return url 

