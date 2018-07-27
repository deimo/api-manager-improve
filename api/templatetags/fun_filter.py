#!/usr/bin/env python
# coding: utf-8
# author: tang

import hashlib
import time
import ujson as json

from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.filter(name='gen_md5')
def gen_md5(api_id):
    return hashlib.md5(str(api_id).encode('utf8')).hexdigest()


@register.filter(name='get_username')
def get_username(uid):
    ret = User.objects.get(id=uid)
    return ret.username


@register.filter(name='get_time')
def get_time(timestamp):
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    return dt


@register.filter(name='convert')
def convert(content):
    return eval(content)
