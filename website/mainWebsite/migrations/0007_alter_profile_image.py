# Generated by Django 3.2.4 on 2021-06-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainWebsite', '0006_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='userPics'),
        ),
    ]
