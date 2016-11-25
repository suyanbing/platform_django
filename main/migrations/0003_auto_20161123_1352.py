# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_dmis_field_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='dmis_field_report',
            name='Country',
            field=models.ManyToManyField(to='main.Dmis_countries'),
        ),
        migrations.AddField(
            model_name='dmis_field_report',
            name='DisasterType',
            field=models.ManyToManyField(to='main.Dmis_disasters'),
        ),
    ]
