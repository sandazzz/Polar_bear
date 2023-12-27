from django.contrib import admin
from .models import *

admin.site.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('content', 'date', 'user')
    list_filter = ('user', 'date')
    search_fields = ['user']
