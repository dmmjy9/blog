# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 10:59
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20171126_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='read',
            new_name='read_nums',
        ),
        migrations.AddField(
            model_name='article',
            name='comment_nums',
            field=models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
    ]
