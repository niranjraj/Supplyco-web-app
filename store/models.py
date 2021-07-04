from django.db import models
from django.contrib.auth import get_user_model
from accounts.validators import validate_aadhaar
from products.imagepath import get_filename
from products.models import ShippingAddress
import uuid

User = get_user_model()
# Create your models here.


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)
    if (instance.pk):
        new_filename = instance.pk
    else:
        new_filename = uuid.uuid4().hex
    final_name = f"{new_filename}{ext}"
    return f"avatars/{final_name}"


class Customer (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    aadhaar = models.CharField(unique=True, validators=[
                               validate_aadhaar], max_length=12)
    phoneNumber = models.CharField(blank=True, max_length=10)
    avatar = models.ImageField(
        upload_to=upload_image_path, blank=True, default='avatars/10.png')
    phoneOtp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url


class Delivery (models.Model):

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Delivering', 'Delivering'),
        ('Delivered', 'Delivered'),

    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    deliverAddress = models.ForeignKey(
        ShippingAddress, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=50, default='Available')

    def __str__(self):
        return str(self.id)


class Help(models.Model):
    name = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(blank=True, max_length=10)
    question = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=255, unique=True)
    read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.read)
