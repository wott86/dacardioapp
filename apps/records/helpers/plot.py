import matplotlib.pyplot as plt


def get_channel_image(channel, file_like, format_='png', limit=None, offset=None):
    x = []
    y = []
    points = channel.points.all().order_by('x')
    if limit is not None and offset is not None:
        points = points[offset:limit]
    elif limit is not None and offset is None:
        points = points[:limit]
    elif limit is None and offset is not None:
        points = points[offset:]
    else:
        points = points[:3000]
    for point in points:
        x.append(point.x)
        y.append(point.y)
    get_image(x, y, file_like, 'ECG: %s' % channel.record.patient.full_name, format_=format_)


def get_media_image(channel, file_like, initial_time, final_time, interval, format_='png'):
    x, y = channel.get_media_points(initial_time, final_time, interval)
    get_image(x, y, file_like, 'RR Media: %s' % channel.record.patient.full_name, format_=format_)


def get_image(x, y, file_like, title=None, format_='png', xlabel=None, ylabel=None):
    plt.clf()
    plt.plot(x, y, 'g-')
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
