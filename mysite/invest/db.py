from .models import sharePrice
import json
from django.core import serializers
from .forms import addCompanyData
from django.db import connections
import sqlite3
import datetime
from datetime import date

# cx = sqlite3.connect("/Users/cengchengpeng/Downloads/django_test/cmdb/db.sqlite3")
# cursor = cx.cursor()
# cursor.execute("""
# ... select
# ... (select count(1) from ucloud_uhost) as uhost,
# ... (select count(1) from ucloud_project) as project,
# ... (select count(1) from ucloud_zone) as zone
# ... """)
# cursor.description
# columns = [_[0].lower() for _ in cursor.description]

def connect(path):
    conn=sqlite3.connect(path)
    return conn

def close(cur,conn):
    cur.close()
    conn.close()

def db_insert(path, table, company, date, price):
    conn = connect(path)
    cur=conn.cursor()
    number = cur.execute("select * from %s where company=? and date=?" % (table), (company,date,))
    temp = number.fetchone()
    print company,date,price
    print type(company),type(date),type(price)
    if(temp==None):
        cur.execute("insert into %s (company,date,price) values(?,?,?)" % (table), (company,date,price,))
        conn.commit()
        close(cur,conn)
        return 'insert ok'
    elif(temp[2]==price):
        close(cur,conn)
        return 'exist already'
    elif(temp[2]!=price):
        close(cur,conn)
        db_update(path, table, company, date, price)

def db_del(databaseName):
    conn = connect('localhost',3306,'yefei','123456',databaseName)
    cur=conn.cursor()
    cur.execute("delete from cron_time where r_type='%s' AND rid = %s" %(msg['r_type'],msg['rid']))
    conn.commit()
    close(cur,conn)

def db_update(path, table, company, date, price):
    conn = connect(path)
    cur=conn.cursor()
    number = cur.execute("select * from %s where company=? and date=?" % (table), (company,date,))
    temp = number.fetchone()
    if(temp==None):
        close(cur,conn)
        return 'no this company and date dbdata'
    elif(temp[2]==price):
        close(cur,conn)
        return 'exist already'
    elif(temp[2]!=price):
        cur.execute("update %s set price=? where company=? and date=?" % (table), (price,company,date,))
        conn.commit()
        close(cur,conn)

def db_query(path, table, kind):
    conn = connect(path)
    cur=conn.cursor()
    t = (kind,table)
    number = cur.execute("select %s from %s order by id desc" %t)
    temp = number.fetchall()
    i = 0
    list = []
    while i < len(temp):
        # row = cur.fetchone()
        #print row[1]
        list.append(temp[i][1])
        i = i + 1
    close(cur,conn)
    print list
    return list

def db_queryprice(path, table, company, date):
    conn = connect(path)
    cur=conn.cursor()
    t = (table,company, date)
    number = cur.execute("select * from %s where company=? and date=?" % (table), (company,date,))
    temp = number.fetchone()
    if(temp==None):
        close(cur,conn)
        print 'no this company and date dbdata'
        return 0
    close(cur,conn)
    return temp[2]


def compareData(path, table, company):
    conn = connect(path)
    cur=conn.cursor()
    t = (kind,table)
    number = cur.execute("select %s from %s order by id desc" %t)
    temp = number.fetchall()
    i = 0
    list = []
    while i < len(temp):
        # row = cur.fetchone()
        #print row[1]
        list.append(temp[i][1])
        i = i + 1
    close(cur,conn)
    print list
    return list

 
def openDb(sql, connection_name='default'):
    dbs = connections[connection_name]
    cursor = dbs.cursor()
    cursor.execute(sql)
    columns = [_[0].lower() for _ in cursor.description]
    results = [dict(zip(columns, _)) for _ in cursor]
    cursor.close()
    return results

def filterCompany(request):
    company_list = sharePrice.objects.all()
    # time.strftime('%Y-%m-%d', time.strptime("30 Nov 17", "%d %b %y"))
    data = serializers.serialize("json", company_list)
    companlist = []
    for i in data:
        if(i.fields.company in companylist == false):
            datalist.push(i.fields.company)
    context = {
        #'company_list': json.dumps(company_list),
        'company_list': data,
    }
    return render(request, 'invest/index.html', context)


def insertdate(year,month,day,data,companylist):
    while (datetime.date.today() > date(year, month, day)):
        dict = {}
        month = month + 1
        if month > 12:
            year = year + 1
            month = 1
        if (datetime.date.today() > date(year, month, day)):
            dict['date'] = date(year, month, day)
            i = 0
            while(i<len(companylist)):
                dict[companylist[i]] = 0
                i = i + 1
            data.append(dict)

    return data

def insertcompany(path,data,table,companylist):
    for i in data:
        for company in companylist:
            # db_queryprice(path, table, company, date)
            i[company] = db_queryprice(path, table, company, i['date'])
    print data
    return data



if __name__ == '__main__':
    db_query('/home/website/demo/mysite/db.sqlite3', 'invest_sharePrice', "*")