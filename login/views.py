# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from . models import User
from .forms import UserForm, RegisterForm


def index(request):

    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    print('登录成功')
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = username
                    return redirect('/index/')
                else:
                    print('密码错误')
                    message = '用户名或密码错误'
            except:
                print('该用户名不存在')
                message = '用户名或密码错误'
        else:
            print('null error')
            message = '不守法'
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session['is_login', None]:
        print('已经登录不能注册')
        return redirect('/index/')
    register_form = RegisterForm(request.POST)

    return render(request, 'login/register.html')


def logout(request):
    if request.session.get('is_login', None):
        # 如果登录了，则清除session
        print('清除session')
        request.session.flush()
    else:
        print('未登录')
    return render(request, 'login/index.html')














