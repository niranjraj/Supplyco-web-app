from django.db import models
from .imagepath import upload_image_path




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

