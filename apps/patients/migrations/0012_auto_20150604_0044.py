# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20150603_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='habits',
            field=models.ManyToManyField(related_name='patients', to='patients.Habit', blank=True),
        ),
    ]
