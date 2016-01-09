from django.template import Library, Node, Variable

register = Library()


@register.simple_tag(takes_context=True)
def add_get_params(context):
    request = Variable('request').resolve(context)
    params = request.GET.copy()
    if 'order' in params:
        params.pop('order')
    if 'page' in params:
        params.pop('page')
    params = '&%s' % params.urlencode()
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