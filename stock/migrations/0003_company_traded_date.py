# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-15 16:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20170613_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 6, 15)),
        ),
    ]
