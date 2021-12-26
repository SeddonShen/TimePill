# TimePill
A Django Project to make a timepill.（时间胶囊）
打算数据库实验复刻一下这个项目，作业已经完成

```
python manage.py runserver
```

# 思路

用户表

文章表（主键是文章的id）

这个类似一个博客系统，但是唯一的区别就在于

到期的东西全部在广场显示 可以考虑markdown等编辑器富文本

不到期的就到时候就自己看（甚至自己都不能看）

目前了解的技术是用一个定时触发器，但是应该还有别的方法，这个具体再说

2021年11月25日 记录

## 解决的Bug

SAMESITE的Cookie问题：

[dajngo设置cookie的samesite属性_libo的博客-CSDN博客](https://blog.csdn.net/qq_31910669/article/details/116497899)

Vue使用中主要遇到的问题是跨域了，加油加油



## 定时任务依赖

run ./pron 路径

## 具体实现
见实验报告&说明文档
