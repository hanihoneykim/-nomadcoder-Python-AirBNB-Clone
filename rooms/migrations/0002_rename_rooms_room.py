# Generated by Django 4.1.3 on 2022-11-07 15:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Rooms",
            new_name="Room",
        ),
    ]
