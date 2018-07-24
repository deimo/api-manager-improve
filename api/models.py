import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def _generate_now():
    return datetime.datetime.now()


class Projects(models.Model):
    """
    所在项目信息
    """
    id = models.AutoField(primary_key=True)
    desc = models.CharField(verbose_name='项目信息描述', max_length=256)
    created_by = models.OneToOneField(User, verbose_name='创建者')
    created_time = models.DateTimeField(verbose_name='项目创建时间', default=_generate_now())


class Category(models.Model):
    """
    接口分类信息
    """
    cid = models.AutoField(primary_key=True, verbose_name="分类id")
    cname = models.CharField(max_length=200, verbose_name='分类名称')
    cdesc = models.CharField(max_length=200, verbose_name='分类描述')
    isdel = models.IntegerField(default=0, verbose_name='是否删除{0:正常,1删除}')
    addtime = models.DateTimeField(verbose_name='添加时间', default=_generate_now())

    class Meta:
        verbose_name = "接口分类表"
        db_table = "cate"


class Api(models.Model):
    """
    API详情描述
    """
    medthods_choices = ((0, 'GET'), (1, 'POST'), (2, 'PUT'), (3, 'DELETE'), (4, 'PATCH'))

    id = models.AutoField(primary_key=True, verbose_name="接口编号")
    cid = models.IntegerField(default=0, verbose_name='接口分类id')
    methods = models.IntegerField(default=0, choices=[], null=False)
    login_required = models.BooleanField(default=False)
    url = models.CharField(max_length=255, null=True, verbose_name=u'请求地址')
    name = models.CharField(max_length=100, null=True, verbose_name=u'接口名')
    des = models.CharField(max_length=300, null=True, verbose_name=u'接口描述')
    parameter = models.TextField(verbose_name=u'请求参数{所有的主求参数,以json格式在此存放}')
    memo = models.TextField(verbose_name=u'备注')
    reruen_value = models.TextField(verbose_name=u'返回值')
    lasttime = models.IntegerField(null=True, verbose_name='提后操作时间')
    firstuid = models.IntegerField(null=True, verbose_name='首次增加uid')
    lastuid = models.IntegerField(null=True, verbose_name='最后修改uid')
    isdel = models.IntegerField(default=0, verbose_name='{0:正常,1:删除}')
    type = models.CharField(null=True, max_length=11, verbose_name='请求方式')
    ord = models.IntegerField(default=0, verbose_name='排序(值越大,越靠前)')

    class Meta:
        verbose_name = "接口明细表"
        db_table = "api"

