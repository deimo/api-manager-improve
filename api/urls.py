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
    path('new_cate/', views.new_cate, name='new_cate'),
    path('edit_cate/', views.edit_cate, name='edit_cate'),
    path('del_cate/', views.del_cate, name='del_cate'),
    path('api/list/', views.api_list, name='api_list'),
    path('new_api/', views.new_api, name='new_api'),
    path('del_api/', views.del_api, name='del_api'),
    path('copy_api/', views.copy_api, name='copy_api'),
    path('edit_api/', views.edit_api, name='edit_api'),
]
