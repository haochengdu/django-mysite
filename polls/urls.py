# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'polls'  # 关键是这行
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^order/$', views.order, name='order'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


]









