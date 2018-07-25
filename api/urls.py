"""
Brief Desc: App下的视图函数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-06-07 15:07:44. Created By jadger.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.urls import path
from api import views

# app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_proj/', views.new_proj, name='new_proj'),
    path('del_proj/', views.del_proj, name='del_proj'),
    path('category_list/', views.category_list, name='category_list'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
]