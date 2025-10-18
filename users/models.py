from typing import Iterable
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from users.managers import CustomUserManager 

class CustomUser(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    

    class Meta():
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    

