# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_channel_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='end_date',
        ),
    ]
