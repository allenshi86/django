from django.shortcuts import render
import pymysql
from app01.models import Assets
# Create your views here.


def index(request):

    return render(request, 'index.html')

'''
def show(request):
    db = pymysql.connect(host='127.0.0.1', user='root', password='momo2021', database='momo')
    cursor = db.cursor()
    cursor.execute("select * from software_tbl limit 10")
    data = cursor.fetchall()
#    print(data)
    db.close()
    dict1 = {'data': data}
    return render(request,'show.html',dict1)

'''
def show(request):
    assets = Assets.objects.all()
    dict1 = {'data': assets}
    return render(request, 'show.html', dict1)
