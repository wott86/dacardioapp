from apps.records.helpers import time
from django.template import Library, Variable
from dateutil import parser

register = Library()


def get_interval(context):
    request = Variable('request').resolve(context)
    interval_start = request.POST.get('interval_start')
    interval_end = request.POST.get('interval_end')

    interval_start = time.convert_time_to_milli(Variable('channel').resolve(context), parser.parse(interval_start))
    interval_end = time.convert_time_to_milli(Variable('channel').resolve(context), parser.parse(interval_end))
    return interval_start, interval_end


@register.simple_tag(takes_context=True)
def standard_deviation(context, channel):
    """

    :param context:
    :param channel:
    :return:
    """
    interval_start, interval_end = get_interval(context)

    if interval_start == '':
        interval_start = 0

    if interval_end == '':
        interval_end = 5000
    return "{0:.2f}".format(channel.get_standard_deviation(interval_start, interval_end))


@register.simple_tag(takes_context=True)
def media(context, channel):
    """

    :param context:
    :param channel:
    :return:
    """
    interval_start, interval_end = get_interval(context)

    if interval_start == '':
        interval_start = 0

    if interval_end == '':
        interval_end = 5000
    return "{0:.2f}".format(channel.get_media(interval_start, interval_end))


@register.simple_tag(takes_context=True)
def pnn50(context, channel):
    """

    :param context:
    :param channel:
    :return:
    """
    interval_start, interval_end = get_interval(context)

    if interval_start == '':
        interval_start = 0

    if interval_end == '':
        interval_end = 5000
    res = channel.get_PNN50(interval_start, interval_end)
    return "{0:.2f}".format(res)
