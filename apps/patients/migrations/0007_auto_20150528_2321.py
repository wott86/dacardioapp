# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20150428_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habit',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='occupation',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relationshiptype',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ses',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
