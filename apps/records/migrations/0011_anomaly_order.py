# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20151129_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='anomaly',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='orden'),
        ),
    ]
