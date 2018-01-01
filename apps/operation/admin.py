# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['add_time', ]
    list_display = ['comment', 'article', 'add_time']
    list_filter = ['article__title', 'article__category__category']
    search_fields = ['comment', 'article__title']
    list_per_page = 30
    date_hierarchy = 'add_time'


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['add_time', ]
    list_display = ['tag_name', 'add_time']


admin.site.register(Comment, CommentAdmin)