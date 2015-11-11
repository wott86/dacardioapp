import matplotlib.pyplot as plt


def get_image(channel, file_like, format_='png', limit=None, offset=None):
    #plt.plot([1,2,3,4])
    plt.clf()
    x = []
    y = []
    points = channel.points.all()
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
    plt.plot(x, y, 'g-')
    #plt.ylabel('some numbers')
    plt.title('ECG: %s' % channel.record.patient.full_name)
    plt.savefig(file_like, format=format_)
    plt.show()

if __name__ == '__main__':
    get_image(None, 'test.png')
