# -*- coding:utf-8 -*-
import os

from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    # send_mail(
    #     '来自www.liujiangblog.com的测试邮件',
    #     '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
    #     'xxxx@sina.cn',
    #     ['8xxxx@qq.com'],
    # )
    """
    对于send_mail方法，第一个参数是邮件主题subject；第二个参数是邮件具体内容；
    第三个参数是邮件发送方，需要和你settings中的一致；第四个参数是接受方的邮件地址列表。
    """

    # 发送html邮件
    subject, from_email, to = '来自www.liujiangblog.com的测试邮件', 'xxxxm@sina.cn', '8xxxxx@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

