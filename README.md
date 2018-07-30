## 项目介绍

一个使用django生成的简单的API管理工具，可以方便编写API文档，感谢原作者提供的代码，原作者项目所在[地址](https://github.com/tangguoying2018/api_manager)

和原作者相比增加了以下特性
1. 支持python3+
2. django2.0+
3. 可以在windows上开发并预览（使用了pymysql数据库驱动连接）
4. 修复了textarea无法随文字高度变化的bug
5. 简化参数处理，自定义中间件，自定义异常处理
6. 修改了部分模型


## 要求
1. python3 required
2. django 2.0+ required
3. mysql required
4. pymysql required
5. uwsgi required
6. supervisor required

## 使用方法
1. 创建虚拟环境
    ```
    python3 -m venv env
    ```

2. 安装依赖
    ```
    env/bin/pip install -r requirements.txt
    ```

3. 生成配置文件
   ```
   cd deploy.template
   sh genconf.sh
   ```

4. 修改配置文件

    本地调试修改dev_settings.py即可
    正式上线请修改prod_settings

5. 同步数据库
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. 收集静态文件
    ```
    python manage collectstatic
    ```
7. 创建用户
    ```
    python manage.py createsuperuser
    ```

8. 开始本地测试
    ```
    python manage runserver
    ```

## 部署方法
0. 将项目上传至服务器

1. 生成配置文件
   ```
   cd deploy.template
   sh genconf.sh
   ```
2. 配置uwsgi
    修改deploy下的uwsgi配置参数，注意要将server修改为prod，表示为正式环境
    相关示例文件可参考**deploy/uwsgi.ini**
    更多uwsgi配置项可以参考[官方文档](http://uwsgi-docs.readthedocs.io/en/latest/)

3. 配置nginx
    相关实例文件参考deploy目录下**nginx_api.conf**文件
    更多nginx配置项请参阅[官方文档](http://nginx.org/en/docs/)

4. 使用supervisor管理uwsgi进程
    具体可参考**deploy/api_manager.conf**
    如果你对supervisor还不是很了解，你可以先查阅下[官方文档](http://www.supervisord.org/)
    当然，你也可以不使用supervisor，直接在screen裸跑uwsgi也是可以的

5. 建立log目录，根据需要touch出相应的日志文件


## 应用截图

![首页](screenshots/1.jpg)

![登录](screenshots/2.jpg)

![新建项目](screenshots/3.jpg)

![新建分类](screenshots/4.jpg)

![新建接口](screenshots/5.jpg)

![接口预览](screenshots/6.jpg)


## FAQ
1. 如何重启？
    
    进入项目所在目录执行**reload.sh**脚本即可~注意，要想此重启方法有效，你必须按照上述部署规范部署项目


## 特别致谢

   再次感谢原作者提供的代码和授权，如果你觉得这个工具不错，不妨也给原作者一个star吧，这里是原作者的[github地址](https://github.com/tangguoying2018)


## LICENSE

   项目遵循LGPL-3.0开源协议，具体详情请参阅相关许可文件的详细信息


