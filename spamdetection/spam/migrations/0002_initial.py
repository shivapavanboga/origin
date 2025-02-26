# Generated by Django 5.1.5 on 2025-01-24 12:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spam', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='spamreport',
            name='spammed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='spamreport',
            index=models.Index(fields=['phone'], name='spam_spamre_phone_801e08_idx'),
        ),
        migrations.AddConstraint(
            model_name='spamreport',
            constraint=models.UniqueConstraint(fields=('phone', 'spammed_by'), name='unique_spam_report'),
        ),
    ]
