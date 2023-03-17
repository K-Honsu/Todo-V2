from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Please enter a valid email address')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user
    
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
