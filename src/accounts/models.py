from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import validate_aadhaar

class UserManager(BaseUserManager):
    def create_user(self,email,aadhaar, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')     
        user = self.model(
            aadhaar=aadhaar,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,aadhaar, password):
        user = self.create_user(
            email,
            aadhaar,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,aadhaar, password):
        user = self.create_user(
            email,
            aadhaar,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user






class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
    aadhaar=models.CharField(unique=True,validators=[validate_aadhaar],max_length=12)
 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['aadhaar'] 


    objects = UserManager()

    def __str__(self):            
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True    


    @property
    def is_staff(self):
  
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active