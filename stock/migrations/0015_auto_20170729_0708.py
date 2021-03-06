# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-29 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20170728_0723'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrainingNews',
        ),
        migrations.AlterField(
            model_name='adbl',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='adbl_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='banking',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='chcl',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='chcl_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='company',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='devbank',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='finance',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='floatindex',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='hydropower',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='nabil',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='nabil_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='nepse',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='nlic',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='nlic_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='ntc',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='ntc_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='ohl',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='ohl_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='others',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='plic',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='plic_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='sbi',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='sbi_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='scb',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='scb_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='shl',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
        migrations.AlterField(
            model_name='shl_live',
            name='traded_date',
            field=models.DateField(default=datetime.date(2017, 7, 29)),
        ),
    ]
