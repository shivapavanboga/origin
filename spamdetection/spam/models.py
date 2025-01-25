from django.db import models

from user.models import User


class SpamReport(models.Model):
    phone = models.CharField(max_length=15)
    spammed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="spams")
    def __str__(self):
        return f"{self.phone}"
    class Meta:
        indexes = [
            models.Index(fields=['phone']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['phone', 'spammed_by'], name='unique_spam_report')
        ]

