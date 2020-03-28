from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.


class RegisteredUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    isCustomer = models.BooleanField(default=False)
    isClient = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Customer(models.Model):
    userEmail = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    bio = models.CharField(max_length=200)


class Client(models.Model):
    userEmail = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=200)
    workingHours = models.CharField(max_length=200)
    workingDays = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Admin(models.Model):
    userEmail = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, primary_key=True)

