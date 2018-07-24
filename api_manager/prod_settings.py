"""
Brief Desc: 线上开发配置文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-06-07 15:07:44. Created By jadger.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

from api_manager.base_settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': ['SET default_storage_engine=INNODB', "SET sql_mode='STRICT_TRANS_TABLES'", ],
            'charset': 'utf8mb4'
        },
        'NAME': 'api_manager',
        'USER': '',
        'PASSWORD': ''
    }
}
