# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0023_auto_20151124_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='attachment',
            field=models.FileField(null=True, upload_to=apps.patients.models.get_upload_path, blank=True),
        ),
    ]
