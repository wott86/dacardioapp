# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_auto_20151111_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='record',
            field=models.ForeignKey(related_name='channels', verbose_name='registro', to='records.Record'),
        ),
    ]
