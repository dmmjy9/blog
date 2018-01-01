# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50, verbose_name=u"文章分类", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.category

    def get_article_count(self):
        return self.article_set.count()
    get_article_count.short_description = u"文章数"


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name=u"标签名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name=u"文章分类")
    title = models.CharField(max_length=100, verbose_name=u"文章题目", default="")
    author = models.CharField(max_length=20, verbose_name=u"作者", default="")
    content = UEditorField(width=1000, height=500,imagePath="", filePath="",verbose_name=u"文章内容")
    abstract = models.CharField(max_length=600, verbose_name=u"摘要", default="")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=u"标签")
    read_nums = models.IntegerField(default=0, verbose_name=u"阅读量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def get_comment_count(self):
        return self.comment_set.count()
    get_comment_count.short_description = u"评论数"
