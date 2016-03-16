#!/usr/bin/env python
import os
import re
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardio.settings")
    django.setup()

    from apps.records.models import Point, Record, Channel
    f = open('samples/sanos/Sano_10002_01:00:00pm_Srr.dat')
    #f = open('samples/ecgsyn.dat')
    results = re.findall(r'(\d+)', f.read())
    #results = re.findall(r'(\d+\.?\d+)\s+(\d+\.?\d+)\s+(\d+)', f.read())
    record = Record.objects.get(pk=1)
    channel = Channel.objects.create(record=record, name='RR', type='r')

    length = len(results)
    _sum = 0

    for index, result in enumerate(results):
        print 'Reading %d entry of %s' % (index+1, length)
        y = int(result)
        _sum += y
        Point.objects.create(channel=channel, x=index, y=y, y_accumulative=_sum)

    print 'Finished reading %d entries' % length
