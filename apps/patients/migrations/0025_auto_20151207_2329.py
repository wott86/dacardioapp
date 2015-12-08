# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0024_diagnosis_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='attachment',
            field=models.FileField(upload_to=apps.patients.models.get_upload_path, null=True, verbose_name='Adjunto', blank=True),
        ),
    ]
