from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=255,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username