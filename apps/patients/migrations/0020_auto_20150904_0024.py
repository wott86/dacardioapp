# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0019_diagnosis_made_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='chart_number',
            field=models.CharField(verbose_name='n\xfamero de historia', max_length=50, blank=True, null=True, help_text=''),
        ),
    ]
