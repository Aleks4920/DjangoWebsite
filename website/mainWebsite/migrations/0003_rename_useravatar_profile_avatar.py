# Generated by Django 3.2.4 on 2021-06-24 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainWebsite', '0002_profile_useravatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userAvatar',
            new_name='avatar',
        ),
    ]