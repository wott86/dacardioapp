# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20150428_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone_home',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_mobile',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_office',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ses',
            field=models.ForeignKey(related_name='patients', verbose_name='Estatus socioecon\xf3mico', to='patients.Ses'),
        ),
    ]
