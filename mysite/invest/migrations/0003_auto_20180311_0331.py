# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-11 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_auto_20180228_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareprice',
            name='data',
            field=models.DateField(verbose_name='month'),
        ),
    ]
