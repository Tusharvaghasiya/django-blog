# Generated by Django 2.2.5 on 2019-10-14 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191012_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 17, 41, 38, 51914, tzinfo=utc)),
        ),
    ]
