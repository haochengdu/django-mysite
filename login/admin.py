# -*- coding:utf-8 -*-
from django.contrib import admin
from . models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'email', 'sex', 'c_time']
    list_filter = ['name', 'sex', 'c_time']


admin.site.register(User, UserAdmin)


