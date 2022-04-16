# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as djangoLogin
from image_search.models.userinfo.dao import UserInfo


def login(request):
    if request.user.is_authenticated:
        return redirect("http://43.154.99.88:8000/")
    else:
        return render(request, 'image_search/login/login.html')


def login_check(request):
    username = request.GET.get('username').strip()
    password = request.GET.get('password').strip()
    user = authenticate(username=username, password=password)  # 从数据库中查找这个用户
    if not user:  # 如果没有就直接返回不成功
        return JsonResponse({
            'result': "用户名或密码不正确"
        })
    djangoLogin(request, user)  # 找到了就登录
    return JsonResponse({
        'result': "succ"
    })


def register(request):
    return render(request, 'image_search/login/register.html')


def register_check(request):
    data = request.GET
    username = data.get("username", "").strip()
    nikename = data.get("nikename", "").strip()
    password = data.get("password", "").strip()
    repeat_password = data.get("repeat_password", "").strip()
    if not username or not password:
        return JsonResponse({
            'result': "用户名和密码不能为空"
        })
    if password != repeat_password:
        return JsonResponse({
            'result': "两个密码不一致",
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "帐号名已存在"
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    UserInfo.objects.create(user=user, nikename=nikename)
    djangoLogin(request, user)
    return JsonResponse({
        'result': "succ",
    })
