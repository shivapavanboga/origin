from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    model stores registered users only
    """
    name = models.CharField(max_length=20,null=False,blank=False)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.phone}"
    class Meta:
        indexes = [
            models.Index(fields=['phone']),
        ]

