# Generated by Django 3.2.4 on 2021-06-18 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainWebsite', '0006_auto_20210617_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
