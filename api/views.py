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
    return render(request, 'categories.html', res)


@login_required
@require_POST
def new_cate(request, pid):
    p = Projects.objects.get(id=pid)
    cname = request_post(request, 'cname', required=True)
    cdesc = request_post(request, 'cdesc', required=True)
    new_cate = Category.objects.create(project=p, cname=cname, cdesc=cdesc, add_by=request.user)
    new_cate.save()
    return HttpResponseRedirect(reverse('api.views.category_list'))


@login_required
@require_POST
def edit_cate(request, cid):
    cname = request_post(request, 'cname')
    cdesc = request_post(request, 'cdesc')
    c = Category.objects.get(aid=cid)
    c.cname = cname
    c.cdesc = cdesc
    c.save()

    return HttpResponseRedirect('/')


@login_required
@require_POST
def del_class(request, cid):
    get_cate = Category.objects.get(aid=cid)
    get_cate.isdel = 1
    get_cate.save()
    return HttpResponseRedirect(reverse('api.views.category_list'))


@login_required
def api_list(request, cid):
    cate = Category.objects.get(aid=cid)
    cname = cate.cname
    all_api = Api.objects.filter(cate=cate).filter(isdel=0)

    return render(request, 'cate_detail.html', locals())


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
def del_api(request):
    if request.method == "POST":
        api_id = request.POST["api_id"]
        api_object = Api.objects.get(id=int(api_id))
        api_object.isdel = 1
        api_object.save()
        return HttpResponse("success")


def get_create_update_arg(request):
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
        else:
            continue
            # print tmp
            # print parameter

    print("parameter: {}".format(parameter))

    kw = {
        "num": request.POST['num'].strip(),
        "url": request.POST['url'].strip(),
        "name": request.POST['name'].strip(),
        "des": request.POST['des'].strip(),
        "parameter": parameter,
        "memo": request.POST['memo'].strip(),
        "re": request.POST['re'].strip(),
        "type": request.POST['type'].strip(),
        "firstuid": request.user.id,
        "lastuid": request.user.id,
        "lasttime": int(time.time()),
    }
    return kw


@login_required
def edit_api(request):
    try:
        aid, all_api, class_name = get_all_api(request)
    except Exception as e:
        print(e)
        print("new_api_fail_1")
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))
    try:
        api_id = request.GET["id"]
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))
    if request.method == "POST":
        kw = get_create_update_arg(request)
        kw['aid'] = aid
        del kw['firstuid']
        Api.objects.filter(id=api_id).update(**kw)
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))
    edit_api_object = Api.objects.get(id=int(api_id))
    return render(request, 'op_api.html', locals())


@login_required
def new_api(request):
    try:
        aid, all_api, class_name = get_all_api(request)
    except Exception as e:
        print(e)
        print("new_api_fail_1")
        return HttpResponseRedirect('/')

    if request.method == "POST":
        kw = get_create_update_arg(request)
        kw['aid'] = aid
        api_objects = Api.objects.create(**kw)
        api_objects.save()
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))

    return render(request, 'op_api.html', locals())


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
    return HttpResponseRedirect(reverse('api.index'))


@login_required
@require_POST
def del_proj(request):
    """删除一个项目"""
    pid = request_post(request, 'pid', required=True)
    ps = Projects.objects.filter(id=pid).all()
    for p in ps:
        p.isdel = 1
        p.save()

    return HttpResponseRedirect(reverse('api.index'))
