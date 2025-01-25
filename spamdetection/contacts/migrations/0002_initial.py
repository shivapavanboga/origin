
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['phone'], name='contacts_co_phone_5a60c7_idx'),
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.UniqueConstraint(fields=('user', 'phone'), name='unique_user_contact'),
        ),
    ]
