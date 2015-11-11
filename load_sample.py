#!/usr/bin/env python
import os
import re
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardio.settings")
    django.setup()

    from apps.records.models import Point, Record, Channel
    f = open('samples/aami3a.txt')
    #f = open('samples/ecgsyn.dat')
    results = re.findall(r'(\d+)\s+(\d+)', f.read())
    #results = re.findall(r'(\d+\.?\d+)\s+(\d+\.?\d+)\s+(\d+)', f.read())
    record = Record.objects.get(pk=1)
    channel = Channel.objects.create(record=record, name='test')

    length = len(results)

    for index, result in enumerate(results):
        print 'Reading %d entry of %s' % (index+1, length)
        Point.objects.create(channel=channel, x=result[0], y=result[1])

    print 'Finished reading %d entries' % length
