# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.


class sharePrice(models.Model):
    company = models.CharField(max_length=200)
    data = models.DateField('month')
    price = models.FloatField(default=0)
    def __str__(self):
        return self.company



#class Choice(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  #  choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    def __str__(self):
#        return self.choice_text
