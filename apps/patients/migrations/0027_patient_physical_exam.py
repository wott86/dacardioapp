# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0026_auto_20151207_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='physical_exam',
            field=models.TextField(default=b'', verbose_name='examen f\xedsico', blank=True),
        ),
    ]
