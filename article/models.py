from django.db import models

from login.models import User
# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # deleted alive
    status = models.CharField(max_length=10)
    author_id = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
