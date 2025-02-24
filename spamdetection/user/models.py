from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """global db"""
    name = models.CharField(max_length=20,null=True,blank=True)
    phone = models.CharField(max_length=15,null=False,blank=False,unique=True)
    email = models.EmailField(unique=True)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.phone}"
    class Meta:
        indexes = [
            models.Index(fields=['phone']),
        ]

