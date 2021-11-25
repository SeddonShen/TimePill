#! /usr/bin/env python
# _*_ coding:utf-8 _*_


import os
from django.core.mail import send_mail,EmailMultiAlternatives


# 由于我们当前是单独运行send_mail.py文件，
# 无法自动链接Django环境，需要通过os模块对环境变量进行设置：
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__=='__main__':
    # send_mail(
    #     '来自www.naughoy.com的测试邮件',
    #     '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点',
    #     '1083559808@qq.com',
    #     ['18768755688@163.com'],
    #     fail_silently=False,
    # )
    subject= '来自naughoy'
    from_email='1083559808@qq.com'
    to='18768755688@163.com'
    text_content = '欢迎访问www.naughoy.com'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

