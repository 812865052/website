from .models import sharePrice
import json
from django.core import serializers
from .forms import ChooseForm
from django.db import connections
import sqlite3

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

def db_insert(databaseName):
    conn = connect('localhost',3306,'yefei','123456',databaseName)
    cur=conn.cursor()
    sqli="insert into cron_time values(%s,%s-1,%s,%s)"
    cur.execute(sqli,(msg['r_type'],msg['weekday'],msg['hour'],msg['rid']))
    conn.commit()
    close(cur,conn)

def db_del(databaseName):
    conn = connect('localhost',3306,'yefei','123456',databaseName)
    cur=conn.cursor()
    cur.execute("delete from cron_time where r_type='%s' AND rid = %s" %(msg['r_type'],msg['rid']))
    conn.commit()
    close(cur,conn)

def db_update(databaseName):
    conn = connect('localhost',3306,'yefei','123456',databaseName)
    cur=conn.cursor()
    cur.execute("update cron_time set week_day=%s-1,hour=%s where r_type='%s' AND rid=%s" %(msg['weekday'],msg['hour'],msg['r_type'],msg['rid']))
    conn.commit()
    close(cur,conn)

def db_query(path, table, kind):
    conn = connect(path)
    cur=conn.cursor()
    t = (kind,table)
    number = cur.execute("select %s from %s order by id desc", t)
    print number
    i = 0
    list = []
    while i < number:
        row = cur.fetchone()
        #print row[1]
        list.append(row[1])
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


if __name__ == '__main__':
    db_query('/home/website/demo/mysite/db.sqlite3', 'invest_sharePrice', "*")