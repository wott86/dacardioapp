# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20150902_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='record',
            field=models.ForeignKey(related_name='points', verbose_name='registro', to='records.Record'),
        ),
    ]
