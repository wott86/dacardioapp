# coding=utf-8
import matplotlib.pyplot as plt
from django.utils.translation import ugettext as _


def get_channel_image(channel, file_like, format_='png', interval_start=0, interval_end=None, clear=False, color='r', line_style='-'):
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
    get_image(
        x,
        y,
        file_like,
        'ECG: %s' % channel.record.patient.full_name,
        format_=format_,
        ylabel=_('Tiempo (ms)') if channel.is_time else None,
        xlabel=_('Secuencia') if channel.is_time else 'ms',
        hide_axis=not channel.is_time,
        color=color,
        line_style=line_style,
        clear=clear
    )


def get_media_image(channel, file_like, initial_time, final_time, interval, format_='png', clear=False, color='r', line_style='-'):
    x, y = channel.get_media_points(initial_time, final_time, interval)
    get_image(
        x,
        y,
        file_like,
        'RR Media: %s' % channel.record.patient.full_name,
        format_=format_,
        ylabel=_('Media (ms)'),
        xlabel=_('Secuencia'),
        hide_axis=not channel.is_time,
        clear=clear,
        color=color,
        line_style=line_style
    )


def get_standard_deviation_image(channel, file_like, initial_time, final_time, interval, format_='png', clear=False, color='r', line_style='-'):
    x, y = channel.get_standard_deviation_points(
        initial_time, final_time, interval)
    get_image(
        x,
        y,
        file_like,
        _(u'RR Desviación estándar: %(patient)s') % {
            'patient': channel.record.patient.full_name
        },
        format_=format_,
        ylabel=_('STD (ms)'),
        xlabel=_('Secuencia'),
        hide_axis=not channel.is_time,
        clear=clear,
        color=color,
        line_style=line_style
    )


def get_return_map_image(channel, file_like, initial_time, final_time, format_='png', clear=False, color='r', line_style='.'):
    x, y = channel.get_return_map(initial_time, final_time)
    get_image(
        x,
        y,
        file_like,
        _('RR Mapa de retorno: %(patient)s') % {
            'patient': channel.record.patient.full_name
        },
        format_=format_,
        ylabel=_('Tiempo (t + 1)'),
        xlabel=_('Tiempo (t)'),
        hide_axis=not channel.is_time,
        clear=clear,
        color=color,
        line_style=line_style
    )


def get_SDSD_image(channel, file_like, initial_time, final_time, interval, format_='png', clear=False, color='r', line_style='-'):
    x, y = channel.get_SDSD(initial_time, final_time, interval)
    get_image(
        x,
        y,
        file_like,
        _(u'RR SDSD: %(patient)s') % {
            'patient': channel.record.patient.full_name
        },
        format_=format_,
        ylabel=_('SDSD (ms)'),
        xlabel=_('Intervalo'),
        hide_axis=not channel.is_time,
        clear=clear,
        color=color,
        line_style=line_style

    )


def get_PNN50_image(channel, file_like, initial_time, final_time, interval, format_='png', clear=False, color='r', line_style='-'):
    x, y = channel.get_PNN50_points(
        initial_time, final_time, interval)
    get_image(
        x,
        y,
        file_like,
        _(u'RR PNN50: %(patient)s') % {
            'patient': channel.record.patient.full_name
        },
        format_=format_,
        ylabel=_('PNN50 (ms)'),
        xlabel=_('Intervalo (%(interval)d m)') % {'interval': interval / 60000},
        hide_axis=not channel.is_time,
        clear=clear,
        color=color,
        line_style=line_style

    )

def get_image(x, y, file_like, title=None, format_='png', xlabel=None, ylabel=None, line_style='-', hide_axis=False, clear=False, color='r'):
    if clear:
        plt.clf()
    plt.plot(x, y, line_style, color=color)
    plt.xlim(min(x), max(x))
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    fig = plt.figure()
    fig.gca()
    plt.figure(1)

    plt.grid(True)

    if hide_axis:
        # plt.axis('off')
        plt.tick_params(
                axis='both',
                which='both',
                bottom='off',
                top='off',
                labelbottom='off',
                left='off',
                labelleft=False)
    # fig.savefig(file_like, format=format_)
    plt.tight_layout()
    plt.savefig(file_like, format=format_, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    get_channel_image(None, 'test.png')

