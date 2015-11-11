# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0006_auto_20151111_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annotation_type', models.CharField(max_length=45, verbose_name='tipo')),
                ('annotation', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creaci\xf3n')),
                ('anomaly', models.ForeignKey(verbose_name='anomal\xeda', blank=True, to='records.Anomaly', null=True)),
                ('created_by', models.ForeignKey(verbose_name='creado por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'anotaci\xf3n',
                'verbose_name_plural': 'anotaciones',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'n', max_length=2, verbose_name='tipo', choices=[(b'n', b'Normal'), (b'i', b'Integrated'), (b'c', b'Cuadratic'), (b'r', b'Raw'), (b'd', b'Derivated')])),
                ('name', models.CharField(default=b'', max_length=50, verbose_name='nombre', blank=True)),
                ('description', models.TextField(default=b'', verbose_name='descripci\xf3n', blank=True)),
                ('record', models.ForeignKey(related_name='channel', verbose_name='registro', to='records.Record')),
            ],
            options={
                'verbose_name': 'canal',
                'verbose_name_plural': 'canales',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.FloatField(db_index=True)),
                ('y', models.FloatField()),
                ('wave', models.CharField(blank=True, max_length=1, null=True, verbose_name='onda detectada', choices=[(None, b'None'), (b'p', b'p'), (b'q', b'q'), (b'r', b'r'), (b's', b's'), (b'u', b'u')])),
                ('flagged', models.BooleanField(default=False, verbose_name='marca')),
                ('channel', models.ForeignKey(related_name='points', verbose_name='canal', to='records.Channel')),
            ],
            options={
                'verbose_name': 'punto',
            },
        ),
        migrations.AddField(
            model_name='annotation',
            name='point',
            field=models.ForeignKey(verbose_name='punto', to='records.Point'),
        ),
    ]
