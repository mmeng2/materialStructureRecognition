import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
# 导入`connection`
from django.db import connection
import MySQLdb
import time
import uuid
import json

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import os
import shutil
import math
from scipy.optimize import leastsq
from scipy.interpolate import spline
from PIL import Image

# Create your views here.
DATA_DIR = 'projectData'
UPLOAD_Dir = 'testFiles'

# # Fe的E0能量
# Fe的吸收边(E0)范围
E0 = 7112
E0_first = E0 - 50
E0_last = E0 + 50

# 边前拟合延伸范围
pre_edge_range_last = -50
# 边后拟合延伸范围
post_edge_range_first = 100


# (0,1)归一化
def MaxMinNormalization(x,Max,Min):
    _x = (x - Min) / (Max - Min)
    return _x


def get_nor_data(filepath):
    # 读取文件中的数据
    arr = []
    with open(filepath, 'r') as file:
        while True:
            content_list = file.readline()
            if not content_list:
                break
                pass
            E_tmp = [x for x in content_list.split()]
            arr.append(E_tmp)
            pass
    # 查询抬头之后的数据
    tempI = 0
    for i in range(0, len(arr) - 1):
        # print(i)
        if (len(arr[i]) == len(arr[i + 1]) and len(arr[i]) > 4 and '#' not in arr[i][0]
                and '\\' not in arr[i][0] and '-' not in arr[i][0] and ':' not in arr[i][0]
                and '(' not in arr[i][0] and ')' not in arr[i][0]):
            # lie = arr[i]
            # 第i个数据为抬头后的第一列数据
            tempI = i
            break
    # 除去抬头后，取文件中的数据arrTemp
    arrTemp = []
    for i in range(tempI, len(arr) - 1):
        arrTemp.append(arr[i])
    # list转换成numpy
    arrTemp = np.array(arrTemp)
    # 读取文件中的首列(能量),并将string数据转换成float
    lie = [float(i) for i in arrTemp[:, 0]]
    # # 读取文件中的最后一列（吸收系数）,并将string数据转换成float
    last_lie = [float(i) for i in arrTemp[:, arrTemp.shape[1] - 1]]
    # 解决数据中有nan或inf，使用0代替数组中的nan元素，使用有限的数字代替inf元素
    last_lie = np.nan_to_num(last_lie)

    # 预处理

    # 获取吸收边E0,需求曲线的一阶导数(先拟合，在求导)
    # 曲线一阶导数,gradient得到的是和x同维数向量
    # diff(y) / diff(x)
    # 一阶导数dp
    # np.gradient(lie)除数不能为0，需判断，梯度为0时，导数是0
    for i in range(0, len(lie) - 1):
        if (np.gradient(lie[i]) == 0):
            dp[i] = 0
        else:
            dp = np.gradient(last_lie) / np.gradient(lie)
    dp_temp = dp.tolist()
    dp_index = dp_temp.index(max(dp))

    # E0是一阶导数曲线的最大值
    E0 = lie[dp_index]

    # 边前延申曲线
    # 数据拟合
    # 截取固定范围的数组(第一列:能量)
    lie_crop_pre = []
    for i in lie:
        if (lie[3] <= i <= (E0 + pre_edge_range_last)):
            # if ((E0 + pre_edge_range_first) <= i <= (E0 + pre_edge_range_last)):
            lie_crop_pre.append(i)
    # 获取截取数组的长度

    lie_crop_shape_pre = np.array(lie_crop_pre)
    # 获得范围内第一个下标
    crop_index_first_pre = lie.index(lie_crop_pre[0])
    # 获得范围内最后一个下标
    crop_index_last_pre = lie.index(lie_crop_pre[lie_crop_shape_pre.shape[0] - 1])

    # 截取固定范围的数组(最后一列:u(E))
    last_lie_crop_pre = []
    for j in range(crop_index_first_pre, crop_index_last_pre + 1):
        # if (crop_index_first_pre <= last_lie.index(j) <= crop_index_last_pre):
        last_lie_crop_pre.append(last_lie[j])

    # pre-edge-line函数:pre_edge;一次多项式拟合
    pre_edge = np.polyfit(lie_crop_pre, last_lie_crop_pre, 1)
    pre_edge_y = np.polyval(pre_edge, lie)

    # 边后延申曲线
    # 数据拟合
    # 截取固定范围的数组(第一列:能量)
    lie_crop = []
    for i in lie:
        if ((E0 + post_edge_range_first) <= i):
            # if ((E0 + post_edge_range_first) <= i <= (E0 + post_edge_range_last)):
            lie_crop.append(i)
    # 获取截取数组的长度
    lie_crop_shape = np.array(lie_crop)
    # 获得范围内第一个下标
    crop_index_first = lie.index(lie_crop[0])
    # 获得范围内最后一个下标
    crop_index_last = lie.index(lie_crop[lie_crop_shape.shape[0] - 1])

    # 截取固定范围的数组(最后一列:u(E))
    last_lie_crop = []
    for j in range(crop_index_first, crop_index_last + 1):
        # if(crop_index_first <= last_lie.index(j) <= crop_index_last):
        last_lie_crop.append(last_lie[j])

    # post-edge-line函数:post_edge;二次多项式拟合
    post_edge = np.polyfit(lie_crop, last_lie_crop, 2)
    post_edge_y = np.polyval(post_edge, lie)

    # 归一化
    # last_lie为曲线y坐标，post_edge_y为边后曲线y2，pre_edge_y为边前曲线y1;做(0,1)归一化处理
    normal_y = MaxMinNormalization(last_lie, post_edge_y, pre_edge_y)
    # normal_y = normal_y[:,np.newaxis]
    data = np.concatenate((np.array(lie)[:,np.newaxis], np.array(last_lie)[:,np.newaxis]), axis=1).tolist()
    nor_data = np.concatenate((np.array(lie)[:,np.newaxis], normal_y[:,np.newaxis]), axis=1).tolist()
    # nor_data = zip(lie, normal_y.tolist())

    # # 绘出
    # plt.plot(lie, normal_y)
    # plt.show()
    return data, nor_data


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
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "123456", "msrplatform", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    if request.method == 'POST':
        id = uuid.uuid1()
        file = request.FILES.get('file', None)
        project_name = request.POST.get('projectName')
        comment = request.POST.get('comment')
        new_name = str(id) + file.name
        if file:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # SQL 插入语句
            sql = "INSERT INTO projectlist(id, projectName, uploadTime, textFileName, comment) VALUES ('%s', '%s', '%s', '%s', '%s')" % (id, project_name, now_time, new_name, comment)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
        f = open(DATA_DIR + "/" + new_name, 'wb')
        # todo
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK')
        # 关闭数据库连接
    db.close()


# 下载测试文件
def post_download_file(request):
    id = request.POST.get('id')
    print(id)
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "123456", "msrplatform", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = 'SELECT textFileName FROM projectlist WHERE id = "%s"' % (id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()
    file_pathname = DATA_DIR + '/' + fname
    file = open(file_pathname, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="data.zip"'
    return response

# 删除测试文件
def delete_file(request):
    id = request.POST.get("id")
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "123456", "msrplatform", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = 'SELECT textFileName FROM projectlist WHERE id = "%s"' % (id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
    except:
        print("Error: unable to fecth data")
    # SQL 删除语句
    sql = "DELETE FROM projectlist WHERE id = '%s'" % (id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()
    file_pathname = DATA_DIR + '/' + fname
    os.remove(file_pathname)
    return HttpResponse('OK')


def get_XAFS_data(request):
    filepath = 'data/2017-04-26 21-40 Fe-2-c3.4'
    data, nor_data = get_nor_data(filepath)
    result = np.append([data], [nor_data], axis=0)
    keys = ['data', 'nor_data']
    print(dict(zip(keys, result.tolist())))

    rows = dict(zip(keys, result.tolist()))
    return JsonResponse(rows, safe=False, json_dumps_params={'ensure_ascii': False})
