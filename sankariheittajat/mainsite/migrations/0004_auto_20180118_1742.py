# Generated by Django 2.0 on 2018-01-18 17:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20180118_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uutiset',
            name='aika',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 1, 18, 17, 42, 22, 355409, tzinfo=utc)),
        ),
    ]