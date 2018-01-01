# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from index.models import Article, Category, Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['read_nums', 'get_comment_count','add_time']
    list_filter = ['category__category', 'tag']
    search_fields = ['title', 'category__category', 'tag__tag_name']
    list_display = ['title', 'author', 'category', 'read_nums', 'get_comment_count', 'add_time']
    list_per_page = 20
    date_hierarchy = 'add_time'


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['get_article_count', 'add_time']
    list_display = ['category', 'get_article_count', 'add_time']
    list_per_page = 20


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['add_time', ]
    list_display = ['tag_name', 'add_time']
    search_fields = ['tag_name', ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)