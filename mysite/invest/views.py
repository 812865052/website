# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import sharePrice
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import json
from django.core import serializers
from db import db_query, insertdate, insertcompany
from .forms import ChooseForm, compareCompany

def index(request):
    company_list = sharePrice.objects.all()
    # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
    data = serializers.serialize("json", company_list)
    companylist = db_query('/home/website/demo/mysite/db.sqlite3', 'invest_sharePrice', "*")
    context = {
        #'company_list': json.dumps(company_list),
        'company_list': data,
        'companylist': companylist,
    }
    return render(request, 'invest/index.html', context)

def dataoperation(request):
    company_list = sharePrice.objects.all()
    # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
    data = serializers.serialize("json", company_list)
    companylist = db_query('/home/website/demo/mysite/db.sqlite3', 'invest_sharePrice', "*")
    context = {
        #'company_list': json.dumps(company_list),
        'company_list': data,
        'companylist': companylist,
    }
    return render(request, 'invest/data.html', context)

# def test(request):
#     context = {
#         #'company_list': json.dumps(company_list),
#         'company_list': data,
#     }
#     return render(request, 'invest/index.html', context)

def adddb(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChooseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            return render(request, 'invest/index_temp.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChooseForm()

    return render(request, 'index.html', {'form': form})


def compare(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = compareCompany(request.POST)
        print request.POST.getlist('selectCompany')
        companylist = request.POST.getlist('selectCompany')
        data = []
        year = 2017
        month = 2
        day = 8
        table = 'invest_sharePrice'
        path = '/home/website/demo/mysite/db.sqlite3'
        insertdate(year,month,day,data,companylist)
        insertcompany(path,data,table,companylist) #insertcompany(path,data,table,companylist)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            context = {
                'data' = data,
                'form': companylist,
            }
            return render(request, 'invest/index_temp.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = compareCompany()

    return render(request, 'index.html', {'form': form})
