# -*-coding:utf-8 -*-

from django.conf.urls import url

from .views import CategoryArticleView, ArticleContentView, SearchView

urlpatterns = [
    url(r'category/(?P<category_id>\d+)/$', CategoryArticleView.as_view(), name='category'),
    url(r'(?P<article_id>\d+)/$', ArticleContentView.as_view(), name='content'),
    url(r'^search/$', SearchView.as_view(), name='search')
]