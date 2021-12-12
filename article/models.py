from django.db import models

from login.models import User
# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    diary = (
        ('pill', '胶囊日记'),
        ('primary', '普通日记'),
    )
    diary_type = models.CharField(max_length=8, choices=diary, default='胶囊日记')
    title = models.CharField(max_length=50)
    content = models.TextField()
    # deleted alive
    square_open = models.BooleanField(default=False)
    expire_time = models.DateTimeField()
    status = models.CharField(max_length=10)  # 到期与否 用户不填
    author_id = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
