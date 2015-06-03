# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_auto_20150602_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='modified_field',
            field=models.TextField(default=b'ALL'),
        ),
    ]
