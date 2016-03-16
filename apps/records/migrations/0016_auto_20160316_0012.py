# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def fill_y_accumulatives(apps, schema_editor):
    Channel = apps.get_model("records", "Channel")

    for channel in Channel.objects.filter(type='r'):
        sum = 0
        for point in channel.points.all().order_by('x'):
            sum += point.y
            point.y_accumulative = sum
            point.save()


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0015_auto_20160316_0008'),
    ]

    operations = [
        migrations.RunPython(fill_y_accumulatives)
    ]
