# Generated by Django 2.2.5 on 2019-10-14 18:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191014_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 18, 5, 3, 951812, tzinfo=utc)),
        ),
    ]
