# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment_nums',
        ),
    ]
