# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20150728_2336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotation',
            options={'verbose_name': 'anotaci\xf3n', 'verbose_name_plural': 'anotaciones'},
        ),
        migrations.AlterModelOptions(
            name='anomaly',
            options={'verbose_name': 'anomal\xeda'},
        ),
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'punto'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'registro'},
        ),
    ]
