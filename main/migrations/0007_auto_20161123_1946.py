# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_dmis_disasters_aggregation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmis_field_report',
            name='NumericalReport',
            field=models.ManyToManyField(blank=True, to='main.Dmis_numericalreport'),
        ),
    ]
