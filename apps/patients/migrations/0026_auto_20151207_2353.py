# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0025_auto_20151207_2329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name': 'diagn\xf3stico', 'verbose_name_plural': 'diagn\xf3sticos'},
        ),
    ]
