from django.contrib import admin

# Register your models here.
from . import models
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['title', 'content', 'status']})
    ]
    list_display = (
    ['expire_time', 'diary_type', 'square_open', 'add_date', 'mod_date', 'id', 'title', 'content', 'status',
     'author_id'])


# title = title,
# content = content,
# square_open = square_open,
# expire_time = expire_time,
# status = status,
# author_id_id = user_id,
# diary_type = diary_type,
# admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Article)
