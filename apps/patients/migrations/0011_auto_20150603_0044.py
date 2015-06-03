# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_auto_20150603_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='modified_new_value',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='history',
            name='modified_old_value',
            field=models.TextField(default=b''),
        ),
    ]
