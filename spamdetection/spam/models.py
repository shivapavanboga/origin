from django.db import models
from user.models import User


class SpamReport(models.Model):
    spam_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reported_as_spam")
    spammed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports_made")

    def __str__(self):
        return f"{self.spam_user.id}"

    class Meta:
        indexes = [
            models.Index(fields=['spam_user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['spam_user', 'spammed_by'], name='unique_spam_report')
        ]


class SpamUser(models.Model):  # Added `models.Model`
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spam_count = models.IntegerField(default=0)
