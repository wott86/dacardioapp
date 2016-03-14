from django.template import Library, Variable

register = Library()


@register.simple_tag(takes_context=True)
def standard_deviation(context, channel):
    """

    Args:
        context: template context
        *args: list of exclude params

    Returns:

    """
    request = Variable('request').resolve(context)
    interval_start = request.POST.get('interval_start', 0)
    interval_end = request.POST.get('interval_end', 5000)
    if interval_start == '':
        interval_start = 0

    if interval_end == '':
        interval_end = 5000
    return "{0:.2f}".format(channel.get_standard_deviation(interval_start, interval_end))


@register.simple_tag(takes_context=True)
def media(context, channel):
    """

    Args:
        context: template context
        *args: list of exclude params

    Returns:

    """
    request = Variable('request').resolve(context)
    interval_start = request.POST.get('interval_start', 0)
    interval_end = request.POST.get('interval_end', 5000)
    if interval_start == '':
        interval_start = 0

    if interval_end == '':
        interval_end = 5000
    return "{0:.2f}".format(channel.get_media(interval_start, interval_end))
