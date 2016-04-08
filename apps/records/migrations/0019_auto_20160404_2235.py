# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0018_auto_20160316_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de inicio', blank=True),
        ),
    ]
