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
    name = models.CharField(verbose_name='项目名', max_length=255, unique=True)
    desc = models.CharField(verbose_name='项目信息描述', max_length=256)
    domain = models.CharField(verbose_name='域名', max_length=255)
    isdel = models.IntegerField(default=0, verbose_name='{0:正常,1:删除}')
    created_by = models.ForeignKey(User, verbose_name='创建者', on_delete=models.PROTECT)
    created_time = models.DateTimeField(verbose_name='项目创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '项目表'
        db_table = 'projects'


class Category(models.Model):
    """
    接口分类信息
    """
    id = models.AutoField(primary_key=True, verbose_name="分类id")
    project = models.ForeignKey(Projects, verbose_name='所在项目', on_delete=models.PROTECT)
    cname = models.CharField(max_length=200, verbose_name='分类名称')
    cdesc = models.CharField(max_length=200, verbose_name='分类描述')
    isdel = models.IntegerField(default=0, verbose_name='是否删除{0:正常,1删除}')
    addtime = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    add_by = models.ForeignKey(User, verbose_name='添加人', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "接口分类表"
        db_table = "category"


class Api(models.Model):
    """
    API详情描述
    """
    MEDTHODS_CHOICES = ((0, 'GET'), (1, 'POST'), (2, 'PUT'), (3, 'DELETE'), (4, 'PATCH'))

    id = models.AutoField(primary_key=True)
    num = models.CharField(verbose_name='接口编号', max_length=200)
    cate = models.ForeignKey(Category, verbose_name='分类', on_delete=models.PROTECT)
    method = models.IntegerField(default=0, choices=MEDTHODS_CHOICES, null=False)
    name = models.CharField(max_length=100, null=True, verbose_name='接口名')
    url = models.CharField(max_length=255, null=True, verbose_name='请求地址')
    login_required = models.BooleanField(default=False, verbose_name='是否需要登录')
    desc = models.CharField(max_length=300, null=True, verbose_name='接口描述')
    parameter = models.TextField(verbose_name='请求参数{所有的主求参数,以json格式在此存放}')  # 不使用mysql的json字段是为了兼容低版本的MySQL
    memo = models.TextField(verbose_name='备注')
    return_value = models.TextField(verbose_name='返回值')
    isdel = models.IntegerField(default=0, verbose_name='{0:正常,1:删除}')
    ord = models.IntegerField(default=0, verbose_name='排序(值越大,越靠前)',)
    created_user = models.ForeignKey(User, null=True, verbose_name='首次添加的大佬', on_delete=models.PROTECT)
    updated_by = models.IntegerField(null=True, verbose_name='最后修改的大佬')
    createte_time = models.DateTimeField(null=True, verbose_name='最后的操作时间', auto_now_add=True)
    update_time = models.DateTimeField(null=True, verbose_name='最后的操作时间', auto_now=True)

    class Meta:
        verbose_name = "接口明细表"
        db_table = "api"
