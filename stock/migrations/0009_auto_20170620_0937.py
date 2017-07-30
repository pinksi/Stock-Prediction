# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-20 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20170620_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='banking',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='devbank',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='finance',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='floatindex',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hydropower',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='insurance',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nepse',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='others',
            name='volume',
            field=models.BigIntegerField(default=0),
        ),
    ]
