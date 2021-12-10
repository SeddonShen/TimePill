from django.contrib import admin

# Register your models here.
from . import models
from .models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['sex', 'email', 'c_time', 'has_confirmed']})
    ]
    list_display = (['name', 'sex', 'email', 'c_time', 'has_confirmed'])  # add more columns.
    search_fields = ['name']  # add search function.


admin.site.register(User, UserAdmin)
# admin.site.register(models.User)
admin.site.register(models.ConfirmString)
