# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20150831_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='annotation_type',
            field=models.CharField(verbose_name='tipo', max_length=45, help_text=''),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='anomaly',
            field=models.ForeignKey(verbose_name='anomal\xeda', blank=True, null=True, help_text='', to='records.Anomaly'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='created',
            field=models.DateTimeField(verbose_name='fecha de creaci\xf3n', help_text='', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='created_by',
            field=models.ForeignKey(verbose_name='creado por', help_text='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='point',
            field=models.ForeignKey(verbose_name='punto', help_text='', to='records.Point'),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='name',
            field=models.CharField(verbose_name='nombre', max_length=256, help_text=''),
        ),
        migrations.AlterField(
            model_name='point',
            name='flagged',
            field=models.BooleanField(verbose_name='marca', default=False, help_text=''),
        ),
        migrations.AlterField(
            model_name='point',
            name='record',
            field=models.ForeignKey(verbose_name='registro', help_text='', to='records.Record'),
        ),
        migrations.AlterField(
            model_name='point',
            name='wave',
            field=models.CharField(verbose_name='onda detectada', max_length=1, blank=True, null=True, choices=[(None, b'None'), (b'p', b'p'), (b'q', b'q'), (b'r', b'r'), (b's', b's'), (b'u', b'u')], help_text=''),
        ),
        migrations.AlterField(
            model_name='record',
            name='created',
            field=models.DateTimeField(verbose_name='fecha de creaci\xf3n', help_text='', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='modified',
            field=models.DateTimeField(verbose_name='fecha de modificaci\xf3n', help_text='', auto_now=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='patient',
            field=models.ForeignKey(verbose_name='paciente', help_text='', to='patients.Patient'),
        ),
        migrations.AlterField(
            model_name='record',
            name='taken_by',
            field=models.ForeignKey(verbose_name='registrado por', help_text='', to=settings.AUTH_USER_MODEL),
        ),
    ]
