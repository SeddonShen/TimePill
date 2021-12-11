from django.db import models


# Create your models here.


class User(models.Model):
    gender = (
        ('male', '男'),
        ('femal', '女'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    # choice选项绑定
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    # 标识邮箱验证与否，默认为否
    has_confirmed = models.BooleanField(default=False)

    # 帮助人性化显示对象信息
    def __str__(self):
        return self.name

    # 元数据
    # 定义用户按创建时间的反序排列，也就是最近的最先显示
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


# 邮件确认信息表
# 用户和注册码之间的关系，一对一的形式
class ConfirmString(models.Model):
    # 哈希后的注册码
    code = models.CharField(max_length=256)
    # 关联的一对一用户
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    # 注册的提交时间
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
