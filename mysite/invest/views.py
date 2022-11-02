# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3

from django.shortcuts import render
import os
import uuid
from . import excel2json
from django.conf import settings
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
from .db import db_query, insertdate, insertcompany, db_insert, db_delete, db_deleteid,returndbdate,insertdbdate,date_db_insert
from .forms import addCompanyData, compareCompany, deleteCompanyData, deleteCompanyidData, deleteCompanyidbatchData
from django.views.decorators.csrf import csrf_exempt, csrf_protect

static_path = '/Users/yefei/Documents/shopee/Python/website/mysite/polls/static'
sqlite3_path =  '/Users/yefei/Documents/shopee/Python/website/mysite/db.sqlite3'

def index(request):
    company_list = sharePrice.objects.all()
    print(f"all company_list:{company_list}")
    # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
    data = serializers.serialize("json", company_list)
    print(f"all json company_list:{data}")
    companylist = db_query(sqlite3_path, 'invest_sharePrice', "*")
    print(f"companylist:{companylist}")
    print('index 方法')
    context = {
        #'company_list': json.dumps(company_list),
        'company_list': data,
        'companylist': companylist,
    }
    return render(request, 'invest/index.html', context)

def dataoperation(request):
    print("dataoperation 方法")
    company_list = sharePrice.objects.all()
    # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
    data = serializers.serialize("json", company_list)
    companylist = db_query(sqlite3_path, 'invest_sharePrice', "*")
    context = {
        #'company_list': json.dumps(company_list),
        'company_list': data,
        'companylist': companylist,
    }
    return render(request, 'invest/data.html', context)

def insert(request):
    print("insert 方法")
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
            dbdatetable = 'invest_datedb'
            path = sqlite3_path
            db_insert(path, table, company, date, price)
            date_db_insert(path, dbdatetable, date)
            company_list = sharePrice.objects.all()
            # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
            data = serializers.serialize("json", company_list)
            companylist = db_query(sqlite3_path, 'invest_sharePrice', "*")
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
    print("delete 方法")
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
            path = sqlite3_path
            db_delete(path, table, company, date)
            company_list = sharePrice.objects.all()
            # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
            data = serializers.serialize("json", company_list)
            companylist = db_query(sqlite3_path, 'invest_sharePrice', "*")
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
    print("deleteid 方法")
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
            path = sqlite3_path
            db_deleteid(path, table, companyid)
            company_list = sharePrice.objects.all()
            # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
            data = serializers.serialize("json", company_list)
            companylist = db_query(sqlite3_path, 'invest_sharePrice', "*")
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

def deleteidbatch(request):
    print("deleteidbatch 方法")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = deleteCompanyidbatchData(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            companyid = form.cleaned_data['companyidbatch']
            data = []
            table = 'invest_sharePrice'
            path = sqlite3_path
            i = 0
            while(i<companyid):
                db_deleteid(path, table, i)
                i = i + 1
            
            company_list = sharePrice.objects.all()
            # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
            data = serializers.serialize("json", company_list)
            companylist = db_query(sqlite3_path, 'invest_sharePrice', "*")
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
    print("adddb 方法")
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
    print("compare 方法")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = compareCompany(request.POST)
        print(f"选择的公司：{request.POST.getlist('selectCompany')}")
        print(f"提交的数据：{request.POST}")
        selectCompany = request.POST.getlist('selectCompany')
        
        data = []
        year = 2017
        month = 2
        day = 8
        table = 'invest_sharePrice'
        dbdatetable = 'invest_datedb'
        path = sqlite3_path
        # insertdate(year,month,day,data,companylist)
        insertdbdate(data,returndbdate(path,dbdatetable),selectCompany)
        insertcompany(path,data,table,selectCompany) #insertcompany(path,data,table,companylist)
        company_list = serializers.serialize("json", sharePrice.objects.all())
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            print('chart html')
            context = {
                'data': data,
                'companylist': selectCompany,
                'company_list':company_list,
            }
            return render(request, 'invest/chart.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = compareCompany()

    print('form is not valid')
    return render(request, 'index.html', {'form': form})

def save_uploaded_file(f, filename):
    print("save_uploaded_file 方法")
    destination = open(filename, 'wb')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
def multiFileUpload(fileContent):
    print("multiFileUpload 方法")
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
    print("uploadify_script 方法")
    print('upload..........')
    ret="0"  
    new_name = ''
    #request.FILES['data']
    filename = request.FILES.get("Filedata",None)
    # if request.FILES and request.FILES['Filedata']:
    #   print request.FILES['Filedata'].name
    # print 'here'
    # filename = request.FILES['Filedata'].name
    print('filename '+filename.name)
    if filename:
        result,new_name=file_upload(filename)
        if result:
            ret="1"
        else:
            ret="2"
    import json            
    source={'ret':ret,'save_name':new_name}
    print(source)
    return HttpResponse(json.dumps(source))
  
  
def file_upload(filename):
    print("file_upload 方法")
    '''''文件上传函数'''  
    if filename:
        print('file_upload')
        path=os.path.join(static_path,'upload')
        if not os.path.exists(path):
            os.mkdir(path,755)
        print(path)
        #file_name=str(uuid.uuid1())+".jpg"  
        file_name=str(uuid.uuid1())+'-'+filename.name
        #fname = os.path.join(settings.MEDIA_ROOT,filename)
        path_file=os.path.join(path,file_name)
        print(file_name)
        print(path_file)
        fp = open(path_file, 'wb')
        for content in filename.chunks():
            fp.write(content)
        fp.close()
        excel2json.Excel2array(path_file.encode('ascii','ignore'),0)
        return (True,file_name) #change
    return (False,file_name)   #change
  
#用户管理-添加用户-删除附件  
@csrf_exempt
def file_delete(request): 
    print("file_delete 方法") 
    del_file=request.POST.get("delete_file",'')
    print('in delete file')
    if del_file:  
        path_file=os.path.join(settings.MEDIA_ROOT,'upload',del_file)
        if not os.path.exists(path_file):
            print('file exists')
            os.remove(path_file)
        else:
            print('file not exists')
    else:
        print('delete file not exists')
