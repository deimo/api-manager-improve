"""
Brief Desc: 系统运行配置文件，请勿在此修改配置信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-06-07 15:07:44. Created By jadger.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import os
import traceback
from configparser import ConfigParser

cf = ConfigParser()
path = os.getcwd()
real_path = path + '/deploy/uwsgi.ini'
DEBUG = True
try:
    cf.read(real_path)
    svrtype = cf.get("server", "type")
    if svrtype != 'dev':
        DEBUG = False
except Exception as e:
    print(traceback.format_exc())
    pass
if DEBUG:
    from api_manager.dev_settings import *
else:
    from api_manager.prod_settings import *
