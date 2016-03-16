# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def fix_rr_x(apps, schema_editor):
    Channel = apps.get_model("records", "Channel")

    for channel in Channel.objects.filter(type='r'):
        sum = 0
        for point in channel.points.all().order_by('x'):
            point.x = sum
            sum += 1
            point.save()


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0016_auto_20160316_0012'),
    ]

    operations = [
        migrations.RunPython(fix_rr_x)
    ]
