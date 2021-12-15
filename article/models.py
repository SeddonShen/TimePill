from django.db import models

from login.models import User
import django.utils.timezone as timezone
# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='日记标题')
    content = models.TextField(verbose_name='日记内容')
    # # deleted alive
    square_open = models.BooleanField(default=False, verbose_name='是否公开')
    expire_time = models.DateTimeField(editable=True, null=True, verbose_name='解封日期')
    status = models.BooleanField(default=False, verbose_name='是否到期')  # 到期与否 用户不填
    diary = (
        ('pill', '胶囊日记'),
        ('primary', '普通日记'),
    )
    diary_type = models.CharField(max_length=8, choices=diary, default='胶囊日记', verbose_name='日记类型')
    author_id = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING, verbose_name='作者ID')
    add_date = models.DateTimeField('保存日期', default=timezone.now, editable=False)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)


class Comment(models.Model):  # 定义评论模型
    article = models.ForeignKey(to=Article, to_field='id', on_delete=models.DO_NOTHING, verbose_name='评论文章')
    comment_content = models.TextField(verbose_name='评论内容')
    comment_author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, verbose_name='评论者')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    pre_comment = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True,
                                    verbose_name='父评论id')  # 父级评论，如果没有父级则为空NULL, "self"表示外键关联自己
    #
    # class Meta:
    #     db_table = 'comment_tb'
    #     verbose_name = '评论'
    #     verbose_name_plural = verbose_name
