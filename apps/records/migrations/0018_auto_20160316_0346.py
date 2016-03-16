# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_auto_20160316_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='y_accumulative',
            field=models.FloatField(default=0, help_text='La sumatoria de todos los valores "Y" hasta el actual, se calcula con Channel.fill_accumulatives', verbose_name='Y acumulativo'),
        ),
    ]
