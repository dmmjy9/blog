#-*-coding:utf-8-*-
from django import forms
from captcha.fields import CaptchaField

from .models import Comment


class CommentForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})