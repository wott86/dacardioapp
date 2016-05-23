from django.template import Library, Variable
from django.http.request import QueryDict

register = Library()


def filter_params(params, *args):
    data = QueryDict('', mutable=True)
    data.update({param:params[param] for param in params if param not in args})
    print data, args
    return data


@register.simple_tag(takes_context=True)
def add_get_params(context, *args):
    request = Variable('request').resolve(context)
    params = request.GET.copy()
    if 'order' in params:
        params.pop('order')
    if 'page' in params:
        params.pop('page')
    params = filter_params(params, *args)
    params = '&%s' % params.urlencode()
    return params


@register.simple_tag(takes_context=True)
def add_post_params(context, *args):
    request = Variable('request').resolve(context)
    params = request.POST.copy()
    params = filter_params(params, *args)
    params = params.urlencode()
    return params


@register.simple_tag(takes_context=True)
def add_get_params_hidden(context, *args):
    """

    Args:
        context: template context
        *args: list of exclude params

    Returns:

    """
    request = Variable('request').resolve(context)
    params = request.GET.copy()
    hiddens = []
    for param in params:
        if param not in args:
            hiddens.append('<input type="hidden" name="%s" value="%s" />' % (param, params[param]))

    return ''.join(hiddens)


@register.simple_tag(takes_context=True)
def add_post_params_hidden(context, *args):
    """

    Args:
        context: template context
        *args: list of exclude params

    Returns:

    """
    request = Variable('request').resolve(context)
    params = request.POST.copy()
    hiddens = []
    for param in params:
        if param not in args:
            hiddens.append('<input type="hidden" name="%s" value="%s" />' % (param, params[param]))

    return ''.join(hiddens)
