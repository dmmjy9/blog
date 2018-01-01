# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from index.models import Article


# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name=u"评论文章")
    comment = models.TextField(verbose_name=u"评论内容")
    email= models.EmailField(default="", verbose_name=u"评论者邮箱")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"文章评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.comment