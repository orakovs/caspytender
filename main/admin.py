from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pub_date']

admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory)