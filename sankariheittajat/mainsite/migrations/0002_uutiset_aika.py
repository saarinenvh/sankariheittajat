# Generated by Django 2.0 on 2018-01-18 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uutiset',
            name='aika',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 17, 33, 57, 95641)),
        ),
    ]
