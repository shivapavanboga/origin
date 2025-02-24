from django.db import models
from user.models import User

class Contact(models.Model):
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.contact.id}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'contact'], name='unique_user_contact')
        ]
