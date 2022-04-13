# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}  # 【1】定义1个字典
    context['hello'] = 'hello world!!!'  # 【2】向字典写一个键：值（hello:'hello world!!'）
    context['wa'] = 'wawawawawahahahaha!'
    context['list'] = list(range(1, 10))
    # 【3】返回：把context渲染到app1/index.html的模板文件
    return render(request, 'image_search/index.html', context)
