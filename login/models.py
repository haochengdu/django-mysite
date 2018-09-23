# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=28, unique=True)  # 用户名
    password = models.CharField(max_length=256)  # 密码
    email = models.EmailField(unique=True)  # 邮箱地址
    sex = models.CharField(max_length=32, choices=gender, default='男')  # 性别
    c_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户列表'







