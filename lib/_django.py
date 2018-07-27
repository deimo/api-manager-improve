"""
Brief Desc: 与django有关的通用功能，修改默认_django行为
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2018-06-05 15:22:33. Created By jadger.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from functools import partial

from lib._exception import Http400, Http500


def __get_param(request, key, default=None, ptype=None, required=False, mapping_key=None,
                minvalue=None, maxvalue=None, choices=None, autominvalue=False,
                automaxvalue=False):
    """获取django request对象中的参数,
       注意此方法中默认的参数类型为str，required字段只能区分“物理空”，不会区分“逻辑空”，情形如下：
       当客户端传入空字符串且required字段为True时将不会返回400，而是字段验证通过
    :param request  django中的request对象
    :param key: 参数名
    :param default: 参数默认值
    :param ptype: 参数类型
    :param mapping_key: request.XXXX (GET, POST, PUT, DELETE, META)
    :param required: 参数是否必须
    :param minvalue 限制参数最小值
    :param maxvalue 限制参数最大值
    :param choices 限制参数值选择
    :param autominvalue 值小于minvalue则调整为minvalue
    :param automaxvalue 值大于maxvalue则调整为maxvalue
    """
    mapping = getattr(request, mapping_key, {})
    if required is True and key not in mapping:
        print("missing param %s" % key)
        raise Http400('missing param %s' % key)
    value = mapping.get(key, default)
    if ptype is not None:
        try:
            value = ptype(value)
        except (ValueError, TypeError):
            print("invild param type %s, %s needed" % (key, ptype))
            raise Http400('invild param type %s, %s needed' % (key, ptype))

            # return HttpResponse(400, "invild param type %s, %s needed" % (key, ptype))
        except Exception as e:
            print(e)
            raise Http500(500, 'unknow error')

    if minvalue is not None and value < minvalue:
        if autominvalue is True:
            value = minvalue
        else:
            raise Http400('param %s less than minvalue %s' % (key, minvalue))
    if maxvalue is not None and value > maxvalue:
        if automaxvalue is True:
            value = maxvalue
        else:
            raise Http400('param %s bigger than maxvalue %s' % (key, maxvalue))
    if choices is not None and value not in choices:
        raise Http400('prams %s is not available' % key)

    return value


# 在真是请求中请使用以下偏函数
# 当有参数类型与定义的要求不匹配时，会自动截断请求：返回给客户端400， 或其它未知异常发生时服务端返回500

request_get = partial(__get_param, mapping_key="GET")
request_post = partial(__get_param, mapping_key="POST")
request_put = partial(__get_param, mapping_key="put")
request_headers = partial(__get_param, mapping_key="META")
