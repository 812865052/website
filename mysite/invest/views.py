# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os
import uuid
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
from db import db_query, insertdate, insertcompany, db_insert, db_delete, db_deleteid
from .forms import addCompanyData, compareCompany, deleteCompanyData, deleteCompanyidData
from django.views.decorators.csrf import csrf_exempt, csrf_protect

static_path = '/home/website/demo/mysite/invest/static/'

def index(request):
    company_list = sharePrice.objects.all()
    # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
    data = serializers.serialize("json", company_list)
    companylist = db_query('/home/website/demo/mysite/db.sqlite3', 'invest_sharePrice', "*")
    print companylist
    print 'index'
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

def insert(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addCompanyData(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            company = form.cleaned_data['company']
            date = form.cleaned_data['date']
            price = form.cleaned_data['companyprice']
            data = []
            table = 'invest_sharePrice'
            path = '/home/website/demo/mysite/db.sqlite3'
            db_insert(path, table, company, date, price)
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

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addCompanyData()

    return render(request, 'invest/index.html', {'form': form})


def delete(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = deleteCompanyData(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            company = form.cleaned_data['company']
            date = form.cleaned_data['date']
            data = []
            table = 'invest_sharePrice'
            path = '/home/website/demo/mysite/db.sqlite3'
            db_delete(path, table, company, date)
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

    # if a GET (or any other method) we'll create a blank form
    else:
        form = deleteCompanyData()

    return render(request, 'invest/index.html', {'form': form})

def deleteid(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = deleteCompanyidData(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            companyid = form.cleaned_data['companyid']
            data = []
            table = 'invest_sharePrice'
            path = '/home/website/demo/mysite/db.sqlite3'
            db_deleteid(path, table, companyid)
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

    # if a GET (or any other method) we'll create a blank form
    else:
        form = deleteCompanyidData()

    return render(request, 'invest/index.html', {'form': form})

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
        form = addCompanyData(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            return render(request, 'invest/index_temp.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addCompanyData()

    return render(request, 'index.html', {'form': form})


def compare(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = compareCompany(request.POST)
        print request.POST.getlist('selectCompany')
        unicodelist = request.POST.getlist('selectCompany')
        print unicodelist
        companylist = []
        for i in unicodelist:
            companylist.append(i.encode('ascii','ignore'))
        print companylist
        data = []
        year = 2017
        month = 2
        day = 8
        table = 'invest_sharePrice'
        path = '/home/website/demo/mysite/db.sqlite3'
        insertdate(year,month,day,data,companylist)
        insertcompany(path,data,table,companylist) #insertcompany(path,data,table,companylist)
        company_list = serializers.serialize("json", sharePrice.objects.all())
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            print 'chart html'
            context = {
                'data': data,
                'companylist': companylist,
                'company_list':company_list,
            }
            return render(request, 'invest/chart.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = compareCompany()

    print 'form is not valid'
    return render(request, 'index.html', {'form': form})

def save_uploaded_file(f, filename):
    destination = open(filename, 'wb')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
def multiFileUpload(fileContent):
    addr = str(uuid.uuid3(uuid.NAMESPACE_OID, str(fileContent.name)))
    path = os.path.join(static_path, addr)
    if not os.path.exists(path):
        os.mkdir(path)
    filename = os.path.join(path, fileContent.name)
    new_name = filename
    save_uploaded_file(fileContent, filename)

    return (True,new_name)

    
@csrf_exempt
def uploadify_script(request):
    print 'upload..........'
    ret="0"  
    new_name = ''
    #request.FILES['data']
    filename = request.FILES.get("Filedata",None)
    # if request.FILES and request.FILES['Filedata']:
    #   print request.FILES['Filedata'].name
    # print 'here'
    # filename = request.FILES['Filedata'].name
    print 'filename '+filename.name
    if filename:
        result,new_name=file_upload(filename)
        if result:
            ret="1"
        else:
            ret="2"
    import json            
    source={'ret':ret,'save_name':new_name}
    print source
    return HttpResponse(json.dumps(source))
  
  
def file_upload(filename):  
    '''''文件上传函数'''  
    if filename:
        print 'profile_upload'
        path=os.path.join(static_path,'upload')
        if not os.path.exists(path):
            os.mkdir(path,0755)
        print path
        #file_name=str(uuid.uuid1())+".jpg"  
        file_name=str(uuid.uuid1())+'-'+filename.name
        #fname = os.path.join(settings.MEDIA_ROOT,filename)
        path_file=os.path.join(path,file_name)
        print file_name
        print path_file
        fp = open(path_file, 'wb')
        for content in filename.chunks():
            fp.write(content)
        fp.close()
        return (True,file_name) #change
    return (False,file_name)   #change
  
#用户管理-添加用户-删除附件  
 
@csrf_exempt
def file_delete(request):  
    del_file=request.POST.get("delete_file",'')  
    if del_file:  
        path_file=os.path.join(settings.MEDIA_ROOT,'upload',del_file)  
        os.remove(path_file)