# Generated by Django 2.2 on 2019-05-16 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0006_auto_20190516_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='datetime',
            field=models.DateTimeField(default='2019YYY-05m-16d 17H:13M'),
        ),
    ]