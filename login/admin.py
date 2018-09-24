# -*- coding:utf-8 -*-
from django.contrib import admin
from . models import User, ConfirmString

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'email', 'sex', 'c_time', 'has_confirmed']
    list_filter = ['name', 'sex', 'c_time', 'has_confirmed']


class ConfirmStringAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'c_time']
    list_filter = ['user', 'c_time']


admin.site.register(User, UserAdmin)
admin.site.register(ConfirmString, ConfirmStringAdmin)


