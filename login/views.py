# -*- coding:utf-8 -*-
import datetime

from django.shortcuts import render, redirect

from mysite import settings
from .utils import hash_code, make_confirm_string, send_mail
from .forms import UserForm, RegisterForm
from .models import User, ConfirmString


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
                if user.password == hash_code(password):
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
    if request.session.get('is_login', None):
        print('已经登录不能注册')
        return redirect('/index/')
    if request.method == 'POST':
        message = '请检查填写的信息'
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print('对注册信息进行校验')
            user_name = register_form.cleaned_data['username']
            password_1 = register_form.cleaned_data['password1']
            password_2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password_1 != password_2:
                message = '两次输入的密码不一致'
                return render(request, 'login/register.html', locals())
            else:
                same_user_name = User.objects.filter(name=user_name)
                if same_user_name:
                    message = '该用户名已经被注册，请使用其他用户名'
                    return render(request, 'login/register.html', locals())
                same_email = User.objects.filter(email=email)
                if same_email:
                    message = '该邮箱已经被使用,请使用其他邮箱'
                    return render(request, 'login/register.html', locals())
                # print('注册成功，跳转到首页')
                user = User()
                user.name = user_name
                user.password = hash_code(password_1)
                user.email = email
                user.sex = sex
                user.save()
                # request.session['is_login'] = True
                # request.session['user_id'] = user.id
                # request.session['user_name'] = user_name
                code = make_confirm_string(user)
                send_mail(email, code)
                message = '请前往注册邮箱，进行邮件确认！'
                return render(request, 'login/register.html', locals())
        else:
            print('填写注册信息不完整')
            return render(request, 'login/register.html', locals())
    else:
        register_form = RegisterForm()
        return render(request, 'login/register.html', locals())


def logout(request):
    if request.session.get('is_login', None):
        # 如果登录了，则清除session
        print('清除session')
        request.session.flush()
    else:
        print('未登录')
    return render(request, 'login/index.html')


def user_confirm(request):
    """注册确认"""
    code = request.GET.get('code')
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now_time = datetime.datetime.now()
    if now_time > (c_time + datetime.timedelta(settings.CONFIRM_DAYS)):
        confirm.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())







