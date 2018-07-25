"""
Brief Desc: 开发模式下的配置文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-06-07 15:07:44. Created By jadger.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from api_manager.base_settings import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB;',
            'charset': 'utf8mb4'
        },
        'NAME': 'api_manager2',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}
