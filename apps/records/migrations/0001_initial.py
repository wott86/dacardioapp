# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20150604_0044'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annotation_type', models.CharField(max_length=45)),
                ('annotation', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('wave', models.CharField(blank=True, max_length=1, null=True, choices=[(None, b'None'), (b'p', b'p'), (b'q', b'q'), (b'r', b'r'), (b's', b's'), (b'u', b'u')])),
                ('flagged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(to='patients.Patient')),
                ('taken_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='record',
            field=models.ForeignKey(to='records.Record'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='anomaly',
            field=models.ForeignKey(blank=True, to='records.Anomaly', null=True),
        ),
        migrations.AddField(
            model_name='annotation',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='annotation',
            name='point',
            field=models.ForeignKey(to='records.Point'),
        ),
    ]
