# Generated by Django 2.2 on 2019-05-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]