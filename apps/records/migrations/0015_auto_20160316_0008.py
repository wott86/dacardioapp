# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_remove_channel_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='y_accumulative',
            field=models.FloatField(default=0, help_text='La sumatoria de todos los valores "Y" hasta el actual, se calcula con Channel,fill_accumulatives', verbose_name='Y acumulativo'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='type',
            field=models.CharField(default=b'n', max_length=2, verbose_name='tipo', choices=[(b'n', 'Normal'), (b'i', 'Integrada'), (b'c', 'Cuadr\xe1tica'), (b'o', 'Original'), (b'd', 'Derivada'), (b'f', 'Filtrada'), (b'r', 'RR')]),
        ),
    ]
