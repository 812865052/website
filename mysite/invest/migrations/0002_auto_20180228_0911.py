# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareprice',
            name='data',
            field=models.DateTimeField(verbose_name='month'),
        ),
    ]
