from django.db import models
import django.utils.timezone as timezone
from login.models import User


# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='日记标题')
    content = models.TextField(verbose_name='日记内容')
    # deleted alive
    status = models.BooleanField(default=False, verbose_name='是否到期')
    square_open = models.BooleanField(default=False, verbose_name='是否公开')
    expire_time = models.DateTimeField(editable=True, null=True, verbose_name='解封日期')
    diary = (
        ('pill', '胶囊日记'),
        ('primary', '普通日记'),
    )
    diary_type = models.CharField(max_length=8, choices=diary, default='胶囊日记', verbose_name='日记类型')
    author_id = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING, verbose_name='作者ID')
    add_date = models.DateTimeField('保存日期', default=timezone.now, editable=False)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)
