# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_auto_20160312_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de finalizaci\xf3n', blank=True),
        ),
    ]
