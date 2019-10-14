from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# 导入`connection`
from django.db import connection
from django.core import serializers
import json

# Create your views here.


def test(request):
    return HttpResponse('OK')


# 将数据转换成字典格式
def dict_fetch_all(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]


def get_recognize_table_list(request):
    cursor = connection.cursor()
    # 要想使用sql原生语句，必须用到execute()函数
    # 然后在里面写入sql原生语句
    cursor.execute("SELECT * FROM projectlist WHERE isRecognized=0 ORDER BY uploadTime DESC")
    # 获取所有的数据
    # rows = cursor.fetchall()
    # 将获取到的数据转换成字典格式
    rows = dict_fetch_all(cursor)
    # print(rows)
    return JsonResponse(rows, safe=False, json_dumps_params={'ensure_ascii': False})


def get_recognized_card_list(request):
    cursor = connection.cursor()
    # 要想使用sql原生语句，必须用到execute()函数
    # 然后在里面写入sql原生语句
    cursor.execute("SELECT * FROM projectlist WHERE isRecognized=1 ORDER BY uploadTime DESC")
    # 获取所有的数据
    # rows = cursor.fetchall()
    # 将获取到的数据转换成字典格式
    rows = dict_fetch_all(cursor)
    # print(rows)
    return JsonResponse(rows, safe=False, json_dumps_params={'ensure_ascii': False})
