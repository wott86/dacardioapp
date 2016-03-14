# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_anomaly_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='sampling_rate',
            field=models.IntegerField(default=500, verbose_name='Tasa de muestreo'),
        ),
        migrations.AddField(
            model_name='channel',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de inicio', blank=True),
        ),
    ]
