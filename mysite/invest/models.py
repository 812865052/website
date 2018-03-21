# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.


class sharePrice(models.Model):
    company = models.CharField(max_length=200)
    date = models.DateField('month')
    price = models.FloatField(default=0)
    def __str__(self):
        return self.company

class datedb(models.Model):
    date = models.DateField('month')
    def __str__(self):
        return self.date
