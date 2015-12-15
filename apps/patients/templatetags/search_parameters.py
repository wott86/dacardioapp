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
