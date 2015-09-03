# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0016_auto_20150831_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='date',
            field=models.DateTimeField(verbose_name='fecha de creaci\xf3n', null=True, help_text='', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(verbose_name='paciente', help_text='', related_name='diagnosis', to='patients.Patient'),
        ),
    ]
