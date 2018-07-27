# -*- coding:utf-8 -*-
"""
Brief Desc: 项目自定义中间件集合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-03-05 14:53:13. Created By deimo.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.http import HttpResponseBadRequest, HttpResponseServerError

from lib._django import Http400, Http500


class ErrorHandlingMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http400):
            return HttpResponseBadRequest(exception)
        if isinstance(exception, Http500):
            return HttpResponseServerError(exception)
