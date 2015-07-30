# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20150604_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birth_place',
            field=models.CharField(max_length=256, blank=True, default=b'', help_text=''),
        ),
    ]
