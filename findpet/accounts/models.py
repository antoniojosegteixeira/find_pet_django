from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# User creator


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        '''
    if extra_fields.get("is_superuser"):
        raise ValueError("Superuser must have 'is_superuser'")

    if extra_fields.get("is_staff"):
        raise ValueError("Superuser must have 'is_staff'")
            '''

        return self.create_user(email=email, password=password, **extra_fields)

# User Model


class User(AbstractUser):

    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=45)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
