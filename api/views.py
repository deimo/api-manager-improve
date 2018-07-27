"""
Brief Desc: 视图函数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-06-07 15:07:44. Created By jadger.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import time

from django.urls import reverse
from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from api.models import Category, Api, Projects
from django.http import HttpResponseRedirect
from lib._django import request_get, request_post


# Create your views here.
def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')


def index(request):
    """首页显示项目"""
    items = Projects.objects.all()
    return render(request, 'index.html', locals())


@login_required
def category_list(request):
    pid = request_get(request, 'pid', ptype=int, required=True)
    p = Projects.objects.get(id=pid)
    all_cate = Category.objects.filter(project=p).all()

    res = dict(all_cate=all_cate)
    res['pid'] = pid
    return render(request, 'categories.html', res)


@login_required
@require_POST
def new_cate(request):
    pid = request_post(request, 'pid', ptype=int, required=True)
    cname = request_post(request, 'cname', required=True)
    cdesc = request_post(request, 'cdesc', required=True)
    p = Projects.objects.get(id=pid)
    Category.objects.create(project=p, cname=cname, cdesc=cdesc, add_by=request.user)
    return HttpResponseRedirect(reverse('category_list') + '?pid=' + str(pid))


@login_required
@require_POST
def edit_cate(request, cid):
    cname = request_post(request, 'cname')
    cdesc = request_post(request, 'cdesc')
    c = Category.objects.get(aid=cid)
    c.cname = cname
    c.cdesc = cdesc
    c.save()

    return HttpResponseRedirect(reverse('category_list'))


@login_required
@require_POST
def del_cate(request, cid):
    cid = request_post(request, 'cid', ptype=int, required=True)
    get_cate = Category.objects.get(aid=cid)
    get_cate.isdel = 1
    get_cate.save()
    return HttpResponseRedirect(reverse('api.views.category_list'))


@login_required
def api_list(request):
    cid = request_get(request, 'cid', ptype=int, required=True)
    cate = Category.objects.get(id=cid)
    all_api = Api.objects.filter(cate=cate).filter(isdel=0).all()
    res = dict(items=all_api)
    res['cid'] = cid

    return render(request, 'cate_detail.html', res)


@login_required
@require_POST
def copy_api(request):
    api_id = request.POST["api_id"]
    api_name = request.POST["api_name"]
    api_object = Api.objects.get(id=int(api_id))
    api_object.id = None
    api_object.name = api_name
    api_object.save()
    return HttpResponse("success")


@login_required
@require_POST
def del_api(request):
    api_id = request.POST["api_id"]
    api_object = Api.objects.get(id=int(api_id))
    api_object.isdel = 1
    api_object.save()

    return HttpResponse("success")


def _get_create_update_arg(request, created=None):
    parameter = {}
    for i in request.POST:
        if i.startswith("param_"):
            """
                param_1_0 : username
                param_1_1 : int
            """
            # print i, request.POST[i].encode('utf-8')
            f1 = i.split('_')[1]
            f2 = i.split('_')[2]
            try:
                tmp = parameter[int(f2)]
            except Exception as e:
                tmp = {}
            tmp[int(f1)] = request.POST[i].strip()
            parameter[int(f2)] = tmp
    kw = {
        "num": request.POST['num'].strip(),
        "url": request.POST['url'].strip(),
        "name": request.POST['name'].strip(),
        "desc": request.POST['desc'].strip(),
        'login_required': True if request.POST['login'].strip() == '1' else False,
        "parameter": parameter,
        "memo": request.POST['memo'].strip(),
        "return_value": request.POST['return_value'].strip(),
        "method": request.POST['method'].strip(),
    }
    if created:
        kw['created_user'] = request.user
    kw['updated_by'] = request.user.id

    return kw


@login_required
def edit_api(request):
    cid = request_get(request, 'cid', ptype=int, required=True)
    api_id = request_get(request, 'id', ptype=int, required=True)

    cate = Category.objects.get(id=cid)
    cname = cate.cname
    all_api = Api.objects.filter(cate=cate).filter(isdel=0).all()

    if request.method == "POST":
        kw = _get_create_update_arg(request)
        cate = Category.objects.filter(id=cid).first()
        kw['cate'] = cate
        Api.objects.filter(id=api_id).update(**kw)
        return HttpResponseRedirect(reverse('api_list') + '?cid=' + str(cid))
    edit_api_object = Api.objects.get(id=api_id)
    print('the edit_api_object: ', edit_api_object)
    print('edit_api_object: ', edit_api_object.desc)
    return render(request, 'op_api.html', locals())


@login_required
def new_api(request):
    cid = request_get(request, 'cid', ptype=int)
    if request.method == 'GET':
        cate = Category.objects.filter(id=cid).first()
        all_api = Api.objects.filter(cate=cate).filter(isdel=0).all()

        return render(request, 'op_api.html', locals())

    if request.method == 'POST':
        kw = _get_create_update_arg(request, created=True)
        cate = Category.objects.filter(id=cid).first()
        kw['cate'] = cate
        api_objects = Api.objects.create(**kw)
        api_objects.save()

        return HttpResponseRedirect(reverse('api_list') + '?cid=' + str(cid))


@login_required
@require_POST
def new_proj(request):
    """添加一个项目"""
    name = request_post(request, 'pname', required=True)
    desc = request_post(request, 'pdesc', required=True)
    p = Projects.objects.filter(name=name).first()
    if not p:
        p = Projects()
        p.name = name
        p.desc = desc
        p.domain = 'http://' + request.META.get('HTTP_HOST')
        p.created_by = request.user
    p.name = name
    p.desc = desc
    p.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
@require_POST
def del_proj(request):
    """删除一个项目"""
    pid = request_post(request, 'pid', required=True)
    ps = Projects.objects.filter(id=pid).all()
    for p in ps:
        p.isdel = 1
        p.save()

    return HttpResponseRedirect(reverse('index'))
