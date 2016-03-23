# coding=utf-8
import matplotlib.pyplot as plt
from django.utils.translation import ugettext as _


def get_channel_image(channel, file_like, format_='png', interval_start=0, interval_end=None):
    x = []
    y = []
    kwargs = {
        ('x__gte' if not channel.is_time else 'y_accumulative__gte'): interval_start if channel.is_time else interval_start / channel.sampling_rate
    }
    if interval_end not in (None, ''):
        kwargs['x__lte' if not channel.is_time else 'y_accumulative__lte'] = interval_end if channel.is_time else interval_end / channel.sampling_rate

    points = channel.points.filter(**kwargs).order_by('x')

    for point in points:
        x.append(point.x)
        y.append(point.y)
    get_image(x, y, file_like, 'ECG: %s' % channel.record.patient.full_name, format_=format_)


def get_media_image(channel, file_like, initial_time, final_time, interval, format_='png'):
    x, y = channel.get_media_points(initial_time, final_time, interval)
    get_image(x, y, file_like, 'RR Media: %s' % channel.record.patient.full_name, format_=format_)


def get_standard_deviation_image(channel, file_like, initial_time, final_time, interval, format_='png'):
    x, y = channel.get_standard_deviation_points(initial_time, final_time, interval)
    get_image(x, y, file_like, _(u'RR Desviación estándard: %s') % channel.record.patient.full_name, format_=format_)


def get_return_map_image(channel, file_like, initial_time, final_time, format_='png'):
    x, y = channel.get_return_map(initial_time, final_time)
    get_image(x, y, file_like, 'RR Mapa de retorno: %s' % channel.record.patient.full_name, format_=format_, line_style='.')


def get_image(x, y, file_like, title=None, format_='png', xlabel=None, ylabel=None, line_style='-'):
    plt.clf()
    plt.plot(x, y, line_style)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.savefig(file_like, format=format_)
    plt.show()


if __name__ == '__main__':
    get_channel_image(None, 'test.png')

