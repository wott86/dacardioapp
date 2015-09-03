# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20150902_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='active',
            field=models.BooleanField(default=True, help_text=''),
        ),
    ]
