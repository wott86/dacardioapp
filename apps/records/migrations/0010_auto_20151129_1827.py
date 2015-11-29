# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_auto_20151114_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='patient',
            field=models.ForeignKey(related_name='records', verbose_name='paciente', to='patients.Patient'),
        ),
        migrations.AlterField(
            model_name='record',
            name='taken_by',
            field=models.ForeignKey(related_name='records_loaded', verbose_name='registrado por', to=settings.AUTH_USER_MODEL),
        ),
    ]
