# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_article_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='index.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
