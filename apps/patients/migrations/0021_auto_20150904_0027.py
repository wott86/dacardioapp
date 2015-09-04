# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0020_auto_20150904_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='description',
            field=models.TextField(verbose_name='descripci\xf3n', blank=True, default=b'', help_text=''),
        ),
    ]
