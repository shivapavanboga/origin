from django.db import models

from user.models import User


class Contact(models.Model):
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="contacts")
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.phone}"
    class Meta:
        indexes = [
            models.Index(fields=['phone']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'phone'], name='unique_user_contact')
        ]
