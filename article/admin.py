from django.contrib import admin

# Register your models here.
from . import models
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['title', 'content', 'status']})
    ]
    list_display = (['id', 'title', 'content', 'status'])


admin.site.register(Article, ArticleAdmin)