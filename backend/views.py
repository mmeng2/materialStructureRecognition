import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# 导入`connection`
from django.db import connection
import time
import uuid
import json

# Create your views here.

UPLOAD_Dir = 'testFiles'


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


# 添加数据，上传测试文件
def post_upload_file(request):
    if request.method == 'POST':
        # 获得前台传来的值，转换为json形式
        # data = request.body
        # post_body_str = data.decode('utf-8')
        # json_result = json.loads(post_body_str)
        # print(json_result)
        id = uuid.uuid1()
        file = request.FILES.get('file', None)
        project_name = request.POST.get('projectName')
        comment = request.POST.get('comment')
        new_name = str(id) + project_name
        if file:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # 插入sql语句
            # cursor = connection.cursor()
            # sql = 'insert into '
            # cursor.execute(sql)
            print(now_time)
        print(id)
        print(file)
        print(project_name)
        print(new_name)
        print(comment)

    # if request.method == "POST":
    #     f = request.FILES.get('personico')
    #     baseDir = os.path.dirname(os.path.abspath(__name__))
    #     jpgdir = os.path.join(baseDir, 'static', 'jpg')
    #
    #     filename = os.path.join(jpgdir, f.name)
    #     fobj = open(filename, 'wb')
    #     for chrunk in f.chunks():
    #         fobj.write(chrunk)
    #     fobj.close()
    #     return HttpResponse('OK')
    # else:
    #     return HttpResponse('ERROR')
    # if request.method == 'POST':
    #     file = request.data
    #     # myfile = request.FILES['file']
    #     # fs = FileSystemStorage()
    #     # filename = fs.save(myfile.name, myfile)
    #
    #     print(file)
    return HttpResponse('OK')
