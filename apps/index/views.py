# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Category

# Create your views here.

class IndexView(View):
    def get(self, request):
        categorys = Category.objects.all()
        all_articles = Article.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'categorys': categorys,
            'articles': articles
        })


class CategoryArticleView(View):
    def get(self, request, category_id):
        tmp_articles = []
        all_articles = Article.objects.all()
        categorys = Category.objects.all()
        for article in all_articles:
            if int(article.category.id) == int(category_id):
                tmp_articles.append(article)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(tmp_articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'categorys': categorys,
            'articles': articles
        })


class SearchView(View):
    def get(self, request):
        categorys = Category.objects.all()
        all_articles = Article.objects.all()
        search_keywords = request.GET.get("search_keywords", "")
        if search_keywords:
            all_articles = all_articles.filter(
                Q(title__icontains=search_keywords)
            )
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'categorys': categorys,
            'articles': articles
        })



class ArticleContentView(View):
    def get(self, request, article_id):
        content = Article.objects.get(id=article_id)
        try:
            article_last = Article.objects.get(id=int(article_id)-1)
        except:
            article_last = content
        try:
            article_next = Article.objects.get(id=int(article_id)+1)
        except:
            article_next = content
        comments = content.comment_set.all()
        content.read_nums += 1
        content.save()
        return render(request, 'article-content.html', {
            'article': content,
            'comments': comments,
            'last': article_last,
            'next': article_next
        })


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
