# Generated by Django 2.2 on 2019-05-16 21:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0007_auto_20190516_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 21, 16, 24, 364960, tzinfo=utc)),
        ),
    ]