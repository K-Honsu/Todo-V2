from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


class UserAccountManagerr(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('enter a valid email')
        
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.password = make_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            last_name,
            first_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True #this allows a user make changes in the admin panel
        user.save(using=self._db)
        return user
    
    
class UserAcct(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=22, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    
    objects = UserAccountManagerr()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
