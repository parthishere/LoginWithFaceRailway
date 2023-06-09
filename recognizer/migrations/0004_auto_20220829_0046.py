# Generated by Django 3.2.15 on 2022-08-28 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recognizer', '0003_alter_userprofile_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionattendancemodel',
            name='requested_users',
            field=models.ManyToManyField(blank=True, related_name='requested_sessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='accept_with_request',
            field=models.BooleanField(default=False),
        ),
    ]
