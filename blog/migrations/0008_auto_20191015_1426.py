# Generated by Django 2.2.5 on 2019-10-15 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191014_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 14, 26, 1, 537999, tzinfo=utc)),
        ),
    ]