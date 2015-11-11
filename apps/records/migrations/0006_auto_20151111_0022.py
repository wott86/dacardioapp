# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20151109_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='anomaly',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='point',
        ),
        migrations.RemoveField(
            model_name='point',
            name='record',
        ),
        migrations.DeleteModel(
            name='Annotation',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]
