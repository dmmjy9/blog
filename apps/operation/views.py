# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Comment
from index.models import Article
from .forms import CommentForm

# Create your views here.
class CommentView(View):
    def post(self, request, article_id):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_comment = request.POST.get('comment', '')
            post_email = request.POST.get('email', '')
            if post_comment:
                article_comment = Comment()
                article = Article.objects.get(id=int(article_id))
                article_comment.article = article
                article_comment.comment = post_comment
                article_comment.email = post_email
                article_comment.save()
            return HttpResponseRedirect(reverse('article:content', args=article_id))
        else:
            return HttpResponseRedirect(reverse('article:content', args=article_id))